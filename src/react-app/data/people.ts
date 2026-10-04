/**
 * Susunan organisasi PT. Segi Tiga Tambora.
 * Foto (opsional): taruh berkas di `public/tim/` lalu isi `photo`, mis.
 * photo: "/tim/anwar.jpg". Tanpa foto, ditampilkan lingkaran inisial.
 */

export type GroupKey =
	| "pendiri"
	| "komisaris"
	| "manajemen"
	| "teknik"
	| "keuangan";

export const groups: { key: GroupKey; title: string }[] = [
	{ key: "pendiri", title: "Pendiri" },
	{ key: "komisaris", title: "Dewan Komisaris" },
	{ key: "manajemen", title: "Manajemen" },
	{ key: "teknik", title: "Teknik" },
	{ key: "keuangan", title: "Keuangan" },
];

export type Person = {
	name: string;
	role: string;
	group: GroupKey;
	photo?: string;
};

export const people: Person[] = [
	{ name: "Anwar", role: "Co-Founder", group: "pendiri" },
	{ name: "Ima Nur Aini", role: "Komisaris Utama", group: "komisaris" },
	{ name: "Nur Farid Habib", role: "Komisaris", group: "komisaris" },
	{ name: "Muhammad Fatur Aditia", role: "Komisaris", group: "komisaris" },
	{
		name: "Muhammad Amin Kusnandi",
		role: "General Manager",
		group: "manajemen",
	},
	{
		name: "La Ode Andreas",
		role: "Senior Architect / Engineer",
		group: "teknik",
	},
	{ name: "Khamila", role: "Finance Controller", group: "keuangan" },
];

export const groupTitle = (key: GroupKey) =>
	groups.find((g) => g.key === key)?.title ?? "";

export const initials = (name: string) => {
	const w = name.split(/\s+/).filter(Boolean);
	return (w[0][0] + (w.length > 1 ? w[w.length - 1][0] : "")).toUpperCase();
};
