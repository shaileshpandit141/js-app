base_dir = 'js-app'

list_directory_name = [
    'styles',
    'src',
    'media',
    'media/icons',
    'media/images',
]


default_html_templete = (
    '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Linked favicon. -->
    <link rel="shortcut icon" href="./media/icons/favicon.ico" type="image/x-icon">

    <!-- Default document title. -->
    <title>Document</title>

    <!-- Linked stylesheet files. -->
    <link rel="stylesheet" href="./styles/styles.css">
</head>

<body>
    <!-- Edit here to update document. -->

    <!-- Linked script files. -->
    <script type="module" src="./src/index.js"></script>
</body>

</html>
''')


default_css_styles = (
    '''/* Reset default styles. */
* {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
}


/* CSS Font Size Variables. */
:root {
    
    /* For Display Text  */
    --display: 4rem;
    --display-height: 44px;

    /* For Heading Text  */
    --heading: 2.813rem;
    --heading-height: 36px;

    /* For Title Text  */
    --title: 1.5rem;
    --title-height: 24px;
    --title-spacing: 0.15px;

    /* For Label Text  */
    --label: 1.125rem;
    --label-height: 16px;
    --label-spacing: 0.5px;

    /* For body Text  */
    --body-m: 0.875rem;
    --body-m-height: 20px;
    --body-m-spacing: 0.25px;

    /* Define Color variables */
    --background-color: #fff;
    --text-color: #09090b;
    --header-background: unset;
    --sidebar-background: unset;
    --footer-background: unset;
    --hover-color: unset;
}


/* Setting scroll-behavior. */
html {
    scroll-behavior: smooth;
}


/* Body styles. */
body {
    display: grid;
    background-color: var(--background-color);
    font-family: Arial, Helvetica, sans-serif;
    grid-template-columns: repeat(12, 1fr);
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


/* Protect Link OverFlow during Click.  */
.protect--link--overflow {
    display: flex;
    overflow: hidden;
    width: fit-content;
}
''')


default_js_script = (
    '''// Setting the default document title.
document.title = 'js-app'

// Default html, css, and js code for test 
const default_test_code = (
    `<!-- js-app test code, injected by JavaScript usin src/index.js file. -->
    <style>
    .test {
        grid-column: 2/-2;
        font-family: Arial, Helvetica, sans-serif;
        height: fit-content;
        min-height: 100vh;
        width: 100%;
        user-select: none;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    h1 {
        font-size: 28px;
        text-align: center;
        letter-spacing: 0.03em;
        line-height: 24px;
        margin-block: 16px;
    }

    span {
        text-wrap: nowrap;
        letter-spacing: 0.03em;
        color: #7f02ad;
    }

    button {
    font-size: 16px;
    letter-spacing: 0.03em;
    font-weight: 600;
    border: none;
    padding: 8px 16px;
    border-radius: 999rem;
    background-color: #e7e7e7;
    transition: background-color 0.3s ease-in-out;
    }

    button:hover {
        background-color: #dadada;
    }
</style>
<section class="test">
    <h1>Welcome to <span>js-app</span></h1>
    <button id='test--btn--js' type="button">Test</button>
</section>
`
)

document.body.insertAdjacentHTML('beforeend', default_test_code)

const testBtnJs = document.getElementById('test--btn--js')

testBtnJs.addEventListener('click', () => {
    alert('Now js-app is working fine, you can edit index.html or src/index.js file to update the document.')
})
''')
