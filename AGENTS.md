# AGENTS.md — Situs Perusahaan Pandu

Situs web perusahaan konstruksi Pandu. Bahasa antarmuka: Indonesia.

## Arsitektur

- `src/react-app/` — SPA React, disajikan sebagai static assets.
- `src/worker/index.ts` — Worker Hono; hanya menangani `/api/*` (lihat `run_worker_first` di `wrangler.jsonc`).
- `test/index.test.ts` — tes Worker via `SELF.fetch`.

## Konvensi

- Rute API baru ditaruh di bawah `/api/` dan ditambah tes.
- Setelah mengubah `wrangler.jsonc`, jalankan ulang `npx wrangler types`.
- Nama Worker di `wrangler.jsonc` jangan diubah tanpa menyesuaikan build di dasbor Cloudflare.

## Validasi

```bash
npm run build
npm test
```
