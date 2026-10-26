"""Denah situasi, denah pondasi, rencana atap."""
import math
from draft import *
from bldg import *
import sheets as S

LOT_W, LOT_D = 28.0, 33.0
BX, BY = 4.0, 4.0           # posisi as bangunan (x=0,y=0) dalam koordinat lahan


def tree(v, x, y, r=1.4):
    v.circ(x, y, r, "#e7efe0", "#5d7f4f", 0.25)
    v.circ(x, y, r * 0.55, "none", "#5d7f4f", 0.15)
    v.circ(x, y, 0.1, "#5d7f4f", "#5d7f4f", 0.1)


def a01(idx):
    sh = Sheet()
    s = 5.0
    v = View(sh, 62, 60, s)
    # ---- jalan & trotoar (selatan)
    v.rect(-6, 33, 36, 1.5, "#ececec", INK, 0.2)
    v.rect(-6, 34.5, 36, 7.5, "#d9dcdf", INK, 0.25)
    v.line(-6, 38.25, 30, 38.25, 0.3, dash="6 4", c="#fff")
    v.text(12, 40.1, "JALAN LINGKUNGAN (lebar ± 7 m)", 1.8, c="#444")
    # ---- lahan
    v.rect(0, 0, LOT_W, LOT_D, "#fcfcf8", INK, 0.2)
    # rumput / area hijau
    for (x, y, w, h) in ((0, 4, 4, 15), (24.1, 4, 3.9, 1.8), (0, 31, 11, 2), (17, 31, 11, 2), (0, 0, 4, 4)):
        v.rect(x, y, w, h, "url(#grass)", None)
    # perkerasan parkir/aisle
    v.rect(0, 19.7, LOT_W, 11.3, "#eceeef", None)
    v.rect(11, 31, 6, 2, "#eceeef", None)
    # bangunan
    bv = View(sh, v.X(BX), v.Y(BY), s)
    bv.rect(-0.6, YEB, 21.2, YEF - YEB, "#f6e3da", INK, 0.3)          # atap (bayangan)
    bv.line(-0.6, YR, 20.6, YR, 0.3, dash="5 1.5 1 1.5")
    bv.rect(-0.075, -0.075, 20.15, 12.15, "#f0f1f2", INK, 0.6)
    bv.rect(-0.075, 12.075, 20.15, TERR_Y - 12.075, "#fafafa", INK, 0.4)
    bv.text(10.0, 6.2, "RUMAH MAKAN\nSELERA NUSANTARA\n(1 lantai ± 245 m²)", 2.6, bold=True)
    bv.text(10.0, 13.3, "TERAS (beratap)", 1.8)
    bv.rect(8.5, TERR_Y, 3, 0.45, "#fff", INK, 0.25)
    bv.rect(14.0, TERR_Y, 3.84, 1.2, "#fff", INK, 0.25)
    # tanda pintu masuk
    bv.line(10, 12.2, 10, 19.0, 0.3, dash="1.5 1")
    # ---- tapak: belakang
    v.rect(6.3, 0.9, 1.6, 1.0, "#fff", INK, 0.25); v.text(7.1, 1.4, "BAK\nLEMAK", 1.2)
    v.rect(10.9, 0.9, 1.3, 1.0, "#fff", INK, 0.25); v.text(11.55, 1.4, "LPG", 1.2)
    v.rect(13.0, 0.7, 3.6, 2.2, "#fff", INK, 0.25); v.text(14.8, 1.8, "TPS / BAK\nSAMPAH", 1.3)
    v.rect(19.0, 0.9, 3.2, 1.6, "#fff", INK, 0.3); v.text(20.6, 1.7, "SEPTIC TANK\n2,0 m³", 1.2)
    v.circ(25.3, 1.7, 0.8, "#fff", INK, 0.3); v.text(25.3, 3.2, "SUMUR\nRESAPAN", 1.2)
    v.line(22.2, 1.7, 24.5, 1.7, 0.25, dash="1.2 0.8")
    v.rect(1.2, 0.9, 2.2, 1.6, "#fff", INK, 0.25); v.text(2.3, 1.7, "TANDON\nAIR 2 m³", 1.2)
    # jalur servis ke pintu dapur
    v.line(BX + 5.95, 3.9, BX + 5.95, 1.0, 0.3, dash="1.5 1")
    v.rect(BX + 5.0, 1.9, 2.0, 2.0, "#e9e9e9", None)
    v.text(BX + 6.0, 3.0, "bordes\nservis", 1.1, c="#555")
    # ---- parkir motor (timur)
    for i in range(12):
        v.rect(25.2, 6.0 + i * 0.8, 2.0, 0.8, "#fff", INK, 0.12)
    v.text(26.2, 5.3, "PARKIR MOTOR (12)", 1.4)
    # ---- parkir mobil
    for i in range(4):
        v.rect(1.0 + i * 2.5, 26, 2.5, 5, "#fff", INK, 0.2)
        v.text(2.25 + i * 2.5, 28.5, str(i + 1), 1.5, c="#666")
    v.rect(17, 26, 3.5, 5, "#e6f0fa", INK, 0.25)
    v.text(18.75, 28.5, "D", 2.0, bold=True, c="#0a5aa8")
    for i in range(3):
        v.rect(20.5 + i * 2.5, 26, 2.5, 5, "#fff", INK, 0.2)
        v.text(21.75 + i * 2.5, 28.5, str(i + 6), 1.5, c="#666")
    v.text(6.0, 31.9, "PARKIR MOBIL — 8 SRP (1 difabel)", 1.5)
    # panah sirkulasi
    for (x1, y1, x2, y2) in ((14, 33.2, 14, 25.0), (14, 25, 8, 22.5)):
        v.line(x1, y1, x2, y2, 0.3, dash="2 1.2")
    sh.add(f'<polygon points="{n(v.X(8))},{n(v.Y(22.5))} {n(v.X(8.8))},{n(v.Y(22.3))} {n(v.X(8.6))},{n(v.Y(23.2))}" fill="{INK}"/>')
    # pagar & gerbang
    v.line(0, 0, LOT_W, 0, 1.0)
    v.line(0, 0, 0, LOT_D, 1.0)
    v.line(LOT_W, 0, LOT_W, LOT_D, 1.0)
    v.line(0, LOT_D, 11, LOT_D, 0.8)
    v.line(17, LOT_D, LOT_W, LOT_D, 0.8)
    v.line(11, LOT_D, 17, LOT_D, 0.35, dash="2 1")
    v.text(14, 32.2, "GERBANG GESER 6,0 m", 1.4, bold=True)
    # pohon
    for (x, y) in ((2.0, 8), (2.0, 14), (1.8, 21.5), (26.2, 21.5)):
        tree(v, x, y, 1.2)
    # ---- dimensi
    chain_h(v, [0, BX, BX + 20.15, LOT_W], 0, v.Y(0) - 12, over=1.2)
    chain_h(v, [0, LOT_W], 0, v.Y(0) - 20)
    chain_v(v, [0, BY, BY + 12.15, BY + TERR_Y, 26, 31, 33], 0, v.X(0) - 8)
    chain_v(v, [0, 33], 0, v.X(0) - 16)
    # ---- notasi
    north_arrow(sh, 236, 52, 8)
    scale_bar(sh, 218, 80, s, (0, 2, 4, 6, 8, 10))
    T(sh, 218, 92, "SKALA 1 : 200", 2.0, "start", bold=True)
    lt = LOT_W * LOT_D
    foot = 20.15 * 12.15
    roofed = foot + 20.15 * (TERR_Y - 12.075)
    T(sh, 218, 104, "DATA LAHAN & BANGUNAN (ASUMSI)", 2.2, "start", bold=True)
    rows = [("Luas lahan", "28,0 × 33,0", f"{lt:.0f} m²"), ("Luas bangunan lt.1", "20,15 × 12,15", f"{foot:.1f} m²"),
            ("Luas teras beratap", "20,15 × 2,43", f"{20.15 * (TERR_Y - 12.075):.1f} m²"), ("Total beratap (KDB)", "", f"{roofed:.1f} m²"),
            ("KDB (terbangun)", f"{roofed:.1f} / {lt:.0f}", f"{roofed / lt * 100:.1f} %"), ("KLB", "1 lantai", f"{roofed / lt:.2f}"),
            ("Sempadan belakang", "", "± 3,9 m"), ("Sempadan samping", "kiri / kanan", "± 3,9 m"),
            ("Parkir mobil / motor", "", "8 SRP / 12")]
    table(sh, 218, 107, [38, 27, 22], 5.0, ["Uraian", "Hitungan", "Hasil"], rows, fs=1.75, hfs=1.8, aligns=["start", "middle", "middle"])
    T(sh, 218, 168, "LEGENDA", 2.2, "start", bold=True)
    L(sh, 218, 175, 229, 175, 1.0)
    T(sh, 231, 175, "Pagar bata h=2,0 (samping & belakang)", 1.75, "start")
    R(sh, 218, 179, 11, 3, "url(#grass)", INK, 0.2)
    T(sh, 231, 180.5, "Taman / resapan (RTH)", 1.75, "start")
    R(sh, 218, 185, 11, 3, "#f6e3da", INK, 0.3)
    T(sh, 231, 186.5, "Proyeksi atap + bubungan", 1.75, "start")
    R(sh, 218, 191, 11, 3, "#eceeef", INK, 0.2)
    T(sh, 231, 192.5, "Perkerasan paving block / beton", 1.75, "start")
    T(sh, 218, 202, "CATATAN", 2.2, "start", bold=True)
    for i, t in enumerate(["Orientasi muka bangunan ke selatan (jalan).", "Lahan diasumsikan datar, persegi 28×33 m;",
                           "sesuaikan dengan sertifikat/IMB & GSB", "setempat sebelum konstruksi.", "Pengolahan limbah: bak lemak → septic",
                           "tank → sumur resapan (jarak ≥10 m dari", "sumber air bersih).", "Drainase keliling lahan U-ditch 30×40."]):
        T(sh, 218, 208 + i * 4.2, t, 1.75, "start")
    ptitle(sh, 62, 276, "DENAH SITUASI (SITE PLAN)", "SKALA 1 : 200")
    frame(sh, "A-01", "DENAH SITUASI\n(SITE PLAN)", "1 : 200", idx, S.TOTAL, [
        "Satuan: meter (kecuali tertulis\nlain).", "Gambar asumsi — lokasi & ukuran\nlahan belum ditentukan.",
        "Lihat A-02 untuk denah lantai."])
    return sh.svg()


def a04(idx):
    sh = Sheet()
    v = View(sh, 48, 62, 10)
    # latar dinding tipis
    for w in WALLS:
        _, x1, y1, x2, y2, t = w
        v.line(x1, y1, x2, y2, 0.15, c="#aaa")
    # pondasi menerus (lebar bawah 0.6) putus-putus
    for w in WALLS:
        _, x1, y1, x2, y2, t = w
        if y1 == y2:
            v.rect(x1 - (0.3 if w[0] in EXTW else 0.0), y1 - 0.3, (x2 - x1) + (0.6 if w[0] in EXTW else 0), 0.6, "none", INK, 0.2, "2.2 1")
        else:
            v.rect(x1 - 0.3, y1 - (0.3 if w[0] in EXTW else 0.0), 0.6, (y2 - y1) + (0.6 if w[0] in EXTW else 0), "none", INK, 0.2, "2.2 1")
    # sloof (as)
    for w in WALLS:
        _, x1, y1, x2, y2, t = w
        v.line(x1, y1, x2, y2, 0.9, c="#444")
    # balok tepi teras & kolom teras
    v.line(0, 14.4, 20, 14.4, 0.9, c="#444", dash="4 1")
    for x in XS:
        v.line(x, 12, x, 14.4, 0.5, c="#444", dash="4 1")
    # footplat F1
    for x in XS:
        for y in YS + [14.4]:
            v.rect(x - 0.4, y - 0.4, 0.8, 0.8, "#fff", INK, 0.3)
            v.line(x - 0.4, y - 0.4, x + 0.4, y + 0.4, 0.08)
            v.line(x - 0.4, y + 0.4, x + 0.4, y - 0.4, 0.08)
    draw_columns(v)
    # label
    v.text(6.0, 5.55, "SL1  15/20", 1.5, c="#222")
    v.text(10, 13.2, "SL2 15/20 (balok tepi teras)", 1.6, c="#222")
    v.text(10, 9.0, "Pondasi batu kali menerus (P1) di bawah semua dinding & sloof SL1", 1.6, c="#222")
    leader(sh, v.X(8), v.Y(14.8), v.X(8) + 12, v.Y(14.8) + 12, "F1 = footplat 80×80×20 (24 titik)", 1.7)
    # dimensi
    chain_h(v, XS, -0.4, v.Y(0) - 14)
    chain_h(v, [0, 20], -0.4, v.Y(0) - 22)
    chain_v(v, YS + [14.4], -0.4, v.X(0) - 14)
    xr = v.X(20) + 14
    chain_v(v, [0, 5, 12, 14.4], 20.4, xr)
    for i, x in enumerate(XS):
        bubble(sh, v.X(x), v.Y(0) - 32, str(i + 1), 3.0)
        axis_line(sh, v.X(x), v.Y(0) - 29, v.X(x), v.Y(0) - 3)
    for lab, y in zip(["C", "B", "A"], YS):
        bubble(sh, xr + 11, v.Y(y), lab, 3.0)
    ptitle(sh, 48, 266, "DENAH PONDASI & SLOOF", "SKALA 1 : 100", sub="Tampak atas — garis putus = pondasi batu kali menerus; kotak X = footplat F1; as 1-6 / A-C")
    # tabel tipe
    T(sh, 290, 40, "TABEL TIPE STRUKTUR", 2.2, "start", bold=True)
    rows = [("P1", "Pondasi batu kali menerus: atas 30, bawah 60, tinggi 80; di atas lantai kerja pasir t=10"),
            ("F1", "Footplat setempat 80×80×20; tulangan Ø12-150 dua arah; di bawah kolom as"),
            ("K1", "Kolom beton 20/20; 4Ø12, sengkang Ø6-150; mutu K-225"),
            ("SL1", "Sloof 15/20; 4Ø10, sengkang Ø6-150"),
            ("SL2", "Balok tepi teras 15/20; 4Ø10, sengkang Ø6-150"),
            ("RB", "Ring balk 15/20; 4Ø10, sengkang Ø6-150 (lihat A-07)")]
    yy = 45
    for k, t in rows:
        R(sh, 290, yy, 11, 9.4, "#e4e7ea", INK, 0.25)
        T(sh, 295.5, yy + 4.7, k, 2.0, bold=True)
        R(sh, 301, yy, 37, 9.4, "none", INK, 0.25)
        words, line, lines = t.split(), "", []
        for w_ in words:
            if len(line + " " + w_) > 34:
                lines.append(line.strip()); line = w_
            else:
                line += " " + w_
        lines.append(line.strip())
        T(sh, 302, yy + 4.7, "\n".join(lines), 1.55, "start", ls=1.2)
        yy += 9.4
    T(sh, 290, yy + 7, "CATATAN STRUKTUR", 2.1, "start", bold=True)
    for i, t in enumerate(["Daya dukung tanah diasumsikan ≥ 1,0 kg/cm²;", "wajib uji sondir/boring bila tanah lunak.", "Kedalaman pondasi 80 cm dari tanah asli",
                           "(−1,15 dari ±0,00); sesuaikan kondisi.", "Mutu beton K-225, baja BJTP-24 (polos) /", "BJTD-40 (ulir).",
                           "Kolom di as 1-6 × A-C selalu bertumpu", "pada footplat F1 (24 titik).", "Perhitungan struktur final oleh ahli",
                           "teknik sipil bersertifikat."]):
        T(sh, 290, yy + 12 + i * 4.2, t, 1.7, "start")
    frame(sh, "A-04", "DENAH PONDASI\n& SLOOF", "1 : 100", idx, S.TOTAL, S.NOTES_COMMON + ["Pondasi ditunjukkan dengan garis\nputus-putus (di bawah tanah)."])
    return sh.svg()


def a08(idx):
    sh = Sheet()
    v = View(sh, 56, 62, 10)
    # penutup atap
    v.rect(-0.6, YEB, 21.2, YEF - YEB, "#fff", INK, 0.7)
    y = YEB + 0.35
    while y < YEF:
        v.line(-0.6, y, 20.6, y, 0.07, c="#aaa")
        y += 0.35
    # bayangan dinding
    for r_ in [r for w in WALLS for r in wall_rects(w[0])]:
        v.rect(r_[0], r_[1], r_[2], r_[3], "none", "#999", 0.15, "1.5 1")
    # kuda-kuda tiap as 1-6
    for x in XS:
        v.line(x, YEB + 0.1, x, YEF - 0.1, 0.5, c="#444", dash="5 1.2")
    # nok, ring
    v.line(-0.8, YR, 20.8, YR, 0.8, dash="8 1.5 1.2 1.5")
    v.text(21.0, YR, "NOK", 1.4, anchor="start")
    # talang & pipa tegak
    v.line(-0.55, YEB + 0.15, 20.55, YEB + 0.15, 0.6, c="#444")
    v.line(-0.55, YEF - 0.15, 20.55, YEF - 0.15, 0.6, c="#444")
    for (x, yy) in ((0.35, YEB + 0.15), (19.65, YEB + 0.15), (0.35, YEF - 0.15), (19.65, YEF - 0.15)):
        v.circ(x, yy, 0.12, "#fff", INK, 0.4)
        v.text(x + 0.25 if x < 10 else x - 0.25, yy + (0.5 if yy < 0 else -0.5), "TP", 1.2, anchor="start" if x < 10 else "end")
    # panah kemiringan
    for (y1, y2) in ((YEB + 2.0, YEB + 4.5), (YEF - 2.0, YEF - 4.5)):
        for x in (6.0, 14.0):
            v.line(x, y1, x, y2, 0.4)
            sh.add(f'<polygon points="{n(v.X(x))},{n(v.Y(y2) + (1.2 if y2 > y1 else -1.2))} {n(v.X(x) - 0.9)},{n(v.Y(y2) + (-0.6 if y2 > y1 else 0.6))} {n(v.X(x) + 0.9)},{n(v.Y(y2) + (-0.6 if y2 > y1 else 0.6))}" fill="{INK}"/>')
    v.text(10, YEB + 3.2, "i = 20°", 2.0, bold=True)
    v.text(10, YEF - 3.2, "i = 20°", 2.0, bold=True)
    v.text(10, YR - 1.2, "ATAP GENTENG METAL PASIR", 2.0, bold=True)
    v.text(10, YR + 1.2, "rangka baja ringan C75 + reng 3×3", 1.6)
    # cerobong
    v.circ(2.5, 0.5, 0.2, "#fff", INK, 0.5)
    v.line(2.5 - 0.2, 0.5 - 0.2, 2.5 + 0.2, 0.5 + 0.2, 0.2)
    leader(sh, v.X(2.5), v.Y(0.5), v.X(2.5) - 4, v.Y(0.5) - 11, "Cerobong dapur Ø40", 1.7, anchor="end")
    # dimensi
    chain_h(v, [-0.6] + XS + [20.6], YEB, v.Y(YEB) - 14)
    chain_h(v, [-0.6, 20.6], YEB, v.Y(YEB) - 22)
    chain_v(v, [YEB, 0, YR, 12, YEF], -0.6, v.X(-0.6) - 14)
    chain_v(v, [YEB, YEF], -0.6, v.X(-0.6) - 22)
    for i, x in enumerate(XS):
        bubble(sh, v.X(x), v.Y(YEB) - 31, str(i + 1), 3.0)
        axis_line(sh, v.X(x), v.Y(YEB) - 28, v.X(x), v.Y(YEB) - 2)
    ptitle(sh, 56, 266, "RENCANA ATAP", "SKALA 1 : 100", sub="Atap pelana (gable) ± 20°, bubungan memanjang timur–barat pada y = +7,25; menutup bangunan & teras")
    T(sh, 290, 40, "KETERANGAN ATAP", 2.2, "start", bold=True)
    for i, t in enumerate(["Penutup: genteng metal pasir t=0,4", "Rangka: baja ringan C75 / reng TS 3×3", "Jarak kuda-kuda: 4,00 m (as 1–6)",
                           "Gording: C75 ±1,20 m searah lereng", "Kemiringan: 20° (36%)", "Tepi atap: 80 cm (belakang), 80 cm",
                           "(depan, di luar teras), 60 cm (samping)", "Talang: PVC Ø4\" kemiringan 1:200", "Pipa tegak (TP): Ø3\" × 4 titik",
                           "Lisplang: GRC 20 cm", "Nok: galvalum + ventilasi nok", "Cerobong: Ø40 galvanis, tinggi +7,00",
                           "(≥ 1,0 m di atas nok)"]):
        T(sh, 290, 46 + i * 4.4, "• " + t, 1.7, "start")
    T(sh, 290, 112, "LEGENDA", 2.2, "start", bold=True)
    L(sh, 290, 119, 304, 119, 0.8, INK, "8 1.5 1.2 1.5"); T(sh, 306, 119, "Nok / bubungan", 1.7, "start")
    L(sh, 290, 124, 304, 124, 0.5, "#444", "5 1.2"); T(sh, 306, 124, "Kuda-kuda (rangka)", 1.7, "start")
    L(sh, 290, 129, 304, 129, 0.6, "#444"); T(sh, 306, 129, "Talang air", 1.7, "start")
    L(sh, 290, 134, 304, 134, 0.15, "#999", "1.5 1"); T(sh, 306, 134, "Dinding di bawah atap", 1.7, "start")
    frame(sh, "A-08", "RENCANA ATAP", "1 : 100", idx, S.TOTAL, S.NOTES_COMMON)
    return sh.svg()
