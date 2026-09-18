# PBD Biologi — kit hosting (PWA)

Fail dalam folder ini menjadikan **sistem-pbd-biologi.html** boleh dipasang
sebagai aplikasi (ikon sendiri, berfungsi luar talian selepas lawatan pertama).

> Fail induk masih di luar folder ini (`..\sistem-pbd-biologi.html`).
> **Jangan** sunting index.html secara terus — selepas menyunting fail induk,
> jalankan:  `python build_kit.py`

## Uji di komputer sendiri

```
python -m http.server 8080
```
kemudian buka http://localhost:8080

## Pilihan A — GitHub Pages (percuma, kekal)

1. Cipta akaun/daftar masuk di https://github.com
2. Cipta repositori **public** baharu, contoh nama: `pbd-biologi`
3. Muat naik SEMUA fail dalam folder ini ke repositori itu
   (drag-and-drop melalui halaman repositori — "uploading an existing file")
4. Settings → Pages → Source: **Deploy from a branch** → Branch: `main`, folder `/ (root)` → Save
5. Tunggu 1–2 minit; URL anda: `https://<nama-anda>.github.io/pbd-biologi/`
6. Buka URL itu pada telefon → menu pelayar → **Add to Home screen / Install app**

## Pilihan B — Netlify Drop

1. Pergi ke https://app.netlify.com/drop
2. Seret folder ini ke halaman itu → dapat URL serta-merta
3. Daftar masuk (percuma) untuk mengekalkan URL tersebut

## Pilihan C — baris arahan (gh CLI)

```
cd pbd-mrsm-web
git init -b main
git add -A
git commit -m "PBD Biologi — PWA"
gh repo create pbd-biologi --public --source . --push
gh api -X POST repos/{owner}/pbd-biologi/pages -f "source[branch]=main" -f "source[path]=/"
```

## Nota penting

- **Data pelajar TIDAK masuk ke dalam repositori ini.** Data disimpan dalam
  pelayar setiap peranti (localStorage). Untuk pindah data antara peranti:
  Tetapan → Data → "Muat turun sandaran (JSON)" → muat naik pada peranti baharu,
  atau sambungkan Supabase (Tetapan → Awan).
- Versi hos ialah asalan (origin) BERLAINAN daripada fail tempatan — data lama
  pada fail `file://` tidak muncul secara automatik; gunakan sandaran JSON.
- Service worker hanya menyimpan cache fail daripada asalan yang sama;
  panggilan ke Supabase sentiasa melalui rangkaian (data tidak basi).
