import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { cloudflare } from "@cloudflare/vite-plugin";

export default defineConfig({
	optimizeDeps: {
		exclude: ["hono"],
	},
	plugins: [react(), cloudflare({ remoteBindings: false })],
});
