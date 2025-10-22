### Main Menu

# =======================
from tabulate import tabulate

tabel_cuci = [
    { 'index': 0, 
    'menu': 'cuci aja', 
    'treatment': '''exterior pre wash
tyre & wheel cleaning(face & barrel)
wheel wall cleaning
drying with microfibre towel
inal touch with quick detailer
carpet cleaning
interior vacuuming
interior wiping
window cleaning
tyre dressing'''
    },

    { 'index': 1, 
    'menu': 'cuci premium', 
    'treatment': '''exterior pre wash with shampoo foaming
tyre & wheel cleaning(face & barrel)
wheel wall cleaning
undercarriage rinsing
drying with drying aide, microfibre towel & air compressor
nooks & crannies cleaning
waxing
carpet cleaning
interior vacuuming
interior cleaning & dressing
steering wheel & pedal cleaning
window cleaning
windshield glass sealant
tyre dressing'''
    },

    { 'index': 2, 
    'menu': 'cuci banget', 
    'treatment': '''exterior pre wash
tyre & wheel cleaning(face & barrel)
wheel wall cleaning
undercarriage rinsing
drying with microfibre towel
tar & iron removal
claying
nooks & crannies cleaning
waxing with dual action polisher
carpet cleaning
quick interior detailing
quick engine bay detailing
window cleaning
tyre dressing'''
    }
]

tabel_cuci_sorted = sorted(tabel_cuci, key=lambda x: x['index'])

print(tabulate(tabel_cuci_sorted, headers="keys", tablefmt="fancy_grid"))

# =======================

from tabulate import tabulate

tabel_price = [
    {'index':0, 
    'menu': 'cuci aja', 
    'ukuran': '''s
m
l
xl''', 
    'harga': '''100k
110k
120k
130k'''
    }, 
    
    { 'index':1, 
    'menu': 'cuci premium', 
    'ukuran': '''s
m
l
xl''',
    'harga': '''400k
450k
500k
600k'''
    }, 
    
    { 'index':2, 
    'menu': 'cuci banget', 
    'ukuran': '''s
m
l
xl''',
    'harga': '''550k
650k
750k
850k'''
    }
    ]

tabel_price_sorted = sorted(tabel_price, key=lambda x: x['index'])

print(tabulate(tabel_price_sorted, headers="keys", tablefmt="fancy_grid"))

# =======================
from tabulate import tabulate

tabel_order = [
    {'index': 0, 
     'nama': 'a', 
     'telp': '0811', 
     'alamat': 'jl. apel 1', 
     'jarak(km)':2, 
     'jenis': 'fortuner', 
     'warna': 'putih', 
     'nopol': 'd 101 a', 
     'menu': 'cuci aja', 
     'jadwal': 'senin'
     },

    {'index': 1, 
     'nama': 'b', 
     'telp': '0812', 
     'alamat': 'jl. belimbing 1', 
     'jarak(km)':3, 
     'jenis': 'pajero', 
     'warna': 'hitam', 
     'nopol': 'd 102 b', 
     'menu': 'cuci premium', 
     'jadwal': 'selasa'
     },

    {'index': 2, 
     'nama': 'c', 
     'telp': '0813', 
     'alamat': 'jl. celana 1', 
     'jarak(km)':4, 
     'jenis': 'innova', 
     'warna': 'abu', 
     'nopol': 'd 103 c', 
     'menu': 'cuci banget', 
     'jadwal': 'rabu'
     },

    {'index': 3, 
     'nama': 'd', 
     'telp': '0814', 
     'alamat': 'jl. dasi 1', 
     'jarak(km)':5, 
     'jenis': 'jimny', 
     'warna': 'hijau', 
     'nopol': 'd 104 d', 
     'menu': 'cuci premium', 
     'jadwal': 'kamis'
     },

    {'index': 4, 
     'nama': 'e', 
     'telp': '0815', 
     'alamat': 'jl. elang 1', 
     'jarak(km)':6, 
     'jenis': 'subaru', 
     'warna': 'biru', 
     'nopol': 'd 105 e', 
     'menu': 'cuci banget', 
     'jadwal': 'jumat'
     },

    {'index': 5, 
     'nama': 'f', 
     'telp': '0816', 
     'alamat': 'jl. flamingo 1', 
     'jarak(km)':7, 
     'jenis': 'jazz', 
     'warna': 'merah', 
     'nopol': 'd 106 f', 
     'menu': 'cuci aja', 
     'jadwal': 'sabtu'
     }
]

tabel_order_sorted = sorted(tabel_order, key=lambda x: x['index'])

print(tabulate(tabel_order_sorted, headers="keys", tablefmt="fancy_grid"))

# =======================
def tampilkan_cuci():
    print("\nDaftar Menu:")
    print(tabulate(tabel_cuci, headers="keys", tablefmt="grid"))

def tampilkan_price():
    print("\nDaftar Price:")
    print(tabulate(tabel_price, headers="keys", tablefmt="grid"))

def tampilkan_order():
    print("\nDaftar Order:")
    print(tabulate(tabel_order, headers="keys", tablefmt="grid"))

def tambah_order():
    print("\nMenambah Data Order")
    nama = (input("Masukkan nama baru: ")).capitalize()
    telp = (input("Masukkan nomer telepon: ")).lower()
    alamat = (input("Masukkan alamat rumah: ")).lower()
    jarak = (input("Masukkan jarak rumah: "))
    jenis = (input("Masukkan jenis mobil: ")).lower()
    warna = (input("Masukkan warna mobil: ")).lower()
    nopol = (input("Masukkan nomor polisi kendaraan: ")).lower()
    menu = (input("Masukkan pilihan menu cuci: ")).lower()
    jadwal = (input("Masukkan pilihan hari order: ")).capitalize()

    print(f"\nOrder '{nama}' berhasil ditambahkan!")
    print(f'\n=== Konfirmasi Order Qoombah Baru ===')
    print(f'\nnama: {nama}')
    print(f'telp: {telp}')
    print(f'alamat: {alamat}')
    print(f'jarak: {jarak}')
    print(f'jenis: {jenis}')
    print(f'warna: {warna}')
    print(f'nopol: {nopol}')
    print(f'menu: {menu}')
    print(f'jadwal: {jadwal}')

    konfirmasi = input("\nApakah data sudah benar? (y/n) : ")

# =======================
while True:
    daftar_tanya = [
    print("\n===== Selamat Datang di Qoombah ====="),
    print("\nList Menu:"),
    print("\n1. Menampilkan Menu Cuci"),
    print("2. Menampilkan Menu Pricelist"),
    print("3. Menampilkan Jadwal Orderan Hari Ini"),
    print("4. Menambah Order"),
    print("5. Exit Program")
    ]

    pilihan = input("Masukkan angka menu yang ingin dijalankan: ")

    if pilihan == "1":
        tampilkan_cuci()
    elif pilihan == "2":
        tampilkan_price()
    elif pilihan == "3":
        tampilkan_order()
    elif pilihan == "4":
        tambah_order()
    elif pilihan == "5":
        print("\nOrderan telah selesai! Terima kasih sudah mencuci di Qoombah!")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

# =======================
### READ
while True:
    daftar_tanya = [
    print("\n===== Selamat Datang di Qoombah ====="),
    print("\nList Menu:"),
    print("\n1. Menampilkan Menu Cuci"),
    print("2. Menampilkan Menu Pricelist"),
    print("3. Menampilkan Jadwal Orderan Hari Ini"),
    print("4. Menambah Order"),
    print("5. Exit Program")
    ]

    pilihan = input("Masukkan angka menu yang ingin dijalankan: ")

    if pilihan == "1":
        tampilkan_cuci()
    elif pilihan == "2":
        tampilkan_price()
    elif pilihan == "3":
        tampilkan_order()
    elif pilihan == "4":
        tambah_order()
    elif pilihan == "5":
        print("\nOrderan telah selesai! Terima kasih sudah mencuci di Qoombah!")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

### membaca keys dan value
# Tampilkan semua key
# print("Keys:", tabel_order.keys())

# Tampilkan semua value
# print("Values:", tabel_order.values())

# Tampilkan key dan value
# for key, value in tabel_order.items():
#    print(f"{key}: {value}")
    
# =======================
### CREATE

def tampilkan_cuci():
    print("\nDaftar Menu:")
    print(tabulate(tabel_cuci, headers="keys", tablefmt="grid"))

def tampilkan_price():
    print("\nDaftar Price:")
    print(tabulate(tabel_price, headers="keys", tablefmt="grid"))

def tampilkan_order():
    print("\nDaftar Order:")
    print(tabulate(tabel_order, headers="keys", tablefmt="grid"))

def tambah_order():
    print("\nMenambah Data Order")
    nama = (input("Masukkan nama baru: ")).capitalize()
    telp = (input("Masukkan nomer telepon: ")).lower()
    alamat = (input("Masukkan alamat rumah: ")).lower()
    jarak = (input("Masukkan jarak rumah: "))
    jenis = (input("Masukkan jenis mobil: ")).lower()
    warna = (input("Masukkan warna mobil: ")).lower()
    nopol = (input("Masukkan nomor polisi kendaraan: ")).lower()
    menu = (input("Masukkan pilihan menu cuci: ")).lower()
    jadwal = (input("Masukkan pilihan hari order: ")).capitalize()

    print(f"\nOrder '{nama}' berhasil ditambahkan!")
    print(f'\n=== Konfirmasi Order Qoombah Baru ===')
    print(f'\nnama: {nama}')
    print(f'telp: {telp}')
    print(f'alamat: {alamat}')
    print(f'jarak: {jarak}')
    print(f'jenis: {jenis}')
    print(f'warna: {warna}')
    print(f'nopol: {nopol}')
    print(f'menu: {menu}')
    print(f'jadwal: {jadwal}')

    konfirmasi = input("\nApakah data sudah benar? (y/n) : ")

while True:
    daftar_tanya = [
    print("\n===== Selamat Datang di Qoombah ====="),
    print("\nList Menu:"),
    print("\n1. Menampilkan Menu Cuci"),
    print("2. Menampilkan Menu Pricelist"),
    print("3. Menampilkan Jadwal Orderan Hari Ini"),
    print("4. Menambah Order"),
    print("5. Exit Program")
    ]

    pilihan = input("Masukkan angka menu yang ingin dijalankan: ")

    if pilihan == "1":
        tampilkan_cuci()
    elif pilihan == "2":
        tampilkan_price()
    elif pilihan == "3":
        tampilkan_order()
    elif pilihan == "4":
        tambah_order()
    elif pilihan == "5":
        print("\nOrderan telah selesai! Terima kasih sudah mencuci di Qoombah!")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
# =======================
### UPDATE
while True:
    daftar_tanya = [
    print("\n===== Selamat Datang di Qoombah ====="),
    print("\nList Menu:"),
    print("\n1. Menampilkan Menu Cuci"),
    print("2. Menampilkan Menu Pricelist"),
    print("3. Menampilkan Jadwal Orderan Hari Ini"),
    print("4. Menambah Order"),
    print("5. Exit Program")
    ]

    pilihan = input("Masukkan angka menu yang ingin dijalankan: ")

    if pilihan == "1":
        tampilkan_cuci()
    elif pilihan == "2":
        tampilkan_price()
    elif pilihan == "3":
        tampilkan_order()
    elif pilihan == "4":
        tambah_order()
    elif pilihan == "5":
        print("\nOrderan telah selesai! Terima kasih sudah mencuci di Qoombah!")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

### mengupdate nilai key yang sudah ada
# tabel_cuci.update({"menu": "promo cuci"})
# print(tabel_cuci)

### menambahkan keys baru
# tabel_order["sabun"] = "scholab"
# print(tabel_order)

### mengupdate beberapa keys sekaligus
# tabel_price.update ({
#    "ukuran": "all size",
#    "harga": "seikhlasnya",
#    "menu": "promo cuci"
# })
#print(tabel_price)

# =======================
### DELETE
while True:
    daftar_tanya = [
    print("\n===== Selamat Datang di Qoombah ====="),
    print("\nList Menu:"),
    print("\n1. Menampilkan Menu Cuci"),
    print("2. Menampilkan Menu Pricelist"),
    print("3. Menampilkan Jadwal Orderan Hari Ini"),
    print("4. Menambah Order"),
    print("5. Exit Program")
    ]

    pilihan = input("Masukkan angka menu yang ingin dijalankan: ")

    if pilihan == "1":
        tampilkan_cuci()
    elif pilihan == "2":
        tampilkan_price()
    elif pilihan == "3":
        tampilkan_order()
    elif pilihan == "4":
        tambah_order()
    elif pilihan == "5":
        print("\nOrderan telah selesai! Terima kasih sudah mencuci di Qoombah!")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

### menghapus 1 item berdasarkan keys
# del tabel_order["nama"]

### menghapus semua data dari dict
# tabel_order.clear()
# print(tabel_order)

### menghapus beberapa keys sekaligus
# for key in ["nama", "warna"]:
# data.pop(key, None)
# print(tabel_order)
