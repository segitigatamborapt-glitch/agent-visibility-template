import PageHeader from "../components/PageHeader";
import PersonCard from "../components/PersonCard";
import { people } from "../data/people";
import { site } from "../site";

const team = people.filter((p) =>
	["manajemen", "teknik", "keuangan"].includes(p.group),
);

export default function Management() {
	return (
		<>
			<PageHeader title="Manajemen" parent="Tentang Kami" />
			<section className="container section">
				<p className="lead-dark center">Tim manajemen {site.name}.</p>
				<div className="org-cards org-cards-solo">
					{team.map((p) => (
						<PersonCard key={p.name} person={p} />
					))}
				</div>
			</section>
		</>
	);
}
