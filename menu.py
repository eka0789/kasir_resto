import json
import os

MENU_FILE = 'menu.json'

def load_menu():
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"Error: File {MENU_FILE} rusak. Membuat menu kosong.")
                return {}
    return {}

def save_menu(menu):
    with open(MENU_FILE, 'w') as f:
        json.dump(menu, f, indent=4)

def add_menu_item(menu):
    name = input("Nama item: ").strip()
    price_str = input("Harga item: ").strip()
    stock_str = input("Jumlah stok awal: ").strip()
    try:
        price = float(price_str)
        stock = int(stock_str)
        if name and price > 0 and stock >= 0:
            menu[name] = {'price': price, 'stock': stock}
            save_menu(menu)
            print(f"'{name}' dengan harga Rp {price:,.2f} dan stok {stock} berhasil ditambahkan.")
        else:
            print("Input tidak valid. Nama dan harga harus diisi, harga harus positif, stok harus non-negatif.")
    except ValueError:
        print("Harga dan stok harus berupa angka.")

def view_menu(menu):
    if not menu:
        print("Menu masih kosong.")
        return
    print("\n--- DAFTAR MENU ---")
    print(f"{'No.':<4} {'Item':<20} {'Harga':>10} {'Stok':>5}")
    print("--------------------------------------------------")
    for i, (item, details) in enumerate(menu.items(), 1):
        print(f"{i:<4} {item:<20} {details['price']:>10,.2f} {details['stock']:>5}")
    print("--------------------------------------------------")

def update_menu_item(menu):
    view_menu(menu)
    if not menu:
        return
    item_to_update = input("Nama item yang akan diupdate (harga/stok): ").strip()
    if item_to_update in menu:
        print(f"Mengupdate '{item_to_update}'. Harga saat ini: Rp {menu[item_to_update]['price']:,.2f}, Stok saat ini: {menu[item_to_update]['stock']}")
        new_price_str = input(f"Harga baru (kosongkan jika tidak diubah): ").strip()
        new_stock_str = input(f"Stok baru (kosongkan jika tidak diubah): ").strip()

        updated = False
        if new_price_str:
            try:
                new_price = float(new_price_str)
                if new_price > 0:
                    menu[item_to_update]['price'] = new_price
                    updated = True
                else:
                    print("Harga harus positif.")
            except ValueError:
                print("Harga harus berupa angka.")

        if new_stock_str:
            try:
                new_stock = int(new_stock_str)
                if new_stock >= 0:
                    menu[item_to_update]['stock'] = new_stock
                    updated = True
                else:
                    print("Stok harus non-negatif.")
            except ValueError:
                print("Stok harus berupa angka.")

        if updated:
            save_menu(menu)
            print(f"'{item_to_update}' berhasil diupdate.")
        else:
            print("Tidak ada perubahan yang dilakukan.")
    else:
        print(f"Item '{item_to_update}' tidak ditemukan di menu.")

def delete_menu_item(menu):
    view_menu(menu)
    if not menu:
        return
    item_to_delete = input("Nama item yang akan dihapus: ").strip()
    if item_to_delete in menu:
        del menu[item_to_delete]
        save_menu(menu)
        print(f"'{item_to_delete}' berhasil dihapus dari menu.")
    else:
        print(f"Item '{item_to_delete}' tidak ditemukan di menu.")

# Fungsi baru untuk manajemen stok
def manage_stock(menu):
    while True:
        print("\n--- MANAJEMEN STOK ---")
        print("1. Lihat Stok")
        print("2. Tambah Stok Item")
        print("3. Kembali ke Menu Utama")
        choice = input("Pilih opsi: ")

        if choice == '1':
            view_menu(menu) # View menu sudah menampilkan stok
        elif choice == '2':
            view_menu(menu)
            if not menu:
                continue
            item_name = input("Nama item yang akan ditambah stoknya: ").strip()
            if item_name in menu:
                try:
                    add_qty = int(input(f"Jumlah stok yang akan ditambahkan untuk '{item_name}': ").strip())
                    if add_qty > 0:
                        menu[item_name]['stock'] += add_qty
                        save_menu(menu)
                        print(f"Stok '{item_name}' berhasil ditambah {add_qty}. Stok baru: {menu[item_name]['stock']}")
                    else:
                        print("Jumlah harus positif.")
                except ValueError:
                    print("Jumlah harus berupa angka.")
            else:
                print(f"Item '{item_name}' tidak ditemukan.")
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid.")

# Contoh penggunaan dalam menu.py (untuk pengujian terpisah)
if __name__ == '__main__':
    current_menu = load_menu()
    while True:
        print("\n--- MANAJEMEN MENU ---")
        print("1. Tambah Item")
        print("2. Lihat Menu (dengan Stok)")
        print("3. Update Harga/Stok Item")
        print("4. Hapus Item")
        print("5. Manajemen Stok (khusus)")
        print("6. Kembali ke Menu Utama")
        choice = input("Pilih opsi: ")

        if choice == '1':
            add_menu_item(current_menu)
        elif choice == '2':
            view_menu(current_menu)
        elif choice == '3':
            update_menu_item(current_menu)
        elif choice == '4':
            delete_menu_item(current_menu)
        elif choice == '5':
            manage_stock(current_menu)
        elif choice == '6':
            break
        else:
            print("Pilihan tidak valid.")