# Default Configuration for js-app.
default_js_config = (
    '''// Configure meta data object.
const config = {
    title: 'js-app',
}

// Setting the default document title.
document.title = config.title

'''
)

# Default Styles for document.
default_css_config = (
    '''/* Reset default styles. */
* {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
}

/* Setting scroll-behavior. */
html {
    scroll-behavior: smooth;
}

body {
    display: grid;
    font-family: Arial, Helvetica, sans-serif;
    height: fit-content;
    width: 100%;
    position: relative;
    overflow: hidden;
    overflow-y: auto;
}

/* Apply font on input and button tags. */
input,
button {
    font-family: Arial, Helvetica, sans-serif;
}
'''
)
