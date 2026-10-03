import { useEffect } from "react";
import { NavLink, Outlet, useLocation } from "react-router";
import { contact, navLinks, site } from "../site";

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
			<main>
				<Outlet />
			</main>
			<footer className="site-footer">
				<div className="container footer-grid">
					<div>
						<strong>{site.name}</strong>
						<p>{site.tagline}</p>
					</div>
					<div>
						<strong>Menu</strong>
						<ul>
							{navLinks.map((link) => (
								<li key={link.to}>
									<NavLink to={link.to}>{link.label}</NavLink>
								</li>
							))}
						</ul>
					</div>
					<div>
						<strong>Kontak</strong>
						<p>{contact.address}</p>
						<p>{contact.email}</p>
						<p>{contact.phone}</p>
					</div>
				</div>
				<div className="container footer-bottom">
					<p>
						&copy; {new Date().getFullYear()} {site.name}. Hak cipta
						dilindungi.
					</p>
				</div>
			</footer>
		</>
	);
}
