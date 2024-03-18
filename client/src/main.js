import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'
import { customTheme } from '@/plugins/vuetify'
import { createPinia } from 'pinia'
import { useTokenInRequest } from '@/middleware/accessToken'
import { VSparkline } from 'vuetify/labs/components'

useTokenInRequest()

const vuetify = createVuetify({
  components: {
    ...components,
    VSparkline
  },
  directives,
  theme: {
    defaultTheme: 'customTheme',
    themes: {
      customTheme
    }
  }
})

const pinia = createPinia()

createApp(App).use(vuetify).use(pinia).use(router).mount('#app')
