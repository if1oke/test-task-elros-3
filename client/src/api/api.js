import { baseInstance } from '@/api/index'

export const APIMethods = {
  auth: {
    profile: () => baseInstance.get('user/'),
    login: (payload) => baseInstance.post('user/login/', payload),
    register: (payload) => baseInstance.post('user/register/', payload),
    token: (payload) => baseInstance.post('user/token/', payload)
  },
  wallet: {
    info: () => baseInstance.get('wallet/')
  },
  exchange: {
    rates: {
      current: () => baseInstance.get('exchange/rate/'),
      history: () => baseInstance.get('exchange/rate/history/')
    }
  }
}
