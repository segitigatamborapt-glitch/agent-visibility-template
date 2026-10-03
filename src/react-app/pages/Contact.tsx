import Icon from "../components/Icon";
import PageHeader from "../components/PageHeader";
import Sample from "../components/Sample";
import { contact } from "../site";

const rows = [
	{ icon: "pin", label: "Alamat", value: contact.address },
	{ icon: "mail", label: "Email", value: contact.email },
	{ icon: "phone", label: "Telepon", value: contact.phone },
] as const;

export default function Contact() {
	return (
		<>
			<PageHeader title="Kontak" />
			<section className="container section">
				<Sample />
				<div className="cards">
					{rows.map((r) => (
						<article key={r.label} className="card">
							<span className="icon-badge">
								<Icon name={r.icon} />
							</span>
							<h3>{r.label}</h3>
							<p>{r.value}</p>
						</article>
					))}
				</div>
				<p>Formulir kontak akan ditambahkan pada langkah berikutnya.</p>
			</section>
		</>
	);
}
