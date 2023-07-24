/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/base.html', './templates/order.html', './templates/fly.html'],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
}

