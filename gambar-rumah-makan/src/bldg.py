"""Data bangunan (satu sumber kebenaran) + penggambar denah."""
import math
from draft import *

# ---- konstanta geometri (meter) ----
EXT, INT = 0.15, 0.10
XS = [0, 4, 8, 12, 16, 20]
YS = [0, 5, 12]
ZG, ZT, ZF = -0.35, -0.03, 0.0      # tanah, teras, lantai dalam
ZW = -0.05                           # lantai area basah
ZC, ZRB = 3.20, 3.60                 # plafon, atas ring balk
SLOPE = math.tan(math.radians(20))
YEB, YEF, YR = -0.8, 15.3, 7.25       # tepi atap belakang, depan, bubungan
ZE = 3.45
ZRIDGE = ZE + (YR - YEB) * SLOPE
TERR_Y = 14.5
COL = 0.20


def zroof(y):
    return ZE + ((y - YEB) if y <= YR else (YEF - y)) * SLOPE


# ---- dinding: id, x1,y1,x2,y2,tebal ----
WALLS = [
    ("N", 0, 0, 20, 0, EXT), ("S", 0, 12, 20, 12, EXT), ("W", 0, 0, 0, 12, EXT), ("E", 20, 0, 20, 12, EXT),
    ("B", 0, 5, 20, 5, INT),
    ("KG", 9.5, 0, 9.5, 5, INT), ("GW", 13, 0, 13, 5, INT), ("WS", 16.5, 0, 16.5, 3, INT),
    ("WC", 13, 3, 20, 3, INT), ("LD", 18, 3, 18, 5, INT),
    ("MW", 15, 8.8, 15, 12, INT), ("MN", 15, 8.8, 20, 8.8, INT), ("MM", 15, 9.9, 20, 9.9, INT),
]
EXTW = {"N", "S", "W", "E"}
WALL = {w[0]: w for w in WALLS}

# ---- bukaan: c=kode, w=dinding, a..b sepanjang as, k=door/win/pass/open, sill/head dalam m ----
OPS = [
    dict(c="P2", w="N", a=5.5, b=6.4, k="door", sill=0, head=2.1, hinge="b", side=-1, tag=(4.85, -0.6)),
    dict(c="BV2", w="N", a=7.2, b=8.6, k="win", sill=1.8, head=2.4, tag=(7.9, -0.55)),
    dict(c="BV4", w="N", a=10.5, b=11.5, k="win", sill=1.8, head=2.4, tag=(11.0, -0.55)),
    dict(c="BV3", w="N", a=14.7, b=15.5, k="win", sill=1.8, head=2.4, tag=(15.1, -0.55)),
    dict(c="BV3", w="N", a=16.7, b=17.5, k="win", sill=1.8, head=2.4, tag=(17.1, -0.55)),
    dict(c="J1", w="S", a=1.2, b=3.6, k="win", sill=0.6, head=2.4, tag=(2.4, 11.45)),
    dict(c="J1", w="S", a=4.4, b=6.8, k="win", sill=0.6, head=2.4, tag=(5.6, 11.45)),
    dict(c="P1", w="S", a=9.1, b=10.9, k="door", dbl=True, sill=0, head=2.4, hinge="a", side=1, tag=(10.0, 11.2)),
    dict(c="J1", w="S", a=12.9, b=15.3, k="win", sill=0.6, head=2.4, tag=(14.1, 11.45)),
    dict(c="J5", w="S", a=17.0, b=18.5, k="win", sill=1.0, head=2.2, tag=(17.75, 12.62)),
    dict(c="J3", w="W", a=3.1, b=4.5, k="win", sill=1.0, head=2.1, tag=(-0.55, 3.8)),
    dict(c="J2", w="W", a=6.6, b=8.4, k="win", sill=0.9, head=2.4, tag=(-0.55, 7.5)),
    dict(c="J2", w="W", a=9.4, b=11.2, k="win", sill=0.9, head=2.4, tag=(-0.55, 10.3)),
    dict(c="BV3", w="E", a=3.4, b=4.2, k="win", sill=1.8, head=2.4, tag=(20.55, 3.8)),
    dict(c="J4", w="E", a=5.4, b=6.8, k="win", sill=0.9, head=2.4, tag=(20.55, 6.1)),
    dict(c="P9", w="E", a=7.4, b=8.4, k="door", sill=0, head=2.1, hinge="b", side=1, tag=(21.3, 7.35)),
    dict(c="BV1", w="E", a=9.0, b=9.7, k="win", sill=1.7, head=2.3, tag=(20.55, 9.35)),
    dict(c="J6", w="E", a=10.4, b=11.5, k="win", sill=1.0, head=2.2, tag=(20.55, 10.95)),
    dict(c="JL1", w="B", a=1.0, b=3.9, k="pass", sill=0.9, head=2.2, tag=(2.45, 5.75)),
    dict(c="JL2", w="B", a=4.1, b=7.4, k="pass", sill=0.9, head=2.2, tag=(5.75, 5.75)),
    dict(c="P3", w="B", a=8.2, b=9.1, k="door", sill=0, head=2.1, hinge="b", side=1, tag=(8.3, 6.1)),
    dict(c="LB", w="B", a=15.0, b=17.0, k="open", sill=0, head=2.4, tag=(16.0, 5.55)),
    dict(c="P4", w="KG", a=3.5, b=4.4, k="door", sill=0, head=2.1, hinge="a", side=-1, tag=(8.45, 4.45)),
    dict(c="P5", w="WC", a=14.5, b=15.4, k="door", sill=0, head=2.1, hinge="b", side=-1, tag=(14.1, 3.55)),
    dict(c="P5", w="WC", a=16.6, b=17.5, k="door", sill=0, head=2.1, hinge="a", side=-1, tag=(17.0, 3.55)),
    dict(c="P6", w="LD", a=3.9, b=4.8, k="door", sill=0, head=2.1, hinge="b", side=-1, tag=(17.0, 3.35)),
    dict(c="P8", w="MW", a=8.95, b=9.75, k="door", sill=0, head=2.1, hinge="b", side=1, tag=(14.6, 9.35)),
    dict(c="P8", w="MM", a=18.4, b=19.2, k="door", sill=0, head=2.1, hinge="a", side=1, tag=(18.8, 10.9)),
]

# ---- ruang ----
def net(x1, y1, x2, y2, l, r, t, b):
    return (x2 - x1 - l - r) * (y2 - y1 - t - b)

E2, I2 = EXT / 2, INT / 2
AREA = {
    "R01": net(0, 5, 20, 12, E2, E2, I2, E2) - (19.925 - 14.95) * (11.925 - 8.75),
    "R02": (20.15) * (TERR_Y - 12.075),
    "R03": net(0, 0, 9.5, 5, E2, I2, E2, I2),
    "R04": net(9.5, 0, 13, 5, I2, I2, E2, I2),
    "R05": net(13, 0, 16.5, 3, I2, I2, E2, I2),
    "R06": net(16.5, 0, 20, 3, I2, E2, E2, I2),
    "R07": net(13, 3, 18, 5, I2, I2, I2, I2),
    "R08": net(18, 3, 20, 5, I2, E2, I2, I2),
    "R09": net(15, 8.8, 20, 9.9, I2, E2, I2, I2),
    "R10": net(15, 9.9, 20, 12, I2, E2, I2, E2),
}
# kode, nama, lantai, dinding, plafon, level
ROOMS = [
    ("R01", "Ruang Makan", "Granit tile 60×60 doff", "Cat emulsi + wainscot HPL h=90", "Gypsum 9mm, h=3.20", "±0.00"),
    ("R02", "Teras / Makan Luar", "Keramik 40×40 anti-slip", "Cat tekstur + batu alam", "Plafon PVC / kalsiboard", "-0.03"),
    ("R03", "Dapur", "Keramik 30×30 anti-slip", "Keramik 20×25 h=2.10", "Kalsiboard 6mm, h=3.20", "±0.00"),
    ("R04", "Gudang Kering", "Plester + acian, floor hardener", "Cat tembok", "Kalsiboard 6mm, h=3.20", "±0.00"),
    ("R05", "WC Pria", "Keramik 30×30 anti-slip", "Keramik 20×25 h=2.10", "PVC panel, h=3.00", "-0.05"),
    ("R06", "WC Wanita", "Keramik 30×30 anti-slip", "Keramik 20×25 h=2.10", "PVC panel, h=3.00", "-0.05"),
    ("R07", "Lobi / Wastafel", "Granit tile 60×60 doff", "Cat emulsi + keramik h=1.20", "Gypsum 9mm, h=3.00", "±0.00"),
    ("R08", "WC Difabel", "Keramik 30×30 anti-slip", "Keramik 20×25 h=2.10", "PVC panel, h=3.00", "-0.05"),
    ("R09", "Tempat Wudhu", "Keramik 30×30 anti-slip", "Keramik 20×25 h=2.10", "PVC panel, h=3.00", "-0.05"),
    ("R10", "Musala", "Karpet / granit 60×60", "Cat emulsi", "Gypsum 9mm, h=3.00", "±0.00"),
]
NAME = {r[0]: r[1] for r in ROOMS}

# ---- furnitur ----
DINING4 = [(1.6, 7.6), (4.2, 7.6), (6.8, 7.6), (9.4, 7.6), (12.0, 7.6), (14.6, 7.6), (1.6, 10.3), (4.2, 10.3), (13.0, 10.3)]
LONGT = (17.5, 6.9)
TERR4 = [(1.6, 13.25), (4.2, 13.25), (6.8, 13.25), (13.3, 13.25), (15.9, 13.25), (18.5, 13.25)]
SEATS_IN = len(DINING4) * 4 + 6
SEATS_OUT = len(TERR4) * 4
SEATS = SEATS_IN + SEATS_OUT


# ================= penggambar denah =================
def wall_rects(wid):
    _, x1, y1, x2, y2, t = WALL[wid]
    horiz = y1 == y2
    a0, b0 = (x1, x2) if horiz else (y1, y2)
    if wid in EXTW:
        a0 -= t / 2
        b0 += t / 2
    ops = sorted([o for o in OPS if o["w"] == wid], key=lambda o: o["a"])
    pieces, cur = [], a0
    for o in ops:
        if o["a"] > cur:
            pieces.append((cur, o["a"]))
        cur = o["b"]
    if cur < b0:
        pieces.append((cur, b0))
    rs = []
    for p, q in pieces:
        rs.append((p, y1 - t / 2, q - p, t) if horiz else (x1 - t / 2, p, t, q - p))
    return rs


def draw_walls(v):
    allr = [r for w in WALLS for r in wall_rects(w[0])]
    for r in allr:
        v.rect(*r, fill=INK, stroke=INK, sw=0.7)
    for r in allr:
        v.rect(*r, fill=WALLFILL, stroke=None)


def draw_columns(v, terrace=True):
    for x in XS:
        for y in YS:
            v.rect(x - COL / 2, y - COL / 2, COL, COL, INK, INK, 0.2)
    if terrace:
        for x in XS:
            v.rect(x - COL / 2, 14.4 - COL / 2, COL, COL, INK, INK, 0.2)


def draw_opening(v, o):
    wid = o["w"]
    _, x1, y1, x2, y2, t = WALL[wid]
    horiz = y1 == y2
    a, b = o["a"], o["b"]
    wd = b - a
    c = y1 if horiz else x1

    def pt(u, off):  # u sepanjang as, off tegak lurus
        return (u, c + off) if horiz else (c + off, u)

    def ln(u1, o1, u2, o2, w=0.18, dash=None):
        p, q = pt(u1, o1), pt(u2, o2)
        v.line(p[0], p[1], q[0], q[1], w, dash=dash)

    # kusen/jamb
    ln(a, -t / 2, a, t / 2, 0.25)
    ln(b, -t / 2, b, t / 2, 0.25)
    k = o["k"]
    if k in ("win", "pass"):
        dashed = "1.2 0.8" if o["sill"] >= 1.7 else None
        ln(a, -t / 2, b, -t / 2, 0.22)
        ln(a, t / 2, b, t / 2, 0.22)
        ln(a, -t / 6, b, -t / 6, 0.12, dashed)
        ln(a, t / 6, b, t / 6, 0.12, dashed)
    elif k == "open":
        ln(a, 0, b, 0, 0.15, "1.4 1")
    elif k == "door":
        w = wd
        dbl = o.get("dbl")
        side = o["side"]
        if dbl:
            hw = wd / 2
            for hinge_u, closed_u in ((a, a + hw), (b, b - hw)):
                H = pt(hinge_u, 0)
                Cc = pt(closed_u, 0)
                O = pt(hinge_u, side * hw)
                v.line(H[0], H[1], O[0], O[1], 0.35)
                v.arc(H[0], H[1], Cc[0], Cc[1], O[0], O[1])
        else:
            hu, cu = (a, b) if o["hinge"] == "a" else (b, a)
            H, Cc, O = pt(hu, 0), pt(cu, 0), pt(hu, side * w)
            v.line(H[0], H[1], O[0], O[1], 0.35)
            v.arc(H[0], H[1], Cc[0], Cc[1], O[0], O[1])


def draw_tag(v, o):
    tx, ty = o["tag"]
    code = o["c"]
    x, y = v.P(tx, ty)
    if o["k"] == "door":
        C(v.sh, x, y, 1.9, "#fff", INK, 0.2)
    else:
        w = 1.45 * len(code) + 1.2
        R(v.sh, x - w / 2, y - 1.45, w, 2.9, "#fff", INK, 0.2)
    T(v.sh, x, y, code, 1.55, bold=True)


def draw_terrace(v, furn=False):
    v.rect(-0.075, 12.075, 20.15, TERR_Y - 12.075, "url(#tilef)", INK, 0.35)
    # tangga depan + ramp
    v.rect(8.5, TERR_Y, 3.0, 0.45, "#fff", INK, 0.3)
    v.line(8.5, TERR_Y + 0.225, 11.5, TERR_Y + 0.225, 0.1, c=GRAY)
    v.text(10.0, TERR_Y + 0.7, "TANGGA (2 anak tangga t=16)", 1.5, base="mid")
    v.rect(14.0, TERR_Y, 3.84, 1.2, "#fff", INK, 0.3)
    for i in range(1, 8):
        v.line(14.0 + i * 3.84 / 8, TERR_Y, 14.0 + i * 3.84 / 8, TERR_Y + 1.2, 0.08, c=GRAY)
    v.line(14.0, TERR_Y + 1.2, 17.84, TERR_Y + 1.2, 0.2, dash="1.5 1")
    v.text(15.92, TERR_Y + 0.6, "RAMP 1:12 (difabel)", 1.6)
    v.line(14.0, TERR_Y + 0.6 + 0.0, 14.0, TERR_Y + 0.6, 0.1)


def draw_fixtures(v):
    # ---- WC pria: bilik kloset, 2 urinoir
    pw = 0.05
    v.line(13.05, 1.6, 14.25, 1.6, 0.18)
    v.line(14.25, 0.075, 14.25, 1.6, 0.18)
    kloset(v, 13.65, 0.075, 0)
    # pintu bilik (daun 0.8, engsel kiri)
    v.line(13.3, 1.6, 13.3, 2.4, 0.3)
    v.arc(13.3, 1.6, 14.1, 1.6, 13.3, 2.4)
    for ux in (15.0, 15.9):
        urinal(v, ux, 0.075)
    v.line(15.45, 0.075, 15.45, 0.6, 0.12)
    floordrain(v, 15.2, 2.0)
    # ---- WC wanita: 2 bilik
    v.line(17.525, 1.6, 19.925, 1.6, 0.18)
    for px in (17.525, 18.725):
        v.line(px, 0.075, px, 1.6, 0.18)
    kloset(v, 18.125, 0.075, 0)
    kloset(v, 19.325, 0.075, 0)
    for hx in (17.7, 18.9):
        v.line(hx, 1.6, hx, 2.4, 0.3)
        v.arc(hx, 1.6, hx + 0.8, 1.6, hx, 2.4)
    floordrain(v, 17.0, 1.3)
    # ---- Lobi: wastafel counter
    v.rect(13.05, 3.25, 0.6, 1.5, "#fff", INK, 0.2)
    for yy in (3.7, 4.3):
        v.ell(13.35, yy, 0.17, 0.2, "#fff", INK, 0.15)
        v.circ(13.35, yy - 0.1, 0.025, INK, INK, 0.05)
    v.rect(13.06, 3.2, 0.05, 1.6, "#d9dde0", INK, 0.1)
    # ---- WC difabel
    kloset(v, 19.4, 3.05, 0, big=True)
    v.rect(18.05, 3.9, 0.45, 0.5, "#fff", INK, 0.2)
    v.ell(18.27, 4.15, 0.14, 0.17, "#fff", INK, 0.15)
    v.line(19.925, 3.5, 19.925, 4.5, 0.4, c="#666")   # handrail
    v.line(19.1, 3.07, 19.7, 3.07, 0.4, c="#666")
    floordrain(v, 18.6, 4.55)
    # ---- Wudhu
    v.rect(15.05, 9.5, 4.85, 0.32, "#fff", INK, 0.2)
    v.text(17.5, 9.66, "BANGKU WUDHU", 1.2, c="#555")
    for xx in (15.8, 16.9, 18.0, 19.1):
        v.circ(xx, 8.93, 0.06, "#fff", INK, 0.15)
    floordrain(v, 16.2, 9.25)


def kloset(v, cx, y0, rot, big=False):
    v.rect(cx - 0.2, y0, 0.4, 0.2, "#fff", INK, 0.18)
    v.ell(cx, y0 + 0.2 + 0.24, 0.18, 0.26, "#fff", INK, 0.18)


def urinal(v, cx, y0):
    v.rect(cx - 0.17, y0, 0.34, 0.12, "#fff", INK, 0.15)
    v.poly([(cx - 0.15, y0 + 0.12), (cx + 0.15, y0 + 0.12), (cx + 0.1, y0 + 0.4), (cx - 0.1, y0 + 0.4)], "#fff", INK, 0.15)


def floordrain(v, x, y):
    v.rect(x - 0.08, y - 0.08, 0.16, 0.16, "#fff", INK, 0.12)
    v.line(x - 0.08, y - 0.08, x + 0.08, y + 0.08, 0.08)
    v.line(x - 0.08, y + 0.08, x + 0.08, y - 0.08, 0.08)


def chair(v, cx, cy, face):
    """face: arah muka kursi (dx,dy) menuju meja. Kursi 0.45."""
    v.rect(cx - 0.225, cy - 0.225, 0.45, 0.45, "#fff", INK, 0.15)
    dx, dy = face
    # sandaran di sisi berlawanan dengan meja
    if dx:
        v.line(cx - dx * 0.2, cy - 0.2, cx - dx * 0.2, cy + 0.2, 0.45)
    else:
        v.line(cx - 0.2, cy - dy * 0.2, cx + 0.2, cy - dy * 0.2, 0.45)


def table4(v, cx, cy):
    off = 0.55
    for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        chair(v, cx + dx * off, cy + dy * off, (-dx, -dy))
    v.rect(cx - 0.4, cy - 0.4, 0.8, 0.8, "#fff", INK, 0.22)
    v.line(cx - 0.4, cy - 0.4, cx + 0.4, cy + 0.4, 0.06, c=GRAY)
    v.line(cx - 0.4, cy + 0.4, cx + 0.4, cy - 0.4, 0.06, c=GRAY)


def table_long(v, cx, cy):
    for i in (-0.8, 0, 0.8):
        chair(v, cx + i, cy - 0.4 - 0.225 + 0.1, (0, 1))
        chair(v, cx + i, cy + 0.4 + 0.225 - 0.1, (0, -1))
    v.rect(cx - 1.2, cy - 0.4, 2.4, 0.8, "#fff", INK, 0.22)


def eq(v, x, y, w, h, label=None, fs=1.3, fill="#fff", rot=0, dash=None, sw=0.2, c=INK):
    v.rect(x, y, w, h, fill, c, sw, dash)
    if label:
        v.text(x + w / 2, y + h / 2, label, fs, rot=rot, c="#333")


def draw_furniture(v):
    # --- dapur
    eq(v, 0.6, 0.075, 4.5, 0.8, None)
    for i in range(4):
        x0 = 0.6 + i * 1.125
        v.line(x0, 0.075, x0, 0.875, 0.1)
        for dx in (0.3, 0.8):
            v.circ(x0 + dx, 0.475, 0.13, "none", INK, 0.14)
            v.circ(x0 + dx, 0.475, 0.06, "none", INK, 0.1)
    v.rect(0.5, 0.075, 4.7, 1.0, "none", GRAY, 0.15, "1.6 1")
    v.text(2.85, 1.25, "KOMPOR 4 TUNGKU + HOOD (cerobong ke atap)", 1.25, c="#333")
    eq(v, 0.075, 1.0, 0.7, 0.8, "KULKAS", 1.0, rot=-90)
    eq(v, 0.075, 1.8, 0.7, 0.8, "FREEZER", 1.0, rot=-90)
    eq(v, 2.2, 2.1, 3.5, 0.8, "MEJA PERSIAPAN (stainless)", 1.3)
    eq(v, 0.075, 2.95, 0.65, 1.85, None)
    for yy in (3.4, 4.35):
        v.rect(0.15, yy - 0.37, 0.5, 0.75, "#fff", INK, 0.15, rx=0.04)
    v.text(0.4, 3.9, "BAK CUCI PIRING", 1.1, rot=-90, c="#333")
    eq(v, 3.0, 4.15, 5.0, 0.75, "MEJA SAJI / PLATING", 1.3)
    eq(v, 1.0, 4.15, 1.9, 0.75, "RAK PIRING", 1.2)
    eq(v, 8.85, 0.075, 0.6, 2.7, "RAK BUMBU", 1.1, rot=-90)
    floordrain(v, 4.0, 3.5)
    floordrain(v, 1.2, 3.9)
    # --- gudang
    eq(v, 9.58, 0.075, 3.35, 0.5, "RAK BAHAN KERING", 1.2)
    eq(v, 12.4, 0.62, 0.53, 2.2, "RAK", 1.1, rot=-90)
    eq(v, 9.6, 2.0, 1.2, 0.9, "CHILLER\n/ FREEZER", 1.2)
    eq(v, 9.6, 3.75, 1.4, 0.9, "STOK\nMINUMAN", 1.2)
    # --- etalase, kasir
    eq(v, 0.9, 5.075, 6.6, 0.8, None)
    v.line(0.95, 5.35, 7.45, 5.35, 0.08, c=GRAY)
    v.text(4.2, 5.62, "ETALASE / COUNTER SAJI (kaca, h=0.90 + vitrin)", 1.25, c="#333")
    eq(v, 6.5, 11.0, 1.8, 0.9, "KASIR", 1.4)
    v.rect(7.5, 11.1, 0.5, 0.35, "#e8ecef", INK, 0.12)
    eq(v, 11.3, 11.05, 1.1, 0.85, "DISPLAY\nMINUMAN", 1.0)
    # --- meja & kursi
    for (x, y) in DINING4 + TERR4:
        table4(v, x, y)
    table_long(v, *LONGT)
    # --- musala
    for xx in (15.2, 16.05, 16.9, 17.75):
        v.rect(xx, 10.95, 0.7, 0.85, "#f0f0f0", INK, 0.12)
        v.line(xx + 0.05, 11.03, xx + 0.65, 11.03, 0.2, c="#777")
    kx, ky = 17.9, 10.75
    ang = math.radians(295)
    dx, dy = math.sin(ang), -math.cos(ang)
    ex, ey = kx + dx * 1.3, ky + dy * 1.3
    v.line(kx, ky, ex, ey, 0.35, c=INK)
    v.sh.add(f'<polygon points="{n(v.X(ex + dx * 0.2))},{n(v.Y(ey + dy * 0.2))} {n(v.X(ex - dy * 0.1))},{n(v.Y(ey + dx * 0.1))} {n(v.X(ex + dy * 0.1))},{n(v.Y(ey - dx * 0.1))}" fill="{INK}"/>')


def room_labels(v, furn=False):
    def lab(x, y, name, area=None, fs=2.4, code=None):
        s = name if area is None else f"{name}\n{area:.1f} m²"
        v.text(x, y, s, fs, bold=True)

    if furn:
        v.text(10.3, 6.6, "R01 RUANG MAKAN  (±0.00)  ·  %.1f m²" % AREA["R01"], 1.8, bold=True, c="#222")
        v.text(10.0, 13.55, "R02 TERAS · %.1f m²" % AREA["R02"], 1.5, bold=True, c="#222")
        v.text(5.6, 1.8, "R03 DAPUR · %.1f m²" % AREA["R03"], 1.6, bold=True)
        v.text(11.25, 1.35, "R04 GUDANG\n%.1f m²" % AREA["R04"], 1.4, bold=True)
        v.text(15.1, 1.1, "WC PRIA", 1.3, bold=True)
        v.text(16.95, 0.95, "WC\nWANITA", 1.1, bold=True)
        v.text(15.6, 4.1, "LOBI /\nWASTAFEL", 1.3, bold=True)
        v.text(19.0, 4.45, "WC\nDIFABEL", 1.0, bold=True)
        v.text(17.5, 9.28, "R09 TEMPAT WUDHU", 1.2, bold=True)
        v.text(19.25, 11.25, "R10\nMUSALA", 1.2, bold=True)
        v.text(16.4, 10.35, "kiblat ± 295°", 1.1, c="#333", italic=True)
        return
    lab(10.0, 8.9, "R01  RUANG MAKAN", AREA["R01"], 3.0)
    v.text(10.0, 9.9, "Lantai ±0.00 · kapasitas dalam ± %d kursi" % SEATS_IN, 1.7, c="#333", italic=True)
    lab(4.5, 13.3, "R02  TERAS / MAKAN LUAR", AREA["R02"], 2.2)
    lab(4.7, 2.6, "R03  DAPUR", AREA["R03"], 2.8)
    lab(11.25, 2.4, "R04\nGUDANG", AREA["R04"], 2.0)
    v.text(15.25, 1.5, "R05\nWC PRIA", 1.7, bold=True)
    v.text(16.95, 0.8, "R06\nWC\nWANITA", 1.2, bold=True)
    v.text(15.9, 4.2, "R07\nLOBI /\nWASTAFEL", 1.3, bold=True)
    v.text(19.05, 4.3, "R08\nWC\nDIFABEL", 1.0, bold=True)
    v.text(17.5, 9.28, "R09  TEMPAT WUDHU", 1.25, bold=True)
    v.text(17.5, 11.05, "R10  MUSALA", 1.6, bold=True)
    v.text(17.5, 11.65, "%.1f m²" % AREA["R10"], 1.3, bold=True)


def draw_plan(v, mode="arch"):
    """mode: 'arch' | 'furn'."""
    furn = mode == "furn"
    sh = v.sh
    draw_terrace(v)
    if furn:
        for (x, y, w, h) in ((0.075, 0.075, 9.4, 4.9), (13.05, 0.075, 6.9, 2.9), (18.05, 3.05, 1.9, 1.9), (15.05, 8.85, 4.9, 1.05)):
            v.rect(x, y, w, h, "#e6edf2", None)
        v.rect(0.075, 5.05, 19.85, 6.875, "url(#tilef)", None)
    draw_walls(v)
    draw_fixtures(v)
    if furn:
        draw_furniture(v)
    for o in OPS:
        draw_opening(v, o)
    draw_columns(v)
    room_labels(v, furn)
    if not furn:
        for o in OPS:
            draw_tag(v, o)


def plan_dims(v, ox_chain=True):
    sh = v.sh
    Y0 = v.Y(0)
    # atas: modul as + total
    chain_h(v, XS, -0.075, v.Y(0) - 14)
    chain_h(v, [0, 20], -0.075, v.Y(0) - 22)
    # bawah: bukaan dinding depan, as, total (terhadap garis y=14.5)
    pts = [0, 1.2, 3.6, 4.4, 6.8, 9.1, 10.9, 12.9, 15.3, 17.0, 18.5, 20]
    ybot = v.Y(TERR_Y + 0.9) + 8
    chain_h(v, pts, 12.075, ybot, label_up=True)
    chain_h(v, XS, 12.075, ybot + 8)
    chain_h(v, [0, 20], 12.075, ybot + 16)
    # kiri: as & total
    xl = v.X(0) - 14
    chain_v(v, YS + [14.5], -0.075, xl)
    # kanan: ruang
    xr = v.X(20) + 14
    chain_v(v, [0, 3, 5, 8.8, 9.9, 12, 14.5], 20.075, xr)
    xr2 = xr + 8
    chain_v(v, [0, 12, 14.5], 20.075, xr2)
    # gelembung as
    for i, x in enumerate(XS):
        bubble(sh, v.X(x), v.Y(0) - 32, str(i + 1), 3.0)
        axis_line(sh, v.X(x), v.Y(0) - 29, v.X(x), v.Y(0) - 3)
    for lab, y in zip(["C", "B", "A"], YS):
        bubble(sh, xr2 + 9, v.Y(y), lab, 3.0)
