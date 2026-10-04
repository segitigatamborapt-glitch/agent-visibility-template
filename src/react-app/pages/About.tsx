import { Link } from "react-router";
import PageHeader from "../components/PageHeader";
import { experience, summary } from "../data/experience";
import { businessLines, contact, site } from "../site";

// Daftar bergaya Indonesia: "A, B dan C" (tanpa koma sebelum "dan").
const formatList = (items: string[]) =>
	items.length < 2
		? items.join("")
		: `${items.slice(0, -1).join(", ")} dan ${items[items.length - 1]}`;

const regions = [...new Set(experience.map((e) => e.province))].sort();

const rows: [string, string][] = [
	["Nama Perusahaan", site.name],
	["Bidang Usaha", "Jasa Konstruksi"],
	["Lini Pekerjaan", formatList(businessLines.map((b) => b.title))],
	["Wilayah Kerja", formatList(regions)],
	["Pengalaman Tercatat", `${summary.works} pekerjaan sejak ${summary.since}`],
	["Alamat", contact.address],
	["Email", contact.email],
	["Telepon", contact.phone],
];

export default function About() {
	return (
		<>
			<PageHeader title="Profil Perusahaan" parent="Tentang Kami" />
			<section className="container section">
				<div className="prose">
					<p className="lead-dark">
						{site.name} adalah perusahaan jasa konstruksi yang berkedudukan di
						Kota Kendari, Sulawesi Tenggara.
					</p>
					<p>
						Perusahaan mengerjakan pekerjaan{" "}
						{formatList(businessLines.map((b) => b.title.toLowerCase()))}{" "}
						untuk pemerintah daerah di {formatList(regions)}, dengan komitmen
						pada mutu, ketepatan waktu, dan keselamatan kerja.
					</p>
				</div>
				<dl className="def-list">
					{rows.map(([k, v]) => (
						<div key={k} className="def-row">
							<dt>{k}</dt>
							<dd>{v}</dd>
						</div>
					))}
				</dl>
				<div className="actions">
					<Link className="button" to="/proyek">
						Pengalaman Proyek
					</Link>
					<Link className="button button-outline" to="/kontak">
						Hubungi Kami
					</Link>
				</div>
			</section>
		</>
	);
}
