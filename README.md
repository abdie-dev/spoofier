# Spoofing Tool by biww ( on Development )

Tool untuk melakukan **IP dan MAC address spoofing** pada jaringan menggunakan `nmcli` (NetworkManager). Tool ini menyediakan mode **Auto Configure** dan **Manual Configure** untuk mengubah konfigurasi interface jaringan.

> ⚠️ **DISCLAIMER:** Tool ini dibuat untuk **tujuan edukasi dan pengujian keamanan (penetration testing)** pada jaringan milik sendiri. Penyalahgunaan tool ini pada jaringan yang bukan milik Anda adalah **ilegal** dan melanggar hukum.

---

## 📋 Fitur

- ✅ **Auto Configuration** dengan 3 mode:
  - `IP + MAC` (beserta DNS Cloudflare 1.1.1.1)
  - `IP only`
  - `MAC only`
- ✅ **Scan** jaringan untuk menampilkan koneksi aktif
- ✅ Deteksi otomatis target interface (main internet device)
- ✅ Input validation untuk mencegah error
- ✅ Error handling pada semua `subprocess` call
- ✅ Refactor: tidak ada duplikasi kode (scanning & grep target hanya dilakukan **sekali**)

---

## 🔧 Requirements

- **OS:** Linux dengan **NetworkManager** (Fedora, Ubuntu, dll)
- **Python:** 3.10+ (menggunakan `match-case` statement)
- **Permissions:** `sudo` / root (diperlukan untuk mengubah konfigurasi jaringan)
- **Tools:** `nmcli` (biasanya sudah terinstall bersama NetworkManager)

Cek dependencies:
```bash
python3 --version
nmcli --version
```

---

## 🚀 Instalasi

```bash
# Clone repository
git clone <repository-url>
cd spoofing

# Tidak ada dependency Python tambahan (hanya stdlib)
```

---

## 💻 Usage

Jalankan dengan **root/sudo** karena mengubah konfigurasi jaringan:
```bash
sudo python3 spoofing.py
```

### Menu Utama

```
1. Auto Configure  → Pilih mode spoofing (IP+MAC / IP only / MAC only)
2. Manual Configure → (Coming soon)
3. Reset           → (Coming soon)
4. Scan            → Tampilkan status DNS resolver
```

### Mode Auto Configure

Setelah memilih `1`, Anda akan diminta memilih:
```
1. IP and MAC ( +DNS cloudflare )
2. IP only
3. MAC only
```

Tool akan otomatis:
1. Melakukan scanning jaringan aktif (`nmcli connection show --active`)
2. Mendeteksi interface utama (target)
3. Menjalankan spoofing sesuai pilihan
4. Restart koneksi untuk apply perubahan

**Konfigurasi default yang digunakan:**
- **IP:** `192.168.1.100/24`
- **Gateway:** `192.168.1.1`
- **DNS:** `1.1.1.1` (Cloudflare)
- **MAC:** `00:11:22:33:44:55`

---

## 📁 Struktur Kode

```
spoofing.py
├── Konstanta warna terminal (MERAH, HIJAU, KUNING, dll)
├── autoConfiguration()  → Menu & logika utama spoofing
├── manualConfiguration() → Placeholder (TODO)
├── scanNetwork()         → Scan DNS resolver
└── __main__              → Menu utama + match-case
```

---

## 🛠️ Troubleshooting

| Masalah | Solusi |
|---------|--------|
| `nmcli: command not found` | Install NetworkManager: `sudo dnf install NetworkManager` |
| `Error scanning network` | Pastikan NetworkManager berjalan: `sudo systemctl start NetworkManager` |
| Tidak ada koneksi aktif | Hubungkan ke WiFi/Ethernet terlebih dahulu |
| Perubahan tidak ter-apply | Cek apakah Anda menjalankan dengan `sudo` |
| **E325: nvim swap file** | Hapus swap: `rm -f ~/.local/state/nvim/swap/*spoofing*.swp` |

---

## 📝 Catatan Pengembangan

### Perubahan dari versi sebelumnya:
- ✨ Refactor: duplikasi kode dihilangkan
- ✨ Validasi input (handle `ValueError` dan input di luar range)
- ✨ Error handling di setiap `subprocess.run` dengan `check=True`
- ✨ Penambahan komentar yang lebih spesifik di setiap blok kode

### TODO:
- [ ] Implementasi `manualConfiguration()` (input IP/MAC manual)
- [ ] Implementasi `Reset` (kembalikan ke konfigurasi default)
- [ ] Deteksi otomatis gateway & subnet (saat ini hardcoded `192.168.1.x`)
- [ ] Support multiple interface selection

---

## 👤 Author

**biww** — [Knox Noble](https://github.com/)

## 📄 License

MIT License — Gunakan dengan bijak dan bertanggung jawab.
