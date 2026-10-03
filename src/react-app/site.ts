export const site = {
	name: "PT. Segi Tiga Tambora",
	shortName: "Segi Tiga Tambora",
	tagline: "Membangun dengan mutu, ketepatan waktu, dan keselamatan kerja.",
	description: "PT. Segi Tiga Tambora, perusahaan konstruksi.",
};

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
			{ label: "Anak Perusahaan", to: "/tentang/anak-perusahaan" },
			{ label: "Kebijakan Perusahaan", to: "/tentang/kebijakan-perusahaan" },
		],
	},
	{
		label: "Informasi Keuangan",
		children: [
			{ label: "Laporan Tahunan", to: "/keuangan/laporan-tahunan" },
			{ label: "Laporan Keuangan", to: "/keuangan/laporan-keuangan" },
		],
	},
	{
		label: "Lini Bisnis",
		children: [
			{ label: "Semua Lini Bisnis", to: "/lini-bisnis" },
			{ label: "Konstruksi Gedung", to: "/lini-bisnis/konstruksi-gedung" },
			{ label: "Infrastruktur", to: "/lini-bisnis/infrastruktur" },
			{ label: "Sipil & Struktur", to: "/lini-bisnis/sipil-struktur" },
		],
	},
	{
		label: "GCG",
		children: [
			{ label: "Pedoman GCG", to: "/gcg/pedoman" },
			{ label: "Pelaporan Pelanggaran", to: "/gcg/pelaporan-pelanggaran" },
		],
	},
	{
		label: "ESG",
		children: [
			{ label: "Keberlanjutan", to: "/esg/keberlanjutan" },
			{ label: "K3 & Lingkungan", to: "/esg/k3-lingkungan" },
		],
	},
	{
		label: "Pusat Informasi",
		children: [
			{ label: "Berita", to: "/informasi/berita" },
			{ label: "Proyek", to: "/proyek" },
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

export type IconName =
	| "building"
	| "road"
	| "structure"
	| "bolt"
	| "wrench"
	| "truck";

// CONTOH — sesuaikan dengan bidang usaha sebenarnya.
export const businessLines: {
	title: string;
	desc: string;
	icon: IconName;
}[] = [
	{
		title: "Konstruksi Gedung",
		desc: "Perkantoran, hunian, dan fasilitas umum.",
		icon: "building",
	},
	{
		title: "Infrastruktur",
		desc: "Jalan, jembatan, dan drainase.",
		icon: "road",
	},
	{
		title: "Sipil & Struktur",
		desc: "Pondasi, struktur beton, dan baja.",
		icon: "structure",
	},
	{
		title: "Mekanikal & Elektrikal",
		desc: "Instalasi MEP untuk bangunan dan industri.",
		icon: "bolt",
	},
	{
		title: "Renovasi & Perawatan",
		desc: "Perbaikan dan peningkatan bangunan existing.",
		icon: "wrench",
	},
	{
		title: "Penyewaan Alat Berat",
		desc: "Dukungan peralatan untuk proyek konstruksi.",
		icon: "truck",
	},
];

// Nilai perusahaan — diturunkan dari tagline; sesuaikan.
export const values = [
	{
		title: "Mutu",
		desc: "Standar kualitas yang konsisten di setiap tahap pekerjaan.",
	},
	{
		title: "Ketepatan Waktu",
		desc: "Perencanaan dan pengendalian jadwal yang disiplin.",
	},
	{
		title: "Keselamatan Kerja",
		desc: "Keselamatan dan kesehatan kerja sebagai prioritas utama.",
	},
];

// Isi `value` dengan angka nyata (mis. "15+"); bagian ini disembunyikan
// otomatis selama semua nilainya masih kosong.
export const stats = [
	{ value: "", label: "Tahun Pengalaman" },
	{ value: "", label: "Proyek Selesai" },
	{ value: "", label: "Tenaga Ahli" },
	{ value: "", label: "Klien" },
];

// CONTOH — ganti dengan proyek nyata.
export const projects = [
	{ title: "Nama Proyek 1", category: "Kategori", meta: "Lokasi · Tahun" },
	{ title: "Nama Proyek 2", category: "Kategori", meta: "Lokasi · Tahun" },
	{ title: "Nama Proyek 3", category: "Kategori", meta: "Lokasi · Tahun" },
];

// CONTOH — ganti dengan data kontak nyata.
export const contact = {
	address: "Alamat kantor akan diisi",
	email: "email@perusahaan.example",
	phone: "Nomor telepon akan diisi",
};
