import { site } from "../site";

export default function Logo() {
	if (site.logo) {
		return (
			<img
				className="logo-img"
				src={site.logo}
				alt={site.name}
				height={52}
				style={{ height: 52, width: "auto" }}
			/>
		);
	}
	return (
		<>
			<svg
				className="logo-mark"
				viewBox="0 0 40 40"
				width="36"
				height="36"
				aria-hidden="true"
			>
				<polygon points="20,4 37,35 3,35" fill="#f28c28" />
				<polygon points="20,15 29,31 11,31" fill="#0f2a47" />
			</svg>
			<span>{site.name}</span>
		</>
	);
}
