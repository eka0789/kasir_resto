from menu import load_menu, view_menu

def create_order(menu):
    if not menu:
        print("Menu kosong. Mohon tambahkan item menu terlebih dahulu.")
        return []

    current_order = []
    print("\n--- BUAT PESANAN ---")
    while True:
        view_menu(menu)
        item_name = input("Masukkan nama item (ketik 'selesai' untuk mengakhiri): ").strip()
        if item_name.lower() == 'selesai':
            break

        if item_name in menu:
            while True:
                try:
                    quantity_str = input(f"Jumlah '{item_name}': ").strip()
                    quantity = int(quantity_str)
                    if quantity > 0:
                        current_order.append({'item': item_name, 'price': menu[item_name], 'quantity': quantity})
                        print(f"{quantity} '{item_name}' ditambahkan ke pesanan.")
                        break
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
                return True
            else:
                print(f"Uang kurang! Masih kurang Rp {total - amount_paid:,.2f}")
        except ValueError:
            print("Jumlah uang harus berupa angka.")