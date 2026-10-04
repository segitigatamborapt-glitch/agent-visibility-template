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
| Logo | File di `public/`; atur `site.logo` (aktif: `logo-lencana.svg`) dan `site.logoShowName`. Alternatif tersedia: `logo.svg` (nama di dalam gambar, set `logoShowName: false`), `logo-lengkap.svg`, `logo-lambang.svg`; `favicon.svg` untuk ikon tab |
| Kontak (alamat, email, telepon) | `contact` |
| Pengalaman proyek | `src/react-app/data/experience.ts` (satu berkas; bidang usaha, proyek unggulan, dan angka di beranda diturunkan otomatis dari sini) |
| Menu dan submenu | `navItems` |

Logo utama adalah lencana `public/logo-lencana.svg` (cocok untuk stempel, papan nama, dan media sosial). Di header, nama perusahaan ditulis sebagai teks di samping lencana karena tulisan di dalamnya terlalu kecil.

Halaman Profil Perusahaan ada di `src/react-app/pages/About.tsx`; halaman submenu lain memakai `InfoPage.tsx` sebagai placeholder sampai isinya dibuat.

## Data pengalaman proyek

Daftar pekerjaan ada di `src/react-app/data/experience.ts`, disalin dari tab **Pengalaman** pada profil penyedia di SIKaP (INAPROC). Untuk memperbarui, tambah atau ubah baris di `experience` (urut dari terbaru). Beranda, halaman *Pengalaman Proyek*, rincian *Lini Bisnis*, dan angka ringkasan ikut berubah otomatis; label "Sedang berjalan" dihitung dari tanggal kontrak.

Belum ada sinkronisasi otomatis dengan SIKaP/INAPROC: data profil penyedia berada di balik login dan tidak ada API resmi yang kami temukan, jadi pembaruan dilakukan manual.
