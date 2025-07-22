import json
import os

MENU_FILE = 'menu.json'

def load_menu():
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_menu(menu):
    with open(MENU_FILE, 'w') as f:
        json.dump(menu, f, indent=4)

def add_menu_item(menu):
    name = input("Nama item: ").strip()
    price_str = input("Harga item: ").strip()
    try:
        price = float(price_str)
        if name and price > 0:
            menu[name] = price
            save_menu(menu)
            print(f"'{name}' dengan harga Rp {price:,.2f} berhasil ditambahkan.")
        else:
            print("Input tidak valid. Nama dan harga harus diisi, harga harus positif.")
    except ValueError:
        print("Harga harus berupa angka.")

def view_menu(menu):
    if not menu:
        print("Menu masih kosong.")
        return
    print("\n--- DAFTAR MENU ---")
    for i, (item, price) in enumerate(menu.items(), 1):
        print(f"{i}. {item:<20} Rp {price:,.2f}")
    print("-------------------")

def update_menu_item(menu):
    view_menu(menu)
    if not menu:
        return
    item_to_update = input("Nama item yang akan diupdate: ").strip()
    if item_to_update in menu:
        new_price_str = input(f"Harga baru untuk '{item_to_update}': ").strip()
        try:
            new_price = float(new_price_str)
            if new_price > 0:
                menu[item_to_update] = new_price
                save_menu(menu)
                print(f"Harga '{item_to_update}' berhasil diupdate menjadi Rp {new_price:,.2f}.")
            else:
                print("Harga harus positif.")
        except ValueError:
            print("Harga harus berupa angka.")
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

# Contoh penggunaan dalam menu.py
if __name__ == '__main__':
    current_menu = load_menu()
    while True:
        print("\n--- MANAJEMEN MENU ---")
        print("1. Tambah Item")
        print("2. Lihat Menu")
        print("3. Update Harga Item")
        print("4. Hapus Item")
        print("5. Kembali ke Menu Utama")
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
            break
        else:
            print("Pilihan tidak valid.")