# 🧹 Keyboard Cleaner

Aplikasi desktop berbasis Python/pygame untuk membersihkan keyboard secara aman. Saat dijalankan, aplikasi ini masuk ke mode layar penuh dan memblokir semua input keyboard agar tidak terdeteksi oleh sistem — sehingga kamu bisa membersihkan keyboard tanpa khawatir memicu tombol secara tidak sengaja.

## bagaimana ini bekerja?

1. kamu menjalankan aplikasi nya
2. aplikasi akan membuat layar penuh dan memblokir semua input keyboard
3. kamu bisa membersihkan keyboard kamu dengan aman
4. aplikasi akan menampilkan jumlah tombol yang sudah dibersihkan
5. aplikasi akan menampilkan tombol terakhir yang terdeteksi
6. aplikasi akan menampilkan efek flash setiap kali tombol ditekan
7. kamu bisa keluar aplikasi dengan menekan Ctrl + Shift + X

## Apakah ini aman buat sistem di laptop ku?
- Ya, pasti aman banget! karna aplikasi ini tidak bekerja di level hardware, dan tidak mematikan sistem keyboard. aplikasi ini hanya memblokir input keyboard agar tidak terdeteksi oleh sistem 

## Sebelum menjalankan aplikasi nya, apa yang harus dilakukan/dipastikan?
- pastikan di laptop kamu ada library dari python, yaitu
  - python v.3.14++
  - pygame (cara menginstallnya: `sudo apt install python3-pygame`)
  
Tidak ada dependensi pihak ketiga — murni menggunakan pustaka standar Python.

## terus gimana jalanin nya?
- nah karna untuk saat ini hanya tersedia di sistem operasi linux, jadi kalau mau jalanin nya buka terminal dari folder project ini dan jalankan perintah
```bash
./install.sh
```
 * **perintah ini akan membuat shortcut di desktop kamu, jadi kamu bisa menjalankan nya dengan mudah**

 sekarang, shortcut nya udah ada di desktop kamu, kamu tinggal klik 2x untuk menjalankan nya!

## warna nya bosen, kalo mau ganti gimana?

- bisa banget! kamu tinggal buka file `app.py` terus cari bagian `__init__`:

### detail nya di tabel ini yaaa:

| Variabel     | Default   | Keterangan           |
| ------------ | --------- | -------------------- |
| `bg_color`   | `#1e2030` | Latar belakang       |
| `text_color` | `#eed49f` | Warna teks counter   |
| `accent_color` | `#8bd5ca` | Warna judul        |
| `muted_color` | `#939ab7` | Warna deskripsi/footer |

*ini warna nya terinspirasi dari catppuccin macchiato ya, mungkin kamu bisa cek [catppuccin](https://github.com/catppuccin/catppuccin)

### *created by ari_chii*
