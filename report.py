import json
from datetime import datetime, timedelta
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

def generate_daily_report():
    transactions = load_transactions()
    if not transactions:
        print("Belum ada transaksi.")
        return

    today = datetime.now().date()
    daily_sales = {}
    total_daily_revenue = 0

    for tx in transactions:
        tx_date_str = tx['timestamp'].split('T')[0]
        tx_date = datetime.fromisoformat(tx_date_str).date()

        if tx_date == today:
            total_daily_revenue += tx['total_amount']
            for item in tx['order_details']:
                item_name = item['item']
                quantity = item['quantity']
                price = item['price']
                if item_name not in daily_sales:
                    daily_sales[item_name] = {'quantity_sold': 0, 'revenue': 0}
                daily_sales[item_name]['quantity_sold'] += quantity
                daily_sales[item_name]['revenue'] += (quantity * price)

    print(f"\n--- LAPORAN PENJUALAN HARIAN ({today.strftime('%d-%m-%Y')}) ---")
    if not daily_sales:
        print("Tidak ada penjualan untuk hari ini.")
        return

    print(f"{'Item':<20} {'Terjual':>10} {'Pendapatan':>15}")
    print("----------------------------------------------------")
    for item, data in daily_sales.items():
        print(f"{item:<20} {data['quantity_sold']:>10} {data['revenue']:>15,.2f}")
    print("----------------------------------------------------")
    print(f"{'Total Pendapatan Harian':<31} {total_daily_revenue:>15,.2f}")
    print("----------------------------------------------------")

def generate_weekly_report():
    transactions = load_transactions()
    if not transactions:
        print("Belum ada transaksi.")
        return

    today = datetime.now().date()
    # Menghitung awal minggu (Senin)
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    weekly_sales = {}
    total_weekly_revenue = 0

    for tx in transactions:
        tx_date_str = tx['timestamp'].split('T')[0]
        tx_date = datetime.fromisoformat(tx_date_str).date()

        if start_of_week <= tx_date <= end_of_week:
            total_weekly_revenue += tx['total_amount']
            for item in tx['order_details']:
                item_name = item['item']
                quantity = item['quantity']
                price = item['price']
                if item_name not in weekly_sales:
                    weekly_sales[item_name] = {'quantity_sold': 0, 'revenue': 0}
                weekly_sales[item_name]['quantity_sold'] += quantity
                weekly_sales[item_name]['revenue'] += (quantity * price)

    print(f"\n--- LAPORAN PENJUALAN MINGGUAN ({start_of_week.strftime('%d-%m-%Y')} s/d {end_of_week.strftime('%d-%m-%Y')}) ---")
    if not weekly_sales:
        print("Tidak ada penjualan untuk minggu ini.")
        return

    print(f"{'Item':<20} {'Terjual':>10} {'Pendapatan':>15}")
    print("----------------------------------------------------")
    for item, data in weekly_sales.items():
        print(f"{item:<20} {data['quantity_sold']:>10} {data['revenue']:>15,.2f}")
    print("----------------------------------------------------")
    print(f"{'Total Pendapatan Mingguan':<31} {total_weekly_revenue:>15,.2f}")
    print("----------------------------------------------------")

def generate_monthly_report():
    transactions = load_transactions()
    if not transactions:
        print("Belum ada transaksi.")
        return

    current_month = datetime.now().month
    current_year = datetime.now().year

    monthly_sales = {}
    total_monthly_revenue = 0

    for tx in transactions:
        tx_datetime = datetime.fromisoformat(tx['timestamp'])
        if tx_datetime.month == current_month and tx_datetime.year == current_year:
            total_monthly_revenue += tx['total_amount']
            for item in tx['order_details']:
                item_name = item['item']
                quantity = item['quantity']
                price = item['price']
                if item_name not in monthly_sales:
                    monthly_sales[item_name] = {'quantity_sold': 0, 'revenue': 0}
                monthly_sales[item_name]['quantity_sold'] += quantity
                monthly_sales[item_name]['revenue'] += (quantity * price)

    print(f"\n--- LAPORAN PENJUALAN BULANAN ({datetime.now().strftime('%B %Y')}) ---")
    if not monthly_sales:
        print("Tidak ada penjualan untuk bulan ini.")
        return

    print(f"{'Item':<20} {'Terjual':>10} {'Pendapatan':>15}")
    print("----------------------------------------------------")
    for item, data in monthly_sales.items():
        print(f"{item:<20} {data['quantity_sold']:>10} {data['revenue']:>15,.2f}")
    print("----------------------------------------------------")
    print(f"{'Total Pendapatan Bulanan':<31} {total_monthly_revenue:>15,.2f}")
    print("----------------------------------------------------")

def sales_report_menu():
    while True:
        print("\n--- LAPORAN PENJUALAN ---")
        print("1. Laporan Harian")
        print("2. Laporan Mingguan")
        print("3. Laporan Bulanan")
        print("4. Kembali ke Menu Utama")
        choice = input("Pilih opsi: ")

        if choice == '1':
            generate_daily_report()
        elif choice == '2':
            generate_weekly_report()
        elif choice == '3':
            generate_monthly_report()
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid.")

# Contoh penggunaan dalam report.py (untuk pengujian terpisah)
if __name__ == '__main__':
    # Contoh data transaksi dummy untuk pengujian
    # Pastikan Anda memiliki menu.json dan transactions.json yang valid
    # atau buat dummy data di sini untuk pengujian
    print("Ini adalah modul laporan. Jalankan main.py untuk aplikasi lengkap.")
    # generate_daily_report()
    # generate_weekly_report()
    # generate_monthly_report()
    # sales_report_menu()