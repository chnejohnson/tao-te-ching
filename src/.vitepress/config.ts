import sidebarJSON from './sidebar.json'

export default {
	title: 'Tao Te Ching',
	description: 'A Book about the Way and the Power of the Way',
	head: [
		// ['link', { rel: 'icon', href: '/favicon.ico', type: 'image/png' }],
		['meta', { name: 'translator', content: 'Johnson' }],
		['meta', { property: 'og:title', content: 'Tao Te Ching' }],
		[
			'meta',
			{
				property: 'og:description',
				content: 'A Book about the Way and the Power of the Way',
			},
		],
	],
	lastUpdated: true,
	themeConfig: {
		sidebar: sidebarJSON,
		socialLinks: [{ icon: 'github', link: 'https://github.com/chnejohnson/tao-te-ching' }],
	},
}
