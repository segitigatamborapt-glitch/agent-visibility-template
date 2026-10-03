import Sample from "../components/Sample";
import { contact } from "../site";

export default function Contact() {
	return (
		<section className="container page">
			<h1>Kontak</h1>
			<Sample />
			<dl className="contact-list">
				<dt>Alamat</dt>
				<dd>{contact.address}</dd>
				<dt>Email</dt>
				<dd>{contact.email}</dd>
				<dt>Telepon</dt>
				<dd>{contact.phone}</dd>
			</dl>
			<p>Formulir kontak akan ditambahkan pada langkah berikutnya.</p>
		</section>
	);
}
