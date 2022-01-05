module.exports = {
	content: ['templates/**/*.html', './**/templates/**/*.html'],
	darkMode: 'class', // or 'media' or 'class'
	theme: {
		fontFamily: {
			sans: ['Inter', 'ui-sans-serif', 'system-ui']
		},
		extend: {}
	},
	variants: {
		extend: {}
	},
	plugins: [require('@tailwindcss/forms')]
};
