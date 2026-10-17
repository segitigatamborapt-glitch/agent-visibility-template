# Panduan Repositori (Bahasa Indonesia)

Repositori ini berisi dua hal yang berbeda:

1. **Dokumen usaha ayam KUB Adeva Farm**: dashboard PDF, gambar kandang, dan RAB Excel. Ini yang dipakai untuk usaha.
2. **Template situs web "Agent Visibility"** dari Cloudflare: kode program bawaan repositori. Tidak ada hubungannya dengan usaha ayam dan tidak perlu diubah.

Kode program (file `.ts`, `.json`, `.jsonc`) tetap berbahasa Inggris karena dibaca oleh komputer. Nama perintah dan nama paket di dalamnya tidak boleh diterjemahkan, karena program akan rusak.

---

## 1. Dokumen usaha ayam KUB

| Folder / file | Isi |
|---|---|
| `dashboard-kub/Dashboard-Ayam-KUB-Petelur-Adeva-Farm.pdf` | Cetakan dashboard studi kelayakan ayam KUB petelur 10.000 ekor: modal awal, untung rugi, skenario, penetasan sendiri, pakan sendiri (jagung 1 ha, resep ransum A/B/C, racikan telur terbaik T1/T2/T3 dan kebutuhan pakan harian), mitigasi risiko, riset pasar, perencanaan, dan asumsi. Versi interaktif (slider bisa digeser) ada di tautan artifact Claude. |
| `kandang-kub-2000/RAB-Kandang-Ayam-KUB-2000-Ekor-Konawe-Selatan.xlsx` | RAB kandang standar 2.000 ekor di lahan 1 ha, harga acuan Kabupaten Konawe Selatan (sekitar Rp 1,02 miliar termasuk bangunan pendukung). |
| `kandang-kub-2000/RAB-HEMAT-Kandang-Ayam-KUB-2000-Ekor-Konawe-Selatan.xlsx` | RAB versi hemat: rangka kayu di atas umpak, atap seng (sekitar Rp 355 juta untuk 2.000 ekor, sekitar Rp 232 juta untuk tahap 1 berisi 1.000 ekor). |
| `kandang-kub-2000/gambar/G-01-rencana-tapak.png` | Rencana tapak: tata letak kandang dan bangunan di lahan 1 ha. |
| `kandang-kub-2000/gambar/G-02-denah-kandang.png` | Denah kandang. |
| `kandang-kub-2000/gambar/G-03-potongan-A-A.png` | Gambar potongan melintang kandang. |
| `kandang-kub-2000/gambar/G-04-tampak-samping-depan.png` | Tampak samping dan tampak depan. |
| `kandang-kub-2000/gambar/G-05-detail-pondasi.png` | Detail pondasi. |
| `kandang-kub-2000/gambar/gambar-kandang-2000-ekor.pdf` | Kelima gambar di atas dalam satu file PDF. |
| `masterplan-4ha/MP-01-masterplan-4ha.png` | Masterplan lahan 4 ha (100 x 400 m) sesuai sketsa pemilik: zona servis, zona kandang semi umbaran, zona kotor, kebun jagung, embung, sungai, pagar harmonika. |
| `masterplan-4ha/MP-02-zona-servis-kandang-kotor.png` | Tata letak 245 m pertama dari jalan: bangunan servis, 6 kandang + umbaran, zona kotor, alur kerja. |
| `masterplan-4ha/MP-03-neraca-lahan-dan-rab.png` | Neraca luas lahan, alur pakan-kompos, perkiraan manfaat, rekap RAB. |
| `masterplan-4ha/Masterplan-Lahan-4-Ha-Adeva-Farm.pdf` | Ketiga gambar masterplan dalam satu file PDF. |
| `desain-konstruksi/gambar-teknik/GT-00-Masterplan-Kawasan-4-Ha.dxf` | Masterplan AutoCAD: MP-01 masterplan 4 ha skala 1:500 (kertas A0) dengan neraca lahan dan potongan kawasan, MP-02 rencana tapak zona servis 1:200 dengan tabel koordinat pematokan, MP-03 rencana sirkulasi dan jaringan air, listrik, drainase. |
| `desain-konstruksi/gambar-teknik/GT-04-Detail-Bangunan-Pendukung.dxf` | Detail bangunan pendukung (denah, tampak, potongan, spesifikasi): B-01 pos jaga + portal, B-02 kantor, B-03 mes anak kandang, B-04 rumah telur, B-05 rumah pakan, B-06 gudang pakan jadi, B-07 rumah kompos, B-08 rumah maggot BSF, B-09 dan B-10 detail 1:20 (pondasi mesin, bak lindi, sekat kompos, biopond, kusen, meja sortir, rak telur, palet, septic tank). |
| `desain-konstruksi/gambar-teknik/GT-01-Kandang-Semi-Umbaran-10x40.dxf` | Gambar teknik AutoCAD kandang 10 x 40 m (satuan cm): denah, pondasi, tampak, potongan, detail pondasi, penulangan, atap, dinding/kawat/tirai, pintu umbaran, pintu, sarang, tenggeran. PDF dengan nama sama untuk dilihat di HP. |
| `desain-konstruksi/gambar-teknik/GT-02-Kawasan-Pagar-Gerbang.dxf` | Rencana tapak 100 x 400 m, tata letak zona, unit kandang + umbaran, detail pagar harmonika + tiang beton, gerbang dan bak celup kendaraan. |
| `desain-konstruksi/gambar-teknik/GT-03-Fasilitas-Peternakan.dxf` | Gudang jagung (gudang tipikal) + tabel semua bangunan, ruang ganti, kandang karantina, lantai jemur, menara tandon + sumur bor, rumah pompa, embung. |
| `desain-konstruksi/RAB-Kawasan-Peternakan-KUB-Semi-Umbaran-Konawe-Selatan.xlsx` | RAB pola AHSP dengan harga dasar perkiraan Konawe Selatan: rekap, harga dasar, analisa, RAB kandang, 11 bangunan pendukung (sesuai GT-03 dan GT-04), pagar & umbaran, utilitas. Total sekitar Rp 5,91 miliar. |
| `animasi-sop/Animasi-SOP-Anak-Kandang-1080p.mp4` | Animasi sinematik "Sehari Bersama Anak Kandang": SOP harian 07.00–16.00 (16 langkah), kamera mengikuti pekerja kandang, durasi 3 menit 6 detik. Versi 4K (3840 x 2160) dengan nama `...-4K.mp4` bila tersedia. |
| `animasi-sop/musik-country-orisinal.mp3` | Musik latar instrumental bergaya country, komposisi orisinal (bukan lagu berhak cipta). |
| `desain-konstruksi/3d/` | Gambar render 3D (kawasan, zona servis, unit kandang, potongan, rangka atap) dan file HTML model 3D interaktif. |

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
