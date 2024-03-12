const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: '/',
  transpileDependencies: true,
  devServer: {
    allowedHosts: 'all',
    client: {
      logging: 'info',
      progress: true
    },
    compress: true,
    watchFiles: {
      paths: ['public/**/*', 'src/**/*'],
      options: {
        usePolling: true
      }
    }
  }
})
