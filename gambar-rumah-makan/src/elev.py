"""Tampak (elevasi)."""
import math
from draft import *
from bldg import *

GLASS = "#e8f1f6"
ROOF_T = 0.20  # tebal paket atap (penutup+reng+kasau) di bawah permukaan


def zu(y):
    """Muka bawah atap."""
    return zroof(y) - ROOF_T


def ground(v, x0, x1):
    v.line(x0, ZG, x1, ZG, 0.9)
    x = x0 + 0.1
    while x < x1:
        v.line(x, ZG, x - 0.28, ZG - 0.28, 0.1, c="#555")
        x += 0.45


def person(v, x, z0, h=1.7, c="#666"):
    """Figur skala manusia sederhana (tinggi h)."""
    r = 0.11 * h / 1.7
    v.circ(x, z0 + h - r, r, "#fff", c, 0.2)
    v.poly([(x - 0.17, z0 + h - 2.2 * r), (x + 0.17, z0 + h - 2.2 * r), (x + 0.14, z0 + 0.8), (x + 0.1, z0), (x - 0.1, z0), (x - 0.14, z0 + 0.8)], "#fff", c, 0.2)


def e_window(v, a, b, z1, z2, code=None, tag_z=None, trans=None):
    w = b - a
    v.rect(a, z1, w, z2 - z1, GLASS, INK, 0.4)
    v.rect(a + 0.05, z1 + 0.05, w - 0.1, z2 - z1 - 0.1, "none", INK, 0.2)
    h = z2 - z1
    if h > 1.2 and trans is None:
        trans = 0.4
    if trans:
        v.line(a, z2 - trans, b, z2 - trans, 0.25)
    if w >= 1.3:
        n_ = int(round(w / 1.2))
        for i in range(1, n_):
            v.line(a + w * i / n_, z1, a + w * i / n_, z2, 0.25)
    # pantulan kaca
    zz = z2 - (trans or 0) - 0.12
    if h > 0.5:
        v.line(a + 0.15 * w, z1 + 0.12, a + 0.15 * w + 0.35, zz, 0.07, c="#8aa")
    # kaca sill
    v.line(a - 0.04, z1, b + 0.04, z1, 0.5)
    if code:
        tz = tag_z if tag_z is not None else z2 + 0.28
        tagbox(v, (a + b) / 2, tz, code)


def tagbox(v, x, z, code, round_=False):
    sx, sy = v.P(x, z)
    if round_:
        C(v.sh, sx, sy, 1.9, "#fff", INK, 0.2)
    else:
        w = 1.45 * len(code) + 1.2
        R(v.sh, sx - w / 2, sy - 1.45, w, 2.9, "#fff", INK, 0.2)
    T(v.sh, sx, sy, code, 1.55, bold=True)


def e_door(v, o, tag_dx=0.0, tag_z=None):
    a, b = o["a"], o["b"]
    z2 = o["head"]
    v.rect(a, 0, b - a, z2, "#fff", INK, 0.4)
    if o.get("dbl"):
        mid = (a + b) / 2
        for (l, r_, hinge) in ((a, mid, a), (mid, b, b)):
            v.rect(l + 0.04, 0.04, r_ - l - 0.08, z2 - 0.08, GLASS, INK, 0.25)
            v.line(l + 0.04, 0.45, r_ - 0.04, 0.45, 0.2)
            far = r_ if hinge == l else l
            v.line(hinge, z2 / 2, far, 0.04, 0.12, dash="1 .8")
            v.line(hinge, z2 / 2, far, z2 - 0.04, 0.12, dash="1 .8")
            hx = (far - 0.12) if far > hinge else (far + 0.12)
            v.line(hx, 0.9, hx, 1.2, 0.5)
    else:
        v.rect(a + 0.04, 0.04, b - a - 0.08, z2 - 0.08, "#fff", INK, 0.25)
        v.line(a + 0.1, 0.9 * z2 - 0.2, b - 0.1, 0.9 * z2 - 0.2, 0.12, c=GRAY)
        hinge = a if o.get("hinge", "a") == "a" else b
        far = b if hinge == a else a
        v.line(hinge, z2 / 2, far, 0.04, 0.12, dash="1 .8")
        v.line(hinge, z2 / 2, far, z2 - 0.04, 0.12, dash="1 .8")
        hx = (far - 0.12) if far > hinge else (far + 0.12)
        v.line(hx, 0.95, hx, 1.15, 0.5)
    tz = tag_z if tag_z is not None else z2 + 0.28
    tagbox(v, (a + b) / 2 + tag_dx, tz, o["c"], True)


def wall_openings(v, wid, tags=True, overrides=None):
    for o in OPS:
        if o["w"] != wid:
            continue
        ov = (overrides or {}).get((o["c"], o["a"]), {})
        if o["k"] == "door":
            e_door(v, o, **ov)
        elif o["k"] in ("win", "pass"):
            e_window(v, o["a"], o["b"], o["sill"], o["head"], o["c"] if tags else None, **ov)


def roof_front(v, x0=-0.6, x1=20.6):
    """Atap dilihat dari depan/belakang (bidang miring)."""
    v.rect(x0, ZE, x1 - x0, ZRIDGE - ZE, "#fff", INK, 0.5)
    z = ZE + 0.25
    while z < ZRIDGE - 0.05:
        v.line(x0, z, x1, z, 0.08, c="#777")
        z += 0.25
    x = x0 + 0.5
    while x < x1:
        v.line(x, ZE, x, ZRIDGE, 0.05, c="#bbb")
        x += 0.8
    v.rect(x0 - 0.05, ZRIDGE, x1 - x0 + 0.1, 0.14, "#d6d9dc", INK, 0.4)       # bubungan
    v.rect(x0, ZE - 0.25, x1 - x0, 0.25, "#e2e5e8", INK, 0.45)                  # lisplang


def downspout(v, x, ztop=3.2, zbot=ZT):
    v.rect(x - 0.04, zbot, 0.08, ztop - zbot, "#fff", INK, 0.2)


def cerobong_front(v, x):
    v.rect(x - 0.2, zroof(0.5), 0.4, 7.0 - zroof(0.5), "#fff", INK, 0.4)
    v.rect(x - 0.3, 7.0, 0.6, 0.12, "#fff", INK, 0.35)
    v.rect(x - 0.27, 6.88, 0.54, 0.12, "#fff", INK, 0.2)


def elev_front(v):
    # tanah + dasar teras
    ground(v, -3.5, 24)
    v.rect(-0.075, ZG, 20.15, ZT - ZG, "url(#stonec)", INK, 0.4)
    # dinding
    v.rect(-0.075, ZT, 20.15, 3.75 - ZT, "#fff", INK, 0.45)
    v.rect(-0.075, ZT, 20.15, 0.6 - ZT, "url(#stonec)", INK, 0.3)
    v.line(-0.075, 0.6, 20.075, 0.6, 0.35)
    wall_openings(v, "S", overrides={("P1", 9.1): dict(tag_z=1.9, tag_dx=1.35)})
    # papan nama
    v.rect(8.12, 2.42, 3.76, 0.66, "#2b2f33", INK, 0.4)
    v.text(10.0, 2.75, "RUMAH MAKAN\nSELERA NUSANTARA", 2.3, bold=True, c="#fff", ls=1.1)
    # kolom teras
    for x in XS:
        v.rect(x - 0.1, ZT, 0.2, 3.7 - ZT, "#fff", INK, 0.4)
        v.rect(x - 0.1, ZT, 0.2, 1.0 - ZT, "url(#stonec)", INK, 0.25)
        v.line(x - 0.1, 1.0, x + 0.1, 1.0, 0.3)
    # tangga & ramp
    v.rect(8.5, ZG, 3.0, -0.19 - ZG, "#fff", INK, 0.35)
    v.line(8.5, -0.19, 11.5, -0.19, 0.5)
    v.poly([(14.0, ZT), (17.84, ZG), (14.0, ZG)], "url(#stonec)", INK, 0.4)
    for px, pz in ((14.0, ZT), (15.28, ZT - 0.107 * 3.84 / 3.84 * 0 + (ZG - ZT) * (1.28 / 3.84)), (16.56, ZT + (ZG - ZT) * (2.56 / 3.84)), (17.84, ZG)):
        v.line(px, pz, px, pz + 0.9, 0.25)
    v.line(14.0, ZT + 0.9, 17.84, ZG + 0.9, 0.35)
    v.line(14.0, ZT + 0.5, 17.84, ZG + 0.5, 0.15)
    # atap + talang
    roof_front(v)
    downspout(v, 0.35)
    downspout(v, 19.65)


def elev_rear(v):
    ground(v, -3.5, 24)
    v.rect(-0.075, ZG, 20.15, 3.8 - ZG, "#fff", INK, 0.45)
    v.rect(-0.075, ZG, 20.15, 0.6 - ZG, "url(#stonec)", INK, 0.3)
    v.line(-0.075, 0.6, 20.075, 0.6, 0.35)
    v.line(-0.075, 0, 20.075, 0, 0.2, c=GRAY, dash="2 1")
    wall_openings(v, "N", overrides={("P2", 5.5): dict(tag_z=2.4)})
    # bordes + anak tangga pintu servis
    v.rect(5.0, ZG, 2.0, -0.05 - ZG, "#fff", INK, 0.35)
    v.line(5.0, -0.2, 7.0, -0.2, 0.2, c=GRAY)
    # bak lemak, tabung gas (siluet)
    roof_front(v)
    downspout(v, 0.35, 3.2, ZG)
    downspout(v, 19.65, 3.2, ZG)
    cerobong_front(v, 2.5)


def roof_side(v):
    """Profil atap dilihat dari samping (horizontal = y)."""
    pts = [(YEB, ZE), (YR, ZRIDGE), (YEF, ZE), (YEF, ZE - 0.25), (YR, ZRIDGE - 0.25), (YEB, ZE - 0.25)]
    v.poly(pts, "#fff", INK, 0.5)
    # papan angin (tebal 0.20 sejajar kemiringan)
    off = 0.22
    v.line(YEB, ZE - off, YR, ZRIDGE - off, 0.15, c="#777")
    v.line(YR, ZRIDGE - off, YEF, ZE - off, 0.15, c="#777")
    # penutup
    for t in range(1, 9):
        y = YEB + t * (YR - YEB) / 9
        v.line(y, zroof(y), y, zroof(y) - 0.25, 0.06, c="#999")
    for t in range(1, 9):
        y = YR + t * (YEF - YR) / 9
        v.line(y, zroof(y), y, zroof(y) - 0.25, 0.06, c="#999")
    v.rect(YR - 0.1, ZRIDGE - 0.02, 0.2, 0.14, "#d6d9dc", INK, 0.3)


def elev_side(v, side):
    """side: 'W' (tampak kiri, horizontal=y) atau 'E' (tampak kanan, flipx)."""
    ground(v, -3.5, 19.2)
    # tanah/teras
    v.rect(12.075, ZG, TERR_Y - 12.075, ZT - ZG, "url(#stonec)", INK, 0.4)
    v.rect(TERR_Y, ZG, 0.45, -0.19 - ZG, "#fff", INK, 0.3)
    # dinding gable
    wall = [(-0.075, ZG), (12.075, ZG), (12.075, zu(12.075)), (YR, zu(YR)), (-0.075, zu(-0.075))]
    v.poly(wall, "#fff", INK, 0.45)
    v.rect(-0.075, ZG, 12.15, 0.6 - ZG, "url(#stonec)", INK, 0.3)
    v.line(-0.075, 0.6, 12.075, 0.6, 0.35)
    # kolom depan teras
    xcol = 14.4
    for yc in (xcol,):
        v.rect(yc - 0.1, ZT, 0.2, 3.55 - ZT, "#fff", INK, 0.4)
        v.rect(yc - 0.1, ZT, 0.2, 1.0 - ZT, "url(#stonec)", INK, 0.25)
    v.line(12.075, zu(12.075), YEF, ZE - 0.25, 0.2, c="#888")
    # plafon teras
    v.line(12.075, 3.2, 15.2, 3.2, 0.3, dash="2 1")
    # bukaan
    wid = "W" if side == "W" else "E"
    wall_openings(v, wid)
    # ramp / handrail
    if side == "W":
        v.rect(TERR_Y, ZG, 1.2, ZT - ZG, "url(#stonec)", INK, 0.3)
    else:
        v.line(15.65, ZG, 15.65, ZG + 0.9, 0.25)
        v.line(14.5, ZT + 0.9, 15.65, ZG + 0.9, 0.2, dash="1.5 1")
    roof_side(v)
    # cerobong
    v.rect(0.3, zroof(0.5), 0.4, 7.0 - zroof(0.5), "#fff", INK, 0.4)
    v.rect(0.2, 7.0, 0.6, 0.12, "#fff", INK, 0.35)
    # talang vertikal
    v.rect(-0.35, ZG, 0.08, 3.2 - ZG, "#fff", INK, 0.2)
    v.rect(15.0, ZG + 0.0, 0.08, 3.2 - ZG, "#fff", INK, 0.2)
    person(v, 13.5, ZT, 1.7)
