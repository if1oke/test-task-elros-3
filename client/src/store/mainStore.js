import { defineStore } from 'pinia'
import { APIMethods } from '@/api/api'
import { LSGetToken, LSSetToken } from '@/utils'

export const mainStore = defineStore('main-store', {
  state: () => ({
    exchange: {
      current: {
        ton: 0,
        btc: 0
      },
      history: {
        btc: [],
        ton: []
      }
    },
    user: {
      authState: false,
      username: null,
      email: null,
      wallet: {
        usd: {
          value: 0
        },
        ton: {
          address: null,
          value: 0
        },
        btc: {
          address: null,
          value: 0
        }
      }
    }
  }),
  actions: {
    async doRegister (username, email, password) {
      const payload = {
        username,
        email,
        password
      }
      const { data } = await APIMethods.auth.register(payload)
      this.user.authState = true
      this.user.username = data.username
      this.user.email = data.email
      LSSetToken(data.tokens.access, data.tokens.refresh)
    },
    async refreshToken () {
      const { access, refresh } = LSGetToken()
      const payload = {
        refresh
      }
      const { data } = await APIMethods.auth.token(payload)
      if (data.access) {
        LSSetToken(access, refresh)
      }
    },
    async doAuth (username, password) {
      localStorage.clear()
      const payload = {
        username,
        password
      }
      const { data } = await APIMethods.auth.login(payload)
      this.user.authState = true
      this.user.username = data.username
      this.user.email = data.email
      LSSetToken(data.tokens.access, data.tokens.refresh)
    },
    async getProfile () {
      const { data } = await APIMethods.auth.profile()
      this.user.authState = true
      this.user.username = data[0].username
      this.user.email = data[0].email
    },
    async getWallet () {
      const { data } = await APIMethods.wallet.info()
      this.user.wallet.usd.value = data.usd.value
      this.user.wallet.ton.value = data.ton.value
      this.user.wallet.ton.address = data.ton.address
      this.user.wallet.btc.value = data.btc.value
      this.user.wallet.btc.address = data.btc.address
    },
    async getExchangeRate () {
      const { data } = await APIMethods.exchange.rates.current()
      this.exchange.current.btc = {
        rate: data.btc,
        currency: 'BTC',
        color: 'orange-lighten-2',
        icon: 'mdi-currency-btc'
      }
      this.exchange.current.ton = {
        rate: data.ton,
        currency: 'TON',
        color: 'indigo-lighten-3',
        icon: 'mdi-diamond-stone'
      }
    },
    async getExchangeHistory () {
      this.exchange.history.btc = []
      this.exchange.history.ton = []
      const { data } = await APIMethods.exchange.rates.history()
      data.forEach(item => {
        this.exchange.history.btc.push(item.btc)
        this.exchange.history.ton.push(item.ton)
      })
      this.exchange.history.btc.reverse()
      this.exchange.history.ton.reverse()
    }
  }
})
