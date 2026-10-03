import Icon from "../components/Icon";
import PageHeader from "../components/PageHeader";
import Sample from "../components/Sample";
import { businessLines } from "../site";

export default function Services() {
	return (
		<>
			<PageHeader title="Lini Bisnis" />
			<section className="container section">
				<Sample />
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
		</>
	);
}
