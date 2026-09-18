"""Bina semula index.html dalam kit ini daripada fail induk.
   Jalankan selepas sebarang suntingan sistem-pbd-biologi.html:  python build_kit.py
"""
import os

KIT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(KIT, "..", "sistem-pbd-biologi.html"))
DST = os.path.join(KIT, "index.html")

HEAD_TAGS = """<link rel="manifest" href="./manifest.webmanifest">
<link rel="icon" type="image/png" href="./icon-192.png">
<link rel="apple-touch-icon" href="./icon-180.png">
<meta name="theme-color" content="#143D6E">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="PBD Biologi">"""

SW_SNIP = """<script>
/* Daftar service worker bila dihoskan (http/https); diabaikan pada fail:// */
if ("serviceWorker" in navigator && /^https?:$/.test(location.protocol)) {
  window.addEventListener("load", function () {
    navigator.serviceWorker.register("./sw.js").catch(function () {});
  });
}
</script>"""

txt = open(SRC, encoding="utf-8").read()
assert txt.count("</head>") == 1, "penanda </head> tidak unik"
assert txt.count("</body>") == 1, "penanda </body> tidak unik"
txt = txt.replace("</head>", HEAD_TAGS + "\n</head>", 1)
txt = txt.replace("</body>", SW_SNIP + "\n</body>", 1)
open(DST, "w", encoding="utf-8").write(txt)
print("index.html dibina daripada:", SRC)
print("saiz:", os.path.getsize(DST), "bait")
