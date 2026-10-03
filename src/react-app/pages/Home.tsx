import { Link } from "react-router";
import HeroArt from "../components/HeroArt";
import Icon from "../components/Icon";
import Sample from "../components/Sample";
import { businessLines, projects, site, stats, values } from "../site";

export default function Home() {
	const shownStats = stats.filter((s) => s.value);

	return (
		<>
			<section className="hero">
				<div className="container hero-inner">
					<div className="hero-text">
						<p className="eyebrow">Perusahaan Konstruksi</p>
						<h1>{site.name}</h1>
						<p className="lead">{site.tagline}</p>
						<div className="hero-actions">
							<Link className="button" to="/lini-bisnis">
								Lini Bisnis
							</Link>
							<Link className="button button-ghost" to="/kontak">
								Hubungi Kami
							</Link>
						</div>
					</div>
					<HeroArt />
				</div>
			</section>

			{shownStats.length > 0 && (
				<section className="container">
					<div className="stats-card">
						{shownStats.map((s) => (
							<div key={s.label} className="stat">
								<strong>{s.value}</strong>
								<span>{s.label}</span>
							</div>
						))}
					</div>
				</section>
			)}

			<section className="section container">
				<header className="section-head">
					<h2>Lini Bisnis</h2>
					<p>Layanan konstruksi untuk berbagai kebutuhan proyek.</p>
					<Sample />
				</header>
				<div className="cards">
					{businessLines.map((b) => (
						<article key={b.title} className="card">
							<span className="icon-badge">
								<Icon name={b.icon} />
							</span>
							<h3>{b.title}</h3>
							<p>{b.desc}</p>
						</article>
					))}
				</div>
			</section>

			<section className="section-soft">
				<div className="container section">
					<header className="section-head">
						<h2>Komitmen Kami</h2>
						<p>Prinsip yang kami pegang di setiap proyek.</p>
					</header>
					<div className="values">
						{values.map((v, i) => (
							<article key={v.title} className="value">
								<span className="value-num">0{i + 1}</span>
								<h3>{v.title}</h3>
								<p>{v.desc}</p>
							</article>
						))}
					</div>
				</div>
			</section>

			<section className="section container">
				<header className="section-head">
					<h2>Proyek Unggulan</h2>
					<p>Sebagian proyek yang telah kami kerjakan.</p>
					<Sample />
				</header>
				<div className="cards cards-3">
					{projects.map((p) => (
						<article key={p.title} className="card project">
							<div className="project-img" aria-hidden="true">
								<span className="badge">{p.category}</span>
							</div>
							<h3>{p.title}</h3>
							<p>{p.meta}</p>
						</article>
					))}
				</div>
				<p className="center">
					<Link className="link-arrow" to="/proyek">
						Lihat semua proyek
					</Link>
				</p>
			</section>

			<section className="cta">
				<div className="container cta-inner">
					<div>
						<h2>Punya rencana proyek?</h2>
						<p>Diskusikan kebutuhan konstruksi Anda dengan tim kami.</p>
					</div>
					<Link className="button" to="/kontak">
						Hubungi Kami
					</Link>
				</div>
			</section>
		</>
	);
}
