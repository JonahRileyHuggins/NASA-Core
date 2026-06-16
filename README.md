<p align="center">
    <img src="./assets/NASA-Core_theme.png" width="1000" />
    <h2 align="center">NASA-Core Theme</h2>
</p>

<h3 align="center">Inspired by the Artemis II lunar flyby album</h3>

<p algin="center"> Not affiliated with the project, just a geek who likes space</p>

## Usage

### Windows Terminal
1. Open `settings.json` from Windows Terminal
2. In the `schemes` section of the file, paste the contents of the `artemis-uswds.scheme.json` file
3. Navigate to the `themes` section and paste the contents of the corresponding theme file (e.g. `artemis-uswds.theme.json`).
4. Update `colorScheme` within the `profiles` section to include your chosen scheme:

    ```json
    {
        "profiles": {
            "defaults": {
                "colorScheme": "Artemis USWDS"
            }
        }
    }
    ```

5. Update `theme` to use your chosen theme:

    ```json
    {
        "theme": "Artemis USWDS"
    }
    ```

### VS Code / Cursor

The VS Code theme lives in the `nasa-core-artemis/` extension folder. After installing, choose **nasa-core-artemis** from the color theme picker.

#### Install from source (recommended)

1. Install [Node.js](https://nodejs.org/) if you do not already have it.
2. Install the VS Code extension packaging tool:

    ```powershell
    npm install -g @vscode/vsce
    ```

3. Package the extension from the repo root:

    ```powershell
    cd nasa-core-artemis
    vsce package
    ```

4. Install the generated `.vsix` file:
   - **VS Code / Cursor:** open the Extensions view, open the `...` menu, choose **Install from VSIX...**, and select `nasa-core-artemis-0.0.1.vsix`
   - **CLI:** `code --install-extension .\nasa-core-artemis-0.0.1.vsix`

5. Reload the editor if prompted.

#### Try without packaging (development)

1. Open the `nasa-core-artemis` folder in VS Code or Cursor.
2. Press `F5` to launch an **Extension Development Host** window.
3. In the new window, open the color theme picker and select **nasa-core-artemis**.

#### Apply the theme

1. Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS).
2. Run **Preferences: Color Theme** (or press `Ctrl+K`, then `Ctrl+T`).
3. Select **nasa-core-artemis**.

#### Theme files

- `nasa-core-artemis/themes/nasa-core-artemis-color-theme.json` — full theme used by the extension
- `artemis-uswds-vscode.json` — minimal reference theme
- `artemis-usdws-vscode.jsonc` — full UI theme with additional workbench color customizations

### Vim
**Windows**
1.  Copy the `artemis_uswds.vim` file into the `~\vimfiles\colors\` directory
2.  Paste `colorscheme artemis_uswds` into your vim configuration file, (i.e. `~\_vimrc`)

**Linux**
1. Copy the `artemis_uswds.vim` file into the `~/.vim/colors/`
2. Paste `colorscheme artemis_uswds` into your vim configuration file `~/.vimrc` 

### PtPython
**Note**: As IPython version 9.7.0, you cannot integrate custom color palettes. However, PtPython allows
this in the integrated iPython functionality (i.e. `ptipython`)

1. Copy the `config.py` file into the location of `$PTPYTHON_CONFIG_HOME`
2. specify the configuration file location to ptpython (e.g. `ptpython --config-file $env:PYTHON_CONFIG_HOME/config.py`

## Gallery

**Windows Terminal**

![Artemis USWDS for Windows Terminal](./assets/windows-terminal.png)

**Vim**

![Artemis USWDS for Vim](./assets/vim-demo.png)

**PtPython**

![Artemis USWDS for PtPython](./assets/ptpython.png)

