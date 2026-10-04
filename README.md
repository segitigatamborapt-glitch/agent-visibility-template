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

Daftar pekerjaan ada di `src/react-app/data/experience.ts`, berisi pekerjaan hasil tender yang tercatat di LPSE (INAPROC): tanggal tender, nama pekerjaan, pemberi kerja, nilai kontrak, dan nomor paket LPSE. Untuk memperbarui, tambah atau ubah baris di `experience`. Beranda, halaman *Pengalaman Proyek*, rincian *Lini Bisnis* (kategori tanpa pekerjaan otomatis disembunyikan), dan angka ringkasan ikut berubah; label "Sedang berjalan" mengikuti isian `ongoing`.

Belum ada sinkronisasi otomatis dengan LPSE/INAPROC; pembaruan dilakukan manual.

## Susunan organisasi

Nama dan jabatan ada di `src/react-app/data/people.ts` (dipakai halaman *Struktur Organisasi* dan *Manajemen*). Untuk menampilkan foto, taruh berkas di `public/tim/` lalu isi `photo` pada orang yang bersangkutan, mis. `photo: "/tim/anwar.jpg"`. Tanpa foto, ditampilkan lingkaran inisial.
