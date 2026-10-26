# Gambar Rencana Teknis — Rumah Makan "Selera Nusantara"

Set gambar teknis (A3, 11 lembar) untuk rumah makan 1 lantai, kapasitas ± 66 kursi
(42 kursi dalam + 24 kursi teras), lahan asumsi 28 × 33 m, luas bangunan 244,8 m² + teras 48,9 m².

| No. | Judul | Skala |
|-----|-------|-------|
| A-00 | Sampul, perspektif aksonometrik, daftar gambar | — |
| A-01 | Denah situasi (site plan) | 1:200 |
| A-02 | Denah lantai 1 — arsitektur | 1:100 |
| A-03 | Denah layout furnitur & peralatan | 1:100 |
| A-04 | Denah pondasi & sloof | 1:100 |
| A-05 | Tampak depan & belakang | 1:100 |
| A-06 | Tampak kiri & kanan | 1:100 |
| A-07 | Potongan I-I & II-II | 1:100 |
| A-08 | Rencana atap | 1:100 |
| A-09 | Detail konstruksi | 1:25 / 1:5 |
| A-10 | Jadwal pintu, jendela, finishing & peralatan | — |

- `rumah-makan-gambar-teknis.pdf` — seluruh lembar (A3 landscape, vektor)
- `sheets/*.svg` — tiap lembar sebagai SVG
- `index.html` — pratinjau semua lembar di browser
- `src/` — generator (Python). Satu sumber data (`bldg.py`) dipakai oleh denah, tampak, potongan, atap, dan jadwal sehingga semua gambar konsisten.

## Membangun ulang

```bash
cd src
python3 build.py                              # tulis sheets/*.svg
NODE_PATH=$(npm root -g) node make-pdf.cjs    # tulis PDF + index.html (butuh playwright)
```

Ubah ukuran/ruang di `src/bldg.py` (dinding `WALLS`, bukaan `OPS`, furnitur) lalu bangun ulang.

## Catatan

Ini rencana awal berbasis asumsi (ukuran lahan, orientasi, program ruang). Struktur, MEP, dan
kesesuaian dengan peraturan setempat (GSB/KDB, sanitasi, K3, izin) wajib diverifikasi oleh tenaga ahli.
