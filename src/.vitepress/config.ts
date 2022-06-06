import { defineConfig } from 'vitepress'
import sidebarJSON from './sidebar.json'

export default defineConfig({
  lang: 'en-US',
  title: 'Tao Te Ching',
  description: 'A Book about the Way and the Power of the Way.',

  themeConfig: {
    sidebar: sidebarJSON,
    socialLinks: [{ icon: 'github', link: 'https://github.com/chnejohnson/tao-te-ching' }],

    // footer: {
    //   message: 'Released under the MIT License.',
    //   copyright: 'Copyright © 2019-present Evan You',
    // },
  },
})
