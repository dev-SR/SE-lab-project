module.exports = {
	content: ['templates/**/*.html', './**/templates/**/*.html'],
	darkMode: 'class', // or 'media' or 'class'
	theme: {
		fontFamily: {
			sans: ['Inter', 'ui-sans-serif', 'system-ui']
		},
		extend: {
			spacing: {
				'25vh': '25vh',
				'50vh': '50vh',
				'75vh': '75vh'
			},
			borderRadius: {
				xl: '1.5rem'
			},
			minHeight: {
				'50vh': '50vh',
				'75vh': '75vh'
			}
		}
	},
	variants: {
		extend: {}
	},
	plugins: [require('@tailwindcss/forms')]
};
