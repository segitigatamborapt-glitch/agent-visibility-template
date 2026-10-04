import { Link } from "react-router";
import Icon from "../components/Icon";
import PageHeader from "../components/PageHeader";
import { businessLines } from "../site";

export default function Services() {
	return (
		<>
			<PageHeader title="Lini Bisnis" />
			<section className="container section">
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
		</>
	);
}
