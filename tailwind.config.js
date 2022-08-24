/** @type {import('tailwindcss').Config} */
module.exports = {
  plugins: [
    require('flowbite/plugin')
  ],
  content: ['./*.html'],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px'
    },
    extend: {
      colors: {
        'gold': '#C7B287',
        'darkerGold': '#A98F5A'
      }
    },
    fontFamily: {
      'sans': ['Nunito'],
      'serif': ['Abril Fatface'],
      'display': ['Nunito'],
      'h1': ['Abril Fatface']
    }
  },
  plugins: [],
}
