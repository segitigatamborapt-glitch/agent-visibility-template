import PageHeader from "../components/PageHeader";
import PersonCard from "../components/PersonCard";
import { people, type GroupKey } from "../data/people";
import { site } from "../site";

const sections: { title: string; keys: GroupKey[] }[] = [
	{ title: "Pendiri", keys: ["pendiri"] },
	{ title: "Dewan Komisaris", keys: ["komisaris"] },
	{ title: "Manajemen dan Tim", keys: ["manajemen", "teknik", "keuangan"] },
];

export default function Organization() {
	return (
		<>
			<PageHeader title="Struktur Organisasi" parent="Tentang Kami" />
			<section className="container section">
				<p className="lead-dark center">
					Susunan pendiri, dewan komisaris, dan tim kerja {site.name}.
				</p>
				<div className="org">
					{sections.map((sec) => {
						const members = people.filter((p) => sec.keys.includes(p.group));
						if (members.length === 0) return null;
						return (
							<div className="org-row" key={sec.title}>
								<h2 className="org-label">{sec.title}</h2>
								<div className="org-cards">
									{members.map((p) => (
										<PersonCard key={p.name} person={p} />
									))}
								</div>
							</div>
						);
					})}
				</div>
			</section>
		</>
	);
}
