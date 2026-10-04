import { Link } from "react-router";

export default function PageHeader({
	title,
	parent,
}: {
	title: string;
	parent?: string;
}) {
	return (
		<section className="page-banner">
			<div className="container">
				<nav aria-label="Breadcrumb" className="crumbs">
					<Link to="/">Beranda</Link>
					{parent && <span>{parent}</span>}
					<span aria-current="page">{title}</span>
				</nav>
				<h1>{title}</h1>
			</div>
		</section>
	);
}
