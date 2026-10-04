import { groupTitle, initials, type Person } from "../data/people";

export default function PersonCard({ person }: { person: Person }) {
	return (
		<article className="person-card">
			{person.photo ? (
				<img className="avatar" src={person.photo} alt="" width={72} height={72} />
			) : (
				<span className="avatar avatar-initials" aria-hidden="true">
					{initials(person.name)}
				</span>
			)}
			<h3 className="person-name">{person.name}</h3>
			<p className="person-role">{person.role}</p>
			<span className="chip-static">{groupTitle(person.group)}</span>
		</article>
	);
}
