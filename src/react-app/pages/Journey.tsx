import { Link } from "react-router";
import PageHeader from "../components/PageHeader";
import { experience, summary, yearOf } from "../data/experience";

const years = [...new Set(experience.map((e) => yearOf(e.date)))].sort(
	(a, b) => b - a,
);

export default function Journey() {
	return (
		<>
			<PageHeader title="Jejak Langkah" parent="Tentang Kami" />
			<section className="container section">
				<p className="lead-dark">
					Sejak {summary.since}, {summary.works} pekerjaan tercatat dalam rekam
					jejak kami.
				</p>
				<ol className="timeline">
					{years.map((y) => {
						const works = experience.filter((e) => yearOf(e.date) === y);
						return (
							<li key={y}>
								<span className="timeline-year">{y}</span>
								<p className="timeline-sum">{works.length} pekerjaan tercatat</p>
								<ul>
									{works.map((w) => (
										<li key={w.title + w.date}>
											{w.title} <span>— {w.client}</span>
										</li>
									))}
								</ul>
							</li>
						);
					})}
				</ol>
				<p className="source-note">
					Sebagian pekerjaan hasil tender yang tercatat di LPSE (INAPROC).{" "}
					<Link className="link-arrow" to="/proyek">
						Lihat pengalaman proyek
					</Link>
				</p>
			</section>
		</>
	);
}
