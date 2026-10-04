import PageHeader from "../components/PageHeader";
import { culture } from "../data/about";

export default function Culture() {
	return (
		<>
			<PageHeader title="Budaya Perusahaan" parent="Tentang Kami" />
			<section className="container section">
				<p className="lead-dark">
					Nilai-nilai yang kami pegang dalam setiap pekerjaan dan hubungan
					kerja.
				</p>
				<div className="cards">
					{culture.map((c, i) => (
						<article key={c.title} className="card">
							<span className="value-num">0{i + 1}</span>
							<h3>{c.title}</h3>
							<p>{c.desc}</p>
						</article>
					))}
				</div>
			</section>
		</>
	);
}
