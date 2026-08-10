/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        purple: {
          50: '#F5F2F9',
          100: '#EAE3F4',
          900: '#4A2D7A',
          950: '#2A1747',
        },
      },
    },
  },
  plugins: [],
};
