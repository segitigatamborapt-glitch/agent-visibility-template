import type { IconName } from "../site";

const paths: Record<IconName | "mail" | "phone" | "pin", string> = {
	building:
		"M4 21V5l8-2 8 2v16M9 21v-4h6v4M8 9h2M14 9h2M8 13h2M14 13h2",
	road: "M8 3 4 21M16 3l4 18M12 4v3M12 10v4M12 17v3",
	structure: "M3 21h18M5 21V9h14v12M5 9l7-5 7 5M9 21v-6h6v6",
	bolt: "M13 2 4 14h7l-1 8 9-12h-7z",
	wrench:
		"M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18v3h3l6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z",
	truck:
		"M3 6h11v10H3zM14 9h4l3 3v4h-7M7 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM17 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4z",
	mail: "M3 5h18v14H3zM3 7l9 6 9-6",
	phone:
		"M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z",
	pin: "M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11zM12 12a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z",
};

export default function Icon({
	name,
	size = 24,
}: {
	name: keyof typeof paths;
	size?: number;
}) {
	return (
		<svg
			viewBox="0 0 24 24"
			width={size}
			height={size}
			fill="none"
			stroke="currentColor"
			strokeWidth="1.8"
			strokeLinecap="round"
			strokeLinejoin="round"
			aria-hidden="true"
		>
			<path d={paths[name]} />
		</svg>
	);
}
