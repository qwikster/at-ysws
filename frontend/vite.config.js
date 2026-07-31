import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import { execSync } from 'node:child_process';

const hash = execSync("git rev-parse --short HEAD").toString().trim();

export default defineConfig({
  plugins: [sveltekit()],
  define: {
    __APP_VERSION__: JSON.stringify(hash)
  },
  server: {
    proxy: {
      '/api': 'http://localhost:8000'
    },
    allowedHosts: ["at.qwik.top"]
  },
});
