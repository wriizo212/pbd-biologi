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
<meta name="apple-mobile-web-app-title" content="PBD Biologi">
<link rel="apple-touch-startup-image" href="./splash-828x1792.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)">
<link rel="apple-touch-startup-image" href="./splash-1170x2532.png" media="(device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3)">
<link rel="apple-touch-startup-image" href="./splash-1290x2796.png" media="(device-width: 430px) and (device-height: 932px) and (-webkit-device-pixel-ratio: 3)">
<link rel="apple-touch-startup-image" href="./splash-2048x2732.png" media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)">"""

SW_SNIP = """<script>
/* Daftar service worker bila dihoskan (http/https); diabaikan pada fail:// */
if ("serviceWorker" in navigator && /^https?:$/.test(location.protocol)) {
  window.addEventListener("load", function () {
    navigator.serviceWorker.register("./sw.js").then(function (reg) {
      reg.addEventListener("updatefound", function () {
        var w = reg.installing;
        if (!w) return;
        w.addEventListener("statechange", function () {
          if (w.state === "installed" && navigator.serviceWorker.controller) {
            try { toast("Kemas kini app tersedia — tutup dan buka semula"); } catch (e) {}
          }
        });
      });
    }).catch(function () {});
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
