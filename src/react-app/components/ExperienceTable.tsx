import {
	categories,
	formatDate,
	formatRupiah,
	isOngoing,
	type Experience,
} from "../data/experience";

export default function ExperienceTable({ items }: { items: Experience[] }) {
	return (
		<div className="table-wrap">
			<table className="exp-table">
				<thead>
					<tr>
						<th>Tanggal</th>
						<th>Nama Pekerjaan</th>
						<th>Pemberi Kerja</th>
						<th className="num">Nilai Kontrak</th>
					</tr>
				</thead>
				<tbody>
					{items.map((e) => (
						<tr key={`${e.title}-${e.date}`}>
							<td data-label="Tanggal" className="exp-date">
								{formatDate(e.date)}
							</td>
							<td data-label="Nama Pekerjaan">
								<span className="exp-title">{e.title}</span>
								<span className="exp-tags">
									<span className="chip-static">
										{categories[e.category].short}
									</span>
									{isOngoing(e) && (
										<span className="tag-ongoing">Sedang berjalan</span>
									)}
								</span>
								{e.lpse && (
									<span className="exp-meta">Nomor paket LPSE: {e.lpse}</span>
								)}
							</td>
							<td data-label="Pemberi Kerja">
								<span className="client-pill">{e.client}</span>
							</td>
							<td data-label="Nilai Kontrak" className="num">
								{formatRupiah(e.value)}
							</td>
						</tr>
					))}
				</tbody>
			</table>
		</div>
	);
}
