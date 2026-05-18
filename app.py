#!/usr/bin/env python3
import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Bikin Fullscreen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Keyboard Cleaner")
clock = pygame.time.Clock()

# Warna (Theme: Catppuccin Macchiato)
BG_COLOR = (30, 32, 48)
TEXT_COLOR = (238, 212, 159)
ACCENT_COLOR = (139, 213, 202)
MUTED_COLOR = (147, 154, 183)

# Font
font_title = pygame.font.SysFont("Helvetica", 40, bold=True)
font_desc = pygame.font.SysFont("Helvetica", 24)
font_counter = pygame.font.SysFont("Helvetica", 32, bold=True)

key_count = 0
last_key = "Menunggu input..."
flash_effect = 0

running = True
while running:
    # Mengatur Efek Kilat pas tombol ditekan
    if flash_effect > 0:
        current_bg = (40, 45, 65) # Warna agak terang pas flash
        flash_effect -= 1
    else:
        current_bg = BG_COLOR

    screen.fill(current_bg)

    # Render Teks ke Layar
    title_surface = font_title.render("🧹 KEYBOARD CLEANING MODE ACTIVE", True, ACCENT_COLOR)
    desc_surface1 = font_desc.render("Silakan lap keyboard kamu dengan aman.", True, MUTED_COLOR)
    desc_surface2 = font_desc.render("Semua input diblokir dari sistem harian.", True, MUTED_COLOR)
    counter_surface = font_counter.render(f"{key_count} Tombol Dibersihkan", True, TEXT_COLOR)
    key_surface = font_desc.render(f"Mendeteksi: [ {last_key} ]", True, (238, 153, 160))
    footer_surface = font_desc.render("Keluar: Tekan Ctrl + Shift + X", True, MUTED_COLOR)

    # Posisi Tengah Jendela
    width, height = screen.get_size()
    screen.blit(title_surface, (width//2 - title_surface.get_width()//2, height//3))
    screen.blit(desc_surface1, (width//2 - desc_surface1.get_width()//2, height//3 + 60))
    screen.blit(desc_surface2, (width//2 - desc_surface2.get_width()//2, height//3 + 90))
    screen.blit(counter_surface, (width//2 - counter_surface.get_width()//2, height//3 + 160))
    screen.blit(key_surface, (width//2 - key_surface.get_width()//2, height//3 + 220))
    screen.blit(footer_surface, (width//2 - footer_surface.get_width()//2, height - 80))

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            # Hitung tombol masuk
            key_count += 1
            last_key = pygame.key.name(event.key).upper()
            flash_effect = 5 # Durasi flash frame
            
            # Cek Shortcut Keluar: Ctrl + Shift + X
            mods = pygame.key.get_mods()
            if (mods & pygame.KMOD_CTRL) and (mods & pygame.KMOD_SHIFT) and event.key == pygame.K_x:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()