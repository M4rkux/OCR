export default {
  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Loadout to text',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    bodyAttrs: {
      class: 'has-background-dark has-text-grey-lighter'
    }
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
    '@nuxtjs/bulma',
    '@nuxtjs/fontawesome'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    ['nuxt-fontawesome', {
      imports: [
        {
          set: '@fortawesome/free-solid-svg-icons',
          icons: [
            'faUpload'
          ]
        }
      ]
    }],
    [
      '@nuxtjs/firebase',
      {
        config: {
          apiKey: 'AIzaSyA9LynASpAjhW4Oz7k6VpqCCDxh4uOb0p0',
          authDomain: 'loadout2text.firebaseapp.com',
          projectId: 'loadout2text',
          storageBucket: 'loadout2text.appspot.com',
          messagingSenderId: '893647001991',
          appId: '1:893647001991:web:ee00951e12bb40f9221b22',
          measurementId: 'G-ZCEZCHXKN7'
        },
        services: {
          auth: true // Just as example. Can be any other service.
        }
      }
    ]
  ],

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
}
