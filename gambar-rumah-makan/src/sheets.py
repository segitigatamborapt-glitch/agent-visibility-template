"""Penyusunan lembar gambar."""
from draft import *
from bldg import *

TOTAL = 11

NOTES_COMMON = [
    "Satuan ukuran: cm, kecuali ditulis lain.\nElevasi dalam meter. ±0.00 = lantai\nruang makan.",
    "Ukuran denah as ke as dinding,\nkecuali dinyatakan lain.",
    "Gambar adalah rencana awal; ukuran\nlapangan wajib dicek sebelum\npelaksanaan.",
]


def legend_plan(sh, x, y):
    T(sh, x, y, "LEGENDA", 2.2, "start", bold=True)
    items = [("wall", "Dinding bata ½ bata (t=15) / partisi (t=10)"), ("col", "Kolom beton K1 20/20"),
             ("door", "Pintu + arah bukaan"), ("win", "Jendela / bovenlicht (garis putus = tinggi)")]
    yy = y + 5
    for kind, txt in items:
        if kind == "wall":
            R(sh, x, yy - 1.5, 8, 3, WALLFILL, INK, 0.3)
        elif kind == "col":
            R(sh, x + 2.5, yy - 1.5, 3, 3, INK, INK, 0.2)
        elif kind == "door":
            L(sh, x + 1, yy + 2, x + 1, yy - 2.5, 0.35)
            sh.add(f'<path d="M{n(x + 5.5)},{n(yy + 2)} A4.5,4.5 0 0 0 {n(x + 1)},{n(yy - 2.5)}" fill="none" stroke="{INK}" stroke-width="0.13"/>')
            L(sh, x, yy + 2, x + 8, yy + 2, 0.2)
        elif kind == "win":
            for dyy in (-1.2, 0, 1.2):
                L(sh, x, yy + dyy, x + 8, yy + dyy, 0.15)
        T(sh, x + 10.5, yy, txt, 1.8, "start")
        yy += 5.5


def room_table(sh, x, y):
    rows = [(f"R{i + 1:02d}", NAME[f"R{i + 1:02d}"], f"{AREA[f'R{i + 1:02d}']:.1f}") for i in range(10)]
    yb = table(sh, x, y, [8.5, 28, 11.5], 5.2, ["Kode", "Nama Ruang", "Luas m²"], rows, fs=1.75, hfs=1.8, aligns=["middle", "start", "middle"])
    tot_in = sum(AREA[f"R{i + 1:02d}"] for i in (0, 2, 3, 4, 5, 6, 7, 8, 9))
    T(sh, x, yb + 4, f"Luas bangunan (as-as) 20,15 × 12,15 = {20.15 * 12.15:.1f} m²", 1.7, "start")
    T(sh, x, yb + 8, f"Luas teras = {AREA['R02']:.1f} m²", 1.7, "start")
    T(sh, x, yb + 12, f"Kapasitas: {SEATS_IN} kursi dalam + {SEATS_OUT} teras = {SEATS}", 1.7, "start", bold=True)
    return yb + 12


def a02(idx):
    sh = Sheet()
    v = View(sh, 48, 62, 10)
    draw_plan(v, "arch")
    plan_dims(v)
    # tanda potongan
    section_marker(sh, v, -2.2, 7.6, 22.2, 7.6, "I", 0, -1)
    section_marker(sh, v, 5.0, -2.4, 5.0, 16.9, "II", 1, 0)
    ptitle(sh, 48, 266, "DENAH LANTAI 1", "SKALA 1 : 100", sub="Rencana arsitektur — ukuran as ke as (cm)")
    yb = room_table(sh, 290, 40)
    legend_plan(sh, 290, yb + 12)
    north_arrow(sh, 313, 238, 8)
    notes = NOTES_COMMON + ["Kode pintu (P) & jendela (J/BV)\nlihat Jadwal di lembar A-10.",
                            "Garis potongan I-I & II-II\nlihat lembar A-07."]
    frame(sh, "A-02", "DENAH LANTAI 1\n(Arsitektur)", "1 : 100", idx, TOTAL, notes)
    return sh.svg()


def a03(idx):
    sh = Sheet()
    v = View(sh, 48, 62, 10)
    draw_plan(v, "furn")
    plan_dims(v)
    ptitle(sh, 48, 266, "DENAH LAYOUT FURNITUR & PERALATAN", "SKALA 1 : 100", sub="Tata kursi meja, dapur, musala — kapasitas %d kursi" % SEATS)
    T(sh, 290, 40, "RINGKASAN KAPASITAS", 2.2, "start", bold=True)
    rows = [("Meja 4 kursi (dalam)", str(len(DINING4)), str(len(DINING4) * 4)), ("Meja panjang 6 kursi", "1", "6"),
            ("Meja 4 kursi (teras)", str(len(TERR4)), str(len(TERR4) * 4)), ("JUMLAH", "", str(SEATS))]
    yb = table(sh, 290, 43, [27, 10, 11], 5.2, ["Jenis", "Unit", "Kursi"], rows, fs=1.75, hfs=1.8, aligns=["start", "middle", "middle"])
    T(sh, 290, yb + 6, "Standar yang dipakai:", 1.9, "start", bold=True)
    for i, t in enumerate(["Meja 80×80, kursi 45×45", "Jarak as meja 2,4–2,7 m", "Jalur sirkulasi ≥ 90 cm", "Lorong dapur ≥ 120 cm",
                           "Etalase tinggi 90 cm", "Luas ruang makan ≈ %.1f m²/kursi" % (AREA["R01"] / SEATS_IN)]):
        T(sh, 291, yb + 11 + i * 4.2, "• " + t, 1.75, "start")
    notes = NOTES_COMMON + ["Area biru muda = area basah\n(dapur, WC, wudhu) lantai turun 2–5 cm.",
                            "Peralatan dapur indikatif; sesuaikan\nmenu & vendor."]
    frame(sh, "A-03", "DENAH LAYOUT\nFURNITUR &\nPERALATAN", "1 : 100", idx, TOTAL, notes)
    return sh.svg()


# ================= tampak =================
from elev import *


def callouts(sh, items, x_text, y0, step, fs=1.85, num=False):
    """Callout: teks diurut menurut ketinggian titik agar garis penunjuk hampir horizontal."""
    items = sorted(items, key=lambda it: it[1])
    prev = y0 - step
    for i, (px, py, txt) in enumerate(items):
        if num:
            txt = f"{i + 1}  {txt}"
        ty = max(py, prev + step)
        prev = ty
        L(sh, px, py, x_text - 6, ty, 0.12)
        L(sh, x_text - 6, ty, x_text - 2.2, ty, 0.12)
        C(sh, px, py, 0.45, INK, INK, 0.1)
        T(sh, x_text, ty, txt, fs, "start", ls=1.25)


def levels_left(sh, v, xmark, items, xedge):
    for z, lab in items:
        y = v.Y(z)
        L(sh, xmark, y, xedge, y, 0.1, GRAY, "2 1.2")
        level_mark(sh, xmark, y, lab, side=-1, ln=5.5)


def axis_bubbles(sh, v, ygr, off=17):
    for i, x in enumerate(XS):
        axis_line(sh, v.X(x), ygr + 1, v.X(x), ygr + off - 3.2)
        bubble(sh, v.X(x), ygr + off, str(i + 1), 3.0)


def a05(idx):
    sh = Sheet()
    # ---- depan
    v1 = View(sh, 60, 100, 10, up=True)
    elev_front(v1)
    levels_left(sh, v1, 47, [(ZRIDGE, "+%.2f" % ZRIDGE), (ZE, "+%.2f" % ZE), (0, "±0.00"), (ZT, "-0.03"), (ZG, "-0.35")], v1.X(-0.6) - 1)
    chain_v(v1, [ZG, 0, ZE, ZRIDGE], 20.6, v1.X(20.6) + 7)
    chain_h(v1, [0, 1.2, 3.6, 4.4, 6.8, 9.1, 10.9, 12.9, 15.3, 17.0, 18.5, 20], ZG, v1.Y(ZG) + 9, label_up=True)
    chain_h(v1, XS, ZG, v1.Y(ZG) + 17)
    axis_bubbles(sh, v1, v1.Y(ZG) + 17, 14)
    ptitle(sh, 60, 145, "TAMPAK DEPAN (SELATAN)", "SKALA 1 : 100")
    callouts(sh, [
        (v1.X(17.5), v1.Y(5.0), "Atap genteng metal pasir terakota,\nkemiringan 20°, rangka baja ringan"),
        (v1.X(19.2), v1.Y(ZRIDGE + 0.07), "Bubungan / nok (galvalum)"),
        (v1.X(19.6), v1.Y(3.32), "Lisplang GRC t=20 + talang air Ø4\""),
        (v1.X(19.3), v1.Y(1.9), "Dinding bata plester-acian,\ncat eksterior putih gading"),
        (v1.X(19.6), v1.Y(0.35), "Plint batu alam andesit h=60"),
        (v1.X(20.0), v1.Y(0.85), "Kolom K1 20/20 dilapis batu alam"),
        (v1.X(14.1), v1.Y(1.2), "Kusen aluminium + kaca tempered\n(jendela J1, pintu ganda P1)"),
        (v1.X(16.2), v1.Y(-0.3), "Ramp difabel 1:12 + handrail;\ntangga teras 2 anak tangga (tengah)"),
    ], 282, 55, 10.5)
    # ---- belakang
    v2 = View(sh, 260, 232, 10, up=True, flipx=True)
    elev_rear(v2)
    levels_left(sh, v2, 47, [(ZRIDGE, "+%.2f" % ZRIDGE), (ZE, "+%.2f" % ZE), (0, "±0.00"), (ZG, "-0.35")], v2.X(20.6) - 1)
    chain_v(v2, [ZG, 0, ZE, ZRIDGE], -0.6, v2.X(-0.6) + 7)
    chain_h(v2, [20, 18.5, 17.0, 15.5, 14.7, 11.5, 10.5, 8.6, 7.2, 6.4, 5.5, 0][::1], ZG, v2.Y(ZG) + 9)
    chain_h(v2, XS[::-1], ZG, v2.Y(ZG) + 17)
    axis_bubbles(sh, v2, v2.Y(ZG) + 17, 14)
    ptitle(sh, 60, 273, "TAMPAK BELAKANG (UTARA)", "SKALA 1 : 100")
    callouts(sh, [
        (v2.X(2.5), v2.Y(6.7), "Cerobong exhaust dapur Ø40\n(galvanis + penutup hujan)"),
        (v2.X(5.9), v2.Y(1.5), "Pintu servis dapur (P2) untuk bahan\nbaku & sampah, bordes + 1 anak tangga"),
        (v2.X(7.2), v2.Y(2.25), "Bovenlicht (BV) ventilasi silang"),
        (v2.X(1.0), v2.Y(0.4), "Plint batu alam h=60"),
        (v2.X(1.0), v2.Y(5.2), "Atap — talang & pipa tegak Ø3\""),
    ], 282, 170, 12)
    frame(sh, "A-05", "TAMPAK DEPAN &\nTAMPAK BELAKANG", "1 : 100", idx, TOTAL, NOTES_COMMON + [
        "Warna finishing: dinding putih\ngading, plint & kolom batu alam,\nkusen aluminium hitam doff.",
        "Elevasi tanah rata-rata -0.35;\nsesuaikan kondisi lahan."])
    return sh.svg()


def keyplan(sh, cx, cy):
    """Denah kunci mini dengan arah pandang tampak."""
    s = 1.8
    x, y = cx - 10 * s, cy - 7.25 * s
    R(sh, x, y, 20 * s, 12 * s, "#e4e7ea", INK, 0.4)
    R(sh, x, y + 12 * s, 20 * s, 2.5 * s, "#f3f3f3", INK, 0.3, "1.5 1")
    T(sh, x + 10 * s, y + 6 * s, "BANGUNAN", 1.8, c="#555")

    def arrow(px, py, dx, dy, lab, tx, ty, anc="middle"):
        L(sh, px, py, px + dx * 8, py + dy * 8, 0.5)
        sh.add(f'<polygon points="{n(px + dx * 11)},{n(py + dy * 11)} {n(px + dx * 7 - dy * 2)},{n(py + dy * 7 + dx * 2)} {n(px + dx * 7 + dy * 2)},{n(py + dy * 7 - dx * 2)}" fill="{INK}"/>')
        T(sh, tx, ty, lab, 1.8, anc, bold=True)
    arrow(cx, y + 14.5 * s + 14, 0, -1, "TAMPAK DEPAN", cx, y + 14.5 * s + 17)
    arrow(cx, y - 14, 0, 1, "TAMPAK BELAKANG", cx, y - 17)
    arrow(x - 22, cy, 1, 0, "TAMPAK\nKIRI", x - 24, cy, "end")
    arrow(x + 20 * s + 22, cy, -1, 0, "TAMPAK\nKANAN", x + 20 * s + 24, cy, "start")


def a06(idx):
    sh = Sheet()
    vw = View(sh, 40, 100, 10, up=True)
    elev_side(vw, "W")
    levels_left(sh, vw, 32, [(ZRIDGE, "+%.2f" % ZRIDGE), (ZE, "+%.2f" % ZE), (0, "±0.00"), (ZG, "-0.35")], vw.X(-0.9) - 0.0)
    chain_h(vw, [YEB, 0, 5, 12, TERR_Y, YEF], ZG, vw.Y(ZG) + 9, label_up=True)
    chain_h(vw, [-0.8, 15.3], ZG, vw.Y(ZG) + 17)
    ptitle(sh, 40, 140, "TAMPAK KIRI (BARAT)", "SKALA 1 : 100")
    ve = View(sh, 189, 238, 10, up=True, flipx=True)
    elev_side(ve, "E")
    levels_left(sh, ve, 32 + 0, [(ZRIDGE, "+%.2f" % ZRIDGE), (ZE, "+%.2f" % ZE), (0, "±0.00"), (ZG, "-0.35")], ve.X(15.4) - 1)
    chain_h(ve, [15.3, TERR_Y, 12, 5, 0, YEB], ZG, ve.Y(ZG) + 9)
    chain_h(ve, [15.3, -0.8], ZG, ve.Y(ZG) + 17)
    ptitle(sh, 40, 278, "TAMPAK KANAN (TIMUR)", "SKALA 1 : 100")
    keyplan(sh, 275, 75)
    T(sh, 275, 126, "DENAH KUNCI ARAH TAMPAK", 2.0, bold=True)
    T(sh, 218, 175, "KETERANGAN MATERIAL", 2.2, "start", bold=True)
    mats = ["Atap: genteng metal pasir 0.4 mm, warna terakota", "Rangka atap: baja ringan C75 + reng, kemiringan 20°",
            "Dinding: bata merah ½ bata, plester 1:4, acian", "Plint: batu alam andesit h=60 cm", "Kolom teras: K1 20/20 dilapis batu alam",
            "Kusen: aluminium 4\" hitam doff + kaca tempered", "Lisplang: GRC 20 cm, cat putih", "Talang: PVC/galvalum Ø4\", pipa tegak Ø3\"",
            "Plafon: gypsum 9 mm (dalam), PVC (teras/WC)", "Jendela atas/ventilasi (BV): kaca nako / louvre",
            "Lantai teras: keramik 40×40 anti-slip", "Cerobong dapur: pipa galvanis Ø40 + topi hujan"]
    for i, t in enumerate(mats):
        T(sh, 219, 183 + i * 5.6, "• " + t, 1.85, "start")
    frame(sh, "A-06", "TAMPAK KIRI &\nTAMPAK KANAN", "1 : 100", idx, TOTAL, NOTES_COMMON)
    return sh.svg()


# ================= potongan =================
from secs import *


def hatch_legend(sh, x, y):
    T(sh, x, y, "LEGENDA POTONGAN", 2.2, "start", bold=True)
    items = [("conc", "Beton bertulang (kolom, sloof, ring balk, plat)"), ("brick", "Pasangan bata merah (dinding)"),
             ("stone", "Pondasi batu kali 1:5 (pc:ps)"), ("sand", "Pasir urug / lantai kerja t=5-10"),
             ("earth", "Tanah asli / urugan padat"), ("glass", "Kaca tempered / kusen aluminium")]
    for i, (p, t) in enumerate(items):
        yy = y + 6 + i * 8
        if p == "glass":
            R(sh, x, yy - 2.5, 10, 5, GLASS, INK, 0.3)
        else:
            R(sh, x, yy - 2.5, 10, 5, f"url(#{p})", INK, 0.3)
        T(sh, x + 13, yy, t, 1.8, "start")


def a07(idx):
    sh = Sheet()
    lv = [(ZRIDGE, "+%.2f" % ZRIDGE), (ZRB, "+%.2f" % ZRB), (ZC, "+%.2f" % ZC), (0, "±0.00"), (ZG, "-0.35"), (-1.0, "-1.00")]
    # --- I-I
    v1 = View(sh, 45, 92, 10, up=True)
    section_I(v1)
    levels_left(sh, v1, 31, lv, v1.X(-0.7))
    chain_v(v1, [ZG, 0, ZC, ZRB, ZRIDGE], 20.6, v1.X(20.6) + 7)
    chain_h(v1, XS, ZG - 0.65, v1.Y(ZG) + 14)
    chain_h(v1, [0, 20], ZG - 0.65, v1.Y(ZG) + 22)
    axis_bubbles(sh, v1, v1.Y(ZG) + 22, 9)
    ptitle(sh, 45, 150, "POTONGAN I-I (MEMANJANG)", "SKALA 1 : 100", sub="Dilihat ke arah utara, bidang potong pada y = +7,60 (lihat denah A-02)")
    # --- II-II
    v2 = View(sh, 45, 236, 10, up=True)
    section_II(v2)
    levels_left(sh, v2, 31, lv, v2.X(-0.9))
    chain_v(v2, [ZG, 0, ZC, ZRB, ZRIDGE], 15.4, v2.X(15.4) + 7)
    chain_h(v2, [0, 5, 12, TERR_Y], ZG - 0.65, v2.Y(ZG) + 14)
    chain_h(v2, [YEB, YEF], ZG - 0.65, v2.Y(ZG) + 22)
    ptitle(sh, 45, 277, "POTONGAN II-II (MELINTANG)", "SKALA 1 : 100", sub="Dilihat ke arah timur, bidang potong pada x = +5,00 melalui dapur, counter saji dan teras")
    hatch_legend(sh, 262, 40)
    T(sh, 262, 98, "KETERANGAN STRUKTUR & FINISHING", 2.0, "start", bold=True)
    for i, t in enumerate(["Pondasi: batu kali menerus lebar atas 30,", "   bawah 60, dalam 80 cm dari tanah.",
                           "Sloof SL 15/20 (4Ø10, Ø6-150).", "Kolom K1 20/20 (4Ø12, Ø6-150).",
                           "Ring balk RB 15/20 (4Ø10, Ø6-150).", "Lantai: urug pasir 10 + lantai kerja 5",
                           "   + spesi 3 + keramik/granit tile.", "Atap: kuda-kuda baja ringan, jarak 4,00,",
                           "   penutup genteng metal pasir.", "Plafon: rangka hollow 4×4, gypsum 9 mm,",
                           "   tinggi +3,20 dari lantai.", "Ventilasi atap: lubang angin di lisplang",
                           "   + nok ventilasi."]):
        T(sh, 262, 105 + i * 4.3, t, 1.75, "start")
    frame(sh, "A-07", "POTONGAN I-I &\nPOTONGAN II-II", "1 : 100", idx, TOTAL, NOTES_COMMON + [
        "Struktur indikatif — dimensi final\nmengikuti perhitungan insinyur\nsipil/struktur."])
    return sh.svg()
