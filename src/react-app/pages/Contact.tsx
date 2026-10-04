import Icon from "../components/Icon";
import PageHeader from "../components/PageHeader";
import { contact } from "../site";

const rows = [
	{ icon: "pin", label: "Alamat", value: contact.address, href: "" },
	{
		icon: "mail",
		label: "Email",
		value: contact.email,
		href: `mailto:${contact.email}`,
	},
	{
		icon: "phone",
		label: "Telepon",
		value: contact.phone,
		href: contact.phoneHref,
	},
] as const;

export default function Contact() {
	return (
		<>
			<PageHeader title="Kontak" />
			<section className="container section">
				<div className="cards">
					{rows.map((r) => (
						<article key={r.label} className="card">
							<span className="icon-badge">
								<Icon name={r.icon} />
							</span>
							<h3>{r.label}</h3>
							<p>{r.href ? <a href={r.href}>{r.value}</a> : r.value}</p>
						</article>
					))}
				</div>
				<p>
					Silakan hubungi kami melalui alamat, email, atau telepon di atas.
				</p>
			</section>
		</>
	);
}
