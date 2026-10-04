import { Link } from "react-router";
import HeroSlider from "../components/HeroSlider";
import Icon from "../components/Icon";
import { categories, featured, formatRupiah, yearOf } from "../data/experience";
import { businessLines, stats, values } from "../site";

export default function Home() {
	const shownStats = stats.filter((s) => s.value);

	return (
		<>
			<HeroSlider />

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
					<p>Bidang pekerjaan yang telah kami tangani.</p>
				</header>
				<div className="cards cards-4">
					{businessLines.map((b) => (
						<Link
							key={b.slug}
							to={`/lini-bisnis/${b.slug}`}
							className="card card-link"
						>
							<span className="icon-badge">
								<Icon name={b.icon} />
							</span>
							<h3>{b.title}</h3>
							<p>{b.desc}</p>
							<span className="line-count">{b.count} pekerjaan</span>
						</Link>
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
					<p>Pekerjaan dengan nilai kontrak terbesar yang pernah kami tangani.</p>
				</header>
				<div className="cards cards-3">
					{featured.map((p) => (
						<article key={p.title} className="card project">
							<div className="project-img" aria-hidden="true">
								<span className="badge">{categories[p.category].short}</span>
							</div>
							<h3>{p.title}</h3>
							<p>
								{p.location} · {yearOf(p.start)}
							</p>
							<p className="project-value">{formatRupiah(p.value)}</p>
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
