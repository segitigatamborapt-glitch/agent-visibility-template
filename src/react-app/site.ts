import { culture } from "./data/about";
import {
	categories,
	experience,
	summary,
	type CategoryKey,
} from "./data/experience";

export const site = {
	// Logo (SVG/PNG) di folder `public/`. Kosongkan untuk memakai lambang
	// segitiga sederhana.
	logo: "/logo-lencana.svg" as string,
	// true: nama perusahaan ditulis sebagai teks di samping logo (untuk logo
	// yang tidak memuat nama dalam ukuran terbaca). false: logo sudah memuat nama.
	logoShowName: true,
	name: "PT. Segi Tiga Tambora",
	shortName: "Segi Tiga Tambora",
	tagline: "Membangun dengan mutu, ketepatan waktu, dan keselamatan kerja.",
	description: "PT. Segi Tiga Tambora, perusahaan konstruksi.",
};

// Lini bisnis diturunkan dari kategori pekerjaan pada data pengalaman.
export const businessLines = (
	["jalan-jembatan", "gedung", "dermaga", "air-pantai"] as CategoryKey[]
).map((key) => ({
	slug: key,
	title: categories[key].title,
	desc: categories[key].desc,
	icon: categories[key].icon,
	count: experience.filter((e) => e.category === key).length,
})).filter((b) => b.count > 0);

export type NavChild = { label: string; to: string };
export type NavItem = { label: string; to?: string; children?: NavChild[] };

// CONTOH — struktur menu mengikuti pola situs korporat; sesuaikan seperlunya.
export const navItems: NavItem[] = [
	{
		label: "Tentang Kami",
		children: [
			{ label: "Visi dan Misi", to: "/tentang/visi-dan-misi" },
			{ label: "Jejak Langkah", to: "/tentang/jejak-langkah" },
			{ label: "Profil Perusahaan", to: "/tentang" },
			{ label: "Budaya Perusahaan", to: "/tentang/budaya-perusahaan" },
			{ label: "Struktur Organisasi", to: "/tentang/struktur-organisasi" },
			{ label: "Manajemen", to: "/tentang/manajemen" },
			{ label: "Kebijakan Perusahaan", to: "/tentang/kebijakan-perusahaan" },
		],
	},
	{ label: "Informasi Keuangan", to: "/informasi-keuangan" },
	{
		label: "Lini Bisnis",
		children: [
			{ label: "Semua Lini Bisnis", to: "/lini-bisnis" },
			...businessLines.map((b) => ({
				label: b.title,
				to: `/lini-bisnis/${b.slug}`,
			})),
		],
	},
	{
		label: "Keselamatan & Mutu",
		children: [
			{ label: "Kebijakan K3 / SMKK", to: "/keselamatan-mutu/k3-smkk" },
			{ label: "Kebijakan Mutu", to: "/keselamatan-mutu/mutu" },
			{ label: "Kebijakan Lingkungan", to: "/keselamatan-mutu/lingkungan" },
		],
	},
	{
		label: "Pusat Informasi",
		children: [
			{ label: "Berita", to: "/informasi/berita" },
			{ label: "Pengalaman Proyek", to: "/proyek" },
			{ label: "Galeri", to: "/informasi/galeri" },
			{ label: "Unduhan", to: "/informasi/unduhan" },
		],
	},
	{ label: "Karier", to: "/karier" },
	{ label: "Kontak", to: "/kontak" },
];

export const navLeaves: NavChild[] = navItems.flatMap((item) =>
	item.children ? item.children : item.to ? [{ label: item.label, to: item.to }] : [],
);

// Komitmen di beranda mengikuti tiga nilai pertama budaya perusahaan.
export const values = culture.slice(0, 3);

// Angka diturunkan otomatis dari data pengalaman (`data/experience.ts`).
export const stats = [
	{ value: String(summary.works), label: "Referensi Pekerjaan" },
	{ value: String(summary.clients), label: "Pemberi Kerja" },
	{ value: String(summary.provinces), label: "Provinsi" },
	{ value: String(summary.since), label: "Rekam Jejak Sejak" },
];

export const contact = {
	address: "Lrg. Manggis, Andounohu, Kota Kendari",
	email: "segitigatamborapt@gmail.com",
	phone: "+62 821-1455-5569",
	// Tautan untuk klik langsung (nomor tanpa spasi/tanda hubung)
	phoneHref: "tel:+6282114555569",
};
