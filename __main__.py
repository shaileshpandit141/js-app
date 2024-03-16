from os import system
from make_file import make_file
from settings import (
    default_config,
    list_directory_name,
    default_html_templete,
    default_css_styles,
    default_js_script,
)


if __name__ == "__main__":

    # Reading js-app name from user.
    user_input_app_name = input("\n:: Enter a js-app name:\n:: ")
    print()

    try:
        if " " not in user_input_app_name and "" != user_input_app_name:
            base_dir = user_input_app_name

            # Creating default directorys.
            system(f"mkdir ./{base_dir}")
            for directory_name in list_directory_name:
                system(f"mkdir ./{base_dir}/{directory_name}")

            # Creating default files.
            make_file(f"./{base_dir}/meta/config.js", default_config)
            make_file(f"./{base_dir}/index.html", default_html_templete)
            make_file(f"./{base_dir}/styles/styles.css", default_css_styles)
            make_file(f"./{base_dir}/src/index.js", default_js_script)
            make_file(f"./{base_dir}/README.md", "## Write your app detailes.")

            # Success message.
            print(f"Successfull created your js-app, name is `{base_dir}`.\n")

            # user input and checking for runn created js-app or not.
            is_run = input(":: Do you want ot run it with live-server press [y/n]:\n:: ")
            print()

            # Checking user input.
            if is_run.lower() == "y" or is_run.lower == "yes":
                system(f"cd ./{base_dir} && live-server && cd ..")
            else:
                print('\nExit.\n')

        else:
            print("Please! Enter a valid js-app name.\n")

    except Exception as err:
        print("OOP's somthing is not correct: ", err)
