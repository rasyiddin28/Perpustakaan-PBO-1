import sqlite3
import datetime

databaseName = "Perpus.db" 

#koneksi database
conn = sqlite3.connect(databaseName)

#membuat tabel
conn.execute(
    "CREATE TABLE IF NOT EXISTS Pegawai (IdPegawai int primary key, Nama text, NoTelepon int, Alamat text)"
)
conn.execute(
    "CREATE TABLE IF NOT EXISTS Anggota (IdAnggota int primary key, Nama text, NoTelepon int, Alamat text)"
)
conn.execute(
    "CREATE TABLE IF NOT EXISTS Buku (IdBuku int primary key, Judul text, Penulis text, Kategori text)"
)
conn.execute(
    "CREATE TABLE IF NOT EXISTS Peminjaman (IdPeminjaman int primary key, IdBuku int, IdAnggota int, IdPegawai int, Status text, TanggalKembali text)"
)

#menutup koneksi
conn.close

class Person :
    def __init__(self, Nama, NoTelepon, Alamat) :
        self.Nama = Nama
        self.NoTelepon = NoTelepon
        self.Alamat = Alamat
    #getter
    def get_Nama(self): 
        return self.Nama
    def get_NoTelepon(self):
        return self.NoTelepon
    def get_Alamat(self):
        return self.Alamat 

class Pegawai (Person) :
    def __init__(self, IdPegawai,Nama, NoTelepon, Alamat) :
        super().__init__(Nama, NoTelepon, Alamat)
        self.IdPegawai = IdPegawai
    #getter
    def get_IdPegawai(self) :
        return self.IdPegawai
    def TambahPegawai(self):
        tambah = "Y"
        while tambah != "N" :
            print ("------ Menambahkan Pegawai------")
            Pegawai1 = Pegawai((input("Masukan Id Pegawai : ")),(input("Masukan Nama Pegawai : ")),(input("Masukan NoTelepon Pegawai : ")),(input("Masukan Alamat Pegawai : ")))
            conn.execute("insert into Pegawai values (?,?,?,?)", (Pegawai1.get_IdPegawai(), Pegawai1.get_Nama(), Pegawai1.get_NoTelepon(), Pegawai1.get_Alamat()))
            conn.commit()
            print("Pegawai bernama ",Pegawai1.Nama, "Telah Ditambahkan")
            tambah = input ("Apakah ingin menambahkan Pegawai lagi ? Y/N : ")
        else :
            print ("Terimakasih")

class Anggota (Person) :
    def __init__(self, IdAnggota,Nama, NoTelepon, Alamat) :
        super().__init__(Nama, NoTelepon, Alamat)
        self.IdAnggota = IdAnggota
    def get_IdAnggota(self):
        return self.IdAnggota
    def TambahAnggota(self):
        tambah = "Y"
        while tambah != "N" :
            print ("------ Menambahkan Anggota------")
            Anggota1 = Anggota((input("Masukan Id Anggota : ")),(input("Masukan Nama Anggota : ")),(input("Masukan NoTelepon Anggota : ")),(input("Masukan Alamat Anggota : ")))
            conn.execute("insert into Anggota values (?,?,?,?)", (Anggota1.get_IdAnggota(), Anggota1.get_Nama(), Anggota1.get_NoTelepon(), Anggota1.get_Alamat()))
            conn.commit()
            print("Anggota bernama ",Anggota1.Nama, "Telah Ditambahkan")
            tambah = input ("Apakah ingin menambahkan Anggota lagi ? Y/N : ")
        else :
            print ("Terimakasih")

class Buku : 
    def __init__(self, IdBuku, Judul, Penulis, Kategori, Jumlah) :
        self.IdBuku = IdBuku
        self.Judul = Judul
        self.Penulis = Penulis
        self.Kategori = Kategori
        self.Jumlah = Jumlah

    def get_IdBuku(self):
        return self.IdBuku
    def get_Judul(self):
        return self.Judul
    def get_Penulis(self):
        return self.Penulis
    def get_Kategori(self):
        return self.Kategori
    def get_Jumlah(self):
        return self.Jumlah

    def TambahBuku(self):
        tambah = "Y"
        while tambah != "N" :
            print ("------ Menambahkan Buku------")
            Buku1 = Buku((input("Masukan Id Buku : ")),(input("Masukan Judul Buku : ")),(input("Masukan Penulis Buku : ")),(input("Masukan Kategori Buku : ")),(input("Masukan Jumlah Stok Buku : ")))
            conn.execute("insert into Buku values (?,?,?,?,?)", (Buku1.get_IdBuku(), Buku1.get_Judul(), Buku1.get_Penulis(), Buku1.get_Kategori(), Buku1.get_Jumlah()))
            conn.commit()
            print("Buku berjudul ", Buku1.Judul, "Telah Ditambahkan")
            tambah = input ("Apakah ingin menambahkan buku lagi ? Y/N : ")
        else :
            print ("Terimakasih")
    
    def SearchByKategori (self):
        keyword = input ("Masukkan Kata Kunci Kategori : ")
        cursor = conn.cursor().execute("select * from Buku where Kategori = ?", (keyword, ))
        for row in cursor :
            print (f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}')

class Peminjaman :
    def __init__(self, IdPeminjaman, IdBuku, IdAnggota, IdPegawai, Status):
        self.IdPeminjaman = IdPeminjaman
        self.IdBuku = IdBuku
        self.IdAnggota = IdAnggota
        self.IdPegawai = IdPegawai
        self.Status = Status
    def CatatPeminjaman(self):
        tambah = "Y"
        while tambah != "N" :
            print ("------ Menambahkan Data Peminjaman------")
            Peminjaman1 = Peminjaman((input("Masukan Id Peminjaman : ")),(input("Masukan Id Buku : ")),(input("Masukan Id Anggota : ")),(input("Masukan Id Pegawai : ")),"Belum Selesai")
            #Mengurangi Stok Buku di Tabel Buku
            conn.execute("""UPDATE Buku 
            SET Jumlah = Jumlah-1 
            WHERE IdBuku = ?""",(Peminjaman1.IdPeminjaman, ))
            #memasukkan data ke database
            conn.execute("insert into Peminjaman values (?,?,?,?,?,?)", (Peminjaman1.IdPeminjaman, Peminjaman1.IdBuku, Peminjaman1.IdAnggota, Peminjaman1.IdPegawai, "Belum Selesai",(datetime.datetime.now() + datetime.timedelta(days=7)) ))
            conn.commit()
            print("Peminjaman dengan ID ", Peminjaman1.IdPeminjaman, "Telah Ditambahkan")
            tambah = input ("Apakah ingin menambahkan data Peminjaman lagi ? Y/N : ")
        else :
            print ("Terimakasih")
    def CatatPengembalian(self) :
        idP = input ("Masukkan Id Peminjaman yang akan diubah statusnya : ")
        #Mengubah Status Peminjaman
        conn.execute ("""UPDATE Peminjaman 
        SET Status='Selesai' 
        WHERE IdPeminjaman=?""",(idP, ))
        #Menambah Ulang Stok Buku
        conn.execute("""UPDATE Buku 
        SET Jumlah = Jumlah+1
        WHERE IdPeminjaman=?""",(idP, ))
        conn.commit()


def menu():

    print (""" ---Selamat Datang---
    Masukkan angka dari menu yang anda pilih :
    1. Menambah Data Buku
    2. Mencari Buku Berdasarkan Kategori
    3. Menambah Data Anggota
    4. Menambah Data Pegawai
    5. Mencatat Peminjaman
    6. Mencatat Pengembalian
    7. Exit Program""")
    
    user_input = 0

    while user_input != 7:

        user_input = int(input("Masukan Angka "))

        if user_input == 1:
            Buku.TambahBuku(Buku)

        elif user_input == 2:
            Buku.SearchByKategori(Buku)

        elif user_input == 3:
            Anggota.TambahAnggota(Anggota)

        elif user_input == 4:
            Pegawai.TambahPegawai(Pegawai)

        elif user_input == 5:
            Peminjaman.CatatPeminjaman(Peminjaman)

        elif user_input == 6:
            Peminjaman.CatatPengembalian(Peminjaman)
        
        elif user_input == 7:
            print("Semoga Harimu menyenangkan")

if __name__ == "__main__":
    menu()