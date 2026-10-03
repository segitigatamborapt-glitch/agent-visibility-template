import PageHeader from "../components/PageHeader";
import Sample from "../components/Sample";

export default function About() {
	return (
		<>
			<PageHeader title="Profil Perusahaan" parent="Tentang Kami" />
			<section className="container section prose">
				<Sample />
				<p>Profil perusahaan akan diisi dengan data resmi.</p>
			</section>
		</>
	);
}
