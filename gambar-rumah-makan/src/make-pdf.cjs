// Gabungkan semua lembar SVG menjadi satu PDF A3 landscape. Pakai: node make-pdf.cjs
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = path.join(__dirname, '..', 'sheets');
  const codes = ['A-00','A-01','A-02','A-03','A-04','A-05','A-06','A-07','A-08','A-09','A-10'];
  const pages = codes.map(c => `<section>${fs.readFileSync(path.join(dir, c + '.svg'), 'utf8')}</section>`).join('\n');
  const html = `<!doctype html><html><head><meta charset="utf-8"><title>Gambar Teknis Rumah Makan</title>
<style>@page{size:420mm 297mm;margin:0}html,body{margin:0;padding:0;background:#fff}
section{width:420mm;height:297mm;page-break-after:always;overflow:hidden}section:last-child{page-break-after:auto}svg{display:block}</style></head><body>${pages}</body></html>`;
  fs.writeFileSync(path.join(__dirname, '..', 'index.html'), html);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.setContent(html);
  await p.pdf({ path: path.join(__dirname, '..', 'rumah-makan-gambar-teknis.pdf'), width: '420mm', height: '297mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
