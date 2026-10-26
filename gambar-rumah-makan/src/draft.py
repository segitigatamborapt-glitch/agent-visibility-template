"""Primitif gambar teknik: View (model->kertas), dimensi, simbol, kop gambar. Satuan kertas = mm."""
import math
from xml.sax.saxutils import escape

W, H = 420.0, 297.0
FONT = "'Liberation Sans','DejaVu Sans',Arial,Helvetica,sans-serif"
INK = "#15191d"
GRAY = "#8a9096"
WALLFILL = "#c9cdd1"


def n(v):
    s = f"{v:.3f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


DEFS = """<defs>
<marker id="arr" markerWidth="4" markerHeight="4" refX="3.6" refY="2" orient="auto"><path d="M0 0 L4 2 L0 4 Z" fill="#15191d"/></marker>
</defs>"""


# ---------------- arsir vektor (menggantikan <pattern>, agar PDF ringan) ----------------
_CLIP = [0]


def _hatch_elems(kind, x0, y0, x1, y1):
    """Elemen SVG arsir untuk bounding box (mm)."""
    o = []
    w, h = x1 - x0, y1 - y0
    if kind == "brick":
        step = 2.0 * math.sqrt(2)
        c = x0 + y0
        d = ""
        while c <= x1 + y1:
            d += f"M{n(c - y1)},{n(y1)}L{n(c - y0)},{n(y0)}"
            c += step
        o.append(f'<path d="{d}" stroke="#222" stroke-width="0.14" fill="none"/>')
    elif kind == "earth":
        step = 3.0 * math.sqrt(2)
        c = x0 - y1
        d = ""
        d2 = ""
        while c <= x1 - y0:
            d += f"M{n(c + y0)},{n(y0)}L{n(c + y1)},{n(y1)}"
            c += step
        c = x0 - y1 + step / 2
        while c <= x1 - y0:
            d2 += f"M{n(c + y0)},{n(y0)}L{n(c + y1)},{n(y1)}"
            c += step
        o.append(f'<path d="{d}" stroke="#555" stroke-width="0.12" fill="none"/>')
        o.append(f'<path d="{d2}" stroke="#555" stroke-width="0.12" fill="none" stroke-dasharray="1.2 3.2"/>')
    elif kind == "conc":
        d = ""
        ty = y0 - (y0 % 3.2)
        while ty < y1:
            tx = x0 - (x0 % 3.2)
            while tx < x1:
                for (dx, dy, r) in ((0.6, 0.8, 0.17), (2.2, 0.4, 0.13), (1.4, 2.2, 0.19), (2.9, 2.7, 0.12)):
                    d += f"M{n(tx + dx - r)},{n(ty + dy)}a{n(r)},{n(r)} 0 1,0 {n(2 * r)},0a{n(r)},{n(r)} 0 1,0 {n(-2 * r)},0Z"
                tx += 3.2
            ty += 3.2
        o.append(f'<path d="{d}" fill="#222"/>')
        d = ""
        ty = y0 - (y0 % 3.2)
        while ty < y1:
            tx = x0 - (x0 % 3.2)
            while tx < x1:
                d += f"M{n(tx + 0.3)},{n(ty + 2.8)}L{n(tx + 0.9)},{n(ty + 2.5)}L{n(tx + 0.6)},{n(ty + 3.1)}Z"
                tx += 3.2
            ty += 3.2
        o.append(f'<path d="{d}" fill="none" stroke="#222" stroke-width="0.1"/>')
    elif kind == "sand":
        d = ""
        ty = y0 - (y0 % 2.2)
        while ty < y1:
            tx = x0 - (x0 % 2.2)
            while tx < x1:
                for (dx, dy, r) in ((0.5, 0.6, 0.09), (1.6, 1.5, 0.09), (0.9, 1.9, 0.07)):
                    d += f"M{n(tx + dx - r)},{n(ty + dy)}a{n(r)},{n(r)} 0 1,0 {n(2 * r)},0a{n(r)},{n(r)} 0 1,0 {n(-2 * r)},0Z"
                tx += 2.2
            ty += 2.2
        o.append(f'<path d="{d}" fill="#333"/>')
    elif kind == "stone":
        d = ""
        ty = y0 - (y0 % 4.0)
        while ty < y1:
            tx = x0 - (x0 % 5.0)
            while tx < x1:
                for (cx, cy, rx, ry) in ((1.3, 1.1, 1.1, 0.8), (3.6, 1.4, 1.0, 0.9), (2.4, 3.2, 1.2, 0.7)):
                    d += (f"M{n(tx + cx - rx)},{n(ty + cy)}a{n(rx)},{n(ry)} 0 1,0 {n(2 * rx)},0a{n(rx)},{n(ry)} 0 1,0 {n(-2 * rx)},0Z")
                tx += 5.0
            ty += 4.0
        o.append(f'<path d="{d}" fill="none" stroke="#222" stroke-width="0.13"/>')
    elif kind == "grass":
        d = ""
        ty = y0 - (y0 % 3.0)
        while ty < y1:
            tx = x0 - (x0 % 3.0)
            while tx < x1:
                d += f"M{n(tx + 0.6)},{n(ty + 2.4)}L{n(tx + 1)},{n(ty + 1.2)}L{n(tx + 1.4)},{n(ty + 2.4)}M{n(tx + 1.9)},{n(ty + 1.8)}L{n(tx + 2.3)},{n(ty + 0.8)}L{n(tx + 2.7)},{n(ty + 1.8)}"
                tx += 3.0
            ty += 3.0
        o.append(f'<path d="{d}" fill="none" stroke="#6a8f5a" stroke-width="0.14"/>')
    elif kind == "tilef":
        d = ""
        tx = x0 - (x0 % 4.0)
        while tx < x1:
            d += f"M{n(tx)},{n(y0)}V{n(y1)}"
            tx += 4.0
        ty = y0 - (y0 % 4.0)
        while ty < y1:
            d += f"M{n(x0)},{n(ty)}H{n(x1)}"
            ty += 4.0
        o.append(f'<path d="{d}" fill="none" stroke="#b9c0c6" stroke-width="0.08"/>')
    elif kind == "stonec":
        d = ""
        ty = y0 - (y0 % 2.4)
        while ty < y1:
            tx = x0 - (x0 % 2.4)
            d += f"M{n(x0)},{n(ty + 0.6)}H{n(x1)}M{n(x0)},{n(ty + 1.8)}H{n(x1)}"
            while tx < x1:
                d += f"M{n(tx + 0.6)},{n(ty + 0.6)}V{n(ty + 1.8)}M{n(tx + 1.8)},{n(ty + 1.8)}V{n(ty + 2.4)}M{n(tx + 1.8)},{n(ty)}V{n(ty + 0.6)}"
                tx += 2.4
            ty += 2.4
        o.append(f'<path d="{d}" fill="none" stroke="#555" stroke-width="0.09"/>')
    return o


def pat_fill(sh, pts, kind):
    """Isi poligon (titik kertas) dengan arsir vektor, dipotong clipPath."""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    _CLIP[0] += 1
    cid = f"cp{_CLIP[0]}"
    pp = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
    sh.add(f'<clipPath id="{cid}"><polygon points="{pp}"/></clipPath><g clip-path="url(#{cid})">'
           + "".join(_hatch_elems(kind, min(xs), min(ys), max(xs), max(ys))) + "</g>")


class Sheet:
    def __init__(self):
        self.o = []

    def add(self, s):
        self.o.append(s)

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n(W)} {n(H)}" width="{n(W)}mm" height="{n(H)}mm" '
                f'font-family="{FONT}">' + DEFS + f'<rect width="{n(W)}" height="{n(H)}" fill="#fff"/>' + "".join(self.o) + "</svg>")


class View:
    """Pemetaan koordinat model (meter) -> kertas (mm)."""

    def __init__(self, sh, ox, oy, s, up=False, flipx=False):
        self.sh, self.ox, self.oy, self.s, self.up, self.flipx = sh, ox, oy, s, up, flipx

    def X(self, x):
        return self.ox + (-x if self.flipx else x) * self.s

    def Y(self, y):
        return self.oy + (-y if self.up else y) * self.s

    def P(self, x, y):
        return self.X(x), self.Y(y)

    # ---- primitif (koordinat model) ----
    def line(self, x1, y1, x2, y2, w=0.25, c=INK, dash=None, cap="butt", op=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' stroke-opacity="{op}"' if op else ""
        self.sh.add(f'<line x1="{n(self.X(x1))}" y1="{n(self.Y(y1))}" x2="{n(self.X(x2))}" y2="{n(self.Y(y2))}" '
                    f'stroke="{c}" stroke-width="{n(w)}" stroke-linecap="{cap}"{d}{o}/>')

    def poly(self, pts, fill="none", stroke=INK, w=0.25, dash=None, close=True, join="miter"):
        if fill.startswith("url(#"):
            pat_fill(self.sh, [(self.X(x), self.Y(y)) for x, y in pts], fill[5:-1])
            fill = "none"
        p = " ".join(f"{n(self.X(x))},{n(self.Y(y))}" for x, y in pts)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        tag = "polygon" if close else "polyline"
        st = f'stroke="{stroke}" stroke-width="{n(w)}"' if stroke else 'stroke="none"'
        self.sh.add(f'<{tag} points="{p}" fill="{fill}" {st} stroke-linejoin="{join}"{d}/>')

    def rect(self, x, y, w, h, fill="none", stroke=INK, sw=0.25, dash=None, rx=0):
        x1, y1 = self.P(x, y)
        x2, y2 = self.P(x + w, y + h)
        if fill.startswith("url(#"):
            pat_fill(self.sh, [(x1, y1), (x2, y1), (x2, y2), (x1, y2)], fill[5:-1])
            fill = "none"
        d = f' stroke-dasharray="{dash}"' if dash else ""
        st = f'stroke="{stroke}" stroke-width="{n(sw)}"' if stroke else 'stroke="none"'
        r = f' rx="{n(rx)}"' if rx else ""
        self.sh.add(f'<rect x="{n(min(x1, x2))}" y="{n(min(y1, y2))}" width="{n(abs(x2 - x1))}" height="{n(abs(y2 - y1))}" '
                    f'fill="{fill}" {st}{d}{r}/>')

    def circ(self, x, y, r, fill="none", stroke=INK, sw=0.25, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        st = f'stroke="{stroke}" stroke-width="{n(sw)}"' if stroke else 'stroke="none"'
        self.sh.add(f'<circle cx="{n(self.X(x))}" cy="{n(self.Y(y))}" r="{n(r * self.s)}" fill="{fill}" {st}{d}/>')

    def ell(self, x, y, rx, ry, fill="none", stroke=INK, sw=0.2):
        self.sh.add(f'<ellipse cx="{n(self.X(x))}" cy="{n(self.Y(y))}" rx="{n(rx * self.s)}" ry="{n(ry * self.s)}" '
                    f'fill="{fill}" stroke="{stroke}" stroke-width="{n(sw)}"/>')

    def arc(self, hx, hy, cx, cy, ox, oy, w=0.13, dash=None):
        """Busur pintu: engsel H, ujung tertutup C, ujung terbuka O (model)."""
        hxs, hys = self.P(hx, hy)
        cxs, cys = self.P(cx, cy)
        oxs, oys = self.P(ox, oy)
        r = math.hypot(cxs - hxs, cys - hys)
        cross = (cxs - hxs) * (oys - hys) - (cys - hys) * (oxs - hxs)
        sweep = 1 if cross > 0 else 0
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.sh.add(f'<path d="M{n(cxs)},{n(cys)} A{n(r)},{n(r)} 0 0 {sweep} {n(oxs)},{n(oys)}" fill="none" stroke="{INK}" '
                    f'stroke-width="{n(w)}"{d}/>')

    def text(self, x, y, s, size=2.5, anchor="middle", rot=0, bold=False, c=INK, italic=False, dx=0, dy=0, ls=1.2, base="mid", sp=None):
        T(self.sh, self.X(x) + dx, self.Y(y) + dy, s, size, anchor, rot, bold, c, italic, ls, base, sp)

    def hatch(self, pts, pat, stroke=INK, w=0.35):
        self.poly(pts, fill=f"url(#{pat})", stroke=stroke, w=w)


def T(sh, x, y, s, size=2.5, anchor="middle", rot=0, bold=False, c=INK, italic=False, ls=1.2, base="mid", sp=None):
    """Teks (koordinat kertas). base: 'mid' pusat vertikal, 'bot' garis dasar."""
    lines = str(s).split("\n")
    k = len(lines)
    if base == "mid":
        y0 = y - (k - 1) * size * ls / 2 + size * 0.35
    else:
        y0 = y
    fw = ' font-weight="bold"' if bold else ""
    fs = ' font-style="italic"' if italic else ""
    sps = f' letter-spacing="{sp}"' if sp else ""
    tr = f' transform="rotate({n(rot)} {n(x)} {n(y)})"' if rot else ""
    out = f'<text x="{n(x)}" y="{n(y0)}" font-size="{n(size)}" text-anchor="{anchor}" fill="{c}"{fw}{fs}{sps}{tr}>'
    for i, ln in enumerate(lines):
        if i == 0:
            out += f'<tspan x="{n(x)}">{escape(ln)}</tspan>'
        else:
            out += f'<tspan x="{n(x)}" dy="{n(size * ls)}">{escape(ln)}</tspan>'
    out += "</text>"
    sh.add(out)


def L(sh, x1, y1, x2, y2, w=0.25, c=INK, dash=None, cap="butt"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    sh.add(f'<line x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" y2="{n(y2)}" stroke="{c}" stroke-width="{n(w)}" stroke-linecap="{cap}"{d}/>')


def R(sh, x, y, w, h, fill="none", stroke=INK, sw=0.25, dash=None):
    if fill.startswith("url(#"):
        pat_fill(sh, [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], fill[5:-1])
        fill = "none"
    d = f' stroke-dasharray="{dash}"' if dash else ""
    st = f'stroke="{stroke}" stroke-width="{n(sw)}"' if stroke else 'stroke="none"'
    sh.add(f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" fill="{fill}" {st}{d}/>')


def C(sh, x, y, r, fill="none", stroke=INK, sw=0.25):
    sh.add(f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{n(sw)}"/>')


# ---------------- dimensi ----------------
def cm(m):
    return str(int(round(m * 100)))


def _tick(sh, x, y, size=1.5):
    L(sh, x - size * 0.7, y + size * 0.7, x + size * 0.7, y - size * 0.7, 0.3)


def chain_h(v, xs, y_obj, y_sheet, fs=2.0, gap=1.0, over=1.2, fmt=cm, label_up=True):
    """Rantai dimensi horizontal. xs: koordinat model. y_obj: y model objek (garis ekstensi mulai). y_sheet: posisi garis dimensi (kertas)."""
    sh = v.sh
    yo = v.Y(y_obj)
    d = 1 if y_sheet > yo else -1
    pts = [v.X(x) for x in xs]
    for xp in pts:
        L(sh, xp, yo + d * gap, xp, y_sheet + d * over, 0.13)
    L(sh, min(pts) - over, y_sheet, max(pts) + over, y_sheet, 0.25)
    for xp in pts:
        _tick(sh, xp, y_sheet)
    for i in range(len(xs) - 1):
        seg = abs(xs[i + 1] - xs[i])
        mid = (pts[i] + pts[i + 1]) / 2
        wpx = abs(pts[i + 1] - pts[i])
        txt = fmt(seg)
        if wpx < len(txt) * fs * 0.62 + 0.6:
            T(sh, mid, y_sheet - 1.0 * (1 if label_up else -1) - (fs * 0.9 if (i % 2) else 0) * (1 if label_up else -1), txt, fs * 0.9, base="bot")
        else:
            T(sh, mid, y_sheet - 0.7 if label_up else y_sheet + fs + 0.4, txt, fs, base="bot")


def chain_v(v, ys, x_obj, x_sheet, fs=2.0, gap=1.0, over=1.2, fmt=cm):
    sh = v.sh
    xo = v.X(x_obj)
    d = 1 if x_sheet > xo else -1
    pts = [v.Y(y) for y in ys]
    for yp in pts:
        L(sh, xo + d * gap, yp, x_sheet + d * over, yp, 0.13)
    L(sh, x_sheet, min(pts) - over, x_sheet, max(pts) + over, 0.25)
    for yp in pts:
        _tick(sh, x_sheet, yp)
    for i in range(len(ys) - 1):
        seg = abs(ys[i + 1] - ys[i])
        mid = (pts[i] + pts[i + 1]) / 2
        txt = fmt(seg)
        T(sh, x_sheet - 0.7, mid, txt, fs, rot=-90, base="bot")


def bubble(sh, x, y, label, r=3.0, fs=2.6):
    C(sh, x, y, r, "#fff", INK, 0.3)
    T(sh, x, y, label, fs, bold=True)


def axis_line(sh, x1, y1, x2, y2):
    L(sh, x1, y1, x2, y2, 0.15, INK, "6 1.2 0.8 1.2")


def leader(sh, x1, y1, x2, y2, txt, fs=2.0, anchor="start", dot=True, tdx=1.0):
    L(sh, x1, y1, x2, y2, 0.15)
    if dot:
        C(sh, x1, y1, 0.45, INK, INK, 0.1)
    T(sh, x2 + (tdx if anchor == "start" else -tdx), y2, txt, fs, anchor)


def level_mark(sh, x, y, label, side=1, fs=2.0, ln=14):
    """Tanda elevasi (segitiga terbalik) di titik kertas (x,y). side=1 teks ke kanan, -1 ke kiri."""
    L(sh, x, y, x + side * ln, y, 0.2)
    sh.add(f'<polygon points="{n(x)},{n(y)} {n(x - 1.5)},{n(y - 2.6)} {n(x + 1.5)},{n(y - 2.6)}" fill="#fff" stroke="{INK}" stroke-width="0.2"/>')
    sh.add(f'<polygon points="{n(x)},{n(y)} {n(x - 0.75)},{n(y - 1.3)} {n(x + 0.75)},{n(y - 1.3)}" fill="{INK}"/>')
    T(sh, x + side * 2.2, y - 1.0, label, fs, "start" if side == 1 else "end", base="bot")


def north_arrow(sh, x, y, r=9):
    C(sh, x, y, r, "#fff", INK, 0.3)
    sh.add(f'<polygon points="{n(x)},{n(y - r + 1)} {n(x - 3)},{n(y + r - 2)} {n(x)},{n(y + 2)}" fill="{INK}"/>')
    sh.add(f'<polygon points="{n(x)},{n(y - r + 1)} {n(x + 3)},{n(y + r - 2)} {n(x)},{n(y + 2)}" fill="#fff" stroke="{INK}" stroke-width="0.25"/>')
    T(sh, x, y - r - 2.5, "U", 3.2, bold=True)


def scale_bar(sh, x, y, s, meters=(0, 2, 4, 6, 8, 10), fs=1.8):
    """s = mm per meter."""
    for i in range(len(meters) - 1):
        a, b = meters[i], meters[i + 1]
        R(sh, x + a * s, y, (b - a) * s, 1.4, INK if i % 2 == 0 else "#fff", INK, 0.2)
    for m in meters:
        T(sh, x + m * s, y + 4, str(m), fs)
    T(sh, x + meters[-1] * s + 3, y + 4, "m", fs, "start")


def section_marker(sh, v, x1, y1, x2, y2, label, dirx, diry):
    """Garis potongan pada denah: dua ujung dengan bubble + panah arah pandang (dirx,diry satuan kertas)."""
    P1, P2 = v.P(x1, y1), v.P(x2, y2)
    L(sh, P1[0], P1[1], P2[0], P2[1], 0.3, INK, "9 1.5 1 1.5")
    for (px, py) in (P1, P2):
        L(sh, px, py, px + dirx * 5, py + diry * 5, 0.7)
        sh.add(f'<polygon points="{n(px + dirx * 7.5)},{n(py + diry * 7.5)} {n(px + dirx * 4.5 - diry * 1.6)},{n(py + diry * 4.5 + dirx * 1.6)} '
               f'{n(px + dirx * 4.5 + diry * 1.6)},{n(py + diry * 4.5 - dirx * 1.6)}" fill="{INK}"/>')
        bx, by = px + dirx * 11, py + diry * 11
        bubble(sh, bx, by, label, 2.6, 2.4)


def table(sh, x, y, colw, rowh, header, rows, fs=2.0, hfs=2.1, aligns=None, hfill="#e4e7ea", wrap=None):
    """Tabel sederhana; kembalikan y bawah."""
    tw = sum(colw)
    R(sh, x, y, tw, rowh, hfill, INK, 0.3)
    cx = x
    for i, hd in enumerate(header):
        T(sh, cx + colw[i] / 2, y + rowh / 2, hd, hfs, bold=True)
        if i:
            L(sh, cx, y, cx, y + rowh, 0.2)
        cx += colw[i]
    cy = y + rowh
    for r in rows:
        rh = rowh
        if isinstance(r, tuple) and len(r) == 2 and isinstance(r[1], (int, float)):
            r, rh = r[0], r[1]
        R(sh, x, cy, tw, rh, "none", INK, 0.2)
        cx = x
        for i, cell in enumerate(r):
            al = (aligns[i] if aligns else "middle")
            if al == "start":
                T(sh, cx + 1.2, cy + rh / 2, cell, fs, "start")
            else:
                T(sh, cx + colw[i] / 2, cy + rh / 2, cell, fs)
            if i:
                L(sh, cx, cy, cx, cy + rh, 0.15)
            cx += colw[i]
        cy += rh
    R(sh, x, y, tw, cy - y, "none", INK, 0.45)
    return cy


# ---------------- kop gambar ----------------
PROJECT = "RUMAH MAKAN \"SELERA NUSANTARA\""
SUB = "Perencanaan Bangunan Rumah Makan 1 Lantai\nKapasitas ± 66 Kursi"
TB_X = 340.0


def frame(sh, no, title, scale, idx, total, notes=None, rev=None):
    # bingkai
    R(sh, 5, 5, 410, 287, "none", INK, 0.25)
    R(sh, 10, 10, 400, 277, "none", INK, 0.7)
    x0, w = TB_X, 70.0
    L(sh, x0, 10, x0, 287, 0.7)
    y = 10
    # Proyek
    R(sh, x0, y, w, 36, "#f1f3f5", INK, 0.3)
    T(sh, x0 + w / 2, y + 7, "PROYEK", 1.8, c="#555")
    T(sh, x0 + w / 2, y + 15, PROJECT.replace(" \"", "\n\"", 1), 3.6, bold=True, ls=1.25)
    T(sh, x0 + w / 2, y + 28.5, SUB, 2.0, c="#333", ls=1.35)
    y += 36
    R(sh, x0, y, w, 21, "none", INK, 0.3)
    T(sh, x0 + 2, y + 4, "LOKASI", 1.6, "start", c="#555")
    T(sh, x0 + 2, y + 9, "(diisi sesuai lahan terpilih)", 2.0, "start")
    T(sh, x0 + 2, y + 14.5, "PEMILIK", 1.6, "start", c="#555")
    T(sh, x0 + 2, y + 19, "(diisi nama pemilik)", 2.0, "start")
    y += 21
    # Catatan
    ny = 150.0
    R(sh, x0, y, w, ny - y, "none", INK, 0.3)
    T(sh, x0 + 2, y + 4, "KETERANGAN / CATATAN", 2.0, "start", bold=True)
    if notes:
        cy = y + 9.5
        for t in notes:
            lines = t.split("\n")
            for j, ln in enumerate(lines):
                T(sh, x0 + 2 + (0 if j == 0 else 3.5), cy, ln, 1.85, "start")
                cy += 3.6
            cy += 0.8
    y = ny
    # Revisi
    R(sh, x0, y, w, 24, "none", INK, 0.3)
    T(sh, x0 + 2, y + 3.5, "REVISI", 1.8, "start", bold=True)
    for k, (a, b, c_) in enumerate([("No", "Tanggal", "Keterangan"), ("0", "26-10-2026", "Gambar rencana (usulan awal)"), ("", "", "")]):
        yy = y + 6 + k * 5.5
        L(sh, x0, yy, x0 + w, yy, 0.15)
        T(sh, x0 + 4, yy + 2.8, a, 1.8)
        T(sh, x0 + 17, yy + 2.8, b, 1.8)
        T(sh, x0 + 28, yy + 2.8, c_, 1.7, "start")
    L(sh, x0 + 8, y + 6, x0 + 8, y + 24, 0.15)
    L(sh, x0 + 26, y + 6, x0 + 26, y + 24, 0.15)
    y += 24
    # TTD
    R(sh, x0, y, w, 27, "none", INK, 0.3)
    rows = [("Digambar", "Drafter (Claude)"), ("Diperiksa", "______________"), ("Disetujui", "______________"), ("Tanggal", "26 Oktober 2026")]
    for k, (a, b) in enumerate(rows):
        yy = y + k * 6.75
        L(sh, x0, yy, x0 + w, yy, 0.15)
        T(sh, x0 + 2, yy + 3.5, a, 1.8, "start", c="#555")
        T(sh, x0 + 22, yy + 3.5, b, 2.0, "start")
    L(sh, x0 + 20, y, x0 + 20, y + 27, 0.15)
    y += 27
    # Judul
    R(sh, x0, y, w, 28, "#f1f3f5", INK, 0.3)
    T(sh, x0 + 2, y + 3.4, "JUDUL GAMBAR", 1.6, "start", c="#555")
    T(sh, x0 + w / 2, y + 14, title, 3.8, bold=True, ls=1.2)
    y += 28
    # No / Skala / Lembar
    R(sh, x0, y, w, 287 - y, "none", INK, 0.7)
    h = 287 - y
    for xx, lab, val in ((x0, "NO. GAMBAR", no), (x0 + 28, "SKALA", scale), (x0 + 52, "LEMBAR", f"{idx}/{total}")):
        T(sh, xx + 2, y + 3.2, lab, 1.5, "start", c="#555")
    T(sh, x0 + 14, y + h - 5, no, 4.6, bold=True)
    T(sh, x0 + 40, y + h - 5, scale, 3.2, bold=True)
    T(sh, x0 + 61, y + h - 5, f"{idx}/{total}", 3.0, bold=True)
    L(sh, x0 + 28, y, x0 + 28, 287, 0.2)
    L(sh, x0 + 52, y, x0 + 52, 287, 0.2)


def ptitle(sh, x, y, title, scale, fs=3.6, sub=None):
    """Judul di bawah gambar: lingkaran nomor + judul + garis + skala."""
    T(sh, x, y, title, fs, "start", bold=True)
    wlen = len(title) * fs * 0.62
    L(sh, x, y + 1.6, x + wlen + 22, y + 1.6, 0.6)
    L(sh, x, y + 2.5, x + wlen + 22, y + 2.5, 0.2)
    T(sh, x + wlen + 3, y, scale, fs * 0.72, "start")
    if sub:
        T(sh, x, y + 6, sub, 1.9, "start", c="#444")
