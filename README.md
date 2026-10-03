# Pandu — Situs Perusahaan Konstruksi

Situs web perusahaan Pandu, dibangun dengan React (Vite) dan Cloudflare Workers (Hono).

## Menjalankan

```bash
npm install
npm run dev      # pengembangan lokal
npm run build    # tsc -b && vite build
npm test         # vitest
npm run deploy   # build + wrangler deploy
```

## Struktur

- `src/react-app/` — antarmuka situs (React)
- `src/worker/index.ts` — API Worker (Hono), rute di bawah `/api/*`
- `test/` — tes Worker (vitest-pool-workers)
