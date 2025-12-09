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
                primary: '#FF6B6B',
                secondary: '#4ECDC4',
                accent: '#FFE66D',
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
