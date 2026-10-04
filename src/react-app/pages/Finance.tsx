import PageHeader from "../components/PageHeader";
import { contact, site } from "../site";

const subject = "Permintaan Laporan Keuangan";
const body = `Yth. ${site.name},

Kami mengajukan permintaan laporan keuangan dengan keterangan berikut:

Nama instansi/perusahaan :
Nama dan jabatan pemohon :
Keperluan                :
Tahun buku yang dibutuhkan :

Terima kasih.`;
const mailto = `mailto:${contact.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;

export default function Finance() {
	return (
		<>
			<PageHeader title="Informasi Keuangan" />
			<section className="container section">
				<div className="prose">
					<p className="lead-dark">
						Laporan keuangan {site.name} tersedia atas permintaan bagi pemberi
						tugas, mitra, dan pihak berkepentingan lainnya.
					</p>
					<h2 className="sub-title">Cara mengajukan permintaan</h2>
					<p>
						Hubungi kami melalui email atau telepon, lalu sampaikan hal
						berikut:
					</p>
					<ul className="check-list">
						<li>Nama instansi atau perusahaan pemohon</li>
						<li>Nama dan jabatan pemohon</li>
						<li>Keperluan permintaan</li>
						<li>Tahun buku yang dibutuhkan</li>
					</ul>
					<div className="actions">
						<a className="button" href={mailto}>
							Kirim Email
						</a>
						<a className="button button-outline" href={contact.phoneHref}>
							Hubungi {contact.phone}
						</a>
					</div>
					<p className="source-note">{contact.email}</p>
				</div>
			</section>
		</>
	);
}
