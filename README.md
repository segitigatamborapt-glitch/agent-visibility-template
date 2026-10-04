# PT. Segi Tiga Tambora — Situs Perusahaan

Situs web PT. Segi Tiga Tambora, dibangun dengan React (Vite) dan Cloudflare Workers (Hono).

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

## Mengisi data perusahaan

Semua data ada di `src/react-app/site.ts`. Bagian bertanda `CONTOH` masih berupa placeholder.

| Yang diisi | Di mana |
| --- | --- |
| Logo | File di `public/` (`logo.svg` untuk header, `logo-lengkap.svg`, `logo-lambang.svg`, `favicon.svg`); atur `site.logo` |
| Kontak (alamat, email, telepon) | `contact` |
| Bidang usaha | `businessLines` |
| Proyek | `projects` |
| Angka keunggulan | `stats` (isi `value`; bagian ini tampil otomatis saat ada nilainya) |
| Menu dan submenu | `navItems` |

Logo alternatif bergaya lencana: `public/logo-lencana.svg` (untuk stempel, papan nama, media sosial; teks di dalamnya terlalu kecil untuk header).

Halaman Profil Perusahaan ada di `src/react-app/pages/About.tsx`; halaman submenu lain memakai `InfoPage.tsx` sebagai placeholder sampai isinya dibuat.
