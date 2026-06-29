# -*- coding: utf-8 -*-
"""
Artemis USWDS Light — custom color palette override for PtPython REPL application.

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
        # base — black predominant
        "": "#000000",

        # comments — Artemis grey
        "pygments.comment": "italic #71767a",

        # keywords — NASA red
        "pygments.keyword": "#ed1c24",
        "pygments.keyword.control": "#0066b3",
        "pygments.keyword.namespace": "#0066b3",

        # operators & punctuation
        "pygments.operator": "#333333",
        "pygments.operator.word": "#0066b3",

        # names — black (strings, functions, variables) — dark theme
        "pygments.name": "#000000",
        "pygments.name.function": "#000000",
        "pygments.name.builtin": "#000000",
        "pygments.name.class": "#0066b3",

        "pygments.string.escape": "#000000",
        "pygments.string": "#000000",

        # numbers — Artemis orange accent
        "pygments.number": "#f15a29",

        "pygments.punctuation": "#333333",
    })

    repl.app.style = merge_styles([repl.app.style, custom])
