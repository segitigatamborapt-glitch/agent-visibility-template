import PageHeader from "../components/PageHeader";
import { missions, vision } from "../data/about";

export default function Vision() {
	return (
		<>
			<PageHeader title="Visi dan Misi" parent="Tentang Kami" />
			<section className="container section">
				<div className="vision-box">
					<p className="eyebrow-dark">Visi</p>
					<p className="vision-text">{vision}</p>
				</div>
				<h2 className="sub-title">Misi</h2>
				<ol className="mission-list">
					{missions.map((m) => (
						<li key={m.title}>
							<strong>{m.title}</strong>
							<p>{m.text}</p>
						</li>
					))}
				</ol>
			</section>
		</>
	);
}
