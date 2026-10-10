# Panduan Repositori (Bahasa Indonesia)

Repositori ini berisi dua hal yang berbeda:

1. **Dokumen usaha ayam KUB Adeva Farm**: dashboard PDF, gambar kandang, dan RAB Excel. Ini yang dipakai untuk usaha.
2. **Template situs web "Agent Visibility"** dari Cloudflare: kode program bawaan repositori. Tidak ada hubungannya dengan usaha ayam dan tidak perlu diubah.

Kode program (file `.ts`, `.json`, `.jsonc`) tetap berbahasa Inggris karena dibaca oleh komputer. Nama perintah dan nama paket di dalamnya tidak boleh diterjemahkan, karena program akan rusak.

---

## 1. Dokumen usaha ayam KUB

| Folder / file | Isi |
|---|---|
| `dashboard-kub/Dashboard-Ayam-KUB-Petelur-Adeva-Farm.pdf` | Cetakan dashboard studi kelayakan ayam KUB petelur 1.000 ekor: modal awal, untung rugi, skenario, penetasan sendiri, pakan sendiri (jagung 1 ha, resep ransum A/B/C), mitigasi risiko, riset pasar, perencanaan, dan asumsi. Versi interaktif (slider bisa digeser) ada di tautan artifact Claude. |
| `kandang-kub-2000/RAB-Kandang-Ayam-KUB-2000-Ekor-Konawe-Selatan.xlsx` | RAB kandang standar 2.000 ekor di lahan 1 ha, harga acuan Kabupaten Konawe Selatan (sekitar Rp 1,02 miliar termasuk bangunan pendukung). |
| `kandang-kub-2000/RAB-HEMAT-Kandang-Ayam-KUB-2000-Ekor-Konawe-Selatan.xlsx` | RAB versi hemat: rangka kayu di atas umpak, atap seng (sekitar Rp 355 juta untuk 2.000 ekor, sekitar Rp 232 juta untuk tahap 1 berisi 1.000 ekor). |
| `kandang-kub-2000/gambar/G-01-rencana-tapak.png` | Rencana tapak: tata letak kandang dan bangunan di lahan 1 ha. |
| `kandang-kub-2000/gambar/G-02-denah-kandang.png` | Denah kandang. |
| `kandang-kub-2000/gambar/G-03-potongan-A-A.png` | Gambar potongan melintang kandang. |
| `kandang-kub-2000/gambar/G-04-tampak-samping-depan.png` | Tampak samping dan tampak depan. |
| `kandang-kub-2000/gambar/G-05-detail-pondasi.png` | Detail pondasi. |
| `kandang-kub-2000/gambar/gambar-kandang-2000-ekor.pdf` | Kelima gambar di atas dalam satu file PDF. |

Catatan: angka di RAB dan dashboard adalah perkiraan perencanaan. Harga bahan perlu dicek ulang ke toko bangunan, toko pakan, dan pemasok setempat sebelum dipakai untuk keputusan.

---

## 2. Template situs web (kode program)

Bagian ini bawaan template Cloudflare. Fungsinya membuat isi situs mudah dibaca oleh AI. Anda tidak perlu menyentuhnya.

| Folder / file | Isi |
|---|---|
| `src/worker/` | Program server yang berjalan di Cloudflare Workers. |
| `src/enrichment/` | Pengolah isi situs memakai Workers AI. |
| `src/lib/` | Fungsi bantu: penyimpanan data, contoh isi, dan tipe data. |
| `src/react-app/` | Tampilan halaman web (React). |
| `test/` | Pengujian otomatis. |
| `package.json` | Daftar paket (pustaka program) yang dipakai dan perintah build. |
| `package-lock.json` | Catatan versi persis setiap paket, supaya build selalu sama. Dibuat otomatis oleh npm, jangan diedit tangan. |
| `wrangler.jsonc` | Pengaturan untuk mengunggah situs ke Cloudflare. |
| `tsconfig*.json`, `vite.config.ts`, `vitest.config.ts` | Pengaturan alat build dan pengujian. |
| `worker-configuration.d.ts` | Daftar tipe yang dibuat otomatis oleh wrangler. |
| `README.md`, `AGENTS.md` | Penjelasan template dalam bahasa Inggris. |

### Tentang perubahan `package-lock.json`

Paket `@cloudflare/workers-types` dinaikkan dari versi 4 ke versi 5, karena alat `wrangler` mewajibkan versi 5. Sebelum diganti, perintah `npm install` gagal karena bentrok versi. Perubahan ini tidak memengaruhi dokumen usaha ayam.

### Tentang build Cloudflare yang gagal

Pemeriksaan "Workers Builds" di pull request masih gagal. Build di komputer pengembang berhasil, jadi penyebabnya ada di tahap build atau unggah di server Cloudflare. Lognya hanya bisa dilihat di dashboard Cloudflare (menu Workers > agent-visibility-template > Builds). Kegagalan ini tidak memengaruhi dashboard, PDF, maupun RAB.

---

## Istilah singkat

| Istilah | Arti |
|---|---|
| Repositori (repo) | Folder proyek yang disimpan di GitHub beserta riwayat perubahannya. |
| Commit | Satu catatan perubahan, seperti "simpan" disertai keterangan. |
| Branch | Cabang kerja terpisah, supaya perubahan tidak langsung mengubah versi utama. |
| Pull request (PR) | Usulan untuk menggabungkan branch ke versi utama, bisa diperiksa dulu sebelum disetujui. |
| Build | Proses mengubah kode menjadi situs yang siap dijalankan. |
| Paket / dependensi | Pustaka program buatan orang lain yang dipakai proyek ini. |
