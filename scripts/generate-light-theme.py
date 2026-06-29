#!/usr/bin/env python3
"""Generate Artemis USWDS light theme files from dark theme sources."""

import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DARK = ROOT / "dark"
LIGHT = ROOT / "light"

# Workbench UI: dark surface -> light surface
UI_COLOR_MAP = {
    "#0B0F14": "#FFFFFF",
    "#0b0f14": "#ffffff",
    "#11151C": "#F5F5F5",
    "#11151c": "#f5f5f5",
    "#191A1B": "#F0F0F0",
    "#191a1b": "#f0f0f0",
    "#202122": "#EEEEEE",
    "#1A1F2A": "#E8E8E8",
    "#1a1f2a": "#e8e8e8",
    "#262626": "#E0E0E0",
    "#2b2b2b": "#E0E0E0",
    "#2a2a2a": "#D8D8D8",
    "#2a2b2c": "#D0D0D0",
    "#333536": "#CCCCCC",
    "#313131": "#E8E8E8",
    "#3c3c3c": "#CCCCCC",
    "#383a49": "#E0E0E0",
    "#222222": "#E8E8E8",
    "#1f1f1f": "#E0E0E0",
    "#2b2b2b": "#D8D8D8",
    "#2e3031": "#D0D0D0",
    "#3a3d41": "#D8D8E8",
    "#4b4c4d": "#D0D0D0",
    "#878889": "#B0B0B0",
    "#444444": "#888888",
    "#555555": "#767676",
    "#ffffff17": "#00000017",
    "#ffffff18": "#00000012",
    "#ffffff10": "#0000000d",
    "#ffffff0d": "#0000000a",
    "#ffffff0f": "#0000000f",
    "#ffffff13": "#00000010",
    "#ffffff22": "#00000018",
    "#ffffffa0": "#000000a0",
    "#191b1d4d": "#0000001a",
    "#71767A33": "#71767A40",
    "#71767A66": "#71767A80",
    "#71767A99": "#71767A99",
    "#8c8c8c4d": "#8c8c8c66",
    "#c8cacc80": "#71767a80",
}

# Foreground/text: light-on-dark -> dark-on-light (UI keys only)
UI_FOREGROUND_MAP = {
    "#FFFFFF": "#000000",
    "#ffffff": "#000000",
    "#F0F0F0": "#1A1A1A",
    "#f0f0f0": "#1a1a1a",
    "#8C8C8C": "#71767A",
    "#8c8c8c": "#71767a",
}

# Token syntax: invert primary text, keep accent colors
TOKEN_FOREGROUND_MAP = {
    "#FFFFFF": "#000000",
    "#ffffff": "#000000",
    "#F0F0F0": "#333333",
    "#f0f0f0": "#333333",
}

# Keys where white text must stay (badges/buttons on colored backgrounds)
KEEP_WHITE_KEYS = {
    "activityBarBadge.foreground",
    "activityErrorBadge.foreground",
    "agentsBadge.foreground",
    "agentsUnreadBadge.foreground",
    "badge.foreground",
    "button.foreground",
    "extensionButton.prominentForeground",
    "quickInputList.focusForeground",
    "quickInputList.focusHighlightForeground",
    "quickInputList.focusIconForeground",
    "statusBar.debuggingForeground",
    "statusBarItem.prominentForeground",
    "statusBarItem.remoteForeground",
    "statusBarItem.hoverForeground",
    "list.activeSelectionIconForeground",
}


def should_keep_white(key: str) -> bool:
    return key in KEEP_WHITE_KEYS


def is_foreground_key(key: str) -> bool:
    lowered = key.lower()
    return lowered == "foreground" or lowered.endswith(".foreground")


def map_ui_color(key: str, value: str) -> str:
    if not isinstance(value, str) or not value.startswith("#"):
        return value

    if should_keep_white(key):
        return value

    alpha = ""
    base = value
    if len(value) == 9:
        base = value[:7]
        alpha = value[7:]

    mapped = base
    if is_foreground_key(key):
        if base.upper() in ("#FFFFFF", "#F0F0F0", "#8C8C8C"):
            mapped = UI_FOREGROUND_MAP.get(base, UI_FOREGROUND_MAP.get(base.upper(), base))
    elif base in UI_COLOR_MAP:
        mapped = UI_COLOR_MAP[base]
    else:
        for k, v in UI_COLOR_MAP.items():
            if k.upper() == base.upper():
                mapped = v
                break

    return mapped + alpha


def transform_vscode_theme(data: dict, name: str, theme_type: str) -> dict:
    result = copy.deepcopy(data)
    result["name"] = name
    result["type"] = theme_type

    if "colors" in result:
        result["colors"] = {
            key: map_ui_color(key, value)
            for key, value in result["colors"].items()
        }
        # Ensure core editor colors
        result["colors"]["editor.background"] = "#FFFFFF"
        result["colors"]["editor.foreground"] = "#000000"
        result["colors"]["editorCursor.foreground"] = "#000000"
        result["colors"]["terminal.background"] = "#FFFFFF"
        result["colors"]["terminal.foreground"] = "#000000"
        result["colors"]["terminalCursor.foreground"] = "#000000"
        result["colors"]["terminalCursor.background"] = "#FFFFFF"

    if "tokenColors" in result:
        for entry in result["tokenColors"]:
            settings = entry.get("settings", {})
            fg = settings.get("foreground")
            if fg in TOKEN_FOREGROUND_MAP:
                settings["foreground"] = TOKEN_FOREGROUND_MAP[fg]
            # Todo: dark text on orange badge -> white on orange for contrast
            if fg and fg.upper() == "#0B0F14" and settings.get("background", "").upper() == "#F15A29":
                settings["foreground"] = "#FFFFFF"

    return result


def load_jsonc(text: str) -> dict:
    # Remove trailing commas only; preserve // in URLs like vscode://schemas/...
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    return json.loads(text)


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent="\t" if path.suffix == ".jsonc" else 4)
        f.write("\n")


def generate_vscode_files() -> None:
    dark_minimal = json.loads((DARK / "artemis-uswds-dark-vscode.json").read_text(encoding="utf-8"))
    light_minimal = transform_vscode_theme(dark_minimal, "Artemis USWDS Light", "light")
    write_json(LIGHT / "artemis-uswds-light-vscode.json", light_minimal)

    dark_full_text = (DARK / "artemis-uswds-dark-vscode.jsonc").read_text(encoding="utf-8")
    dark_full = load_jsonc(dark_full_text)
    light_full = transform_vscode_theme(dark_full, "Artemis USWDS Light", "light")
    write_json(LIGHT / "artemis-uswds-light-vscode.jsonc", light_full)

    dark_ext = json.loads(
        (ROOT / "nasa-core-artemis/themes/nasa-core-artemis-dark-color-theme.json").read_text(encoding="utf-8")
    )
    light_ext = transform_vscode_theme(dark_ext, "nasa-core-artemis-light", "light")
    write_json(ROOT / "nasa-core-artemis/themes/nasa-core-artemis-light-color-theme.json", light_ext)


def generate_terminal_scheme() -> None:
    scheme_text = (DARK / "artemis-uswds-dark.scheme.json").read_text(encoding="utf-8")
    scheme = json.loads(scheme_text)
    scheme["name"] = "Artemis USWDS Light"
    scheme["background"] = "#FFFFFF"
    scheme["foreground"] = "#000000"
    scheme["cursorColor"] = "#000000"
    scheme["black"] = "#000000"
    scheme["selectionBackground"] = "#E8E8E8"
    scheme["white"] = "#1A1A1A"
    write_json(LIGHT / "artemis-uswds-light.scheme.json", scheme)


def generate_terminal_theme() -> None:
    theme = json.loads((DARK / "artemis-uswds-dark.theme.json").read_text(encoding="utf-8"))
    theme["name"] = "Artemis USWDS Light"
    theme["tab"]["background"] = "#FFFFFFFF"
    theme["tabRow"]["background"] = "#F0F0F0FF"
    theme["tabRow"]["unfocusedBackground"] = "#71767AFF"
    theme["window"]["applicationTheme"] = "light"
    write_json(LIGHT / "artemis-uswds-light.theme.json", theme)


def generate_vim() -> None:
    dark_vim = (DARK / "artemis_uswds_dark.vim").read_text(encoding="utf-8")
    light_vim = dark_vim.replace("Artemis-USWDS Dark", "Artemis-USWDS Light")
    light_vim = light_vim.replace('g:colors_name = "artemis_uswds_dark"', 'g:colors_name = "artemis_uswds_light"')
    light_vim = light_vim.replace("guifg=#ffffff guibg=#0b0f14", "guifg=#000000 guibg=#ffffff")
    light_vim = light_vim.replace("guibg=#11151c", "guibg=#f5f5f5")
    light_vim = light_vim.replace("guibg=#1a1f2a", "guibg=#e8e8e8")
    light_vim = light_vim.replace("guifg=#ffffff", "guifg=#000000")
    light_vim = light_vim.replace("guifg=#f0f0f0", "guifg=#333333")
    light_vim = light_vim.replace("guifg=#ffffff guibg=#11151c", "guifg=#1a1a1a guibg=#f0f0f0")
    light_vim = light_vim.replace("guifg=#1a1f2a", "guifg=#e8e8e8")
    light_vim = light_vim.replace("guifg=#0b0f14 guibg=#f15a29", "guifg=#ffffff guibg=#f15a29")
    (LIGHT / "artemis_uswds_light.vim").write_text(light_vim, encoding="utf-8")


def generate_ptpython() -> None:
    dark_py = (DARK / "ptpython-config-dark.py").read_text(encoding="utf-8")
    light_py = dark_py.replace("Artemis USWDS Dark", "Artemis USWDS Light")
    light_py = light_py.replace('"": "#ffffff"', '"" : "#000000"')
    light_py = re.sub(r'"" : "#000000"', '"" : "#000000"', light_py, count=1)
    light_py = light_py.replace('"" : "#000000"', '"" : "#000000"', 1)
    # Fix the botched replace - do it cleanly
    light_py = dark_py.replace("Artemis USWDS Dark", "Artemis USWDS Light")
    light_py = light_py.replace('# base — white predominant\n        "": "#ffffff",', '# base — black predominant\n        "": "#000000",')
    light_py = light_py.replace('"pygments.operator": "#f0f0f0"', '"pygments.operator": "#333333"')
    light_py = light_py.replace('"pygments.name": "#ffffff"', '"pygments.name": "#000000"')
    light_py = light_py.replace('"pygments.name.function": "#ffffff"', '"pygments.name.function": "#000000"')
    light_py = light_py.replace('"pygments.name.builtin": "#ffffff"', '"pygments.name.builtin": "#000000"')
    light_py = light_py.replace('"pygments.string.escape": "#ffffff"', '"pygments.string.escape": "#000000"')
    light_py = light_py.replace('"pygments.string": "#ffffff"', '"pygments.string": "#000000"')
    light_py = light_py.replace('"pygments.punctuation": "#f0f0f0"', '"pygments.punctuation": "#333333"')
    (LIGHT / "ptpython-config-light.py").write_text(light_py, encoding="utf-8")


def main() -> None:
    LIGHT.mkdir(parents=True, exist_ok=True)
    generate_vscode_files()
    generate_terminal_scheme()
    generate_terminal_theme()
    generate_vim()
    generate_ptpython()
    print("Light theme files generated in", LIGHT)
    print("Extension light theme:", ROOT / "nasa-core-artemis/themes/nasa-core-artemis-light-color-theme.json")


if __name__ == "__main__":
    main()
