import menu
import order
import receipt
import report # Import modul laporan

def main():
    current_menu = menu.load_menu()

    while True:
        print("\n=== APLIKASI KASIR RESTORAN ===")
        print("1. Manajemen Menu")
        print("2. Buat Pesanan Baru")
        print("3. Laporan Penjualan") # Opsi baru
        print("4. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            while True:
                print("\n--- MANAJEMEN MENU ---")
                print("1. Tambah Item")
                print("2. Lihat Menu (dengan Stok)")
                print("3. Update Harga/Stok Item")
                print("4. Hapus Item")
                print("5. Manajemen Stok (khusus)") # Opsi baru di submenu menu
                print("6. Kembali ke Menu Utama")
                menu_choice = input("Pilih opsi: ")

                if menu_choice == '1':
                    menu.add_menu_item(current_menu)
                elif menu_choice == '2':
                    menu.view_menu(current_menu)
                elif menu_choice == '3':
                    menu.update_menu_item(current_menu)
                elif menu_choice == '4':
                    menu.delete_menu_item(current_menu)
                elif menu_choice == '5': # Panggil fungsi manajemen stok
                    menu.manage_stock(current_menu)
                elif menu_choice == '6':
                    break
                else:
                    print("Pilihan tidak valid.")
        elif choice == '2':
            new_order = order.create_order(current_menu)
            if new_order:
                total_amount = order.calculate_total(new_order)
                amount_paid, change = order.process_payment(total_amount) # process_payment sekarang mengembalikan nilai
                if amount_paid is not None: # Jika pembayaran berhasil
                    order.finalize_order(new_order, total_amount, amount_paid, change, current_menu) # Finalisasi order, kurangi stok, simpan transaksi
                    receipt.generate_receipt(new_order, total_amount, amount_paid, change)
        elif choice == '3': # Panggil menu laporan penjualan
            report.sales_report_menu()
        elif choice == '4':
            print("Terima kasih telah menggunakan aplikasi kasir.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()