/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './store/templates/**/*.html',
        './**/templates/**/*.html',
    ],
    theme: {
        extend: {
            colors: {
                primary: '#004C97',
                secondary: '#B3B5B7',
                accent: '#D9D9D9',
                dark: '#2D3436',
                light: '#F7F9FC',
            },
            fontFamily: {
                sans: ['Poppins', 'sans-serif'],
            },
        },
    },
    plugins: [],
}
