# Aplikasi Kasir Restoran (CLI)

-----

Aplikasi ini adalah sistem kasir berbasis teks (CLI) sederhana yang dibuat dengan **Python murni**, dirancang khusus untuk restoran. Aplikasi ini memungkinkan Anda mengelola menu, membuat pesanan, memproses pembayaran, dan mencetak struk transaksi.

-----

## Fitur Utama

  * **Manajemen Menu:**
      * Menambahkan item makanan/minuman baru beserta harganya.
      * Melihat daftar semua item menu yang tersedia.
      * Memperbarui harga item menu yang sudah ada.
      * Menghapus item menu dari daftar.
  * **Pembuatan Pesanan:**
      * Memilih item dari menu dan menentukan kuantitasnya.
      * Menghitung subtotal dan total pesanan secara otomatis.
  * **Pemrosesan Pembayaran:**
      * Menerima jumlah pembayaran dan menghitung kembalian.
  * **Pencetakan Struk:**
      * Menghasilkan struk transaksi yang rapi dan menyimpannya sebagai file teks (`.txt`).
      * Struk disimpan di dalam folder `receipts/` dengan nama file berdasarkan tanggal dan waktu transaksi.

-----

## Struktur Proyek

Aplikasi ini dipecah menjadi beberapa modul Python untuk menjaga kode tetap rapi dan mudah dikelola:

  * `main.py`: File utama yang menjalankan aplikasi dan mengoordinasikan semua modul.
  * `menu.py`: Berisi fungsi-fungsi untuk mengelola menu (tambah, lihat, update, hapus).
  * `order.py`: Berisi fungsi-fungsi untuk membuat pesanan dan memproses pembayaran.
  * `receipt.py`: Berisi fungsi untuk menghasilkan dan menyimpan struk transaksi.
  * `menu.json`: File ini secara otomatis dibuat dan digunakan untuk menyimpan data menu.
  * `receipts/`: Folder ini akan otomatis dibuat dan berisi semua file struk transaksi yang dihasilkan.

-----

## Cara Menjalankan

Ikuti langkah-langkah mudah ini untuk menjalankan aplikasi:

1.  **Kloning Repositori (Opsional) atau Unduh File:**
    Jika Anda mendapatkan kode ini dari repositori, kloninglah:

    ```bash
    git clone https://github.com/eka0789/kasir_resto
    cd kasir_resto
    ```

    Jika tidak, pastikan Anda memiliki semua file (`main.py`, `menu.py`, `order.py`, `receipt.py`) dalam satu direktori.

2.  **Pastikan Python Terinstal:**
    Aplikasi ini memerlukan **Python 3**. Anda bisa memeriksanya dengan menjalankan:

    ```bash
    python --version
    # atau
    python3 --version
    ```

    Jika Python belum terinstal, kunjungi [python.org](https://www.python.org/) untuk mengunduhnya.

3.  **Jalankan Aplikasi:**
    Buka terminal atau command prompt, navigasikan ke direktori tempat Anda menyimpan file-file aplikasi, lalu jalankan perintah berikut:

    ```bash
    python main.py
    ```

    Aplikasi akan menampilkan menu utama di terminal.

-----

## Penggunaan

Setelah menjalankan `python main.py`, Anda akan melihat menu utama:

```
=== APLIKASI KASIR RESTORAN ===
1. Manajemen Menu
2. Buat Pesanan Baru
3. Keluar
Pilih opsi:
```

  * **Opsi 1: Manajemen Menu:**
    Anda bisa menambah, melihat, mengupdate harga, atau menghapus item dari menu. Data menu akan disimpan secara otomatis di `menu.json`.
  * **Opsi 2: Buat Pesanan Baru:**
    Aplikasi akan menampilkan menu yang tersedia.
    Masukkan nama item dan jumlahnya. Ketik 'selesai' untuk mengakhiri pesanan.
    Setelah pesanan selesai, total akan dihitung dan Anda bisa memproses pembayaran.
    Struk transaksi akan otomatis dibuat dan disimpan di folder `receipts/`.

-----

## Pencetakan Struk

Struk transaksi disimpan dalam format file teks (`.txt`). Untuk mencetaknya, Anda bisa:

1.  **Membuka file struk** (`.txt`) yang berada di folder `receipts/` dan mencetaknya secara manual melalui editor teks favorit Anda.
2.  **Menggunakan perintah cetak dari terminal (Linux/macOS):**
    Jika printer Anda sudah terkonfigurasi di sistem, Anda bisa menggunakan perintah `lp` atau `lpr`:
    ```bash
    lp path/to/receipts/struk_YYYYMMDD_HHMMSS.txt
    ```
    Ganti `path/to/receipts/struk_YYYYMMDD_HHMMSS.txt` dengan lokasi dan nama file struk yang sebenarnya.

-----

## Pengembangan Lanjut (Opsional)

Aplikasi ini adalah dasar yang baik untuk memulai. Beberapa ide pengembangan lebih lanjut meliputi:

  * **Manajemen Stok:** Tambahkan fitur untuk melacak ketersediaan item.
  * **Database:** Ganti penyimpanan JSON dengan database sederhana seperti [SQLite](https://docs.python.org/3/library/sqlite3.html) untuk pengelolaan data yang lebih robust.
  * **Laporan Penjualan:** Implementasikan fitur untuk menghasilkan laporan penjualan harian/mingguan/bulanan.
  * **Antarmuka Grafis (GUI):** Jika Anda ingin tampilan yang lebih interaktif, pertimbangkan untuk membangun GUI menggunakan `Tkinter`, `PyQt`, atau `Kivy`.
  * **Integrasi Printer POS:** Untuk pencetakan struk langsung ke printer POS, Anda mungkin perlu mengintegrasikan library seperti [`python-escpos`](https://www.google.com/search?q=%5Bhttps://pypi.org/project/python-escpos/%5D\(https://pypi.org/project/python-escpos/\)).
