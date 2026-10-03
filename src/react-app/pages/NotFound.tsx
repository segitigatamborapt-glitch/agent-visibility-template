import { Link } from "react-router";

export default function NotFound() {
	return (
		<section className="container page">
			<h1>Halaman tidak ditemukan</h1>
			<p>
				<Link to="/">Kembali ke beranda</Link>
			</p>
		</section>
	);
}
