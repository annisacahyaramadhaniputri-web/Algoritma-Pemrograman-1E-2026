# masukkan input jenis tiket
n = input("masukkan jenis tiket")
# masukkan perulangan jumlah tiket nya serta harga masing masing jenis tiket
for i in range (1, n + 1):
    print("masukkan jumlah tiket", i)
    if n == "regular":
        harga_tiket = 40000
    elif n == "VIP":
        harga_tiket = 75000
    elif n == "VVIP":
        harga_tiket = 100000
    else:
        print("maaf tiket tidak tersedia")
        continue
# masukkan input dari ratisan yang diminta
    if harga_tiket == 40000:
        input("apakah kamu mau minuman seharga 10.000?(y/n)")
    if harga_tiket == 75000:
        input("selamat kamu mendapat minuman gratis")
    if harga_tiket == 100000:
        input("selamat kamu mendapat minuman gratis")
    else:
        print("maaf ya")
# cantumkan keeluruhan tiket yang di beli
input("apakah anda memiliki member card?")