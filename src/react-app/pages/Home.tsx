import { Link } from "react-router";
import { site } from "../site";

export default function Home() {
	return (
		<section className="hero">
			<h1>{site.name}</h1>
			<p className="lead">{site.tagline}</p>
			<p>Konten beranda akan diisi pada langkah berikutnya.</p>
			<Link className="button" to="/kontak">
				Hubungi Kami
			</Link>
		</section>
	);
}
