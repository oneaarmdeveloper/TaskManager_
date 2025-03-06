import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'https://127.0.0.1:', // Replace with your API URL
        changeOrigin: true,
        secure: false, // Set to true if API uses HTTPS
        rewrite: (path) => path.replace(/^\/api/, ''), // Rewrite the API path if needed
      },
    },
  },
})
