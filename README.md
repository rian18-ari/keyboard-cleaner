# 🧹 Keyboard Cleaner

Aplikasi desktop berbasis Python/Tkinter untuk membersihkan keyboard secara aman. Saat dijalankan, aplikasi ini masuk ke mode layar penuh dan memblokir semua input keyboard agar tidak terdeteksi oleh sistem — sehingga kamu bisa membersihkan keyboard tanpa khawatir memicu tombol secara tidak sengaja.

## Fitur

- **Layar penuh & always on top** — menutup seluruh layar agar tidak terganggu aplikasi lain
- **Pemblokiran keyboard** — setiap tombol yang ditekan dicegat dan tidak diteruskan ke OS
- **Penghitung real-time** — menampilkan jumlah tombol yang sudah dibersihkan
- **Indikator tombol langsung** — menampilkan tombol terakhir yang terdeteksi
- **Efek visual flash** — latar belakang berkedip tipis setiap kali tombol ditekan sebagai konfirmasi visual
- **Keluar cepat** — tekan `Ctrl + Shift + X` untuk keluar aplikasi

## Persyaratan

- **Python 3.6+**
- **Tkinter** (biasanya sudah termasuk bawaan Python; di Debian/Ubuntu bisa diinstal via `sudo apt install python3-tk`)

Tidak ada dependensi pihak ketiga — murni menggunakan pustaka standar Python.

## Cara Menjalankan

```bash
python3 app.py
```

Atau buat menjadi executable:

```bash
chmod +x app.py
./app.py
```

## Cara Pakai

1. Jalankan aplikasi
2. Layar akan berubah menjadi gelap dengan judul **Keyboard Cleaning Mode Active**
3. Lap/bersihkan keyboard kamu dengan aman
4. Setiap tombol yang tertekan akan:
   - Menambah angka pada penghitung
   - Menampilkan nama tombol yang terdeteksi
   - Memberi efek flash pada layar
5. Tekan **Ctrl + Shift + X** untuk keluar

## Kustomisasi

Warna dan font dapat diubah langsung di `app.py` pada bagian `__init__`:

| Variabel     | Default   | Keterangan           |
| ------------ | --------- | -------------------- |
| `bg_color`   | `#1e2030` | Latar belakang       |
| `text_color` | `#eed49f` | Warna teks counter   |
| `accent_color` | `#8bd5ca` | Warna judul        |
| `muted_color` | `#939ab7` | Warna deskripsi/footer |

Palet warna terinspirasi dari [Catppuccin Macchiato](https://github.com/catppuccin/catppuccin).

## Lisensi

MIT
