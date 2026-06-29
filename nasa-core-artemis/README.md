# nasa-core-artemis

VS Code / Cursor color themes for the NASA-Core Artemis USWDS palette — **dark** and **light** variants.

## Install

From the repository root:

```powershell
npm install -g @vscode/vsce
cd nasa-core-artemis
vsce package
code --install-extension .\nasa-core-artemis-0.0.1.vsix
```

Or in the editor: **Extensions** → `...` → **Install from VSIX...** → select the packaged file.

## Use

1. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
2. Run **Preferences: Color Theme**.
3. Choose **nasa-core-artemis-dark** or **nasa-core-artemis-light**.

Shortcut: `Ctrl+K`, then `Ctrl+T` (Windows/Linux).

## Development

Open this folder in VS Code or Cursor and press `F5` to launch an Extension Development Host with both themes loaded.

## Related files

Standalone theme files live in [`../dark/`](../dark/) and [`../light/`](../light/) for Windows Terminal, Vim, and PtPython. See the [main README](../README.md) for those instructions.
