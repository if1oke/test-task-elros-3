import { baseInstance } from '@/api'

export const useTokenInRequest = () => {
  baseInstance.interceptors.request.use((req) => {
    const access = localStorage.getItem('access')
    access
      ? (req.headers.Authorization = 'Bearer ' + access)
      : localStorage.clear()
    return req
  })
}
