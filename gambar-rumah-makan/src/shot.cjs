// Render SVG -> PNG untuk pemeriksaan visual. Pakai: node shot.js A-02 [A-03 ...]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1587, height: 1123 } });
  const dir = path.join(__dirname, '..', 'sheets');
  const outdir = process.env.SHOTDIR || '/tmp/shots';
  fs.mkdirSync(outdir, { recursive: true });
  for (const c of process.argv.slice(2)) {
    const svg = fs.readFileSync(path.join(dir, c + '.svg'), 'utf8');
    await p.setContent(`<html><body style="margin:0">${svg}</body></html>`);
    await p.screenshot({ path: path.join(outdir, c + '.png'), clip: { x: 0, y: 0, width: 1587, height: 1123 } });
  }
  await b.close();
})();
