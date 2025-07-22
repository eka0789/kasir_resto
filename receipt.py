from datetime import datetime
import os

RECEIPT_DIR = 'receipts'

def generate_receipt(order, total, amount_paid, change):
    if not os.path.exists(RECEIPT_DIR):
        os.makedirs(RECEIPT_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    receipt_filename = os.path.join(RECEIPT_DIR, f"struk_{timestamp}.txt")

    with open(receipt_filename, 'w') as f:
        f.write("========================================\n")
        f.write("           RESTORAN PYTHON MURNI        \n")
        f.write("========================================\n")
        f.write(f"Tanggal: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write("----------------------------------------\n")
        f.write(f"{'Item':<20} {'Harga':>10} {'Qty':>5}\n")
        f.write("----------------------------------------\n")
        for item in order:
            f.write(f"{item['item']:<20} {item['price']:>10,.2f} {item['quantity']:>5}\n")
        f.write("----------------------------------------\n")
        f.write(f"{'Subtotal':<20} {'':>10} {total:,.2f}\n")
        f.write(f"{'Total':<20} {'':>10} {total:,.2f}\n")
        f.write(f"{'Dibayar':<20} {'':>10} {amount_paid:,.2f}\n")
        f.write(f"{'Kembalian':<20} {'':>10} {change:,.2f}\n")
        f.write("========================================\n")
        f.write("         TERIMA KASIH ATAS KUNJUNGANNYA!\n")
        f.write("========================================\n")

    print(f"\nStruk berhasil disimpan sebagai: {receipt_filename}")
    print("Anda bisa mencetak struk ini secara manual.")

    # Contoh untuk mencetak langsung ke printer (membutuhkan konfigurasi printer)
    # import subprocess
    # try:
    #     subprocess.run(['lp', receipt_filename]) # Untuk Linux/macOS
    #     # subprocess.run(['print', receipt_filename], shell=True) # Untuk Windows (mungkin butuh konfigurasi)
    #     print("Struk dikirim ke printer (jika printer terkonfigurasi).")
    # except FileNotFoundError:
    #     print("Perintah cetak tidak ditemukan. Pastikan printer sudah dikonfigurasi.")
    # except Exception as e:
    #     print(f"Gagal mencetak struk: {e}")