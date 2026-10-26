"""Potongan I-I (memanjang, y=7.6, pandang utara) dan II-II (melintang, x=5.0, pandang timur)."""
from draft import *
from bldg import *
from elev import zu, person, ground, GLASS

CUT = INK


def cut_poly(v, pts, pat="brick", w=0.5):
    v.poly(pts, f"url(#{pat})", INK, w)


def cut_rect(v, x, z, w, h, pat="brick", sw=0.5):
    v.rect(x, z, w, h, f"url(#{pat})", INK, sw)


def foundation(v, c, t=0.15):
    """Pondasi batu kali + sloof + lantai kerja, as di koordinat c (horizontal)."""
    cut_rect(v, c - 0.4, -1.10, 0.8, 0.10, "sand", 0.3)
    cut_poly(v, [(c - 0.30, -1.00), (c + 0.30, -1.00), (c + 0.15, -0.20), (c - 0.15, -0.20)], "stone", 0.45)
    cut_rect(v, c - t / 2, -0.20, t, 0.20, "conc", 0.5)


def wall_cut(v, c, t, z0, z1, pat="brick"):
    cut_rect(v, c - t / 2, z0, t, z1 - z0, pat, 0.45)


def ring(v, c, t=0.15):
    cut_rect(v, c - t / 2, ZRB - 0.20, t, 0.20, "conc", 0.5)


def chair_cut(v, cx, face):
    """Kursi terpotong (tinggi dudukan .45, sandaran .90). face=+1 sandaran di kanan."""
    v.rect(cx - 0.22, 0.42, 0.44, 0.04, INK, INK, 0.2)
    v.rect(cx + face * 0.19, 0.46, 0.03 * face if face > 0 else -0.03, 0.44, INK, INK, 0.2)
    for dx in (-0.2, 0.2):
        v.line(cx + dx, 0, cx + dx, 0.42, 0.35)


def table_cut(v, cx):
    v.rect(cx - 0.4, 0.72, 0.8, 0.04, INK, INK, 0.25)
    for dx in (-0.34, 0.34):
        v.line(cx + dx, 0, cx + dx, 0.72, 0.5)


def table_thin(v, cx, w=0.8, h=0.75):
    v.rect(cx - w / 2, h - 0.04, w, 0.04, "#fff", INK, 0.2)
    for dx in (-w / 2 + 0.05, w / 2 - 0.05):
        v.line(cx + dx, 0, cx + dx, h - 0.04, 0.2)


def column_thin(v, c, z0=0, z1=ZRB):
    v.rect(c - 0.1, z0, 0.2, z1 - z0, "#fff", INK, 0.2)


def truss_y(v, xshow=True):
    """Kuda-kuda baja ringan (tampak, sumbu horizontal = y), sebagian: y 0..14.4."""
    zb = ZRB
    top = lambda y: zroof(y) - 0.12
    pts_b = [0, 2.4, 4.8, 7.25, 9.6, 12.0, 14.4]
    # bottom chord
    v.line(0, zb, 14.4, zb, 0.45, c="#444")
    # top chord
    v.line(0, top(0), YR, top(YR), 0.45, c="#444")
    v.line(YR, top(YR), 14.4, top(14.4), 0.45, c="#444")
    for i, y in enumerate(pts_b[1:-1], 1):
        v.line(y, zb, y, top(y), 0.2, c="#555")
    for i in range(len(pts_b) - 1):
        y0, y1 = pts_b[i], pts_b[i + 1]
        if y1 <= YR:
            v.line(y0, zb, y1, top(y1), 0.18, c="#555") if i % 2 == 0 else v.line(y1, zb, y0, top(y0), 0.18, c="#555")
        else:
            v.line(y0, top(y0), y1, zb, 0.18, c="#555") if i % 2 == 1 else v.line(y1, top(y1), y0, zb, 0.18, c="#555")


def roof_assembly_y(v):
    """Penutup + reng + kasau terpotong di bidang II-II (horizontal = y)."""
    for (y0, y1) in ((YEB, YR), (YR, YEF)):
        p = [(y0, zroof(y0)), (y1, zroof(y1)), (y1, zroof(y1) - 0.07), (y0, zroof(y0) - 0.07)]
        v.poly(p, INK, INK, 0.3)
    # gording (kotak kecil)
    for y in [0.1, 1.3, 2.5, 3.7, 4.9, 6.1, 7.15, 8.4, 9.6, 10.8, 12.0, 13.2, 14.4, 15.2]:
        v.rect(y - 0.04, zroof(y) - 0.15, 0.08, 0.08, "#fff", INK, 0.25)
    # lisplang + talang
    for yy, sgn in ((YEB, -1), (YEF, 1)):
        v.rect(yy - (0.02 if sgn < 0 else 0.02), ZE - 0.25, 0.04, 0.25, "#fff", INK, 0.35)
        v.line(yy, ZE - 0.25, yy + (0.25 if sgn < 0 else -0.25), ZE - 0.25, 0.3)


def section_I(v):
    """Potongan I-I (memanjang). Horizontal = x."""
    ground(v, -3.5, 24)
    # urugan / tanah bawah
    cut_rect(v, -1.5, -1.5, 23, 1.15 - 0.0, "earth", 0.0)
    # lantai dalam
    cut_rect(v, 0.075, -0.30, 19.85, 0.18, "sand", 0.3)
    cut_rect(v, 0.075, -0.12, 19.85, 0.12, "conc", 0.4)
    v.line(0.075, 0, 19.925, 0, 0.6)
    for c in (0, 20):
        foundation(v, c)
    # dinding barat
    wall_cut(v, 0, EXT, 0, 3.40)
    ring(v, 0)
    cut_poly(v, [(-EXT / 2, ZRB), (EXT / 2, ZRB), (EXT / 2, zu(7.6)), (-EXT / 2, zu(7.6))], "brick", 0.45)
    cut_poly(v, [(20 - EXT / 2, ZRB), (20 + EXT / 2, ZRB), (20 + EXT / 2, zu(7.6)), (20 - EXT / 2, zu(7.6))], "brick", 0.45)
    # dinding timur dengan pintu P9 (y 7.4-8.4 mencakup y=7.6)
    wall_cut(v, 20, EXT, 2.1, 3.40)
    cut_rect(v, 20 - EXT / 2, 2.1, EXT, 0.18, "conc", 0.4)
    ring(v, 20)
    v.rect(19.9, 0, 0.0, 2.1, "none", INK, 0.2)
    v.line(19.925, 0, 19.925, 2.1, 0.2, dash="1.5 1")
    v.line(20.075, 0, 20.075, 2.1, 0.2, dash="1.5 1")
    v.text(19.0, 1.05, "P9", 1.5, bold=True)
    # gable: dinding diatas ring sampai muka atap
    # atap terpotong (y=7.6 hampir bubungan)
    zr = zroof(7.6)
    v.poly([(-0.6, zr), (20.6, zr), (20.6, zr - 0.10), (-0.6, zr - 0.10)], INK, INK, 0.3)
    # bubungan di belakang bidang potong
    v.rect(-0.6, ZRIDGE, 21.2, 0.12, "#e0e3e6", INK, 0.3)
    # kuda-kuda dilihat tegak
    for x in XS:
        v.line(x, ZRB, x, zroof(YR) - 0.15, 0.5, c="#555")
    v.line(0, ZRB + 0.0, 20, ZRB, 0.45, c="#555")
    # gording & nok
    v.line(-0.6, zroof(YR) - 0.12, 20.6, zroof(YR) - 0.12, 0.2, c="#555")
    # plafon
    v.line(0.075, ZC, 19.925, ZC, 0.7)
    v.line(0.075, ZC + 0.05, 19.925, ZC + 0.05, 0.2)
    for x in [i * 1.0 + 0.5 for i in range(20)]:
        v.line(x, ZC + 0.05, x, ZRB, 0.1, c="#777")
    # --- tampak dinding y=5 di belakang bidang potong (garis tipis)
    v.line(0.075, 0, 0.075, ZC, 0.15)
    for x in XS[1:-1]:
        column_thin(v, x, 0, ZRB)
    for (a, b, z1, z2) in ((1.0, 3.9, 0.9, 2.2), (4.1, 7.4, 0.9, 2.2)):
        v.rect(a, z1, b - a, z2 - z1, GLASS, INK, 0.25)
        v.line(a, 0.9, b, 0.9, 0.3)
    v.rect(8.2, 0, 0.9, 2.1, "#fff", INK, 0.25)
    v.rect(15.0, 0, 2.0, 2.4, "none", INK, 0.2)
    v.text(16.0, 1.2, "LB", 1.5)
    # etalase
    v.rect(0.9, 0, 6.6, 0.9, "#fff", INK, 0.3)
    v.line(0.9, 0.9, 7.5, 0.9, 0.5)
    # --- furnitur terpotong y=7.6 (meja baris-1)
    for (x, y) in DINING4:
        if abs(y - 7.6) < 0.01:
            table_cut(v, x)
            chair_cut(v, x - 0.55, -1)
            chair_cut(v, x + 0.55, 1)
    for dx in (-0.8, 0, 0.8):
        chair_cut(v, LONGT[0] + dx, 1)
    # manusia
    person(v, 9.5, 0, 1.7)
    person(v, 10.3, 0, 1.6)
    # label
    v.text(10.0, 2.75, "R01  RUANG MAKAN", 2.3, bold=True)


def section_II(v):
    """Potongan II-II (melintang). Horizontal = y (utara di kiri). Bidang potong x=5.0."""
    ground(v, -3.5, 19.5)
    # terasering tanah
    cut_rect(v, -1.5, -1.5, 18, 1.15, "earth", 0.0)
    # lantai dalam & teras
    cut_rect(v, 0.075, -0.30, 11.85, 0.18, "sand", 0.3)
    cut_rect(v, 0.075, -0.12, 11.85, 0.12, "conc", 0.4)
    v.line(0.075, 0, 11.925, 0, 0.6)
    cut_rect(v, 12.075, -0.30, 2.425, 0.18, "sand", 0.3)
    cut_rect(v, 12.075, -0.23, 2.425, 0.20, "conc", 0.45)
    cut_rect(v, 14.30, -0.45, 0.20, 0.45, "conc", 0.45)           # balok tepi teras
    v.line(12.075, ZT, 14.5, ZT, 0.6)
    # pondasi
    for c, t in ((0, EXT), (5, INT), (12, EXT)):
        foundation(v, c, t)
    cut_rect(v, 14.15, -0.70, 0.5, 0.25, "conc", 0.4)               # footplat F1 tepi
    cut_rect(v, 14.3, -0.45, 0.2, 0.0, "conc", 0.0)
    # dinding N: utuh
    wall_cut(v, 0, EXT, 0, 3.40)
    ring(v, 0)
    # dinding B (y=5): terbuka di JL2 (z .9-2.2)
    wall_cut(v, 5, INT, 0, 0.9)
    wall_cut(v, 5, INT, 2.2, 3.40)
    cut_rect(v, 5 - INT / 2, 2.2, INT, 0.0, "conc", 0.0)
    ring(v, 5, INT)
    v.rect(4.95, 0.9, 0.1, 1.3, "none", INK, 0.15, dash="1 1")
    # dinding S: jendela J1 (4.4-6.8) z .6-2.4
    wall_cut(v, 12, EXT, 0, 0.6)
    wall_cut(v, 12, EXT, 2.4, 3.40)
    ring(v, 12)
    cut_poly(v, [(12 - EXT / 2, ZRB), (12 + EXT / 2, ZRB), (12 + EXT / 2, zu(12.075)), (12 - EXT / 2, zu(12.075))], "brick", 0.45)
    v.rect(11.93, 0.6, 0.14, 1.8, GLASS, INK, 0.25)
    v.line(12.0, 0.6, 12.0, 2.4, 0.5)
    # kolom depan teras (di belakang bidang, x=8)
    column_thin(v, 14.4, ZT, 3.6)
    cut_rect(v, 14.3, 3.40, 0.2, 0.20, "conc", 0.45)
    # atap
    roof_assembly_y(v)
    truss_y(v)
    # plafon
    v.line(0.075, ZC, 11.925, ZC, 0.7)
    v.line(0.075, ZC + 0.05, 11.925, ZC + 0.05, 0.2)
    v.line(12.075, ZC, 15.2, ZC, 0.7)
    v.line(12.075, ZC + 0.05, 15.2, ZC + 0.05, 0.2)
    for y in [i * 1.0 + 0.5 for i in range(15)]:
        v.line(y, ZC + 0.05, y, ZRB - 0.02, 0.1, c="#777")
    # ---- perabot
    # dapur: kompor+hood (x=5.0 memotong), meja persiapan, meja saji
    v.rect(0.075, 0, 0.8, 0.85, "#555", INK, 0.3)
    v.rect(0.075, 1.9, 1.0, 0.5, "#fff", INK, 0.35)                # hood
    v.line(0.2, 2.4, 0.5, 2.9, 0.2, c="#555")
    v.rect(2.1, 0, 0.8, 0.85, "#555", INK, 0.3)                        # meja persiapan
    v.rect(4.15, 0, 0.75, 0.85, "#555", INK, 0.3)                      # meja saji
    v.rect(5.075, 0, 0.8, 0.9, "#555", INK, 0.3)                       # etalase
    v.rect(5.075, 0.9, 0.8, 0.5, GLASS, INK, 0.25)                  # vitrin kaca
    # dilihat: rak bumbu, kasir, meja
    v.rect(0.075, 0, 2.7, 1.8, "none", INK, 0.15, dash="1 1")
    table_thin(v, 7.6)
    table_thin(v, 13.25)
    v.rect(11.0, 0, 0.9, 1.0, "#fff", INK, 0.2)
    v.text(11.45, 0.5, "KASIR", 1.1)
    # manusia
    person(v, 8.8, 0, 1.7)
    person(v, 3.4, 0, 1.7)
    # label ruang
    v.text(2.9, 2.78, "R03  DAPUR", 2.1, bold=True)
    v.text(8.5, 2.78, "R01  RUANG MAKAN", 2.1, bold=True)
    v.text(13.25, 2.78, "R02 TERAS", 1.5, bold=True)
