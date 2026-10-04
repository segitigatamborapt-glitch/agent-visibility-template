import { Link } from "react-router";
import PageHeader from "../components/PageHeader";

export default function NotFound() {
	return (
		<>
			<PageHeader title="Halaman tidak ditemukan" />
			<section className="container section">
				<p>Alamat yang Anda tuju tidak tersedia.</p>
				<p>
					<Link className="link-arrow" to="/">
						Kembali ke beranda
					</Link>
				</p>
			</section>
		</>
	);
}
