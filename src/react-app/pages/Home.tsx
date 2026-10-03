import { Link } from "react-router";
import Sample from "../components/Sample";
import { businessLines, projects, site, stats } from "../site";

export default function Home() {
	return (
		<>
			<section className="hero">
				<div className="container hero-inner">
					<p className="eyebrow">Perusahaan Konstruksi</p>
					<h1>{site.name}</h1>
					<p className="lead">{site.tagline}</p>
					<div className="hero-actions">
						<Link className="button" to="/layanan">
							Bidang Usaha
						</Link>
						<Link className="button button-ghost" to="/kontak">
							Hubungi Kami
						</Link>
					</div>
				</div>
			</section>

			<section className="stats">
				<div className="container stats-grid">
					{stats.map((s) => (
						<div key={s.label} className="stat">
							<strong>{s.value}</strong>
							<span>{s.label}</span>
						</div>
					))}
				</div>
			</section>

			<section className="section container">
				<h2>Bidang Usaha</h2>
				<Sample />
				<div className="cards">
					{businessLines.map((b) => (
						<article key={b.title} className="card">
							<h3>{b.title}</h3>
							<p>{b.desc}</p>
						</article>
					))}
				</div>
			</section>

			<section className="section container">
				<h2>Proyek Unggulan</h2>
				<Sample />
				<div className="cards cards-3">
					{projects.map((p) => (
						<article key={p.title} className="card project">
							<div className="project-img" aria-hidden="true" />
							<h3>{p.title}</h3>
							<p>{p.meta}</p>
						</article>
					))}
				</div>
				<p>
					<Link to="/proyek">Lihat semua proyek &rarr;</Link>
				</p>
			</section>

			<section className="cta">
				<div className="container cta-inner">
					<h2>Punya rencana proyek?</h2>
					<p>Diskusikan kebutuhan konstruksi Anda dengan tim kami.</p>
					<Link className="button" to="/kontak">
						Hubungi Kami
					</Link>
				</div>
			</section>
		</>
	);
}
