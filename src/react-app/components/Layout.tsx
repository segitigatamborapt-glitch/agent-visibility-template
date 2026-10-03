import { useEffect } from "react";
import { NavLink, Outlet, useLocation } from "react-router";
import { navLinks, site } from "../site";

export default function Layout() {
	const { pathname } = useLocation();

	useEffect(() => {
		window.scrollTo(0, 0);
	}, [pathname]);

	return (
		<>
			<header className="site-header">
				<div className="container header-inner">
					<NavLink to="/" className="brand">
						{site.name}
					</NavLink>
					<nav aria-label="Navigasi utama">
						<ul className="nav">
							{navLinks.map((link) => (
								<li key={link.to}>
									<NavLink to={link.to} end={link.to === "/"}>
										{link.label}
									</NavLink>
								</li>
							))}
						</ul>
					</nav>
				</div>
			</header>
			<main className="container page">
				<Outlet />
			</main>
			<footer className="site-footer">
				<div className="container">
					<p>
						&copy; {new Date().getFullYear()} {site.name}. Hak cipta
						dilindungi.
					</p>
				</div>
			</footer>
		</>
	);
}
