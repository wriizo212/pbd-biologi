/* Cache app untuk guna luar talian — HANYA fail daripada asalan yang sama.
   Panggilan Supabase (asalan luar) dan apa-apa bukan-GET dibiarkan terus
   ke rangkaian supaya data awan tidak pernah basi. */
const VERSI = "pbd-biologi-v4";
const ASET = ["./", "./index.html", "./manifest.webmanifest", "./icon-192.png", "./icon-512.png", "./icon-180.png", "./splash-828x1792.png", "./splash-1170x2532.png", "./splash-1290x2796.png", "./splash-2048x2732.png"];

self.addEventListener("install", function(e){
  e.waitUntil(caches.open(VERSI).then(function(c){ return c.addAll(ASET); }).then(function(){ return self.skipWaiting(); }));
});
self.addEventListener("activate", function(e){
  e.waitUntil(caches.keys().then(function(ks){
    return Promise.all(ks.filter(function(k){ return k !== VERSI; }).map(function(k){ return caches.delete(k); }));
  }).then(function(){ return self.clients.claim(); }));
});
self.addEventListener("fetch", function(e){
  const req = e.request;
  /* Share Target: terima fail .json yang dikongsi dari telefon */
  if(req.method === "POST"){
    let u0 = null;
    try{ u0 = new URL(req.url); }catch(_){ u0 = null; }
    if(u0 && u0.origin === location.origin){
      e.respondWith((async function(){
        try{
          const fd = await req.formData();
          const f = fd.get("sandaran");
          if(f && f.text){
            const txt = await f.text();
            const c = await caches.open("pbd-kongsi");
            await c.put("./kongsi.json", new Response(txt, {headers:{"Content-Type":"application/json"}}));
          }
        }catch(err){}
        return Response.redirect("./?kongsi=1", 303);
      })());
      return;
    }
  }
  if(req.method !== "GET") return;
  let url;
  try{ url = new URL(req.url); }catch(_){ return; }
  if(url.origin !== location.origin) return;
  if(req.mode === "navigate"){
    e.respondWith(
      fetch(req).then(function(res){
        const cp = res.clone();
        caches.open(VERSI).then(function(c){ return c.put("./index.html", cp); }).catch(function(){});
        return res;
      }).catch(function(){ return caches.match("./index.html"); })
    );
    return;
  }
  e.respondWith(
    caches.match(req, {ignoreSearch: true}).then(function(hit){
      return hit || fetch(req).then(function(res){
        if(res.ok){
          const cp = res.clone();
          caches.open(VERSI).then(function(c){ return c.put(req, cp); }).catch(function(){});
        }
        return res;
      });
    })
  );
});
