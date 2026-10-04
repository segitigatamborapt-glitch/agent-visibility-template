import {
	categories,
	formatDate,
	formatRupiah,
	isOngoing,
	type Experience,
} from "../data/experience";

export default function WorkCard({ item }: { item: Experience }) {
	return (
		<article className="card work">
			<div className="work-top">
				<span className="chip-static">{categories[item.category].short}</span>
				{isOngoing(item) && <span className="tag-ongoing">Sedang berjalan</span>}
			</div>
			<h3>{item.title}</h3>
			<dl className="meta">
				<dt>Lokasi</dt>
				<dd>{item.location}</dd>
				<dt>Pemberi Tugas</dt>
				<dd>{item.client}</dd>
				<dt>Periode</dt>
				<dd>
					{formatDate(item.start)} – {formatDate(item.end)}
				</dd>
				<dt>Nilai Kontrak</dt>
				<dd>{formatRupiah(item.value)}</dd>
			</dl>
		</article>
	);
}
