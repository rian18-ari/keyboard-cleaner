#!/usr/bin/env python3
import tkinter as tk
import sys
import random

class ModernKeyboardCleaner:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Cleaner Pro")
        
        # 1. Fullscreen & Always on Top
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        
        # Tema Warna (Catppuccin Macchiato vibe)
        self.bg_color = "#1e2030"      # Dark Blue-Grey
        self.text_color = "#eed49f"    # Pastel Yellow
        self.accent_color = "#8bd5ca"  # Teal
        self.muted_color = "#939ab7"   # Muted Blue
        
        self.root.configure(bg=self.bg_color)
        
        # Counter untuk menghitung jumlah ketikan saat dibersihkan
        self.key_count = 0

        # 2. Tata Letak GUI
        # Container Utama biar pas di tengah
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(expand=True)

        # Judul Utama
        self.title_label = tk.Label(
            self.main_frame, 
            text="🧹 KEYBOARD CLEANING MODE ACTIVE", 
            font=("Helvetica", 28, "bold"), 
            fg=self.accent_color, 
            bg=self.bg_color
        )
        self.title_label.pack(pady=10)

        # Deskripsi
        self.desc_label = tk.Label(
            self.main_frame, 
            text="Silakan lap keyboard kamu dengan aman.\nSemua input di bawah ini sengaja diblokir dari sistem.", 
            font=("Helvetica", 16), 
            fg=self.muted_color, 
            bg=self.bg_color
        )
        self.desc_label.pack(pady=10)

        # Counter Label (Statistik Real-time)
        self.counter_label = tk.Label(
            self.main_frame, 
            text="0 Tombol Dibersihkan", 
            font=("Helvetica", 20, "bold"), 
            fg=self.text_color, 
            bg=self.bg_color
        )
        self.counter_label.pack(pady=20)

        # Tempat nampilin tombol terakhir yang ditekan (Live Indicator)
        self.live_input_label = tk.Label(
            self.main_frame, 
            text="Menunggu input...", 
            font=("Courier New", 14, "italic"), 
            fg="#ee99a0", 
            bg=self.bg_color
        )
        self.live_input_label.pack(pady=10)

        # Footer Shortcut Informasi
        self.footer_label = tk.Label(
            root, 
            text="Keluar dari aplikasi: Tekan Ctrl + Shift + X", 
            font=("Helvetica", 12, "bold"), 
            fg=self.muted_color, 
            bg=self.bg_color
        )
        self.footer_label.pack(side="bottom", pady=30)

        # 3. Binding Event Keyboard
        self.root.bind("<Key>", self.on_key_pressed)
        
        # Shortcut Keluar (Tetap Konsisten)
        self.root.bind("<Control-Shift-X>", self.exit_application)
        self.root.bind("<Control-Shift-x>", self.exit_application)

    def on_key_pressed(self, event):
        # Tambah hitungan counter
        self.key_count += 1
        self.counter_label.config(text=f"{self.key_count} Tombol Dibersihkan")
        
        # Tampilkan nama tombol yang sedang tertekan di layar
        key_name = event.keysym
        self.live_input_label.config(text=f"Mendeteksi tekanan: [ {key_name} ]", font=("Courier New", 14, "bold"))
        
        # Efek Ambient Flash: Bikin background flash kilat pas ditekan
        # Ini ngasih tahu user secara visual kalau tombolnya sukses diblokir
        self.root.configure(bg="#25293c")
        self.root.after(100, lambda: self.root.configure(bg=self.bg_color))

    def exit_application(self, event):
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernKeyboardCleaner(root)
    root.mainloop()