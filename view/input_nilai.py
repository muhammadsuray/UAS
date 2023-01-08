def input_data(data):
    # buat inputan untuk mengisi nama
    nama = input("Masukkan Nama : ")
    while len(nama) < 3:
        nama = input("Masukkan Nama : ")
    
    # jika nim yang di input tersedia pada variabel data, cetak pesan lalu lakukan input ulang
    while nama in data['nama']:
        print("Mahasiswa dengan nama yang sama sudah ada")
        nama = input("Masukkan Nama : ")
    
    nilai = input("masukkan nilai : ")
    while not nilai.isnumeric():
        nilai = input("masukkan nilai : ")
    
    data['nama'].append(nama)
    data['nilai'].append(int(nilai))
    print("Data Berhasil Ditambah!!")
    return data