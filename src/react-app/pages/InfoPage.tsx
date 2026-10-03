import { useLocation } from "react-router";
import Sample from "../components/Sample";
import { navLeaves } from "../site";
import NotFound from "./NotFound";

export default function InfoPage() {
	const { pathname } = useLocation();
	const leaf = navLeaves.find((l) => l.to === pathname);
	if (!leaf) return <NotFound />;
	return (
		<section className="container page">
			<h1>{leaf.label}</h1>
			<Sample />
			<p>Halaman ini sedang disiapkan.</p>
		</section>
	);
}
