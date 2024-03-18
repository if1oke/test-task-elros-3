export const LSSetToken = (access, refresh) => {
  localStorage.setItem('access', access)
  localStorage.setItem('refresh', refresh)
}

export const LSGetToken = () => {
  return {
    access: localStorage.getItem('access'),
    refresh: localStorage.getItem('refresh')
  }
}
