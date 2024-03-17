# JS-CLI: Create JS App

## Overview

JS-CLI is a command-line tool designed to simplify the creation of vanilla HTML, CSS, and JavaScript frontend boilerplate applications. With just one command, `create-js-app`, developers can generate a basic structure for their frontend projects, enabling them to focus more on coding and less on setup.

## Installation

Clone this repository:
```shell
git clone https://github.com/shaileshpandit141/JS-CLI.git
```

Navigate to the cloned directory:

```shell
cd JS-CLI
```

Make the script executable:
```shell
chmod +x create-js-app.sh
```

## Linux command-line tool setup

1. Move your JS-CLI directory into the `~` directory.
   
2. Make the script `(~/JS-CLI/create-js-app.sh)` executable: You need to give execute permission to your script.
    ```shell
    chmod +x ~/bin/my_script.sh
    ```

3. Add `~/JS-CLI` to your PATH: Open your `.bashrc` or `.bash_profile` file located in your home directory using a text editor (e.g., code, nano, vim, gedit).
    ```shell
    nano ~/.bashrc
    ```
    1. Add the following line at the end of the file:
        ```shell
        export PATH="$PATH:$HOME/JS-CLI"
        ``` 
        
    2. Create one alias for short command
    ```shell
        alias create-js-app='create-js-app.sh'
    ```

    3. Run with `create-js-app.sh` or `create-js-app`
   
    4. Save and close the file.
   
4. Source the changes: To apply the changes to your current terminal session, either close and reopen your terminal or run:
    ```shell
    source ~/.bashrc
    ```

5. Coagulation all configuration are done,
   
   Now, you should be able to run `create-js-app` command from any location in the terminal by simply typing its command name like:
   ```shell
   create-js-app.sh
   ```
   or
   ```shell
   create-js-app
   ```
   to quickly creating a vanilla HTML, CSS, and JavaScript frontend boilerplate for your web-app.

This web-app containing some Directorys and Files for organize your web-app.
Now, you should be able to run `create-js-app` command from any location in the terminal by simply typing its command name like:
   ```shell
   create-js-app.sh
   ```
   or
   ```shell
   create-js-app
   ```
   to quickly creating a vanilla HTML, CSS, and JavaScript frontend boilerplate for your web-app.

    This web-app containing some Directorys and Files for organize your web-app. it look like this.
    ```
    js-app/
      | index.html
      | README.md
      | media/
        | icons/
           | favicon.svg
        | images/
      | meta/
         | congfig_styles.css
         | config._script.js
      | src/
         | index.js
         | others
      | styles/
         | styles.css
         | others
    ```

Files description:

- `index.html`: The main HTML file.
- `styles.css`: The CSS file for styling.
- `index.js`: The JavaScript file for scripting.
- `README.md`: A README file with basic information about the project.

## Dependencies
- Python 3.x
- Bash shell
- live-server (install by `sudo npm install -g live-server`)

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
If you have any questions or need assistance with this project, please contact `Shailesh` at `shaileshpandit141@gmail.com`.

Thank you for using this JS-CLI.