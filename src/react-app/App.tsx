import { BrowserRouter, Route, Routes } from "react-router";
import "./App.css";
import Layout from "./components/Layout";
import About from "./pages/About";
import Culture from "./pages/Culture";
import Contact from "./pages/Contact";
import Finance from "./pages/Finance";
import Home from "./pages/Home";
import Journey from "./pages/Journey";
import Management from "./pages/Management";
import Organization from "./pages/Organization";
import InfoPage from "./pages/InfoPage";
import LineDetail from "./pages/LineDetail";
import Policy from "./pages/Policy";
import Projects from "./pages/Projects";
import Vision from "./pages/Vision";
import Services from "./pages/Services";

export default function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route element={<Layout />}>
					<Route index element={<Home />} />
					<Route path="tentang" element={<About />} />
					<Route path="tentang/visi-dan-misi" element={<Vision />} />
					<Route path="tentang/jejak-langkah" element={<Journey />} />
					<Route path="tentang/struktur-organisasi" element={<Organization />} />
					<Route path="tentang/manajemen" element={<Management />} />
					<Route path="tentang/budaya-perusahaan" element={<Culture />} />
					<Route path="tentang/kebijakan-perusahaan" element={<Policy />} />
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
