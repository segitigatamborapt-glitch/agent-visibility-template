# Project conventions

See AGENTS.md for architecture and conventions.

## Commands
- Build: `npm run build`
- Test: `npm test` (hits live Workers AI, needs credentials)
- Full check: `npm run check`
- After editing `wrangler.jsonc`: `npx wrangler types`

## Stack
- TypeScript, Hono on Cloudflare Workers, Workers AI, KV
- React (surface-explorer UI in `src/react-app`)

## Rules
- `src/enrichment/surfaces.ts` stays pure (no I/O)
- Enrichment must never hard-fail (fall back to `fallbackEnrichment`)
- Tests live in `test/index.test.ts`
