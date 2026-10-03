import { useEffect, useRef, useState } from "react";
import { Link, NavLink, Outlet, useLocation } from "react-router";
import { contact, navItems, site } from "../site";
import Logo from "./Logo";

const hoverCapable = () =>
	window.matchMedia("(hover: hover) and (min-width: 900px)").matches;

export default function Layout() {
	const { pathname } = useLocation();
	const [open, setOpen] = useState<string | null>(null);
	const [mobileOpen, setMobileOpen] = useState(false);
	const headerRef = useRef<HTMLElement>(null);

	useEffect(() => {
		setOpen(null);
		setMobileOpen(false);
		window.scrollTo(0, 0);
	}, [pathname]);

	useEffect(() => {
		const onClick = (e: MouseEvent) => {
			if (!headerRef.current?.contains(e.target as Node)) setOpen(null);
		};
		document.addEventListener("click", onClick);
		return () => document.removeEventListener("click", onClick);
	}, []);

	return (
		<>
			<header
				className="site-header"
				ref={headerRef}
				onKeyDown={(e) => e.key === "Escape" && setOpen(null)}
			>
				<div className="header-inner">
					<Link to="/" className="brand">
						<Logo />
						<span>{site.name}</span>
					</Link>
					<button
						type="button"
						className="menu-toggle"
						aria-expanded={mobileOpen}
						aria-controls="main-nav"
						onClick={() => setMobileOpen((v) => !v)}
					>
						{mobileOpen ? "Tutup" : "Menu"}
					</button>
					<nav
						id="main-nav"
						aria-label="Navigasi utama"
						className={mobileOpen ? "is-open" : ""}
					>
						<ul className="nav">
							{navItems.map((item) => (
								<li
									key={item.label}
									className={open === item.label ? "has-open" : ""}
									onMouseEnter={() =>
										item.children && hoverCapable() && setOpen(item.label)
									}
									onMouseLeave={() => hoverCapable() && setOpen(null)}
								>
									{item.children ? (
										<>
											<button
												type="button"
												aria-expanded={open === item.label}
												onClick={() =>
													setOpen(open === item.label ? null : item.label)
												}
											>
												{item.label}
												<span className="chev" aria-hidden="true" />
											</button>
											<ul className="dropdown">
												{item.children.map((c) => (
													<li key={c.to}>
														<NavLink to={c.to} end>
															{c.label}
														</NavLink>
													</li>
												))}
											</ul>
										</>
									) : (
										<NavLink to={item.to!}>{item.label}</NavLink>
									)}
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
							{navItems.map((item) => (
								<li key={item.label}>
									{item.to ? (
										<NavLink to={item.to}>{item.label}</NavLink>
									) : (
										item.label
									)}
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
