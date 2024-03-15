from os import system
from make_file import make_file
from settings import (
    base_dir,
    list_directory_name,
    default_html_templete,
    default_css_styles,
    default_js_script,
)


if __name__ == '__main__':

    # Creating default directorys
    system(f'mkdir ./{base_dir}')
    for directory_name in list_directory_name:
        system(f'mkdir ./{base_dir}/{directory_name}')

    # Creating default files
    make_file(f'./{base_dir}/index.html', default_html_templete)
    make_file(f'./{base_dir}/styles/styles.css', default_css_styles)
    make_file(f'./{base_dir}/src/index.js', default_js_script)
    make_file(f'./{base_dir}/README.md', '## Write your app detailes.')
