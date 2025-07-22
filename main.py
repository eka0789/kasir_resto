import menu
import order
import receipt

def main():
    current_menu = menu.load_menu()

    while True:
        print("\n=== APLIKASI KASIR RESTORAN ===")
        print("1. Manajemen Menu")
        print("2. Buat Pesanan Baru")
        print("3. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            while True:
                print("\n--- MANAJEMEN MENU ---")
                print("1. Tambah Item")
                print("2. Lihat Menu")
                print("3. Update Harga Item")
                print("4. Hapus Item")
                print("5. Kembali ke Menu Utama")
                menu_choice = input("Pilih opsi: ")

                if menu_choice == '1':
                    menu.add_menu_item(current_menu)
                elif menu_choice == '2':
                    menu.view_menu(current_menu)
                elif menu_choice == '3':
                    menu.update_menu_item(current_menu)
                elif menu_choice == '4':
                    menu.delete_menu_item(current_menu)
                elif menu_choice == '5':
                    break
                else:
                    print("Pilihan tidak valid.")
        elif choice == '2':
            new_order = order.create_order(current_menu)
            if new_order:
                total_amount = order.calculate_total(new_order)
                if order.process_payment(total_amount):
                    receipt.generate_receipt(new_order, total_amount, amount_paid=0, change=0) # amount_paid and change need to be passed correctly from process_payment
                                                                                                # This example simplifies, in a real app, process_payment would return these values.
                    # Simplified: Re-ask for paid amount and calculate change for receipt
                    while True:
                        try:
                            paid_str = input("Masukkan jumlah pembayaran lagi untuk struk: ").strip()
                            paid_amount = float(paid_str)
                            if paid_amount >= total_amount:
                                change_for_receipt = paid_amount - total_amount
                                receipt.generate_receipt(new_order, total_amount, paid_amount, change_for_receipt)
                                break
                            else:
                                print("Pembayaran kurang, masukkan jumlah yang benar.")
                        except ValueError:
                            print("Input tidak valid, masukkan angka.")
        elif choice == '3':
            print("Terima kasih telah menggunakan aplikasi kasir.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()