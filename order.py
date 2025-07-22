from menu import load_menu, save_menu, view_menu
from datetime import datetime
import json
import os

TRANSACTIONS_FILE = 'transactions.json'

def load_transactions():
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"Error: File {TRANSACTIONS_FILE} rusak. Membuat transaksi kosong.")
                return []
    return []

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, 'w') as f:
        json.dump(transactions, f, indent=4)

def create_order(menu):
    if not menu:
        print("Menu kosong. Mohon tambahkan item menu terlebih dahulu.")
        return []

    current_order = []
    print("\n--- BUAT PESANAN ---")
    while True:
        view_menu(menu) # Menampilkan menu dengan stok
        item_name = input("Masukkan nama item (ketik 'selesai' untuk mengakhiri): ").strip()
        if item_name.lower() == 'selesai':
            break

        if item_name in menu:
            item_details = menu[item_name]
            available_stock = item_details['stock']
            if available_stock == 0:
                print(f"Maaf, '{item_name}' sedang kosong.")
                continue

            while True:
                try:
                    quantity_str = input(f"Jumlah '{item_name}' (stok tersedia: {available_stock}): ").strip()
                    quantity = int(quantity_str)
                    if quantity > 0:
                        if quantity <= available_stock:
                            current_order.append({'item': item_name, 'price': item_details['price'], 'quantity': quantity})
                            print(f"{quantity} '{item_name}' ditambahkan ke pesanan.")
                            break
                        else:
                            print(f"Jumlah melebihi stok tersedia. Hanya ada {available_stock} unit.")
                    else:
                        print("Jumlah harus lebih dari 0.")
                except ValueError:
                    print("Jumlah harus berupa angka.")
        else:
            print(f"Item '{item_name}' tidak ditemukan di menu.")
    return current_order

def calculate_total(order):
    total = sum(item['price'] * item['quantity'] for item in order)
    return total

def process_payment(total):
    print(f"\nTotal yang harus dibayar: Rp {total:,.2f}")
    while True:
        try:
            amount_paid_str = input("Jumlah uang yang dibayarkan: ").strip()
            amount_paid = float(amount_paid_str)
            if amount_paid >= total:
                change = amount_paid - total
                print(f"Pembayaran diterima. Kembalian: Rp {change:,.2f}")
                return amount_paid, change
            else:
                print(f"Uang kurang! Masih kurang Rp {total - amount_paid:,.2f}")
        except ValueError:
            print("Jumlah uang harus berupa angka.")

def finalize_order(order, total, amount_paid, change, menu):
    # Kurangi stok
    for item_in_order in order:
        item_name = item_in_order['item']
        quantity = item_in_order['quantity']
        if item_name in menu:
            menu[item_name]['stock'] -= quantity
    save_menu(menu) # Simpan perubahan stok

    # Simpan transaksi
    transactions = load_transactions()
    transaction_record = {
        'timestamp': datetime.now().isoformat(),
        'order_details': order,
        'total_amount': total,
        'amount_paid': amount_paid,
        'change': change
    }
    transactions.append(transaction_record)
    save_transactions(transactions)
    print("Transaksi berhasil dicatat.")