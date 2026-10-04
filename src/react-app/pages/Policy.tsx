import PageHeader from "../components/PageHeader";
import { policies } from "../data/about";

export default function Policy() {
	return (
		<>
			<PageHeader title="Kebijakan Perusahaan" parent="Tentang Kami" />
			<section className="container section">
				<div className="prose">
					<p className="lead-dark">
						Komitmen perusahaan dalam menjalankan usaha konstruksi.
					</p>
					{policies.map((p) => (
						<article key={p.title} className="policy">
							<h2>{p.title}</h2>
							<p>{p.text}</p>
						</article>
					))}
				</div>
			</section>
		</>
	);
}
