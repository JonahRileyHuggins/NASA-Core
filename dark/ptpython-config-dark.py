# -*- coding: utf-8 -*-
"""
Artemis USWDS Dark — custom color palette override for PtPython REPL application.

If no path is returned when executing:
    `echo $env:PTPYTHON_CONFIG_HOME`
Default path to this config needs to be set.

windows powershell
`setx PTPYTHON_CONFIG_HOME "$env:APPDATA\ptpython"`

"""
from prompt_toolkit.styles import Style, merge_styles

def configure(repl):
    print("ptpython config loaded")

    custom = Style.from_dict({
        # base — white predominant
        "": "#ffffff",

        # comments — Artemis grey
        "pygments.comment": "italic #71767a",

        # keywords — NASA red
        "pygments.keyword": "#ed1c24",
        "pygments.keyword.control": "#0066b3",
        "pygments.keyword.namespace": "#0066b3",

        # operators & punctuation
        "pygments.operator": "#f0f0f0",
        "pygments.operator.word": "#0066b3",

        # names — white (strings, functions, variables) — dark theme
        "pygments.name": "#ffffff",
        "pygments.name.function": "#ffffff",
        "pygments.name.builtin": "#ffffff",
        "pygments.name.class": "#0066b3",

        "pygments.string.escape": "#ffffff",
        "pygments.string": "#ffffff",

        # numbers — Artemis orange accent
        "pygments.number": "#f15a29",

        "pygments.punctuation": "#f0f0f0",
    })

    repl.app.style = merge_styles([repl.app.style, custom])
