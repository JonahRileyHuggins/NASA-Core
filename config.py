# -*- coding: utf-8 -*-
"""
Custom color palette override for PtPython REPL application. 

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
        # base
        "": "#f0f0f0",

        # comments
        "pygments.comment": "italic #71767a",

        # --- STATEMENTS (NASA red) ---
        "pygments.keyword": "#ed1c24",
        "pygments.keyword.control": "#ed1c24",

        # --- IMPORT / TYPE-LIKE (purple) ---
        "pygments.keyword.namespace": "#c4a7e7",

        # --- OPERATORS ---
        "pygments.operator": "#f0f0f0",
        "pygments.operator.word": "#ed1c24",  # in, not, and, or

        # --- NAMES ---
        "pygments.name": "#f0f0f0",
        "pygments.name.function": "#f15a29",
        "pygments.name.builtin": "#f15a29",
        
        # --- STRINGS (NASA blue) ---
        "pygments.name.class": "#0066b3",

        # escape characters inside strings
        "pygments.string.escape": "#f0f0f0",
        "pygments.string": "#f0f0f0",


        # --- NUMBERS + special chars ---
        "pygments.number": "#f15a29",

        # --- punctuation ---
        "pygments.punctuation": "#f0f0f0",
    })

    repl.app.style = merge_styles([repl.app.style, custom])
