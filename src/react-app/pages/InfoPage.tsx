import { useLocation } from "react-router";
import PageHeader from "../components/PageHeader";
import Sample from "../components/Sample";
import { navItems, navLeaves } from "../site";
import NotFound from "./NotFound";

export default function InfoPage() {
	const { pathname } = useLocation();
	const leaf = navLeaves.find((l) => l.to === pathname);
	if (!leaf) return <NotFound />;
	const parent = navItems.find((i) => i.children?.some((c) => c.to === pathname));
	return (
		<>
			<PageHeader title={leaf.label} parent={parent?.label} />
			<section className="container section">
				<div className="prose">
				<Sample />
				<p>Halaman ini sedang disiapkan.</p>
				</div>
			</section>
		</>
	);
}
