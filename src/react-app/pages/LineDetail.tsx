import { useParams } from "react-router";
import PageHeader from "../components/PageHeader";
import ExperienceTable from "../components/ExperienceTable";
import { experience } from "../data/experience";
import { businessLines } from "../site";
import NotFound from "./NotFound";

export default function LineDetail() {
	const { slug } = useParams();
	const line = businessLines.find((b) => b.slug === slug);
	if (!line) return <NotFound />;
	const works = experience.filter((e) => e.category === line.slug);
	return (
		<>
			<PageHeader title={line.title} parent="Lini Bisnis" />
			<section className="container section">
				<p className="source-note">{line.desc}</p>
				<h2 className="sub-title">Pekerjaan terkait ({works.length})</h2>
				<ExperienceTable items={works} />
			</section>
		</>
	);
}
