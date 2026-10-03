import Sample from "../components/Sample";
import { businessLines } from "../site";

export default function Services() {
	return (
		<section className="container page">
			<h1>Bidang Usaha</h1>
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
	);
}
