import PageHeader from "../components/PageHeader";
import Sample from "../components/Sample";
import { projects } from "../site";

export default function Projects() {
	return (
		<>
			<PageHeader title="Proyek" parent="Pusat Informasi" />
			<section className="container section">
				<Sample />
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
			</section>
		</>
	);
}
