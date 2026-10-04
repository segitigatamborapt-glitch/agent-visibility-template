import type { IconName } from "../components/Icon";

/**
 * Pengalaman pekerjaan PT. Segi Tiga Tambora.
 * Sumber: profil penyedia di SIKaP (INAPROC), tab "Pengalaman".
 * Untuk memperbarui, tambahkan/ubah baris di `experience` (urut dari terbaru).
 */

export type CategoryKey =
	| "jalan-jembatan"
	| "gedung"
	| "dermaga"
	| "air-pantai"
	| "lainnya";

export const categories: Record<
	CategoryKey,
	{ title: string; short: string; desc: string; icon: IconName }
> = {
	"jalan-jembatan": {
		title: "Jalan & Jembatan",
		short: "Jalan & Jembatan",
		desc: "Peningkatan, rekonstruksi, dan preservasi jalan, serta pembangunan dan perbaikan jembatan.",
		icon: "road",
	},
	gedung: {
		title: "Gedung",
		short: "Gedung",
		desc: "Gedung sekolah dan perguruan tinggi, serta rumah ibadah.",
		icon: "building",
	},
	dermaga: {
		title: "Dermaga & Pelabuhan",
		short: "Dermaga",
		desc: "Pembangunan dan peningkatan dermaga penyeberangan dan dermaga marina.",
		icon: "anchor",
	},
	"air-pantai": {
		title: "Bangunan Air & Pantai",
		short: "Air & Pantai",
		desc: "Jaringan irigasi, talud pemecah ombak dan pengaman pantai, serta drainase.",
		icon: "waves",
	},
	lainnya: {
		title: "Lainnya",
		short: "Lainnya",
		desc: "Pekerjaan konstruksi lainnya.",
		icon: "structure",
	},
};

export type Experience = {
	title: string;
	location: string;
	client: string;
	province: string;
	start: string; // YYYY-MM-DD
	end: string; // YYYY-MM-DD
	value: number; // rupiah
	category: CategoryKey;
};

export const experience: Experience[] = [
	{
		title: "Pembangunan Jembatan Bailley pada Ruas Jalan Gajah Mada – Makunjung (TDF 2023)",
		location: "Kabupaten Murung Raya",
		client: "Pemerintah Daerah Kabupaten Murung Raya",
		province: "Kalimantan Tengah",
		start: "2026-09-03",
		end: "2026-12-26",
		value: 22223950392,
		category: "jalan-jembatan",
	},
	{
		title: "Pembangunan Kampung Nelayan Merah Putih di Desa Tiku Selatan, Desa Pilubang, Desa Ampalu, Desa Marunggi, dan Desa Kota Tinggi Kuranji",
		location: "Provinsi Sumatera Barat",
		client: "Kementerian Kelautan dan Perikanan",
		province: "Sumatera Barat",
		start: "2026-08-19",
		end: "2026-12-16",
		value: 21082643480,
		category: "lainnya",
	},
	{
		title: "Pembangunan Gedung Sekolah Percontohan SDN Labota Kec. Bahodopi",
		location: "Kabupaten Morowali",
		client: "Pemerintah Daerah Kabupaten Morowali",
		province: "Sulawesi Tengah",
		start: "2026-06-05",
		end: "2026-12-31",
		value: 17555999000,
		category: "gedung",
	},
	{
		title: "Preservasi Ruas Jalan Amowe – Lanipa",
		location: "Kabupaten Kolaka Utara",
		client: "Pemerintah Daerah Kabupaten Kolaka Utara",
		province: "Sulawesi Tenggara",
		start: "2026-05-25",
		end: "2026-12-20",
		value: 15225000000,
		category: "jalan-jembatan",
	},
	{
		title: "Rekonstruksi/Peningkatan Jalan Lakidende (2 Jalur)",
		location: "Kabupaten Konawe",
		client: "Pemerintah Daerah Kabupaten Konawe",
		province: "Sulawesi Tenggara",
		start: "2025-11-12",
		end: "2025-12-31",
		value: 34720000000,
		category: "jalan-jembatan",
	},
	{
		title: "Pembangunan Gedung Layanan Akademik Terpadu IAIN Madura SBSN 2024",
		location: "Kampus IAIN Madura",
		client: "Kementerian Agama – Satuan Kerja IAIN Madura",
		province: "Jawa Timur",
		start: "2024-04-26",
		end: "2024-10-24",
		value: 9496387000,
		category: "gedung",
	},
	{
		title: "Pembangunan Ruas Jalan Sumur – Taman Jaya",
		location: "Kabupaten Pandeglang",
		client: "PT. RIS Putra Delta",
		province: "Banten",
		start: "2024-03-22",
		end: "2024-11-17",
		value: 16871700000,
		category: "jalan-jembatan",
	},
	{
		title: "Pembangunan Masjid Pondok Pesantren Tahfidz Baitul Qur'an Al-Askar Kendari",
		location: "Kota Kendari",
		client: "Yayasan Pondok Pesantren Tahfidz Baitul Qur'an Al-Askar Kendari",
		province: "Sulawesi Tenggara",
		start: "2022-04-15",
		end: "2022-10-12",
		value: 17144960000,
		category: "gedung",
	},
	{
		title: "Rehabilitasi Jaringan Irigasi D.I Amohalo (DAK)",
		location: "Kota Kendari",
		client: "Pemerintah Kota Kendari",
		province: "Sulawesi Tenggara",
		start: "2021-04-23",
		end: "2021-10-19",
		value: 2717137239,
		category: "air-pantai",
	},
	{
		title: "Peningkatan Jalan Menuju Kuburan Wakaaka Kec. Wabula (Pinjaman Daerah)",
		location: "Kecamatan Wabula, Kabupaten Buton",
		client: "Pemerintah Daerah Kabupaten Buton",
		province: "Sulawesi Tenggara",
		start: "2021-04-19",
		end: "2021-09-15",
		value: 5861992846.74,
		category: "jalan-jembatan",
	},
	{
		title: "Rehabilitasi dan Rekonstruksi Bangunan Talud Pemecah Ombak dan Bangunan Talud Pengaman Pantai Gu Timur",
		location: "Kabupaten Buton Tengah",
		client: "Pemerintah Daerah Kabupaten Buton Tengah",
		province: "Sulawesi Tenggara",
		start: "2021-02-04",
		end: "2021-07-03",
		value: 3238656531,
		category: "air-pantai",
	},
	{
		title: "Peningkatan Jalan Hot Mix AC-BC",
		location: "Kecamatan Amonggedo, Kabupaten Konawe",
		client: "Pemerintah Daerah Kabupaten Konawe",
		province: "Sulawesi Tenggara",
		start: "2020-09-30",
		end: "2020-12-28",
		value: 363580000,
		category: "jalan-jembatan",
	},
	{
		title: "Peningkatan Jalan Hot Mix AC-BC",
		location: "Kecamatan Amonggedo, Kabupaten Konawe",
		client: "Pemerintah Daerah Kabupaten Konawe",
		province: "Sulawesi Tenggara",
		start: "2020-08-18",
		end: "2020-12-15",
		value: 7751862000,
		category: "jalan-jembatan",
	},
	{
		title: "Peningkatan Jalan Wakoila – Lambu Jaya (RSUD)",
		location: "Kabupaten Muna Barat",
		client: "Pemerintah Daerah Kabupaten Muna Barat",
		province: "Sulawesi Tenggara",
		start: "2020-05-08",
		end: "2020-09-04",
		value: 2671000000,
		category: "jalan-jembatan",
	},
	{
		title: "Peningkatan Jalan Asphalt Hot Mix AC-BC Poros Amesiu – Meluhu Kec. Amonggedo",
		location: "Poros Amesiu – Meluhu, Kec. Amonggedo",
		client: "Pemerintah Daerah Kabupaten Konawe",
		province: "Sulawesi Tenggara",
		start: "2019-08-30",
		end: "2019-12-28",
		value: 9082880000,
		category: "jalan-jembatan",
	},
	{
		title: "Rehabilitasi dan Renovasi Sarana dan Prasarana Sekolah Kab. Konawe, Kab. Kolaka Utara, Kab. Konawe Utara",
		location: "Kabupaten Konawe",
		client: "PT. Roda Indah Perkasa",
		province: "Sulawesi Tenggara",
		start: "2019-08-10",
		end: "2019-12-10",
		value: 3870000000,
		category: "gedung",
	},
	{
		title: "Lanjutan Peningkatan Dermaga Marina",
		location: "Kec. Wangi Wangi, Kabupaten Wakatobi",
		client: "Pemerintah Daerah Kabupaten Wakatobi",
		province: "Sulawesi Tenggara",
		start: "2018-06-25",
		end: "2018-12-21",
		value: 11468000000,
		category: "dermaga",
	},
	{
		title: "Perbaikan Jembatan S. Solongko",
		location: "S. Solongko",
		client: "Pemerintah Daerah Kabupaten Konawe Kepulauan",
		province: "Sulawesi Tenggara",
		start: "2018-01-15",
		end: "2018-06-14",
		value: 2589000000,
		category: "jalan-jembatan",
	},
	{
		title: "Pembangunan Dermaga Penyeberangan Bombana Tahap III Lintas Bombana – Tj. Phising",
		location: "Kabupaten Bombana",
		client: "Kementerian Perhubungan",
		province: "Sulawesi Tenggara",
		start: "2017-03-31",
		end: "2017-11-25",
		value: 6477000000,
		category: "dermaga",
	},
	{
		title: "Pembuatan Drainase Pasangan Batu",
		location: "Kabupaten Muna",
		client: "PT. Fatdeko Tama Waja",
		province: "Sulawesi Tenggara",
		start: "2016-05-24",
		end: "2016-11-20",
		value: 1969290000,
		category: "air-pantai",
	},
];

const rupiah = new Intl.NumberFormat("id-ID", {
	style: "currency",
	currency: "IDR",
	minimumFractionDigits: 0,
	maximumFractionDigits: 2,
});
export const formatRupiah = (n: number) => rupiah.format(n);

const dateFmt = new Intl.DateTimeFormat("id-ID", {
	day: "numeric",
	month: "long",
	year: "numeric",
	timeZone: "UTC",
});
export const formatDate = (iso: string) => dateFmt.format(new Date(iso));

export const yearOf = (iso: string) => Number(iso.slice(0, 4));

/** Sedang berjalan bila hari ini berada di antara tanggal mulai dan selesai kontrak. */
export function isOngoing(e: Experience, today = new Date()) {
	const t = today.toISOString().slice(0, 10);
	return e.start <= t && t <= e.end;
}

/** Tiga pekerjaan dengan nilai kontrak terbesar, untuk bagian "Proyek Unggulan". */
export const featured = [...experience]
	.sort((a, b) => b.value - a.value)
	.slice(0, 3);

export const summary = {
	works: experience.length,
	clients: new Set(experience.map((e) => e.client)).size,
	provinces: new Set(experience.map((e) => e.province)).size,
	since: Math.min(...experience.map((e) => yearOf(e.start))),
};
