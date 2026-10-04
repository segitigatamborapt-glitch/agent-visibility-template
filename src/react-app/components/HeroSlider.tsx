import { useEffect, useState, type ReactNode } from "react";
import { Link } from "react-router";
import {
	categories,
	experience,
	featured,
	formatRupiah,
	isOngoing,
	summary,
} from "../data/experience";
import { site } from "../site";
import HeroArt from "./HeroArt";

type Slide = {
	eyebrow: string;
	title: string;
	text: string;
	cta: { to: string; label: string };
	cta2?: { to: string; label: string };
	aside: ReactNode;
};

const INTERVAL = 6500;

function buildSlides(): Slide[] {
	const road = experience.filter((e) => e.category === "jalan-jembatan").length;
	const ongoing = experience.filter((e) => isOngoing(e));
	const biggest = featured[0];

	const slides: Slide[] = [
		{
			eyebrow: "Perusahaan Konstruksi",
			title: site.name,
			text: site.tagline,
			cta: { to: "/lini-bisnis", label: "Lini Bisnis" },
			cta2: { to: "/kontak", label: "Hubungi Kami" },
			aside: <HeroArt />,
		},
		{
			eyebrow: categories["jalan-jembatan"].title,
			title: `${road} dari ${summary.works} referensi pekerjaan kami adalah jalan dan jembatan`,
			text: categories["jalan-jembatan"].desc,
			cta: { to: "/lini-bisnis/jalan-jembatan", label: "Lihat Pekerjaan" },
			aside: (
				<div className="aside-panel">
					<p className="aside-label">Kontrak terbesar</p>
					<p className="aside-value">{formatRupiah(biggest.value)}</p>
					<p className="aside-label">
						{biggest.title}, {biggest.client}
					</p>
				</div>
			),
		},
		{
			eyebrow: "Rekam Jejak",
			title: `Berpengalaman di ${summary.provinces} provinsi sejak ${summary.since}`,
			text: `Dipercaya oleh ${summary.clients} pemberi tugas, termasuk pemerintah daerah.`,
			cta: { to: "/proyek", label: "Pengalaman Proyek" },
			aside: (
				<div className="aside-panel aside-stats">
					{[
						[summary.works, "Referensi pekerjaan"],
						[summary.clients, "Pemberi tugas"],
						[summary.provinces, "Provinsi"],
					].map(([v, l]) => (
						<div key={l}>
							<p className="aside-value">{v}</p>
							<p className="aside-label">{l}</p>
						</div>
					))}
				</div>
			),
		},
	];

	if (ongoing.length > 0) {
		slides.push({
			eyebrow: "Sedang Berjalan",
			title: `${ongoing.length} pekerjaan sedang kami kerjakan`,
			text: "Pekerjaan yang saat ini masih dalam masa kontrak.",
			cta: { to: "/proyek", label: "Lihat Pengalaman Proyek" },
			aside: (
				<ul className="aside-panel aside-list">
					{ongoing.slice(0, 4).map((e) => (
						<li key={e.title + e.date}>
							<p className="aside-item">{e.title}</p>
							<p className="aside-label">{e.client}</p>
						</li>
					))}
				</ul>
			),
		});
	}
	return slides;
}

export default function HeroSlider() {
	const [slides] = useState(buildSlides);
	const [index, setIndex] = useState(0);
	const [hover, setHover] = useState(false);
	const [userPaused, setUserPaused] = useState(
		() =>
			typeof window !== "undefined" &&
			window.matchMedia("(prefers-reduced-motion: reduce)").matches,
	);
	const count = slides.length;
	const running = !hover && !userPaused && count > 1;

	useEffect(() => {
		if (!running) return;
		const t = setInterval(() => setIndex((i) => (i + 1) % count), INTERVAL);
		return () => clearInterval(t);
	}, [running, count, index]);

	const go = (i: number) => setIndex((i + count) % count);

	return (
		<section
			className="hero slider"
			aria-roledescription="carousel"
			aria-label="Sorotan perusahaan"
			onMouseEnter={() => setHover(true)}
			onMouseLeave={() => setHover(false)}
			onFocus={() => setHover(true)}
			onBlur={() => setHover(false)}
		>
			<div className="slides" aria-live={running ? "off" : "polite"}>
				{slides.map((s, i) => {
					const active = i === index;
					const Title = i === 0 ? "h1" : "h2";
					return (
						<div
							key={s.eyebrow}
							className={`slide${active ? " is-active" : ""}`}
							role="group"
							aria-roledescription="slide"
							aria-label={`${i + 1} dari ${count}`}
							inert={!active}
						>
							<div className="container hero-inner">
								<div className="hero-text">
									<p className="eyebrow">{s.eyebrow}</p>
									<Title>{s.title}</Title>
									<p className="lead">{s.text}</p>
									<div className="hero-actions">
										<Link className="button" to={s.cta.to}>
											{s.cta.label}
										</Link>
										{s.cta2 && (
											<Link className="button button-ghost" to={s.cta2.to}>
												{s.cta2.label}
											</Link>
										)}
									</div>
								</div>
								<div className="slide-aside">{s.aside}</div>
							</div>
						</div>
					);
				})}
			</div>
			{count > 1 && (
				<div className="container slider-controls">
					<button
						type="button"
						className="ctrl-btn"
						onClick={() => go(index - 1)}
						aria-label="Slide sebelumnya"
					>
						‹
					</button>
					<div className="dots">
						{slides.map((s, i) => (
							<button
								key={s.eyebrow}
								type="button"
								className="dot"
								aria-label={`Slide ${i + 1}`}
								aria-current={i === index}
								onClick={() => go(i)}
							/>
						))}
					</div>
					<button
						type="button"
						className="ctrl-btn"
						onClick={() => go(index + 1)}
						aria-label="Slide berikutnya"
					>
						›
					</button>
					<button
						type="button"
						className="ctrl-btn ctrl-text"
						onClick={() => setUserPaused((v) => !v)}
						aria-pressed={userPaused}
					>
						{userPaused ? "Putar" : "Jeda"}
					</button>
				</div>
			)}
		</section>
	);
}
