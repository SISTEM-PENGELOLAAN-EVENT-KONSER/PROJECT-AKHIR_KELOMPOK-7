# PROJECT_AKHIR_KELOMPOK_7

DWI PEBRIYANTO PRADANA 2409116012

ISRINA LUTFIAH 2409116003

MUHAMMAD SADIKIN SAMIR 2409116031

## TEMA : SISTEM PENGELOLAAN EVENT KONSER

# FLOWCHART

![MENU UTAMA-Page-1 (2)](https://github.com/user-attachments/assets/9018241b-e87c-427d-8cdb-6a1e7d72d6d5)

![MENU UTAMA-Page-2 (3)](https://github.com/user-attachments/assets/e6c233e0-f63c-43b0-80b5-a4b6b8013b3f)

![MENU UTAMA-Page-3 (3)](https://github.com/user-attachments/assets/b2840c5f-524d-4943-b3a9-17905cf99ec5)


# PENJELASAN OUTPUT

## Pilih Role

  ![image](https://github.com/user-attachments/assets/407de429-82b2-4138-8184-89b2be69830b)

  saat memulai Program user akan di ucapkan selamat datang,, kemudian diminta untuk menginput angka berapa untuk memlih role.

  - Admin dengan role ini user dapat melakukan Create, Read, Update, dan Delete (CRUD) pada sistem pengelolaan tiket event konser.
  - Pengguna dengan role ini user dapat membuat akun, melihat list konser, melakukan transaksi pembelian tiket, dan Top up E-Money.
  - Pengunjung dengan role ini user hanya dapat melihat list konser saja

### 1. Admin

  a. Menu login admin

  ![Screenshot 2024-11-07 215706](https://github.com/user-attachments/assets/0cd0b377-4af3-4c5d-a74d-007d746573b3)

  Apabila user menginput angka "1" maka akan masuk ke role admin dan diminta untuk memasukkan Username dan Password.

  b. Masuk ke menu admin

  ![Screenshot 2024-11-07 215723](https://github.com/user-attachments/assets/86234a4c-88b9-412a-968b-330b336c3cbb)

  Jika Username dan Password admin sesuai dengan yang ada pada database maka akan langsung masuk pada "MENU ADMIN".

  - Lihat event konser

  ![Screenshot 2024-11-08 235405](https://github.com/user-attachments/assets/8c2dee81-4f5e-40d4-9a65-5d6eba2065ed)

  Jika menginput "1" yaitu menu Lihat Event Konser, Maka List Konser yang berisi Guest Star, Jadwal, dan Harga per satu ticket akan ditampilkan. dan jika sudah ditampilkan maka ada menu sorting dari harga terendah ke tertinggi maupun sebaliknya.

![Screenshot 2024-11-08 235412](https://github.com/user-attachments/assets/54b6cc2e-8e43-401c-9c99-73889d117caf)

![Screenshot 2024-11-08 235417](https://github.com/user-attachments/assets/97ac2088-4867-4fc4-abe2-742adddacfd5)

  Jika meenginput "1" yaitu Harga terendah ke tertinggi, maka list konser akan di sorting sesuai dengan harga mulai dari terendah dan tertinggi ataupun sebaliknya jika menginput "2" yaitu Harga tertinggi ke terendah, maka akan disorting mulai dari harga tertinggi ke terendah.

  ![image](https://github.com/user-attachments/assets/84a7401b-7826-415c-ae21-d941cced2fda)

  Jika mengiput "3" yaitu kembali, maka admin akan kembali ke "MENU ADMIN".
  
  - Tambah event konser

  ![Screenshot 2024-11-08 235721](https://github.com/user-attachments/assets/f17312db-217f-4c2d-887d-359059bce8d7)

  Jika menginput "2" yaitu Tambah Event Konser, Maka Admin diminta untuk memasukkan ID, Guest Star, Tanggal, Bulan, Tahun, dan Harga per satu ticket.

  ![Screenshot 2024-11-08 235736](https://github.com/user-attachments/assets/f4852cc3-0942-4b61-935a-7d7e17bcb38b)

  Jika sudah maka konser yang baru saja ditambah akan otomatis masuk ke list konser.

  ![image](https://github.com/user-attachments/assets/9487ced9-2776-4cd6-97c3-fd127d7b6e77)

  Setelah list konser tertambahkan maka admin akan ditanya apakah ingin menambah konser lagi atau tidak, jika "Ya" maka akan mengulang proses menambah konser namun jika "Tidak admin akan kembali ke Menu Admin.

  - Perbarui event konser

  ![image](https://github.com/user-attachments/assets/42ecf5c3-a055-426a-99a0-a483ea4fb9a8)

  Jika menginput "3" yaitu Perbarui Event Konser, Maka pertama admin diminta untuk memasukkan angka berapa yang ada di list untuk memilih konser yang ingin diperbarui, setelah memasukkan angka selanjutnya admin memasukkan Guest Star, Tanggal, Bulan, Tahun, dan Harga per satu ticket.

  ![image](https://github.com/user-attachments/assets/3fef4d8f-d438-425a-98cc-a431af782b57)

  Setelah itu jika sudah maka list konser akan diperbarui sesuai input admin sebelumnnya.

  ![image](https://github.com/user-attachments/assets/12b647c3-eacb-4185-ab0e-42db21d0e2a8)

  Setelah itu admin ditanya apakah ingin memperbarui konser lagi atau tidak. Jika "Ya" maka akan mengulangi proses perbarui event konser, jika "Tidak" maka akan kembali ke "Menu Admin"

  - Hapus event konser

  ![Screenshot 2024-11-09 000737](https://github.com/user-attachments/assets/f767829f-802f-4c1e-b63c-0435f338af56)

  Jika menginput "4" yaitu Hapus Event Konser, Maka admin diminta memasukkan ID berapa pada list konser yang ingin dihapus.

  ![Screenshot 2024-11-09 000742](https://github.com/user-attachments/assets/2440d542-4802-486c-a780-20ed55314477)

  Setelah memasukkan angka berapa pada list konser yang ingin dihapus maka list konser sesuai angka yang diinput admin akan terhapus dari list konser.

  ![image](https://github.com/user-attachments/assets/941a4516-0400-451c-9295-47d9f9df33f3)

  Setelah list konser dihapuskan maka admin akan ditanya apakah ingin menghapus konser lagi atau tidak, jika "Ya" maka akan mengulang proses menghapus konser namun jika "Tidak admin akan kembali ke Menu Admin.


  - Logout

  ![image](https://github.com/user-attachments/assets/337fa398-1f95-4379-97df-bf959be846fc)

  ika menginput "5" yaitu Logout, maka admin akan logout atau keluar dari role admin dan akan kembali pada menu pilih role.


### 2. Pengguna

  #### a. Menu login pengguna

  ![Screenshot 2024-11-08 063458](https://github.com/user-attachments/assets/36d4b72a-cb52-470a-aca6-fe5e4111516d)

  Jika user menginput angka "2" maka akan akan masuk ke role pengguna dan diminta menginput angka berapa yang user ingin lakukan, apakah 1.Login, 2.Daftar, atau 3.Kembali.

  - Daftar akun

  ![Screenshot 2024-11-08 063538](https://github.com/user-attachments/assets/f1b4d78c-644b-405c-9d64-58b3a7197c30)

  Jika menginput angka "2" yaitu Daftar, Maka pengguna akan masuk ke menu "DAFTAR AKUN" dan pengguna diminta memasukkan username dan password yang mereka inginkan untuk membuat akun.

  ![Screenshot 2024-11-08 063543](https://github.com/user-attachments/assets/e3eb6307-5136-4c91-be2b-bdf44ec45b2f)

  Setelah username dan password yang ingin dibuat dimasukkan, maka akan muncul pemberitahuan bahwa Akun berhasil dibuat.


  - Login

  ![Screenshot 2024-11-08 074909](https://github.com/user-attachments/assets/bc540062-4f14-49d8-a748-2c6cdc52ff67)


  Jika menginput angka "1" yaitu Login, Maka pengguna diminta memasukkan username dan password pengguna.

  ##### a. Menu pengguna

  ![Screenshot 2024-11-08 074916](https://github.com/user-attachments/assets/40a18027-2d69-4b2a-bd82-e94ce947fdb9)

  Jika Username dan Password pengguna sudah sesuai dengan yang ada pada database maka akan langsung masuk pada "MENU PENGGUNA" dan pengguna dapat memasukkan angka berapa pada menu yang ingin dituju.

  - Lihat event konser

![image](https://github.com/user-attachments/assets/38499351-c1f2-4860-99ea-38ba5b25808d)

  Jika menginput "1" yaitu menu Lihat Event Konser, Maka List Konser yang berisi Guest Star, Jadwal, dan Harga per satu ticket akan ditampilkan. dan jika sudah ditampilkan maka ada menu sorting dari harga terendah ke tertinggi maupun sebaliknya.

![Screenshot 2024-11-08 235412](https://github.com/user-attachments/assets/54b6cc2e-8e43-401c-9c99-73889d117caf)

![Screenshot 2024-11-08 235417](https://github.com/user-attachments/assets/97ac2088-4867-4fc4-abe2-742adddacfd5)

  Jika meenginput "1" yaitu Harga terendah ke tertinggi, maka list konser akan di sorting sesuai dengan harga mulai dari terendah dan tertinggi ataupun sebaliknya jika menginput "2" yaitu Harga tertinggi ke terendah, maka akan disorting mulai dari harga tertinggi ke terendah.

  ![image](https://github.com/user-attachments/assets/84a7401b-7826-415c-ae21-d941cced2fda)

  Jika mengiput "3" yaitu kembali, maka admin akan kembali ke "MENU PENGGUNA".

  - Beli tiket event konser

![image](https://github.com/user-attachments/assets/847ab900-5e25-4198-a4f2-8ccb782fa787)

  Jika menginput angka "2" yaitu Beli Tiket Event Konser, Pengguna diminta memasukkan ID konser berapa yang ingin dibeli setelah itu diminta untuk memasukkan jumlah tiket yang ingin dibeli.

![image](https://github.com/user-attachments/assets/c1fb72a6-bea5-454f-84dd-7a1903fdc3cf)

  Setelah harga tiket dikali jumlah tiket yang ingin dibeli maka dihitung jumlah totalnya, dan pengguna ditanya apakah ingin melanjutkan pembayaran atau tidak.

![image](https://github.com/user-attachments/assets/d8f1bee3-e1b9-4eed-9b90-58780da717dc)

  Jika saldo cukup maka akan muncul invoice dari pembelian tiket konser.

![image](https://github.com/user-attachments/assets/398538ce-ef8f-40da-9cd4-0576e93623d4)

  Namun, jika saldo tidak cukup maka proses pembayaran akan dibatalkan dan pengguna diminta untuk melakukaan pengisian saldo.

  - Lihat saldo E-Money

  ![image](https://github.com/user-attachments/assets/df5a3bef-7804-4b23-9b3b-f1a00e8321c9)

  Jika menginput angka "3" yaitu Lihat Saldo E-Money, Maka akan masuk ke menu E-Money yang terdapat informasi jumlah saldo pengguna selain itu pengguna juga diminta memasukkan pilihan apakah ingin melakukan Top up atau kembali.

  ![image](https://github.com/user-attachments/assets/63fbe7ed-6d19-4c8d-9fba-7886c561e00f)

  Jika memilih "1" yaitu Top Up, maka akan masuk ke menu topup yang dimana pengguna dapat melakukan topup sesuai yang mereka inginkan pada menu.

  ![image](https://github.com/user-attachments/assets/4d3e8309-c17c-499e-9e68-2b5ecb66d892)

  Jika pengguna memasukkan angka "3" yaitu Nominal Lain, maka dapat melakukan pengisian saldo mulai dari Rp.200000 sampai dengan Rp.2000000.

  ![image](https://github.com/user-attachments/assets/4789fcfd-455f-44cd-aac6-8f1f314898d4)

  Jika pengguna memasukkan angka "2" yaitu Kembali, maka pengguna akan kembali ke "MENU PENGGUNA".

  - Lihat tiket yang dibeli

  ![image](https://github.com/user-attachments/assets/49e82d2c-6663-44b5-b218-755543d99a1e)

  Jika menginput angka "4" yaitu Lihat tiket yang dibeli, maka akan muncul invoice dari tiket yang pengguna beli.

  ![image](https://github.com/user-attachments/assets/5fac56ef-6089-427f-a58d-cafe6223adf4)

  Jika menginput "ya" maka akan menghapus tiket, namun jika tidak maka akan kembali ke menu pengguna.

  - Logout

  ![image](https://github.com/user-attachments/assets/cda4eedb-931c-4c9c-a82e-63cbf566d0fc)

  Jika menginput "5" yaitu Logout, maka pengguna akan keluar dan kembali ke menu login pengguna.

  ### 3. Pengujung

  ![image](https://github.com/user-attachments/assets/667470a1-b7bf-4954-9732-8c63d2283fa9)

  Jika menginput "3" yaitu pengunjung maka list konser akan langsung ditampilkan, setelah list konser ditampilkan maka pengunjung akan ditanya apakah ingin login sebagai pengguna atau tidak, jika menginput "Login" maka akan masuk ke menu login pengguna, namun jika menginput "Kembali" maka akan kembali ke menu pilih role.

  ### 4. Keluar

![Screenshot 2024-11-09 002513](https://github.com/user-attachments/assets/5b521f62-1007-478e-9378-fc0216864a78)

  Jika menginput "4" yaitu keluar maka, user akan keluar dari program.




     

  

    


     



     


     






       

       
     


       

       


     




     




     
      







     
         

         



     



