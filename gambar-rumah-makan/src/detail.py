"""Lembar detail konstruksi (A-09), jadwal (A-10) dan sampul (A-00)."""
import math
from draft import *
from bldg import *
from secs import cut_rect, cut_poly, foundation, wall_cut, ring
from elev import zu, ground
import sheets as S


# ---------------------------------------------------------------- A-09
def rebar_section(sh, x, y, wid, hgt, nbar, dbar, label, sub, s=200.0):
    """Penampang beton + sengkang + tulangan (skala 1:5, s mm/m). (x,y) = pojok kiri-atas kertas."""
    w, h = wid * s, hgt * s
    R(sh, x, y, w, h, "url(#conc)", INK, 0.5)
    c = 0.025 * s
    R(sh, x + c, y + c, w - 2 * c, h - 2 * c, "none", INK, 0.45)
    r = dbar / 2 * s
    off = c + 0.006 * s + r
    for (bx, by) in ((x + off, y + off), (x + w - off, y + off), (x + off, y + h - off), (x + w - off, y + h - off)):
        C(sh, bx, by, r, INK, INK, 0.2)
    # dimensi
    L(sh, x, y + h + 3, x + w, y + h + 3, 0.25)
    for xx in (x, x + w):
        L(sh, xx, y + h + 1, xx, y + h + 4.5, 0.13)
    T(sh, x + w / 2, y + h + 1.2, str(int(round(wid * 100))), 1.8, base="bot")
    L(sh, x + w + 3, y, x + w + 3, y + h, 0.25)
    for yy in (y, y + h):
        L(sh, x + w + 1, yy, x + w + 4.5, yy, 0.13)
    T(sh, x + w + 2, y + h / 2, str(int(round(hgt * 100))), 1.8, rot=-90, base="bot")
    T(sh, x + w / 2, y + h + 9.5, label, 2.2, bold=True)
    T(sh, x + w / 2, y + h + 13.5, sub, 1.6)


def d1(sh):
    """Detail dinding eksterior belakang (1:25)."""
    v = View(sh, 52, 188, 40, up=True)
    ground(v, -0.95, -0.075)
    # apron paving (luar)
    cut_rect(v, -0.80, ZG - 0.12, 0.725, 0.12, "conc", 0.3)
    cut_rect(v, -0.80, ZG - 0.25, 0.725, 0.13, "sand", 0.25)
    # tanah luar & dalam
    cut_poly(v, [(-0.95, ZG - 0.25), (-0.075, ZG - 0.25), (-0.075, -1.0), (-0.95, -1.0)], "earth", 0.0)
    # lantai dalam
    cut_poly(v, [(0.075, -0.19), (1.15, -0.19), (1.15, -1.0), (0.075, -1.0)], "earth", 0.0)
    cut_rect(v, 0.075, -0.19, 1.075, 0.10, "sand", 0.3)
    cut_rect(v, 0.075, -0.09, 1.075, 0.05, "conc", 0.4)
    v.rect(0.075, -0.04, 1.075, 0.03, "#fff", INK, 0.3)
    v.rect(0.075, -0.01, 1.075, 0.01, INK, INK, 0.3)
    foundation(v, 0, EXT)
    # dinding + plester
    wall_cut(v, 0, EXT, 0, 3.40)
    v.line(-0.075 - 0.02, 0, -0.075 - 0.02, 3.4, 0.2)
    v.line(0.075 + 0.02, 0, 0.075 + 0.02, 3.4, 0.2)
    ring(v, 0)
    # atap: kasau/kuda-kuda (batang atas) dan batang bawah
    top = lambda y: zroof(y) - 0.12
    ytop = 1.15
    v.poly([(-0.80, top(-0.80)), (ytop, top(ytop)), (ytop, top(ytop) - 0.075), (-0.80, top(-0.80) - 0.075)], "#fff", INK, 0.5)
    v.line(0, ZRB, ytop, ZRB, 0.9)
    v.poly([(0, ZRB), (0, ZRB + 0.075), (ytop, ZRB + 0.075), (ytop, ZRB)], "#fff", INK, 0.45)
    # pelat tumpuan & angkur
    v.rect(-0.07, ZRB + 0.0, 0.14, 0.02, INK, INK, 0.3)
    v.line(0.0, ZRB - 0.2, 0.0, ZRB + 0.04, 0.5)
    # penutup + reng
    p = [(-0.80, zroof(-0.80)), (ytop, zroof(ytop)), (ytop, zroof(ytop) - 0.04), (-0.80, zroof(-0.80) - 0.04)]
    v.poly(p, INK, INK, 0.3)
    y = -0.70
    while y < ytop:
        v.rect(y - 0.015, zroof(y) - 0.075, 0.03, 0.03, "#fff", INK, 0.25)
        y += 0.35
    # lisplang & talang
    v.rect(-0.83, ZE - 0.25, 0.03, 0.25, "#fff", INK, 0.4)
    v.poly([(-1.02, ZE - 0.12), (-1.02, ZE - 0.34), (-0.80, ZE - 0.34), (-0.80, ZE - 0.12)], "#fff", INK, 0.35, close=False)
    # plafon luar (soffit)
    v.line(-0.80, ZC, -0.075, ZC, 0.7)
    v.line(-0.80, ZC - 0.03, -0.075, ZC - 0.03, 0.2)
    # plafon dalam
    v.line(0.075, ZC, ytop, ZC, 0.7)
    v.line(0.075, ZC + 0.05, ytop, ZC + 0.05, 0.2)
    v.line(0.5, ZC + 0.05, 0.5, ZRB, 0.3)
    v.line(0.3, ZC + 0.05, 0.3, ZC + 0.05 + 0.0, 0.3)
    # break line lantai
    # dimensi
    chain_v(v, [-1.0, ZG, 0, ZC, ZRB], 1.15, v.X(1.15) + 4)
    T(sh, v.X(-0.4), v.Y(4.05), "80", 1.8, base="bot")
    L(sh, v.X(-0.8), v.Y(3.95), v.X(0), v.Y(3.95), 0.25)
    for yy in (-0.8, 0):
        L(sh, v.X(yy), v.Y(3.95) - 1.5, v.X(yy), v.Y(3.95) + 1.5, 0.15)
    # callouts nomor
    pts = [
        (v.X(0.6), v.Y(zroof(0.6) + 0.02), "Penutup genteng metal pasir + reng 3×3"),
        (v.X(0.6), v.Y(top(0.6) - 0.03), "Batang atas kuda-kuda baja ringan C75"),
        (v.X(-0.815), v.Y(3.32), "Lisplang GRC t=20"),
        (v.X(-1.0), v.Y(3.12), "Talang PVC Ø4\""),
        (v.X(-0.4), v.Y(3.20), "Plafon eave PVC + lubang angin"),
        (v.X(0.0), v.Y(3.50), "Ring balk 15/20 — 4Ø10, Ø6-150"),
        (v.X(0.8), v.Y(3.61), "Batang bawah kuda-kuda (Ø angkur M10)"),
        (v.X(0.8), v.Y(3.22), "Plafon gypsum 9 mm + hollow 4×4 (+3.20)"),
        (v.X(-0.06), v.Y(1.8), "Dinding ½ bata, plester 1:4 + acian + cat"),
        (v.X(0.6), v.Y(0.0), "Keramik/granit tile 60×60"),
        (v.X(0.6), v.Y(-0.025), "Spesi 1:3 t=3 cm"),
        (v.X(0.6), v.Y(-0.065), "Lantai kerja beton t=5 cm"),
        (v.X(0.6), v.Y(-0.14), "Urug pasir t=10 cm"),
        (v.X(0.0), v.Y(-0.1), "Sloof 15/20 — 4Ø10, Ø6-150"),
        (v.X(0.0), v.Y(-0.7), "Pondasi batu kali 1pc:5ps"),
        (v.X(0.0), v.Y(-1.05), "Urug pasir/lantai kerja t=10"),
    ]
    S.callouts(sh, pts, 108, 28, 6.6, fs=1.65, num=True)
    ptitle(sh, 20, 262, "DETAIL A — POTONGAN DINDING BELAKANG & ATAP", "SKALA 1 : 25", fs=2.6)


def d2(sh):
    x0 = 172
    rebar_section(sh, x0, 40, 0.20, 0.20, 4, 0.012, "K1  20/20", "4Ø12 · sengkang Ø6-150")
    rebar_section(sh, x0 + 62, 40, 0.15, 0.20, 4, 0.010, "SL / RB / SL2  15/20", "4Ø10 · Ø6-150")
    rebar_section(sh, x0 + 118, 40, 0.15, 0.20, 4, 0.010, "LINTEL  15/20", "4Ø10 · Ø6-150")
    ptitle(sh, x0, 100, "DETAIL B — PENAMPANG BETON BERTULANG", "SKALA 1 : 5", fs=2.6)
    T(sh, x0, 107, "Selimut beton 25 mm; sambungan tulangan ≥ 40d; kait sengkang 135°.", 1.7, "start")


def d3(sh):
    """Tangga 2 anak tangga (1:25) dan ramp 1:12 (1:50)."""
    w = View(sh, 190, 150, 40, up=True)
    ground(w, 0.45, 2.2)
    w.poly([(-0.6, ZT), (0, ZT), (0, -0.19), (0.45, -0.19), (0.45, ZG - 0.0), (0.45, -0.60), (-0.6, -0.60)], "url(#conc)", INK, 0.5)
    w.line(-0.6, ZT, 0, ZT, 0.9)
    w.line(0, ZT, 0, -0.19, 0.9)
    w.line(0, -0.19, 0.45, -0.19, 0.9)
    w.line(0.45, -0.19, 0.45, ZG, 0.9)
    cut_poly(w, [(0.45, ZG), (2.2, ZG), (2.2, -0.6), (0.45, -0.6)], "earth", 0.0)
    w.line(0.45, ZG, 2.2, ZG, 0.9)
    T(sh, w.X(0.7), w.Y(0.40), "2 anak tangga: tinggi 16 cm,", 1.7, "start")
    T(sh, w.X(0.7), w.Y(0.28), "lebar injakan 45 cm, lebar 3,00 m,", 1.7, "start")
    T(sh, w.X(0.7), w.Y(0.16), "keramik 40×40 anti-slip.", 1.7, "start")
    level_mark(sh, w.X(-0.6) - 2, w.Y(ZT), "-0.03", side=-1, ln=2)
    level_mark(sh, w.X(2.2) + 6, w.Y(ZG), "-0.35", side=1, ln=2)
    ptitle(sh, 172, 178, "DETAIL C — TANGGA TERAS", "SKALA 1 : 25", fs=2.6)
    # ramp
    v = View(sh, 190, 222, 20, up=True)
    rl = 3.84
    ground(v, -2.0, 6.2)
    v.poly([(-1.2, ZT), (0, ZT), (rl, ZG), (rl, ZG - 0.12), (0, ZT - 0.12), (-1.2, ZT - 0.12)], "url(#conc)", INK, 0.5)
    v.line(-1.2, ZT, 0, ZT, 0.9)
    v.line(0, ZT, rl, ZG, 0.9)
    for px in (-1.0, 0.0, 1.28, 2.56, rl):
        pz = ZT if px <= 0 else ZT + (ZG - ZT) * (px / rl)
        v.line(px, pz, px, pz + 0.9, 0.3)
    v.line(-1.0, ZT + 0.9, rl, ZG + 0.9, 0.4)
    v.line(-1.0, ZT + 0.7, rl, ZG + 0.7, 0.2)
    v.text(1.9, 1.15, "RAMP 1:12 — lebar 1,20 m, bordes datar 1,20 m, handrail ganda 0,90 / 0,70", 1.6)
    chain_h(v, [-1.2, 0, rl], ZG - 0.15, v.Y(ZG) + 9)
    level_mark(sh, v.X(-1.2) - 2, v.Y(ZT), "-0.03", side=-1, ln=2)
    level_mark(sh, v.X(rl) + 6, v.Y(ZG), "-0.35", side=1, ln=2)
    ptitle(sh, 172, 252, "DETAIL D — RAMP DIFABEL", "SKALA 1 : 50", fs=2.6)


def a09(idx):
    sh = Sheet()
    d1(sh)
    d2(sh)
    d3(sh)
    frame(sh, "A-09", "DETAIL\nKONSTRUKSI", "1:25 / 1:5", idx, S.TOTAL, S.NOTES_COMMON + [
        "Detail indikatif sesuai praktik\numum; dimensi & tulangan final\nmengikuti hitungan struktur."])
    return sh.svg()



# ---------------------------------------------------------------- A-10
def openings_summary():
    groups = {}
    order = []
    for o in OPS:
        k = o["c"]
        if k not in groups:
            groups[k] = []
            order.append(k)
        groups[k].append(o)
    return order, groups


DESC = {
    "P1": ("Pintu ganda kaca tempered 10 mm, kusen aluminium", "Pintu utama (swing keluar), handle stainless"),
    "P2": ("Pintu plat besi / panel fiber + kusen besi", "Servis dapur (swing keluar), kunci ganda"),
    "P3": ("Pintu panel kayu/HPL, swing dua arah + kaca", "Dapur ↔ ruang makan (jalur pelayan)"),
    "P4": ("Pintu panel PVC/ aluminium", "Dapur ↔ gudang"),
    "P5": ("Pintu PVC/ ABS anti-air", "WC pria & wanita (swing ke dalam)"),
    "P6": ("Pintu aluminium anti-air, lebar bersih 80", "WC difabel (swing keluar), handle tuas"),
    "P8": ("Pintu panel PVC / kayu", "Wudhu & musala"),
    "P9": ("Pintu baja + panic bar", "Pintu darurat, swing keluar"),
    "J1": ("Jendela kaca tempered 8 mm + bovenlicht, alumunium", "Ruang makan (fix + engsel)"),
    "J2": ("Jendela aluminium + kaca bening 5 mm", "Ruang makan samping barat"),
    "J3": ("Jendela aluminium + kaca bening 5 mm", "Dapur — atas bak cuci piring"),
    "J4": ("Jendela aluminium + kaca bening 5 mm", "Ruang makan samping timur"),
    "J5": ("Jendela aluminium + kaca bening 5 mm", "Musala"),
    "J6": ("Jendela aluminium + kaca bening 5 mm", "Musala (timur)"),
    "BV1": ("Bovenlicht aluminium + kaca nako", "Tempat wudhu"),
    "BV2": ("Bovenlicht aluminium + kaca nako", "Dapur (ventilasi silang)"),
    "BV3": ("Bovenlicht aluminium + kaca nako", "WC pria, wanita, difabel"),
    "BV4": ("Louvre aluminium", "Gudang"),
    "JL1": ("Jendela layan geser kaca 5 mm", "Counter saji dapur ↔ etalase"),
    "JL2": ("Jendela layan geser kaca 5 mm", "Counter saji dapur ↔ etalase"),
    "LB": ("Bukaan tanpa daun (ambang beton)", "Lobi WC ↔ ruang makan"),
}


def a10(idx):
    sh = Sheet()
    order, groups = openings_summary()
    pref = {"P": 0, "J": 1, "B": 2}
    def key(k):
        import re
        m = re.match(r"([A-Z]+)(\d*)", k)
        p, num = m.group(1), m.group(2)
        rank = {"P": 0, "J": 1, "BV": 2, "JL": 3, "LB": 4}.get(p, 5)
        return (rank, int(num) if num else 0)
    order = sorted(order, key=key)
    T(sh, 15, 19, "JADWAL PINTU & JENDELA", 3.0, "start", bold=True)
    rows = []
    for k in order:
        g = groups[k]
        sizes = sorted({(round((o["b"] - o["a"]) * 100), round((o["head"] - o["sill"]) * 100)) for o in g})
        sz = " / ".join(f"{w}×{h}" for w, h in sizes)
        sill = ",".join(sorted({str(round(o["sill"] * 100)) for o in g}))
        rows.append((k, sz, sill, str(len(g)), DESC[k][0], DESC[k][1]))
    yb = table(sh, 15, 23, [13, 24, 17, 9, 88, 76], 5.0, ["Kode", "Lebar×Tinggi (cm)", "Ambang (cm)", "Jml", "Bahan / jenis", "Lokasi / keterangan"],
               rows, fs=1.7, hfs=1.8, aligns=["middle", "middle", "middle", "middle", "start", "start"])
    T(sh, 15, yb + 5, "Ambang = tinggi bawah bukaan dari lantai. Kode tampak pada denah A-02 dan tampak A-05/A-06. BV = bovenlicht, JL = jendela layan.", 1.6, "start", c="#444")
    # --- finishing
    y2 = yb + 13
    T(sh, 15, y2, "JADWAL FINISHING RUANG", 3.0, "start", bold=True)
    rows2 = [(r[0], r[1], f"{AREA[r[0]]:.1f}", r[2], r[3], r[4], r[5]) for r in ROOMS]
    yb2 = table(sh, 15, y2 + 4, [11, 33, 15, 52, 54, 42, 13], 5.0, ["Kode", "Ruang", "Luas m²", "Lantai", "Dinding", "Plafon", "Level"], rows2,
                fs=1.65, hfs=1.8, aligns=["middle", "start", "middle", "start", "start", "start", "middle"])
    # --- peralatan
    y3 = yb2 + 9
    T(sh, 15, y3, "DAFTAR PERALATAN DAPUR & FURNITUR (INDIKATIF)", 3.0, "start", bold=True)
    eqs = [("1", "Kompor gas 4 tungku + hood + exhaust fan", "1 set", "4,5 × 0,8 m; cerobong Ø40"), ("2", "Meja persiapan stainless", "1", "3,5 × 0,8 m"),
           ("3", "Bak cuci piring 2 bak + grease trap", "1", "0,65 × 1,85 m"), ("4", "Kulkas 2 pintu / freezer", "2", "0,7 × 0,8 m"),
           ("5", "Meja saji / plating + rak piring", "2", "5,0 × 0,75 m; 1,9 × 0,75 m"), ("6", "Etalase counter saji kaca", "1", "6,6 × 0,8 m, h=0,90"),
           ("7", "Meja makan 4 kursi (dalam + teras)", str(len(DINING4) + len(TERR4)), "0,8 × 0,8 m + 4 kursi"), ("8", "Meja panjang 6 kursi", "1", "2,4 × 0,8 m"),
           ("9", "Kasir + display minuman", "1 set", "1,8 × 0,9 m; 1,1 × 0,85 m")]
    table(sh, 15, y3 + 4, [9, 82, 20, 60], 4.6, ["No", "Peralatan / furnitur", "Jml", "Ukuran / keterangan"], eqs, fs=1.65, hfs=1.8,
          aligns=["middle", "start", "middle", "start"])
    # --- rekap kanan
    x3 = 245
    T(sh, x3, 19, "REKAPITULASI", 3.0, "start", bold=True)
    tot_net = sum(AREA[k] for k in AREA if k != "R02")
    kv = [("Luas bangunan (as-as)", f"{20.15 * 12.15:.1f} m²"), ("Luas teras", f"{AREA['R02']:.1f} m²"), ("Luas total beratap", f"{20.15 * 12.15 + AREA['R02']:.1f} m²"),
          ("Luas ruang makan", f"{AREA['R01']:.1f} m²"), ("Luas dapur + gudang", f"{AREA['R03'] + AREA['R04']:.1f} m²"),
          ("Kursi dalam / teras", f"{SEATS_IN} / {SEATS_OUT}"), ("Total kursi", f"{SEATS}"),
          ("Kloset / urinoir", "4 / 2"), ("Wastafel (lobi+difabel)", "3"), ("Kran wudhu", "4"), ("Parkir mobil / motor", "8 / 12")]
    yb3 = table(sh, x3, 23, [48, 38], 5.0, ["Uraian", "Nilai"], kv, fs=1.7, hfs=1.8, aligns=["start", "middle"])
    T(sh, x3, yb3 + 8, "ASUMSI & CATATAN PERENCANAAN", 2.2, "start", bold=True)
    for i, t in enumerate(["• Gambar rencana awal (DED belum), konsep 1 lantai.", "• Lahan datar 28×33 m, muka ke selatan.",
                           "• Struktur: beton bertulang + atap baja ringan.", "• Jumlah toilet & parkir mengikuti praktik umum;",
                           "  verifikasi dengan peraturan daerah setempat.", "• Gambar MEP (listrik, plumbing, AC, hood)",
                           "  dibuat terpisah setelah menu & peralatan final.", "• Kebutuhan dapur: 8–10 m²/100 kursi tercapai",
                           "  (dapur+gudang ≈ 62 m²).", "• Akses difabel: ramp 1:12, WC difabel,", "  parkir khusus."]):
        T(sh, x3, yb3 + 14 + i * 4.3, t, 1.7, "start")
    frame(sh, "A-10", "JADWAL PINTU,\nJENDELA &\nFINISHING", "—", idx, S.TOTAL, S.NOTES_COMMON)
    return sh.svg()


# ---------------------------------------------------------------- A-00 (sampul + isometri)
def iso_maker(ox, oy, s):
    c30, s30 = math.cos(math.radians(30)), 0.32

    def P(x, y, z):
        return (ox + (x - y) * c30 * s, oy + (x + y) * s30 * s - z * s)
    return P


def poly3(sh, P, pts, fill, stroke=INK, w=0.3):
    p = " ".join(f"{n(P(*q)[0])},{n(P(*q)[1])}" for q in pts)
    sh.add(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{n(w)}" stroke-linejoin="round"/>')


def line3(sh, P, a, b, w=0.25, c=INK):
    x1, y1 = P(*a)
    x2, y2 = P(*b)
    L(sh, x1, y1, x2, y2, w, c)


def box3(sh, P, x0, y0, z0, dx, dy, dz, top, left, right):
    """Balok: sisi atas, sisi selatan (y max), sisi timur (x max) terlihat."""
    x1, y1, z1 = x0 + dx, y0 + dy, z0 + dz
    poly3(sh, P, [(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], left)
    poly3(sh, P, [(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], right)
    poly3(sh, P, [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top)


def iso_building(sh, ox, oy, s):
    P = iso_maker(ox, oy, s)
    # tanah
    poly3(sh, P, [(-4, -3, ZG), (24, -3, ZG), (24, 21, ZG), (-4, 21, ZG)], "#eef2e8", "#b5bfa9", 0.3)
    # perkerasan parkir
    poly3(sh, P, [(-4, 17.5, ZG), (24, 17.5, ZG), (24, 21, ZG), (-4, 21, ZG)], "#dfe2e5", "#b5bfa9", 0.2)
    for i in range(0, 8):
        xx = -2.5 + i * 3.0
        line3(sh, P, (xx, 18.2, ZG), (xx, 20.8, ZG), 0.2, "#fff")
    # teras
    box3(sh, P, 0, 12, ZG, 20, 2.5, ZT - ZG, "#e8e1d4", "#cfc6b5", "#bdb4a3")
    # dinding utama (selatan & timur) + gable timur
    S_ = [(0, 12, ZG), (20, 12, ZG), (20, 12, zu(12.075)), (0, 12, zu(12.075))]
    poly3(sh, P, S_, "#f4efe3")
    E_ = [(20, 0, ZG), (20, 12, ZG), (20, 12, zu(12.075)), (20, YR, zu(YR)), (20, 0, zu(0))]
    poly3(sh, P, E_, "#e2dccd")
    # plint batu alam
    poly3(sh, P, [(0, 12, ZG), (20, 12, ZG), (20, 12, 0.6), (0, 12, 0.6)], "#b9ab95")
    poly3(sh, P, [(20, 0, ZG), (20, 12, ZG), (20, 12, 0.6), (20, 0, 0.6)], "#a89a85")
    # bukaan selatan
    for o in OPS:
        if o["w"] != "S":
            continue
        z1, z2 = (o["sill"], o["head"])
        fill = "#9fc6d9" if o["k"] != "door" else "#7fb2cc"
        poly3(sh, P, [(o["a"], 12, z1), (o["b"], 12, z1), (o["b"], 12, z2), (o["a"], 12, z2)], fill, INK, 0.25)
        if o["k"] == "door":
            line3(sh, P, ((o["a"] + o["b"]) / 2, 12, z1), ((o["a"] + o["b"]) / 2, 12, z2), 0.25)
    # bukaan timur
    for o in OPS:
        if o["w"] != "E":
            continue
        z1, z2 = (o["sill"], o["head"])
        poly3(sh, P, [(20, o["a"], z1), (20, o["b"], z1), (20, o["b"], z2), (20, o["a"], z2)], "#8fb7cb" if o["k"] != "door" else "#6a7f8c", INK, 0.25)
    # papan nama
    poly3(sh, P, [(8.15, 12, 2.45), (11.85, 12, 2.45), (11.85, 12, 3.05), (8.15, 12, 3.05)], "#2b2f33")
    # kolom teras
    for x in XS:
        box3(sh, P, x - 0.1, 14.3, ZT, 0.2, 0.2, 3.6 - ZT, "#fff", "#f4efe3", "#d9d2c2")
        poly3(sh, P, [(x - 0.1, 14.5, ZT), (x + 0.1, 14.5, ZT), (x + 0.1, 14.5, 1.0), (x - 0.1, 14.5, 1.0)], "#b9ab95")
    # tangga + ramp
    box3(sh, P, 8.5, 14.5, ZG, 3.0, 0.45, -0.19 - ZG, "#e8e1d4", "#cfc6b5", "#bdb4a3")
    poly3(sh, P, [(14, 14.5, ZT), (17.84, 14.5, ZG), (17.84, 15.7, ZG), (14, 15.7, ZT)], "#d8d2c6", INK, 0.25)
    # atap: lereng utara (terlihat tipis) & selatan
    poly3(sh, P, [(-0.6, YEB, ZE), (20.6, YEB, ZE), (20.6, YR, ZRIDGE), (-0.6, YR, ZRIDGE)], "#c46a47", INK, 0.35)
    poly3(sh, P, [(-0.6, YR, ZRIDGE), (20.6, YR, ZRIDGE), (20.6, YEF, ZE), (-0.6, YEF, ZE)], "#b8573a", INK, 0.4)
    # garis genteng
    for i in range(1, 22):
        t = i / 22
        line3(sh, P, (-0.6, YR + (YEF - YR) * t, ZRIDGE + (ZE - ZRIDGE) * t), (20.6, YR + (YEF - YR) * t, ZRIDGE + (ZE - ZRIDGE) * t), 0.12, "#8a3d27")
    for i in range(1, 22):
        t = i / 22
        line3(sh, P, (-0.6, YR - (YR - YEB) * t, ZRIDGE - (ZRIDGE - ZE) * t), (20.6, YR - (YR - YEB) * t, ZRIDGE - (ZRIDGE - ZE) * t), 0.1, "#9c4a30")
    # lisplang, tebal tepi timur
    poly3(sh, P, [(20.6, YEF, ZE), (20.6, YEF, ZE - 0.25), (-0.6, YEF, ZE - 0.25), (-0.6, YEF, ZE)], "#f1f1ef")
    poly3(sh, P, [(20.6, YR, ZRIDGE), (20.6, YEF, ZE), (20.6, YEF, ZE - 0.25), (20.6, YR, ZRIDGE - 0.25)], "#f1f1ef")
    poly3(sh, P, [(20.6, YEB, ZE), (20.6, YR, ZRIDGE), (20.6, YR, ZRIDGE - 0.25), (20.6, YEB, ZE - 0.25)], "#f1f1ef")
    # bubungan + cerobong
    line3(sh, P, (-0.6, YR, ZRIDGE), (20.6, YR, ZRIDGE), 1.0, "#6e2f1d")
    box3(sh, P, 2.3, 0.3, zroof(0.5), 0.4, 0.4, 7.0 - zroof(0.5), "#bbb", "#d9d9d9", "#9a9a9a")
    # pohon
    for (x, y, r) in ((-2.5, 8, 2.2), (-2.5, 13, 1.8), (22.5, 19.5, 1.6), (-3.0, 19.5, 1.6)):
        cx, cy = P(x, y, 0)
        C(sh, cx, cy - r * s * 0.9, r * s * 0.65, "#cfe0c3", "#6d8c5a", 0.3)
        C(sh, cx - r * s * 0.2, cy - r * s * 1.0, r * s * 0.3, "#dbe9d0", "none", 0)
        L(sh, cx, cy - r * s * 0.3, cx, cy, 0.5, "#7a5c3c")


def a00(idx):
    sh = Sheet()
    T(sh, 17, 20, "RUMAH MAKAN \"SELERA NUSANTARA\"", 6.5, "start", bold=True)
    T(sh, 17, 29, "GAMBAR RENCANA TEKNIS — RUMAH MAKAN 1 LANTAI · KAPASITAS ± %d KURSI" % SEATS, 3.0, "start", c="#333")
    iso_building(sh, 118, 108, 4.7)
    T(sh, 17, 186, "PERSPEKTIF AKSONOMETRIK (ilustrasi, tanpa skala)", 2.0, "start", italic=True, c="#444")
    # daftar gambar
    T(sh, 240, 44, "DAFTAR GAMBAR", 3.2, "start", bold=True)
    lst = [("A-00", "Sampul, perspektif, daftar gambar"), ("A-01", "Denah situasi (site plan)"), ("A-02", "Denah lantai 1 — arsitektur"),
           ("A-03", "Denah layout furnitur & peralatan"), ("A-04", "Denah pondasi & sloof"), ("A-05", "Tampak depan & belakang"),
           ("A-06", "Tampak kiri & kanan"), ("A-07", "Potongan I-I & II-II"), ("A-08", "Rencana atap"),
           ("A-09", "Detail konstruksi"), ("A-10", "Jadwal pintu, jendela & finishing")]
    scl = ["—", "1:200", "1:100", "1:100", "1:100", "1:100", "1:100", "1:100", "1:100", "1:25 / 1:5", "—"]
    rows = [(a, b, scl[i]) for i, (a, b) in enumerate(lst)]
    table(sh, 240, 48, [14, 56, 16], 5.2, ["No.", "Judul gambar", "Skala"], rows, fs=1.75, hfs=1.8, aligns=["middle", "start", "middle"])
    # data proyek
    T(sh, 17, 194, "DATA PROYEK", 3.0, "start", bold=True)
    kv = [("Fungsi", "Rumah makan (restoran) keluarga + musala"), ("Jumlah lantai", "1 lantai, atap pelana 20°"), ("Lahan (asumsi)", "28 × 33 m = 924 m²"),
          ("Luas bangunan", f"{20.15 * 12.15:.1f} m² + teras {AREA['R02']:.1f} m²"), ("KDB / KLB", "± 31,8 % / 0,32"),
          ("Kapasitas", f"{SEATS_IN} kursi dalam + {SEATS_OUT} kursi teras = {SEATS}"), ("Modul struktur", "As 4,00 m × (5,00 + 7,00 m) + teras 2,40 m"),
          ("Tinggi", "Plafon +3,20 · atap +6,38 · lantai ±0,00 = +0,35 dari tanah")]
    table(sh, 17, 198, [34, 100], 4.8, ["Uraian", "Keterangan"], kv, fs=1.75, hfs=1.8, aligns=["start", "start"])
    # ruang & fungsi
    T(sh, 17, 249, "PROGRAM RUANG", 3.0, "start", bold=True)
    prog = "Ruang makan • Teras makan luar • Dapur • Gudang • Counter saji/etalase • Kasir • WC pria/wanita/difabel • Lobi wastafel • Tempat wudhu • Musala • Area parkir mobil & motor • Ruang servis (TPS, bak lemak, septic)"
    # wrap
    words, line, lines = prog.split(" "), "", []
    for w_ in words:
        if len(line + " " + w_) > 78:
            lines.append(line.strip()); line = w_
        else:
            line += " " + w_
    lines.append(line.strip())
    for i, t in enumerate(lines):
        T(sh, 17, 255 + i * 4.2, t, 1.85, "start")
    # catatan umum
    T(sh, 240, 120, "CATATAN UMUM", 3.0, "start", bold=True)
    notes = ["1. Gambar ini adalah rencana teknis awal (gambar", "    rencana/DED tahap awal) untuk diskusi dan", "    pengurusan perizinan.",
             "2. Ukuran dalam cm, elevasi dalam m, kecuali", "    tertulis lain; as ke as dinding.", "3. Ukuran lahan, daya dukung tanah, dan sempadan",
             "    belum terverifikasi — wajib disesuaikan.", "4. Struktur & MEP dihitung/digambar terpisah oleh", "    tenaga ahli bersertifikat.",
             "5. Dapur harus mengikuti standar higiene sanitasi", "    rumah makan (Permenkes) dan sertifikasi laik", "    higiene sanitasi setempat.",
             "6. Nama proyek, lokasi & pemilik adalah isian", "    sementara (placeholder)."]
    for i, t in enumerate(notes):
        T(sh, 240, 126 + i * 4.6, t, 1.8, "start")
    frame(sh, "A-00", "SAMPUL &\nDAFTAR GAMBAR", "—", idx, S.TOTAL, ["Seluruh lembar berukuran A3\n(420 × 297 mm).",
                                                                       "Skala tercetak benar pada A3.", "Dibuat sebagai file SVG & PDF."])
    return sh.svg()
