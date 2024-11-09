from prettytable import PrettyTable
import json
import pwinput


#memuat daan menyimpan akun pengguna
json_path = r"D:\Vscode\Penilaian Akhir S1\Ngetest\db_pengguna.json"
def memuat_data(json_path):
    try:
        with open(json_path, "r") as databasep:
            data_pengguna=json.load(databasep)
    except FileNotFoundError:
        data_pengguna={}
    return data_pengguna
def simpan_data(json_path, data_pengguna):
    with open(json_path, "w") as databasep :
        json.dump(data_pengguna,databasep, indent =4)

#memuat akun admin
json_path2 = r"D:\Vscode\Penilaian Akhir S1\Ngetest\db_admin.json"
with open(json_path2, "r") as databasea:
    data_admin=json.load(databasea)

#memuat dan menyimpan konser
json_path3 = r"D:\Vscode\Penilaian Akhir S1\Ngetest\db_konser.json"
def memuat_data(json_path3):
    with open(json_path3, "r") as databasek:
        data_konser = json.load(databasek)
    return data_konser
def simpan_data(json_path3, data_konser):
    with open(json_path3, "w") as databasek:
        json.dump(data_konser, databasek, indent=4)

#prettytable
def tampilkan_tabel(data_konser):
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Guest Star", "Jadwal", "Harga"]
    for konser_id, data_konser_item in data_konser["konser"].items():
        jadwal = f"{data_konser_item['tanggal']} {data_konser_item['bulan']} {data_konser_item['tahun']}"
        tabel.add_row([konser_id, data_konser_item["gs"], jadwal, f"Rp.{data_konser_item['harga']}"])
    return tabel

#untuk shorting data konsernya
def update_table(data_konser, kriteria):  
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Guest Star", "Jadwal", "Harga"]
    if kriteria == "harga1": 
        sorted_konser = sorted(data_konser["konser"].items(), key=lambda x: int(x[1]["harga"])) 
    elif kriteria == "harga2": sorted_konser = sorted(data_konser["konser"].items(), key=lambda x: int(x[1]["harga"]), reverse=True)
    else: 
        raise ValueError("Kriteria tidak dikenal")
    for konser_id, data_konser_item in sorted_konser:
        jadwal = f"{data_konser_item['tanggal']} {data_konser_item['bulan']} {data_konser_item['tahun']}"
        tabel.add_row([konser_id, data_konser_item["gs"], jadwal, f"Rp.{data_konser_item['harga']}"])
    print(tabel)


#pilih role
def pilih_role():
    while True:
        try:
            print(f"\n{"="*5} SILAHKAN PILIH ROLE {"="*5}")
            print("[1]. Admin")
            print("[2]. Pengguna")
            print("[3]. Pengunjung ")
            print("[4]. Keluar")
            role = input("Masukkan pilihan = ")
            if role == "1" :
                login_admin()
            elif role == "2":
                pengguna()
            elif role == "3":
                pengunjung()
            elif role == "4":
                print("\n====== ***** SELAMAT TINGGAL DAN TERIMA KASIH ***** ======")
                exit()
            else :
                print("Pilihan tidak tersedia.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C Secara bersamaan!")

#login admin
def login_admin():
    while True :
        try:
            print(f"\n{"="*5} LOGIN ADMIN {"="*5}")
            nama = input("Username = ")
            pw = pwinput.pwinput("Password = ")
            if nama in data_admin and data_admin[nama]==pw:
                menu_admin()
            elif nama in data_admin and data_admin[nama]!=pw:
                print("Password salah!")
                while True :
                    try:
                        kl = input("apakah anda ingin kembali atau lanjut?(kembali/lanjut) = ").lower()
                        if kl == "kembali":
                            pilih_role()
                        elif kl == "lanjut":
                            break
                        else :
                            print("Input tidak sesuai!")
                    except KeyboardInterrupt:
                        print("\nJangan menekan CTRL dan C secara bersamaan!")
            else :
                print("Nama pengguna tidak tersedia.")
                while True :
                    try:
                        kl = input("apakah anda ingin kembali atau lanjut?(kembali/lanjut) = ").lower()
                        if kl == "kembali":
                            pilih_role()
                        elif kl == "lanjut":
                            break
                        else :
                            print("Input tidak sesuai!")
                    except KeyboardInterrupt:
                        print("\nJangan menekan CTRL dan C secara bersamaan!")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#menu admin
def menu_admin():
    while True :
        try:
            print(f"\n{"="*5} MENU ADMIN {"="*5}")
            print("[1]. Lihat Event Konser")
            print("[2]. Tambah Event Konser")
            print("[3]. Perbarui Event Konser")
            print("[4]. Hapus Event Konser")
            print("[5]. Logout")
            pilih = input("Masukkan pilihan = ")
            if  pilih == "1" :
                lihat_konser()
            elif pilih == "2":
                tambah_konser()
            elif pilih == "3":
                perbarui_konser()
            elif pilih == "4":
                hapus_konser()
            elif pilih == "5":
                pilih_role()
            else :
                print("Pilihan tidak tersedia.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#lihat konser admin
def lihat_konser():
    print(f"\n{'='*21} LIST KONSER {'='*21}")
    data_konser = memuat_data(json_path3)
    print(tampilkan_tabel(data_konser))
    while True:
        try:
            print(f"\n{"="*5} PILIH KRITERIA SHORTING {"="*5}")
            print("[1]. Harga terendah ke tertinggi")
            print("[2]. Harga tetinggi ke terendah")
            print("[3]. Kembali")
            pilihan = input("Masukkan nomor pilihan Anda = ").strip()
            if pilihan == "1":
                kriteria = "harga1"
                update_table(data_konser, kriteria)
            elif pilihan == "2":
                kriteria = "harga2"
                update_table(data_konser, kriteria)
            elif pilihan == "3":
                menu_admin()
            else:
                print("Pilihan tidak tersedia.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C Secara bersamaan!")

#Menambah konser
def tambah_konser():
    data_konser = memuat_data(json_path3)
    print(f"\n{"="*21} MENAMBAH KONSER {"="*21}")
    print(tampilkan_tabel(data_konser))
    while True:
        try:
            no = (input("masukan angka untuk ID (Contoh:002) = "))
            if no.isdigit() and 3<=len(no)<4 :
                no = no.zfill(3)
                id_konser = f"DRS{no}"
                if id_konser in data_konser["konser"]:
                    print("ID sudah digunakan.")
                else :
                    break
            else:
                print("Harus memasukan 3 angka")
        except ValueError: 
            print("Input harus angka.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")
    while True :
        try:
            gs = input("Masukkan Guest Star = ").strip().lower().capitalize()
            if 4 <= len(gs) <= 15:
                if not gs:
                    raise ValueError("Nama Guest Star tidak boleh kosong.")
                else :
                    break
            else:
                print("Nama harus antara 4 hingga 15 karakter.")
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")
    while True :
        try:
            tanggal = int(input("Masukkan tanggal (1-31) = "))
            if 0<tanggal<32:
                tanggal = str(tanggal)
                break
            else :
                print("Tanggal tidak sesuai.")
        except ValueError: 
            print("Input harus angka.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")
    while True :
        bulan = input("Masukkan bulan (Januari-Desember) = ").lower().capitalize()
        if bulan not in data_konser["bulan"]:
            print("Bulan tidak tersedia.")
        else :
            break
    while True :
        try:
            tahun = int(input("Masukkan tahun (2024-2030) = "))
            if 2024<=tahun<2031:
                tahun = str(tahun)
                break
            else :
                print("Tahun tidak sesuai.")
        except ValueError: 
            print("Input harus angka.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")
    while True :
        try:
            harga = int(input("Masukkan harga (minimal 50rb dan maksimal 1jt) = Rp."))
            if harga<50000:
                print("Harga terlalu rendah.")
            elif harga>1000000:
                print("Harga terlalu tinggi.")
            else :
                data_konser["konser"][id_konser] = {"gs": gs, "tanggal": tanggal, "bulan": bulan, "tahun": tahun, "harga":harga}
                simpan_data(json_path3, data_konser)
                print(f'Konser baru berhasil ditambahkan dengan ID {no}.')
                print(f"\n{"="*21} LIST KONSER {"="*21}")
                print(tampilkan_tabel(data_konser))
                break
        except ValueError: 
            print("Harap masukkan angka.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")
    while True :
        try:
            yt = input("Ingin menambah konser lagi(Ya/Tidak)? = ").lower()
            if yt == "ya":
                tambah_konser()
            elif yt == "tidak" :
                menu_admin()
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#Perbarui Konser
def perbarui_konser():
    data_konser = memuat_data(json_path3)
    print(f"\n{"="*21} MEMPERBARUI KONSER {"="*21}")
    print(tampilkan_tabel(data_konser))
    while True :
        try :
            id_konser = input("Masukkan ID konser yang ingin di ubah = ")
            if id_konser in data_konser["konser"]:
                while True:
                    try:
                        gs = input("Masukkan Guest Star = ").strip().lower().capitalize()
                        if 4 <= len(gs) <= 15:
                            if not gs:
                                raise ValueError("Nama Guest Star tidak boleh kosong.")
                            else :
                                break
                        else:
                            print("Nama harus antara 4 hingga 15 karakter.")
                    except KeyboardInterrupt:
                        print("\nJangan menekan CTRL dan C secara bersamaan!")
                while True :
                        try:
                            tanggal = (int(input("Masukkan tanggal(1-31) = ")))
                            if 0<tanggal<32:
                                tanggal = str(tanggal)
                                break
                            else :
                                print("tanggal tidak sesuai.")
                        except ValueError: 
                            print("Harap masukkan angka.")
                        except KeyboardInterrupt:
                            print("\nJangan menekan CTRL dan C secara bersamaan!")
                while True :
                    bulan = input("Masukkan bulan (Januari-Desember) = ").lower().capitalize()
                    if bulan not in data_konser["bulan"]:
                        print("Bulan tidak tersedia.")
                    else :
                        break
                while True :
                    try:
                        tahun = int(input ("Masukkan tahun(2024-2030) = "))
                        if 2024<=tahun<2031:
                            tahun = str(tahun)
                            break
                        else :
                            print("Tahun tidak sesuai.")
                    except ValueError: 
                        print("Harap masukkan angka.")
                    except KeyboardInterrupt:
                        print("\nJangan menekan CTRL dan C secara bersamaan!")
                while True :
                    try:
                        harga = int(input("Masukkan Harga (minimal 50rb dan maksimal 1jt) = "))
                        if harga<50000:
                            print("Harga terlalu rendah.")
                        elif harga>1000000:
                            print("Harga terlalu tinggi.")
                        else :
                            data_konser["konser"][id_konser] = {"gs": gs, "tanggal": tanggal, "bulan": bulan, "tahun": tahun, "harga": harga}
                            simpan_data(json_path3, data_konser)
                            print(f"Konser dengan ID {id_konser} berhasil diperbarui.")
                            print(f"\n{"="*21} LIST KONSER {"="*21}")
                            print(tampilkan_tabel(data_konser))
                            while True :
                                yt = input("ingin memperbarui konser lagi(Ya/Tidak)? = ").lower()
                                if yt == "ya":
                                    perbarui_konser()
                                elif yt == "tidak":
                                    menu_admin()
                    except ValueError:
                        print("Harap masukkan angka.")
                    except KeyboardInterrupt:
                        print("\nJangan menekan CTRL dan C secara bersamaan!")
            else :
                print("Nomor konser tidak ditemukan.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#hapus konser
def hapus_konser():
    data_konser = memuat_data(json_path3)
    print(f"\n{"="*21} HAPUS KONSER {"="*21}")
    print(tampilkan_tabel(data_konser))
    while True :
        try:
            id_konser = input("Masukkan nomor konser yang ingin dihapus = ")
            if id_konser in data_konser["konser"]:
                del data_konser["konser"][id_konser]
                simpan_data(json_path3, data_konser)
                print(f"Konser dengan ID {id_konser} berhasil dihapus.")
                print(f"\n{"="*21} LIST KONSER {"="*21}")
                print(tampilkan_tabel(data_konser))
                while True :
                    yt = input("Ingin menghapus konser lagi(Ya/Tidak)? = ").lower()
                    if yt == "ya":
                        hapus_konser()
                    elif yt == "tidak":
                        menu_admin()
            else:
                print("Nomor konser tidak ditemukan.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#pengguna
def pengguna():
    while True:
        try:
            print(f"\n{"="*5} PENGGUNA {"="*5}")
            print("[1]. Login")
            print("[2]. Daftar")
            print("[3]. Kembali")
            pilih = input("Masukkan pilihan = ")
            if  pilih == "1" :
                login_pengguna()
            elif pilih == "2":
                daftar_akun()
            elif pilih == "3":
                pilih_role()
            else :
                print("Pilihan tidak tersedia.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#login akun pengguna
def login_pengguna():
    data_pengguna = memuat_data(json_path)
    while True :
        try:
            print(f"\n{"="*5} LOGIN PENGGUNA {"="*5}")
            nama = input("Username = ")
            pw = pwinput.pwinput("Password = ")
            if nama in data_pengguna and data_pengguna[nama]["password"]==pw:
                menu_pengguna(nama)
            elif nama in data_pengguna and data_pengguna[nama]["password"]!=pw:
                print("Password Salah!")
                kembalilanjut()
            else :
                print("Nama pengguna tidak tersedia.")
                kembalilanjut()
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#daftar akun pengguna
def daftar_akun():
    data_pengguna = memuat_data(json_path)
    while True:
        print(f"\n{"="*5} DAFTAR AKUN {"="*5}")
        try:
            print("\nMasukan Username:")
            nama = input("Username (4-10 karakter) = ").strip()
            if 4 <= len(nama) <= 15:
                if not nama:
                    raise ValueError("Nama tidak boleh kosong.")
                elif nama in data_pengguna:
                    print("Username sudah digunakan.")
                else :
                    while True:
                        try:
                            print("\nMasukan Password anda:")
                            pw = input("Password =").strip()
                            if 4 <= len(pw):
                                if not pw:
                                    raise ValueError("Password tidak boleh kosong.")
                                else :
                                    data_pengguna[nama]={"password":pw, "saldo":0,"tiket":"kosong"}
                                    simpan_data(json_path, data_pengguna)
                                    print("Akun berhasil dibuat.")
                                    pengguna()
                            else:
                                print("Password minimal 4 karakter.")
                        except ValueError as e:
                            print(e)
                        except KeyboardInterrupt:
                            print("\nJangan menekan CTRL dan C secara bersamaan!")
            else:
                print("Nama harus antara 4 hingga 15 karakter.")
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#menu pengguna
def menu_pengguna(nama):
    data_pengguna = memuat_data(json_path)
    while True :
        try:
            print(f"\n{"="*5} MENU PENGGUNA {"="*5}")
            print("[1]. Lihat Event Konser")
            print("[2]. Beli Tiket Event Konser")
            print("[3]. Lihat Saldo E-Money")
            print("[4]. Lihat Tiket yang dibeli")
            print("[5]. Logout")
            pilih = input("Masukkan pilihan = ")
            if  pilih == "1" :
                lihat_konserp(nama)
            elif pilih == "2":
                if data_pengguna[nama]["tiket"] != "kosong":
                    print("\nMaaf anda sudah memiliki tiket")
                    print("Harap hapus tiket anda terlebih dahulu")
                    menu_pengguna(nama)
                else:
                    beli_tiket(nama)
            elif pilih == "3":
                cek_saldo(nama)
            elif pilih == "4":
                invoice(nama)
            elif pilih == "5":
                pengguna()
            else :
                print("Pilihan Tidak Tersedia.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

def lihat_konserp(nama):
    data_konser = memuat_data(json_path3)
    print(f"\n{'='*21} LIST KONSER {'='*21}")
    print(tampilkan_tabel(data_konser))
    while True:
        try:
            print(f"\n{"="*5} PILIH KRITERIA SHORTING {"="*5}")
            print("[1]. Harga terendah ke tertinggi")
            print("[2]. Harga tetinggi ke terendah")
            print("[3]. Kembali")
            pilihan = input("Masukkan nomor pilihan Anda = ").strip()
            if pilihan == "1":
                kriteria = "harga1"
                update_table(data_konser, kriteria)
            elif pilihan == "2":
                kriteria = "harga2"
                update_table(data_konser, kriteria)
            elif pilihan == "3":
                menu_pengguna(nama)
            else:
                print("Pilihan tidak tersedia.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C Secara bersamaan!")

#menu tiket
def beli_tiket(nama):
    data_konser = memuat_data(json_path3)
    data_pengguna = memuat_data(json_path)
    while True:
        try:
            print(f"\n{"="*5} BELI TIKET {"="*5}")
            id_konser = input("Masukkan nomor konser yang ingin dipilih = ")
            if id_konser in data_konser["konser"]:
                while True :
                    try:
                        banyak = int(input("Jumlah tiket yang ingin dibeli = "))
                        harga_tiket = data_konser["konser"][id_konser]["harga"]*banyak
                        print("\nKeterangan :")
                        print(f"Guest Star = {data_konser["konser"][id_konser]["gs"]}")
                        print(f"Rp.{data_konser["konser"][id_konser]["harga"]} X {banyak} = Rp.{harga_tiket}")
                        break
                    except ValueError: 
                        print("Harap masukkan angka.")
                    except KeyboardInterrupt:
                        print("\nJangan menekan CTRL dan C secara bersamaan!")
                while True :
                    try:
                        bayar = input("ingin lanjutkan pembayaran atau kembali ke menu(ya/kembali)? = ").strip().lower()
                        if bayar == "ya":
                            if data_pengguna[nama]["saldo"] >= harga_tiket:
                                data_pengguna[nama]["saldo"] -= harga_tiket
                                data_pengguna[nama]["tiket"] = {"gs":data_konser["konser"][id_konser]["gs"], "harga":data_konser["konser"][id_konser]["harga"], "jumlah":banyak, "total":harga_tiket}
                                simpan_data(json_path, data_pengguna)
                                print(f"\n{"="*5} PEMBELIAN BERHASIL {"="*5}")
                                print(f"Nama : {nama} ")
                                print(f"Guest Star :{data_konser["konser"][id_konser]["gs"]}")
                                print(f"Harga :Rp{data_konser["konser"][id_konser]["harga"]} x {banyak}")
                                print(f"Total :Rp.{harga_tiket}")
                                print("="*30)
                                menu_pengguna(nama)
                            else:
                                print("\nsaldo tidak cukup, silahkan melakukan pengisian.")
                                print("Proses pembayaran dibatalkan.")
                                menu_pengguna(nama)
                        elif bayar == "kembali":
                            print("Proses pembayaran dibatalkan.")
                            menu_pengguna(nama)
                        else :
                            print("Input tidak sesuai.")
                    except KeyboardInterrupt:
                        print("\nJangan menekan CTRL dan C secara bersamaan!")
            else: print("Nomor konser tidak valid.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#Cek saldo
def cek_saldo(nama):
    data_pengguna = memuat_data(json_path)
    while True:
        try:
            print(f"\n{"="*5} E-MONEY {"="*5}")
            print(f"Saldo Anda = Rp.{data_pengguna[nama]["saldo"]}")
            print("[1]. Top Up")
            print("[2]. Kembali")
            pilih = input("Masukkan pilihan = ")
            if  pilih == "1" :
                topup(nama)
            elif pilih == "2":
                menu_pengguna(nama)
            else :
                print("Pilihan tidak tersedia!")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#top up E-Money
def topup(nama):
    data_pengguna = memuat_data(json_path)
    while True :
        try:
            print(f"\n{"="*5} TOP UP {"="*5}")
            print("[1]. Rp.50.000")
            print("[2]. Rp.100.000")
            print("[3]. Nominal lain")
            print("[4]. Batalkan")
            pilih = input("Masukkan pilihan = ")
            if  pilih == "1" :
                data_pengguna[nama]["saldo"] = data_pengguna[nama]["saldo"] + 50000
                simpan_data(json_path, data_pengguna)
                print(f"\n{"="*5} TOP UP BERHASIL {"="*5}")
                print(f"Nama : {nama} ")
                print("Nominal : Rp.50000")
                print("="*27)
                cek_saldo(nama)
            elif pilih == "2":
                data_pengguna[nama]["saldo"] = data_pengguna[nama]["saldo"]+ 100000
                simpan_data(json_path, data_pengguna)
                print(f"\n{"="*5} TOP UP BERHASIL {"="*5}")
                print(f"Nama : {nama} ")
                print("Nominal : Rp.100000")
                print("="*27)
                cek_saldo(nama)
            elif pilih == "3":
                while True :
                    try:
                        print("minimal top up Rp.20000 dan maksimal Rp.2000000")
                        tambah = int(input("Nominal = Rp. "))
                        if tambah < 20000:
                            print("nominal terlalu kecil.")
                        elif tambah > 2000000:
                            print("nominal terlalu besar.")
                        else :
                            data_pengguna[nama]["saldo"] = data_pengguna[nama]["saldo"] + int(tambah)
                            simpan_data(json_path, data_pengguna)
                            print(f"\n{"="*5} TOP UP BERHASIL {"="*5}")
                            print(f"Nama : {nama} ")
                            print(f"Nominal :Rp.{tambah}")
                            print("="*27)
                            cek_saldo(nama)
                    except ValueError:
                        print("nominal tidak valid.")
                    except KeyboardInterrupt:
                        print("\nJangan menekan CTRL dan C secara bersamaan!")
            elif pilih == "4":
                cek_saldo(nama)
            else :
                print("Pilihan Tidak Tersedia.")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

def invoice(nama):
    data_pengguna = memuat_data(json_path)
    if data_pengguna[nama]["tiket"] == "kosong":
        print("\nAnda belum mempunyai tiket.")
        menu_pengguna(nama)
    else :
        data_pengguna = memuat_data(json_path)
        print(f"\n{"="*10} INVOICE {"="*10}")
        print(f"Nama : {nama} ")
        print(f"Guest Star :{data_pengguna[nama]["tiket"]["gs"]}")
        print(f"Harga :Rp{data_pengguna[nama]["tiket"]["harga"]} x {data_pengguna[nama]["tiket"]["jumlah"]}")
        print(f"Total :Rp.{data_pengguna[nama]["tiket"]["total"]}")
        print("="*29)
        while True:
            try:
                hapus = input("apakah anda ingin mengahapus tiket anda (ya/tidak) = ").lower()
                if hapus == "ya":
                    data_pengguna[nama]["tiket"] = "kosong"
                    simpan_data(json_path, data_pengguna)
                    menu_pengguna(nama)
                elif hapus == "tidak":
                    menu_pengguna(nama)
                else :
                    print("Input tidak sesuai.")
            except KeyboardInterrupt:
                print("\nJangan menekan CTRL dan C secara bersamaan!")
    
#pengunjung
def pengunjung():
    data_konser = memuat_data(json_path3)
    print(f"\n{'='*21}  MODE PENGUNJUNG {'='*21}")
    print(f"\n{'='*21}  LIHAT KONSER {'='*21}")
    print(tampilkan_tabel(data_konser))
    while True:
        try:
            kl = input("apakah anda ingin kembali atau login sebagai pengguna?(Kembali/login) = ").lower()
            if kl == "kembali" :
                pilih_role()
            elif kl == "login":
                pengguna()
            else :
                print("Input tidak sesuai!")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#Kembali atau lanjut
def kembalilanjut():
    while True :
        try:
            kl = input("apakah anda ingin kembali atau lanjut?(Kembali/lanjut) = ").lower()
            if kl == "kembali":
                pengguna()
            elif kl == "lanjut":
                break
            else :
                print("Input tidak sesuai!")
        except KeyboardInterrupt:
            print("\nJangan menekan CTRL dan C secara bersamaan!")

#tampilan awal program
def main():
    print("\n====== ***** SELAMAT DATANG DI CTICK.COM ***** ======")
    pilih_role()

#memulai program
main()