import Sample from "../components/Sample";
import { projects } from "../site";

export default function Projects() {
	return (
		<section className="container page">
			<h1>Proyek</h1>
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
		</section>
	);
}
