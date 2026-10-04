import type { IconName } from "../components/Icon";

/**
 * Pengalaman pekerjaan PT. Segi Tiga Tambora.
 * Sumber: daftar pekerjaan hasil tender yang tercatat di LPSE (INAPROC).
 * `date` adalah tanggal tender; `ongoing` mengikuti status "Sedang Berjalan".
 * Untuk memperbarui, tambahkan/ubah baris di `experience`.
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
		desc: "Gedung sekolah dan bangunan gedung lainnya.",
		icon: "building",
	},
	dermaga: {
		title: "Dermaga & Pelabuhan",
		short: "Dermaga",
		desc: "Pembangunan dan peningkatan dermaga.",
		icon: "anchor",
	},
	"air-pantai": {
		title: "Bangunan Air & Pantai",
		short: "Air & Pantai",
		desc: "Jaringan irigasi serta talud pemecah ombak dan pengaman pantai.",
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
	client: string; // pemberi kerja
	province: string;
	date: string; // tanggal tender, YYYY-MM-DD
	value: number; // nilai kontrak, rupiah
	category: CategoryKey;
	lpse?: string; // nomor paket LPSE
	ongoing?: boolean; // status "Sedang Berjalan"
};

export const experience: Experience[] = [
	{
		title: "Pembangunan Gedung Sekolah Percontohan SDN Labota Kec. Bahodopi",
		client: "Kabupaten Morowali",
		province: "Sulawesi Tengah",
		date: "2026-06-05",
		value: 17555999000,
		category: "gedung",
		lpse: "10134063000",
		ongoing: true,
	},
	{
		title: "Preservasi Ruas Jalan Amowe – Lanipa",
		client: "Kabupaten Kolaka Utara",
		province: "Sulawesi Tenggara",
		date: "2026-05-25",
		value: 15225000000,
		category: "jalan-jembatan",
		lpse: "10130945000",
		ongoing: true,
	},
	{
		title: "Pembangunan Gudang",
		client: "Konda 1 Kabupaten Konawe Selatan",
		province: "Sulawesi Tenggara",
		date: "2025-11-27",
		value: 895850000,
		category: "gedung",
	},
	{
		title: "Rekonstruksi/Peningkatan Jalan Lakidende (2 Jalur)",
		client: "Kabupaten Konawe",
		province: "Sulawesi Tenggara",
		date: "2025-10-30",
		value: 34810290000,
		category: "jalan-jembatan",
		lpse: "10085372000",
	},
	{
		title: "Rekonstruksi/Peningkatan Kapasitas Struktur Jalan Asphalt Hot Mix AC-BC Poros Matanggorai – Atodopi",
		client: "Kabupaten Konawe",
		province: "Sulawesi Tenggara",
		date: "2021-04-25",
		value: 3800000000,
		category: "jalan-jembatan",
		lpse: "1828525",
	},
	{
		title: "Peningkatan Jalan Menuju Kuburan Wakaaka Kec. Wabula (Pinjaman Daerah)",
		client: "Kabupaten Buton",
		province: "Sulawesi Tenggara",
		date: "2021-03-18",
		value: 6000000000,
		category: "jalan-jembatan",
		lpse: "3274451",
	},
	{
		title: "Rehabilitasi Jaringan Irigasi D.I Amohalo (DAK)",
		client: "Kota Kendari",
		province: "Sulawesi Tenggara",
		date: "2021-03-18",
		value: 3017430000,
		category: "air-pantai",
		lpse: "2475571",
	},
	{
		title: "Lanjutan Peningkatan Jalan Abadi Jaya – Kembar Maminasa (DAK)",
		client: "Kabupaten Muna Barat",
		province: "Sulawesi Tenggara",
		date: "2021-02-08",
		value: 3053282380,
		category: "jalan-jembatan",
		lpse: "2651689",
	},
	{
		title: "Peningkatan Jalan Abadi – Jaya – Kembar Maminasa (DAK)",
		client: "Kabupaten Muna Barat",
		province: "Sulawesi Tenggara",
		date: "2021-01-29",
		value: 4500000000,
		category: "jalan-jembatan",
		lpse: "2651689",
	},
	{
		title: "Rehabilitasi dan Rekonstruksi Bangunan Talud Pemecah Ombak dan Bangunan Talud Pengaman Pantai Gu Timur",
		client: "Kabupaten Buton Tengah",
		province: "Sulawesi Tenggara",
		date: "2021-01-11",
		value: 3325000000,
		category: "air-pantai",
		lpse: "894728",
	},
	{
		title: "Peningkatan Jalan Asphalt Hot Mix AC-BC Poros Dunggua – Benua",
		client: "Kabupaten Konawe",
		province: "Sulawesi Tenggara",
		date: "2020-09-04",
		value: 3661833000,
		category: "jalan-jembatan",
		lpse: "1786525",
	},
	{
		title: "Peningkatan Jalan Asphalt Hot Mix AC-BC Jaring Jalan Dalam Kecamatan Amonggedo",
		client: "Kabupaten Konawe",
		province: "Sulawesi Tenggara",
		date: "2020-07-12",
		value: 7800000000,
		category: "jalan-jembatan",
		lpse: "1703525",
	},
	{
		title: "Peningkatan Jalan Wakoila – Lombu Jaya (RSUD)",
		client: "Kabupaten Muna Barat",
		province: "Sulawesi Tenggara",
		date: "2020-02-24",
		value: 2690200000,
		category: "jalan-jembatan",
		lpse: "1986689",
	},
	{
		title: "Peningkatan Jalan Asphalt Hot Mix AC-BC Poros Amesiu – Meluhu Kec. Amonggedo",
		client: "Kabupaten Konawe",
		province: "Sulawesi Tenggara",
		date: "2019-08-14",
		value: 9181887000,
		category: "jalan-jembatan",
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

export const isOngoing = (e: Experience) => Boolean(e.ongoing);

/** Tiga pekerjaan dengan nilai kontrak terbesar, untuk bagian "Proyek Unggulan". */
export const featured = [...experience]
	.sort((a, b) => b.value - a.value)
	.slice(0, 3);

export const summary = {
	works: experience.length,
	clients: new Set(experience.map((e) => e.client)).size,
	provinces: new Set(experience.map((e) => e.province)).size,
	since: Math.min(...experience.map((e) => yearOf(e.date))),
};
