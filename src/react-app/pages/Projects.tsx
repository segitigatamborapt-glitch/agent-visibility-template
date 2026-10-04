import { useState } from "react";
import PageHeader from "../components/PageHeader";
import WorkCard from "../components/WorkCard";
import { categories, experience, type CategoryKey } from "../data/experience";

type Filter = CategoryKey | "semua";

const order: CategoryKey[] = [
	"jalan-jembatan",
	"gedung",
	"dermaga",
	"air-pantai",
	"lainnya",
];

export default function Projects() {
	const [filter, setFilter] = useState<Filter>("semua");
	const shown = experience.filter(
		(e) => filter === "semua" || e.category === filter,
	);
	const options: { key: Filter; label: string; count: number }[] = [
		{ key: "semua", label: "Semua", count: experience.length },
		...order
			.map((key) => ({
				key,
				label: categories[key].short,
				count: experience.filter((e) => e.category === key).length,
			}))
			.filter((o) => o.count > 0),
	];

	return (
		<>
			<PageHeader title="Pengalaman Proyek" parent="Pusat Informasi" />
			<section className="container section">
				<p className="source-note">
					Sebagian pekerjaan yang tercatat pada profil penyedia kami di SIKaP
					(INAPROC).
				</p>
				<div className="chips" role="group" aria-label="Filter kategori">
					{options.map((o) => (
						<button
							key={o.key}
							type="button"
							className="chip"
							aria-pressed={filter === o.key}
							onClick={() => setFilter(o.key)}
						>
							{o.label} <span>{o.count}</span>
						</button>
					))}
				</div>
				<div className="cards cards-2">
					{shown.map((e) => (
						<WorkCard key={`${e.title}-${e.start}`} item={e} />
					))}
				</div>
			</section>
		</>
	);
}
