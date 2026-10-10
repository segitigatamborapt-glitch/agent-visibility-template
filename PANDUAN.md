# Panduan — AI Agent Visibility

Panduan berbahasa Indonesia untuk memasang, mengonfigurasi, dan menjalankan
template ini. Untuk referensi lengkap dalam bahasa Inggris, lihat
[README.md](./README.md).

## Apa ini?

Pencarian kini bergeser dari daftar tautan ke jawaban yang disusun oleh AI.
Agar konten Anda muncul di jawaban tersebut, konten harus mudah dibaca oleh
agen AI dan crawler — dalam format apa pun yang dicari masing-masing agen.

Template ini adalah sebuah Cloudflare Worker yang:

1. **Memperkaya** (enrich) konten Anda satu kali dengan
   [Workers AI](https://developers.cloudflare.com/workers-ai/) — menghasilkan
   judul yang rapi, ringkasan ramah-agen, poin-poin kunci, dan tag topik.
2. **Menyimpan** hasilnya di [KV](https://developers.cloudflare.com/kv/)
   sebagai cache.
3. **Menyajikan** satu sumber data yang sama ke banyak "permukaan" (surface)
   penemuan agen:

| Surface                             | Kegunaan                                                       |
| ----------------------------------- | -------------------------------------------------------------- |
| `/llms.txt`, `/llms-full.txt`       | Indeks sesuai konvensi [llms.txt](https://llmstxt.org)         |
| `/index.json`                       | Indeks JSON bertipe untuk agen terstruktur                     |
| `/<slug>.md`                        | Markdown bersih per halaman, cocok untuk grounding dan sitasi  |
| `/robots.txt`                       | Direktif eksplisit yang mengizinkan crawler AI tertentu        |
| Header `Content-Signal`             | Menyatakan bagaimana agen boleh memakai konten Anda            |
| `/jsonld`, `/<slug>.jsonld`         | Data terstruktur schema.org (JSON-LD)                          |
| Web Bot Auth _(opsional)_           | Verifikasi identitas agen yang menandatangani permintaannya    |

Tersedia juga UI di URL root untuk melihat dan menyalin setiap surface secara
langsung.

## Prasyarat

- Node.js dan npm
- Akun Cloudflare (Workers, Workers AI, dan KV)
- `wrangler` (sudah termasuk di `devDependencies`)

## Instalasi cepat

Membuat proyek baru dari template dengan C3:

```bash
npm create cloudflare@latest -- --template=cloudflare/templates/agent-visibility-template
```

Atau, dari salinan repo ini:

1. **Pasang dependensi**

   ```bash
   npm install
   ```

2. **Buat namespace KV**, lalu ganti `id` contoh di `wrangler.jsonc`
   (bagian `kv_namespaces`) dengan ID yang dihasilkan:

   ```bash
   npx wrangler kv namespace create VISIBILITY_CACHE
   ```

3. **Atur identitas situs** di `wrangler.jsonc` pada bagian `vars`
   (`SITE_NAME`, `SITE_DESCRIPTION`).

4. **(Opsional) Atur token admin** agar rute `POST` aktif. Selama belum diatur,
   rute tersebut selalu mengembalikan `401`:

   ```bash
   npx wrangler secret put ADMIN_TOKEN
   ```

5. **Jalankan secara lokal**

   ```bash
   npm run dev
   ```

6. **Deploy**

   ```bash
   npm run deploy
   ```

Setelah mengubah `wrangler.jsonc`, jalankan ulang `npx wrangler types`.

## Setelah deploy

Worker langsung aktif dengan konten contoh — tanpa sumber data tambahan. Buka
URL root untuk UI penjelajah surface, lalu periksa:

- `https://<worker-anda>/llms.txt` dan `/llms-full.txt`
- `https://<worker-anda>/index.json`
- `https://<worker-anda>/getting-started.md` (slug contoh mana pun)
- `https://<worker-anda>/robots.txt`

Permintaan pertama ke sebuah surface akan memperkaya konten dengan Workers AI
dan menyimpannya di cache; permintaan berikutnya dilayani dari KV.

## Konfigurasi

Semua variabel ada di `wrangler.jsonc` pada bagian `vars`:

| Variabel               | Keterangan                                                      | Bawaan                                     |
| ---------------------- | --------------------------------------------------------------- | ------------------------------------------ |
| `SITE_NAME`            | Nama situs, tampil di semua surface                             | `Acme Docs`                                |
| `SITE_DESCRIPTION`     | Deskripsi satu baris untuk agen                                 | _(contoh)_                                 |
| `AI_MODEL`             | Model Workers AI untuk enrichment                               | `@cf/meta/llama-3.3-70b-instruct-fp8-fast` |
| `ENRICHMENT_CACHE_TTL` | Lama cache hasil enrichment di KV (detik)                       | `3600`                                     |
| `CONTENT_SIGNAL`       | Kebijakan Content-Signal (di robots.txt dan sebagai header)     | `ai-input=yes, search=yes, ai-train=no`    |
| `ENABLE_WEB_BOT_AUTH`  | Mengaktifkan surface identitas agen yang opsional               | `false`                                    |

Secret (diatur dengan `npx wrangler secret put <NAMA>`, jangan di-commit):

| Secret        | Keterangan                                                                                         |
| ------------- | -------------------------------------------------------------------------------------------------- |
| `ADMIN_TOKEN` | Bearer token untuk rute yang mengubah data (`POST /api/resources`, `POST /api/refresh`).           |

## Menambahkan konten sendiri

**Opsi A — ubah sumber kode.** Ganti isi `SAMPLE_RESOURCES` di
`src/lib/content.ts` dengan halaman Anda, lalu deploy ulang. Setiap entri
berbentuk:

```ts
{
	slug: "tentang-kami",                    // unik, huruf kecil/angka/tanda hubung
	url: "https://contoh.com/tentang-kami",  // URL kanonik untuk manusia
	title: "Tentang Kami",                   // opsional; jika kosong, AI akan membuatnya
	body: "# Tentang Kami\n\n...",           // HTML atau Markdown
}
```

**Opsi B — kirim lewat API saat runtime.** Dengan `ADMIN_TOKEN` sudah diatur:

```bash
curl -X POST https://worker-anda.workers.dev/api/resources \
  -H "authorization: Bearer $ADMIN_TOKEN" \
  -H "content-type: application/json" \
  -d '{"slug":"tentang-kami","url":"https://contoh.com/tentang-kami","title":"Tentang Kami","body":"<h1>Tentang kami</h1>..."}'
```

Aturan validasi:

- `slug` harus cocok dengan `^[a-z0-9-]{1,63}$`
- `url` harus `http` atau `https`
- `body` maksimal 100 KB
- Store menampung maksimal 100 resource

Panggil `POST /api/refresh` (juga butuh token) untuk mengosongkan cache dan
memperkaya ulang dari sumber.

## Daftar endpoint

| Metode | Path                                  | Keterangan                                                 |
| ------ | ------------------------------------- | ---------------------------------------------------------- |
| GET    | `/llms.txt`                           | Indeks llms.txt (Markdown)                                 |
| GET    | `/llms-full.txt`                      | Seluruh konten dalam satu file (Markdown)                  |
| GET    | `/index.json`                         | Indeks JSON bertipe                                        |
| GET    | `/:slug.md`                           | Markdown per halaman                                       |
| GET    | `/:slug.jsonld`                       | JSON-LD schema.org per halaman                             |
| GET    | `/jsonld`                             | JSON-LD schema.org tingkat situs                           |
| GET    | `/robots.txt`                         | Direktif untuk bot AI                                      |
| GET    | `/api/site`                           | Konfigurasi situs + daftar surface (dipakai UI)            |
| GET    | `/api/resources`                      | Semua resource yang sudah diperkaya (JSON)                 |
| GET    | `/api/resources/:slug`                | Satu resource                                              |
| POST   | `/api/resources`                      | Tambah/ganti resource _(butuh `ADMIN_TOKEN`)_              |
| POST   | `/api/refresh`                        | Kosongkan cache enrichment _(butuh `ADMIN_TOKEN`)_         |
| GET    | `/.well-known/web-bot-auth/directory` | Kunci agen tepercaya _(jika diaktifkan)_                   |
| POST   | `/api/identity`                       | Verifikasi permintaan agen yang ditandatangani _(jika diaktifkan)_ |

## Cara kerja cache

- Enrichment adalah langkah yang mahal (satu panggilan Workers AI per halaman),
  sehingga hasilnya disimpan di KV dan dipakai ulang sampai
  `ENRICHMENT_CACHE_TTL` habis (bawaan 1 jam).
- `POST /api/resources` hanya memperkaya halaman yang baru/berubah lalu
  memperbarui cache.
- Jika Workers AI sedang tidak tersedia, Worker memakai enrichment cadangan
  yang deterministik dan hanya menyimpannya selama 60 detik, sehingga gangguan
  sesaat tidak merusak surface selama satu TTL penuh.

## Web Bot Auth (opsional)

Semua fitur di atas membuat konten **dapat dibaca**. Web Bot Auth menangani
hal lain: membuktikan **siapa** agen yang mengakses, melalui permintaan yang
ditandatangani ([RFC 9421](https://www.rfc-editor.org/rfc/rfc9421), Ed25519).

- Nonaktif secara bawaan; aktifkan dengan `ENABLE_WEB_BOT_AUTH=true`.
- Ganti kunci contoh di `src/lib/web-bot-auth.ts` dengan kunci agen yang
  benar-benar Anda percayai.
- Ini adalah implementasi referensi minimal — tinjau draf Web Bot Auth terbaru
  sebelum memakainya di produksi.

## Struktur proyek

```
src/
  worker/index.ts        Aplikasi Hono: rute untuk setiap surface + API JSON
  enrichment/index.ts    Enrichment Workers AI (halaman mentah -> Resource terstruktur)
  enrichment/surfaces.ts Fungsi render murni, satu per surface
  lib/store.ts           Store berbasis KV (get / upsert / clear)
  lib/content.ts         Konten contoh (data demo tanpa konfigurasi)
  lib/types.ts           Tipe bersama (Resource, RawResource, Env, SiteConfig)
  lib/web-bot-auth.ts    Modul identitas agen OPSIONAL (nonaktif bawaan)
  react-app/             UI penjelajah surface
test/index.test.ts       Tes Worker (vitest-pool-workers, lewat SELF.fetch)
```

## Menambahkan surface baru

1. Tambahkan fungsi render murni (tanpa I/O) di `src/enrichment/surfaces.ts`.
2. Tambahkan rute di `src/worker/index.ts` (kirim header `Content-Signal` untuk
   surface teks/JSON; tambahkan `cors()` bila agen mengaksesnya lintas origin).
3. Masukkan ke daftar `surfaces` di `/api/site` agar tampil di UI.
4. Jika path-nya harus ditangani Worker lebih dulu, tambahkan ke
   `assets.run_worker_first` di `wrangler.jsonc`.
5. Tambahkan tes di `test/index.test.ts`.

## Validasi dan pengujian

```bash
npm run build   # tsc -b && vite build
npm test        # vitest
npm run check   # build + wrangler deploy --dry-run
```

Rangkaian tes mengisi cache KV terlebih dahulu sebelum mengakses surface
publik, sehingga dapat berjalan tanpa memanggil Workers AI.

## Keterbatasan yang diketahui

- **Enrichment berjalan di jalur permintaan.** Permintaan pertama saat cache
  kosong memperkaya semua halaman secara langsung sehingga lebih lambat. Untuk
  situs besar, pindahkan ke [Queue](https://developers.cloudflare.com/queues/)
  atau [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/).
- **Store disimpan dalam dua key KV** dan dibatasi 100 resource / 100 KB per
  body. Untuk katalog besar, gunakan satu key per resource (atau D1) dan
  tambahkan paginasi.
- **KV bersifat eventually consistent.** Setelah `POST`, region lain mungkin
  sesaat masih menyajikan versi lama.
- **Penulisan runtime memakai pola baca-ubah-tulis KV.** Hindari penulisan
  bersamaan; untuk banyak penulis, serialisasikan lewat Durable Object atau
  pindahkan store ke D1.

## Pemecahan masalah

| Gejala                                   | Penyebab / solusi                                                                 |
| ---------------------------------------- | --------------------------------------------------------------------------------- |
| `POST` selalu `401`                      | `ADMIN_TOKEN` belum diatur, atau header `authorization: Bearer ...` salah.         |
| Permintaan pertama lambat                | Normal — enrichment sedang berjalan. Permintaan berikutnya dilayani dari cache.   |
| Ringkasan tampak sederhana/generik       | Workers AI sempat gagal; enrichment cadangan dipakai dan akan diulang ±60 detik.  |
| Perubahan konten belum terlihat          | Tunggu TTL habis, atau panggil `POST /api/refresh`.                               |
| Error binding KV saat deploy             | ID namespace di `wrangler.jsonc` masih ID contoh; ganti dengan ID milik Anda.      |
