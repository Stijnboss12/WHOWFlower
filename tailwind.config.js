/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "whowflower-limegreen": '#4deda1',
        "whowflower-darkgreen": '#275f4b',
        "whowflower-darkgreen-900": '#183B2E',
        "whowflower-black": '#0c0e14',
        "whowflower-black-800": '#10131c',
        "whowflower-black-900": '#0E1017',
        "whowflower-black-600": '#12141d',
        "whowflower-black-500": '#191C29'
      },
      container: {
        center: true,
        padding: "1rem",
        screens : {
          lg: "1600px",
          xl: "1600px",
          "2xl": "1600px"
        }
      }
    },
  },
  plugins: [],
}
