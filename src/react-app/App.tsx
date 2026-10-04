import { BrowserRouter, Route, Routes } from "react-router";
import "./App.css";
import Layout from "./components/Layout";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Finance from "./pages/Finance";
import Home from "./pages/Home";
import InfoPage from "./pages/InfoPage";
import LineDetail from "./pages/LineDetail";
import Projects from "./pages/Projects";
import Services from "./pages/Services";

export default function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route element={<Layout />}>
					<Route index element={<Home />} />
					<Route path="tentang" element={<About />} />
					<Route path="lini-bisnis" element={<Services />} />
					<Route path="lini-bisnis/:slug" element={<LineDetail />} />
					<Route path="informasi-keuangan" element={<Finance />} />
					<Route path="proyek" element={<Projects />} />
					<Route path="kontak" element={<Contact />} />
					<Route path="*" element={<InfoPage />} />
				</Route>
			</Routes>
		</BrowserRouter>
	);
}
