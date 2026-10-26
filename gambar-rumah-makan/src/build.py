import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import sheets, plans, detail

OUT = os.path.join(os.path.dirname(__file__), "..", "sheets")
os.makedirs(OUT, exist_ok=True)

LIST = [
    ("A-02", sheets.a02, 3), ("A-03", sheets.a03, 4), ("A-05", sheets.a05, 6), ("A-06", sheets.a06, 7), ("A-07", sheets.a07, 8), ("A-01", plans.a01, 2), ("A-04", plans.a04, 5), ("A-08", plans.a08, 9), ("A-09", detail.a09, 10), ("A-10", detail.a10, 11), ("A-00", detail.a00, 1),
]
for code, fn, idx in LIST:
    with open(os.path.join(OUT, code + ".svg"), "w") as f:
        f.write(fn(idx))
print("ok")
