"""
=== USE CASE: SISTEM TOKO ONLINE SEDERHANA ===

Contoh nyata penggunaan function untuk membangun fitur toko online.
Mendemonstrasikan:
    - Function untuk setiap fitur (product, cart, order)
    - Cross function calls antar fitur
    - Data management dengan function
    - Error handling dalam function
"""


# ============================================================
# DATA PRODUK
# ============================================================

PRODUK = [
    {"id": "P001", "nama": "Laptop ASUS", "harga": 8500000, "stok": 10, "kategori": "Elektronik"},
    {"id": "P002", "nama": "Mouse Logitech", "harga": 350000, "stok": 50, "kategori": "Elektronik"},
    {"id": "P003", "nama": "Keyboard Mechanical", "harga": 750000, "stok": 30, "kategori": "Elektronik"},
    {"id": "P004", "nama": "Buku Python", "harga": 120000, "stok": 100, "kategori": "Buku"},
    {"id": "P005", "nama": "Buku JavaScript", "harga": 95000, "stok": 80, "kategori": "Buku"},
    {"id": "P006", "nama": "Tas Ransel", "harga": 450000, "stok": 25, "kategori": "Fashion"},
    {"id": "P007", "nama": "Headset Gaming", "harga": 550000, "stok": 0, "kategori": "Elektronik"},
]

keranjang = []
riwayat_order = []


# ============================================================
# FUNCTION: FORMAT & DISPLAY
# ============================================================

def format_rupiah(angka):
    return f"Rp{angka:,.0f}"


def cetak_garis(char="─", panjang=65):
    print(f"  {char * panjang}")


def cetak_header(judul):
    print(f"\n  ╔{'═' * 63}╗")
    print(f"  ║ {judul:<62}║")
    print(f"  ╚{'═' * 63}╝")


# ============================================================
# FUNCTION: PRODUK
# ============================================================

def tampilkan_katalog(kategori=None):
    """Tampilkan daftar produk. Bisa difilter berdasarkan kategori."""
    cetak_header("KATALOG PRODUK" + (f" - {kategori}" if kategori else ""))

    data = PRODUK if not kategori else [p for p in PRODUK if p["kategori"] == kategori]

    print(f"  {'ID':<6} {'Nama':<25} {'Harga':>12} {'Stok':>6} {'Status':<10}")
    cetak_garis()

    for p in data:
        status = "Tersedia" if p["stok"] > 0 else "Habis"
        print(f"  {p['id']:<6} {p['nama']:<25} {format_rupiah(p['harga']):>12} {p['stok']:>6} {status:<10}")

    return data


def cari_produk(product_id):
    """Cari produk berdasarkan ID."""
    for p in PRODUK:
        if p["id"] == product_id:
            return p
    return None


def cek_stok(product_id, qty):
    """Cek apakah stok cukup."""
    produk = cari_produk(product_id)
    if not produk:
        return False, "Produk tidak ditemukan"
    if produk["stok"] < qty:
        return False, f"Stok tidak cukup (tersisa: {produk['stok']})"
    return True, "Stok tersedia"


def kurangi_stok(product_id, qty):
    """Kurangi stok produk."""
    produk = cari_produk(product_id)
    if produk:
        produk["stok"] -= qty
        return True
    return False


def get_kategori():
    """Ambil daftar kategori unik."""
    return sorted(set(p["kategori"] for p in PRODUK))


# ============================================================
# FUNCTION: KERANJANG BELANJA
# ============================================================

def tambah_ke_keranjang(product_id, qty=1):
    """Tambah produk ke keranjang."""
    produk = cari_produk(product_id)
    if not produk:
        print(f"  ❌ Produk {product_id} tidak ditemukan")
        return False

    tersedia, pesan = cek_stok(product_id, qty)
    if not tersedia:
        print(f"  ❌ {pesan}")
        return False

    # Cek apakah sudah ada di keranjang
    for item in keranjang:
        if item["product_id"] == product_id:
            item["qty"] += qty
            print(f"  ✅ {produk['nama']} qty ditambah menjadi {item['qty']}")
            return True

    keranjang.append({
        "product_id": product_id,
        "nama": produk["nama"],
        "harga": produk["harga"],
        "qty": qty,
    })
    print(f"  ✅ {produk['nama']} x{qty} ditambahkan ke keranjang")
    return True


def hapus_dari_keranjang(product_id):
    """Hapus produk dari keranjang."""
    for i, item in enumerate(keranjang):
        if item["product_id"] == product_id:
            dihapus = keranjang.pop(i)
            print(f"  ✅ {dihapus['nama']} dihapus dari keranjang")
            return True
    print(f"  ❌ Produk tidak ada di keranjang")
    return False


def ubah_qty_keranjang(product_id, qty_baru):
    """Ubah qty produk di keranjang."""
    if qty_baru <= 0:
        return hapus_dari_keranjang(product_id)

    for item in keranjang:
        if item["product_id"] == product_id:
            tersedia, pesan = cek_stok(product_id, qty_baru)
            if not tersedia:
                print(f"  ❌ {pesan}")
                return False
            item["qty"] = qty_baru
            print(f"  ✅ {item['nama']} qty diubah menjadi {qty_baru}")
            return True
    print(f"  ❌ Produk tidak ada di keranjang")
    return False


def hitung_subtotal_item(item):
    """Hitung subtotal satu item."""
    return item["harga"] * item["qty"]


def hitung_total_keranjang():
    """Hitung total semua item di keranjang."""
    return sum(hitung_subtotal_item(item) for item in keranjang)


def tampilkan_keranjang():
    """Tampilkan isi keranjang."""
    cetak_header("KERANJANG BELANJA")

    if not keranjang:
        print("  (Keranjang kosong)")
        return 0

    print(f"  {'Nama':<25} {'Harga':>12} {'Qty':>5} {'Subtotal':>14}")
    cetak_garis()

    for item in keranjang:
        subtotal = hitung_subtotal_item(item)
        print(f"  {item['nama']:<25} {format_rupiah(item['harga']):>12} {item['qty']:>5} {format_rupiah(subtotal):>14}")

    total = hitung_total_keranjang()
    cetak_garis()
    print(f"  {'TOTAL':<25} {'':>12} {'':>5} {format_rupiah(total):>14}")
    return total


# ============================================================
# FUNCTION: DISKON & PROMO
# ============================================================

def hitung_diskon(total, kode_promo=None):
    """Hitung diskon berdasarkan total dan kode promo."""
    diskon = 0

    # Diskon berdasarkan total belanja
    if total >= 5000000:
        diskon = 10
    elif total >= 1000000:
        diskon = 5

    # Diskon tambahan dari kode promo
    promo = {
        "HEMAT10": 10,
        "DISKON20": 20,
        "NEWUSER": 15,
    }
    if kode_promo and kode_promo in promo:
        diskon += promo[kode_promo]

    # Max diskon 30%
    diskon = min(diskon, 30)

    return diskon


def hitung_ongkir(total, kota="Jakarta"):
    """Hitung ongkos kirim."""
    tarif = {
        "Jakarta": 10000,
        "Bandung": 15000,
        "Surabaya": 25000,
        "Bali": 35000,
    }
    ongkir = tarif.get(kota, 30000)

    # Free ongkir untuk belanja di atas 500rb
    if total >= 500000:
        return 0
    return ongkir


# ============================================================
# FUNCTION: CHECKOUT & ORDER
# ============================================================

def checkout(kode_promo=None, kota="Jakarta"):
    """Proses checkout."""
    cetak_header("CHECKOUT")

    if not keranjang:
        print("  ❌ Keranjang kosong!")
        return None

    # Hitung total
    subtotal = hitung_total_keranjang()
    diskon_persen = hitung_diskon(subtotal, kode_promo)
    diskon_nominal = int(subtotal * diskon_persen / 100)
    setelah_diskon = subtotal - diskon_nominal
    ongkir = hitung_ongkir(subtotal, kota)
    grand_total = setelah_diskon + ongkir

    # Tampilkan ringkasan
    print(f"  Subtotal:     {format_rupiah(subtotal)}")
    if kode_promo:
        print(f"  Kode Promo:   {kode_promo}")
    print(f"  Diskon:       {diskon_persen}% (-{format_rupiah(diskon_nominal)})")
    print(f"  Ongkir ({kota}): {format_rupiah(ongkir)}" + (" (FREE!)" if ongkir == 0 else ""))
    cetak_garis()
    print(f"  GRAND TOTAL:  {format_rupiah(grand_total)}")

    return {
        "subtotal": subtotal,
        "diskon_persen": diskon_persen,
        "diskon_nominal": diskon_nominal,
        "ongkir": ongkir,
        "grand_total": grand_total,
        "kota": kota,
    }


def proses_order(checkout_data):
    """Finalisasi order: kurangi stok, simpan riwayat, kosongkan keranjang."""
    if not checkout_data:
        return None

    # Kurangi stok
    for item in keranjang:
        kurangi_stok(item["product_id"], item["qty"])

    # Buat order
    order_id = f"ORD-{len(riwayat_order) + 1:04d}"
    order = {
        "order_id": order_id,
        "items": keranjang.copy(),
        **checkout_data,
    }
    riwayat_order.append(order)

    # Kosongkan keranjang
    keranjang.clear()

    cetak_header(f"ORDER BERHASIL - {order_id}")
    print(f"  Order ID:     {order_id}")
    print(f"  Total Item:   {sum(i['qty'] for i in order['items'])}")
    print(f"  Grand Total:  {format_rupiah(order['grand_total'])}")
    print(f"  Kirim ke:     {order['kota']}")

    return order


def tampilkan_riwayat():
    """Tampilkan riwayat order."""
    cetak_header("RIWAYAT ORDER")

    if not riwayat_order:
        print("  (Belum ada order)")
        return

    for order in riwayat_order:
        print(f"  {order['order_id']} | {format_rupiah(order['grand_total']):>14} | {order['kota']}")
        for item in order["items"]:
            print(f"    - {item['nama']} x{item['qty']}")
        cetak_garis()


# ============================================================
# DEMO: Simulasi Belanja
# ============================================================

print("🛒 SIMULASI TOKO ONLINE")
print("=" * 70)

# 1. Lihat katalog
tampilkan_katalog()

# 2. Lihat kategori
print(f"\n  Kategori tersedia: {get_kategori()}")

# 3. Filter katalog
tampilkan_katalog("Elektronik")

# 4. Tambah ke keranjang
print("\n  --- Menambah ke keranjang ---")
tambah_ke_keranjang("P001", 1)     # Laptop
tambah_ke_keranjang("P002", 2)     # Mouse x2
tambah_ke_keranjang("P004", 3)     # Buku Python x3
tambah_ke_keranjang("P007", 1)     # Headset (stok 0)

# 5. Tampilkan keranjang
tampilkan_keranjang()

# 6. Ubah qty
print("\n  --- Mengubah qty ---")
ubah_qty_keranjang("P002", 1)      # Mouse jadi 1

# 7. Hapus item
print("\n  --- Menghapus item ---")
hapus_dari_keranjang("P004")       # Hapus buku

# 8. Tambah lagi
print("\n  --- Menambah item baru ---")
tambah_ke_keranjang("P003", 1)     # Keyboard
tambah_ke_keranjang("P006", 1)     # Tas

# 9. Lihat keranjang final
tampilkan_keranjang()

# 10. Checkout
checkout_data = checkout(kode_promo="HEMAT10", kota="Bandung")

# 11. Proses order
order = proses_order(checkout_data)

# 12. Cek stok setelah order
print("\n  --- Stok setelah order ---")
for pid in ["P001", "P002", "P003", "P006"]:
    p = cari_produk(pid)
    print(f"  {p['nama']:<25} stok: {p['stok']}")

# 13. Order ke-2
print("\n  --- Order ke-2 ---")
tambah_ke_keranjang("P005", 2)
tampilkan_keranjang()
checkout_data2 = checkout(kota="Surabaya")
proses_order(checkout_data2)

# 14. Riwayat
tampilkan_riwayat()

print()
print("=" * 70)
print("Selesai! Use case toko online sudah dicontohkan.")
