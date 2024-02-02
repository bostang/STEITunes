import sys
email = []
password = []
saldo_total = []
current_saldo = 0

# =============================================================================
#                       MENU UTAMA PROGRAM SEBELUM LOGIN
# =============================================================================

def menu_signup_login () :
    print("""
     .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | | _____  _____ | || |  _________   | || |   _____      | || |     ______   | || |     ____     | || | ____    ____ | || |  _________   | |
    | ||_   _||_   _|| || | |_   ___  |  | || |  |_   _|     | || |   .' ___  |  | || |   .'    `.   | || ||_   \  /   _|| || | |_   ___  |  | |
    | |  | | /\ | |  | || |   | |_  \_|  | || |    | |       | || |  / .'   \_|  | || |  /  .--.  \  | || |  |   \/   |  | || |   | |_  \_|  | |
    | |  | |/  \| |  | || |   |  _|  _   | || |    | |   _   | || |  | |         | || |  | |    | |  | || |  | |\  /| |  | || |   |  _|  _   | |
    | |  |   /\   |  | || |  _| |___/ |  | || |   _| |__/ |  | || |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\/_| |_ | || |  _| |___/ |  | |
    | |  |__/  \__|  | || | |_________|  | || |  |________|  | || |   `._____.'  | || |   `.____.'   | || ||_____||_____|| || | |_________|  | |
    | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    """)
    # user memilih action
    print ("Apa yang ingin Anda lakukan?")
    print ("1. Login")
    print ("2. Sign up")
    pilihan = int(input("Pilihan Anda: "))
    
    # user sudah punya akun dan ingin langsung log in
    if pilihan == 1:
        print("")
        login_system()

    # user memilih untuk sign up
    if pilihan == 2:
        print("")
        sign_up() 

# =============================================================================
#                               MENU SIGN UP
# =============================================================================

def sign_up ():
    print("========================================")
    print("             SIGN UP AKUN")
    print("========================================")
    print("Daftarkan akun Anda sekarang")
    emailInput = input("Email: ")

    # jika email yang diinput sudah terdaftar 
    while str(emailInput) in email :
        print("Email sudah terdaftar. Harap menggunakan email yang lain.")
        emailInput = input("Email: ")
    
    # jika email yang diinput belum terdaftar
    if str(emailInput) not in (email) :
        email.append(emailInput)

        print("Buatlah password seunik mungkin!")

        #asumsikan user menginput password sesuai ketentuan
        passwordInput = input("Password: ")
        print("Konfimasikan ulang password Anda!")
        password_konfirmasi = input("Konfirmasi password: ")

        # untuk cek apakah password konfirmasi sudah benar
        while str(password_konfirmasi) != str(passwordInput) : #salah
            print("Password yang Anda masukkan berbeda, silakan coba lagi")
            print("Konfimasikan ulang password Anda")
            print("Konfirmasi password: " , end="")
            password_konfirmasi = input()

        if password_konfirmasi == passwordInput : #benar
            password.append(password_konfirmasi)
            print("Anda berhasil sign up! Silakan login dengan akun yang sudah terdaftar")
            print("")
            login_system()

# =============================================================================
#                                 MENU LOGIN
# =============================================================================

def login_system(): 
    print("========================================")
    print("                 LOGIN")
    print("========================================")
    print ("Silakan login dengan email yang sudah terdaftar")
    emailInput = input("Email: ")
    passwordInput = input("Password: ")
    
    if emailInput not in email:
        print("")
        print("Anda belum mempunyai akun!")
        print("Silahkan membuat terlebih dahulu")
        print("")
        sign_up()
    else:
        emailLocation1 = email.index(emailInput)
    login_counter = 1
    flag1 = True   
    
    while (flag1 == True):

        if (passwordInput == password[emailLocation1]):
            print("Login Berhasil!")
            flag1 = False
            main_menu()
        
        
        else:
            print("Email atau password anda salah!")
            emailInput = input("Email: ")
            passwordInput = input("Password: ")
            emailLocation1 = email.index(emailInput)
            login_counter += 1
            if (login_counter <= 5):
                flag1 = True
            else:
                flag1 = False

# =============================================================================
#                  CEK KESEDIAAN AKUN JIKA 5X SALAH INPUT
# =============================================================================
    
    if (login_counter > 5):
        flag2 = True
        
        while (flag2 == True):
            print("Apakah Anda sudah punya akun?")
            print("1. Ya")
            print("2. Tidak")
            account_check_question = int(input("Pilihan Anda: "))
            
            if (account_check_question == 1):
                login_system()
                flag2 = False
            
            if (account_check_question == 2):
                sign_up()
                flag2 = False

# =============================================================================
#                       MENU UTAMA PROGRAM SETELAH LOGIN
# =============================================================================

def main_menu():
    print(""" 
    .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .-----------------. .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |    _______   | || |  _________   | || |  _________   | || |     _____    | | | |  _________   | || | _____  _____ | || | ____  _____  | || |  _________   | || |    _______   | |
    | |   /  ___  |  | || | |  _   _  |  | || | |_   ___  |  | || |    |_   _|   | | | | |  _   _  |  | || ||_   _||_   _|| || ||_   \|_   _| | || | |_   ___  |  | || |   /  ___  |  | |
    | |  |  (__ \_|  | || | |_/ | | \_|  | || |   | |_  \_|  | || |      | |     | | | | |_/ | | \_|  | || |  | |    | |  | || |  |   \ | |   | || |   | |_  \_|  | || |  |  (__ \_|  | |
    | |   '.___`-.   | || |     | |      | || |   |  _|  _   | || |      | |     | | | |     | |      | || |  | '    ' |  | || |  | |\ \| |   | || |   |  _|  _   | || |   '.___`-.   | |
    | |  |`\____) |  | || |    _| |_     | || |  _| |___/ |  | || |     _| |_    | | | |    _| |_     | || |   \ `--' /   | || | _| |_\   |_  | || |  _| |___/ |  | || |  |`\____) |  | |
    | |  |_______.'  | || |   |_____|    | || | |_________|  | || |    |_____|   | | | |   |_____|    | || |    `.__.'    | || ||_____|\____| | || | |_________|  | || |  |_______.'  | |
    | |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    """)
    print("========================================")
    print("     SELAMAT DATANG DI STEITUNES")
    print("========================================")
    print("")
    print("Apa yang Anda ingin lakukan?")
    print("1. Logout")
    print("2. Top-Up")
    print("3. Beli Lagu")
    activity = int(input("Pilihan Anda: "))

    if (activity == 1):
        print("Logout Successful")
        sys.exit()
    if (activity == 2):
        print("========================================")
        print("             MENU TOP UP")
        print("========================================")
        print("Berapakah saldo yang ingin Anda top-up?")
        saldo_top_up = int(input("Saldo: "))
        saldo_total = top_up(saldo_top_up)
        main_menu()
    if (activity == 3):
        song_search()

# =============================================================================
#                       MENAMBAH DANA (TOP - UP)
# =============================================================================

def top_up(saldo_top_up):
    saldo_total.append(saldo_top_up)
    print("Top up berhasil!")
    print("Saldo Anda menjadi " + str(sum(saldo_total)))
    
# =============================================================================
#                      PROGRAM PENCARIAN LAGU
# =============================================================================

def song_search():
    from random import randint

    # ganti path disini apabila berganti komputer
    # fhand_song = open(r'D:\Drive D\VS Code\Python\Tugas Besar Komputasi\database_lagu.txt','r')   # r di depan untuk mencegah unicode escape error
    fhand_song = open(r'./database_lagu.txt','r')   # r di depan untuk mencegah unicode escape error
    # fhand_author = open(r'D:\Drive D\VS Code\Python\Tugas Besar Komputasi\database_singer.txt','r')
    fhand_author = open(r'./database_singer.txt','r')

    song_database = []  # database mini lagu
    singer_database = [] # database mini penyanyi



    for song in fhand_song:
        song_database.append(song.rstrip()) # menghilangkan whitespace di akhir baris
    for author in fhand_author:
        singer_database.append(author.rstrip()) 

    lagu_pilih = [] # list lagu-lagu yang dipilih
    price_lagu_pilih = [] # harga dari lagu yang dipilih --> nanti akan di-randomisasi
    reccomendation = [] # lagu yang mirip sesuai dengan keyword yang diketikkan

# =============================================================================
#                       MENCARI LAGU BERDASARKAN JUDUL LAGU
# =============================================================================

    def cari_lagu():  
        song_search = input("Cari lagu yang di-inginkan: ") # dapat berupa keyword saja

        for song in song_database:
            if song_search.lower() in song.lower():
                reccomendation.append(song)  
                
        print("Beberapa lagu yang mungkin cocok: ")
        for j in reccomendation:
            y = song_database.index(j) #kebetulan posisi song_database dan singer_database sama
            print(j," || Oleh:",singer_database[y])

# =============================================================================
#                              MENCARI LAGU BERDASARKAN GENRE
# =============================================================================

    def cari_genre():
        print("Daftar genre:")
        print("1. Rock")
        print("2. Indie")
        print("3. Pop")
        print("4. Anime")
        print("5. Jazz")
        genre_pilihan = int(input("Genre pilihan: "))
        
        index = [(k+1) for k in range(50)]
        if (genre_pilihan == 1):
            print("50 lagu dengan genre Rock")
            print("===========================")
            for i in range (50):
                print(str(index[i%50])+". "+song_database[i] + " ||    oleh " + singer_database[i])
        elif (genre_pilihan == 2):
            print("50 lagu dengan genre Indie")
            print("===========================")
            for i in range (1001, 1051):
                print(str(index[i%50-1])+". "+song_database[i] + " ||    oleh " + singer_database[i])
        elif (genre_pilihan == 3):
            print("50 lagu dengan genre Pop")
            print("===========================")
            for i in range (1051, 1101):
                print(str(index[i%50-1])+". "+song_database[i] + " ||    oleh " + singer_database[i])
        elif (genre_pilihan == 4):
            print("50 lagu dengan genre Anime")
            print("===========================")
            for i in range (1101, 1151):
                print(str(index[i%50-1])+". "+song_database[i] + " ||    oleh " + singer_database[i])
        elif (genre_pilihan == 5):
            print("50 lagu dengan genre Jazz")
            print("===========================")
            for i in range (1151, 1201):
                print(str(index[i%50-1])+". "+song_database[i] + " ||    oleh " + singer_database[i])

# =============================================================================
#                         MENCARI LAGU BERDASARKAN PENYANYI
# =============================================================================

    def cari_penyanyi():
        singer_search = input("Cari penyanyi yang anda suka: ")
        
        for singer in range(len(singer_database)):
            if singer_search.lower() in singer_database[singer].lower():
                reccomendation.append(song_database[singer])
        print("Beberapa lagu yang mungkin cocok: ")
        for j in reccomendation:
            y = song_database.index(j) #kebetulan posisi song_database dan singer_database sama
            print(j," || Oleh:",singer_database[y])
    

# =============================================================================
#                       MENGHAPUS LAGU YANG SUDAH DI BELI
# =============================================================================

    def hapus_lagu():
        def hapus_semua(): # menghapus seluruh lagu yang sudah dipilih.
            lagu_pilih.clear()  
        print("MENU MENGHAPUS LAGU YANG SUDAH DIPILIH")
        print("======================================")
        print("Lagu yang sudah dipilih: ")
        for e in range(len(lagu_pilih)):
            print(str(e+1)+". "+lagu_pilih[e])
        hapus_lagu_flag = True
        while hapus_lagu_flag: 
            print("Jika ingin menghapus semua lagu, ketik SEMUA")
            print("Jika selesai, ketik SELESAI")
            print("")
            hapus = input("Nomor lagu berapa yang ingin dihapus? ")
            if hapus == "SEMUA":
                print("Yakin?")
                print("1. Ya")
                print("2. Tidak")
                keyakinan = int(input("Pilihan Anda: "))
                if keyakinan == 1:
                    hapus_semua()
                elif keyakinan == 2:
                    pass # do nothing
            if hapus == "SELESAI" :
                hapus_lagu_flag = False # selesai melaksanakan prosedur menghapus lagu  
            try:
                lagu_pilih.pop(int(hapus)-1)  # menghapus lagu yang sudah dipilih
            except:
                pass
        
# =============================================================================
#                               MEMILIH LAGU 
# =============================================================================

    def pilih_lagu():
        flag_lagu_pilih = True
    
        while flag_lagu_pilih:
            print("Jika telah selesai, ketik SELESAI")
            print("")
            lagu_demand = input("Judul apa yang mau dibeli? ")
            if lagu_demand == "SELESAI":
                flag_lagu_pilih = False
            try:
                if lagu_demand in song_database:
                    lagu_pilih.append(lagu_demand)
                elif lagu_demand != "SELESAI" and lagu_demand not in song_database:
                    print("Lagu tidak ditemukan")
            except:
                pass
                   
# =============================================================================
#                           MENG-GENERATE HARGA
# =============================================================================

    def cost_generator():
        for j in range(len(lagu_pilih)):
            price = randint(10,30)  # harga lagu kisaran 10 sampai 30 ribu
            price_lagu_pilih.append(price*1000) # harga dalam satuan ribu

# =============================================================================
#                             MENU MENCARI LAGU
# =============================================================================   
    selesai_cari_lagu = False
    
    while not selesai_cari_lagu:
        print("")
        print("========================================")
        print("    SELAMAT DATANG DI MENU PEMBELIAN")
        print("========================================")
        print("Mau cari lagu berdasarkan apa?")
        print("1. Berdasarkan judul lagu")
        print("2. Berdasarkan penyanyi")
        print("3. Berdasarkan genre")
        print("Jika selesai memilih lagu, pilih yang mana saja dan ketik lagu asal lalu ketik SELESAI")
        cari_apa = int(input("Pilihan Anda: "))
        if cari_apa == 1:
            cari_lagu() 
        elif cari_apa == 2:
            cari_penyanyi()
        elif cari_apa == 3:
            cari_genre()
        pilih_lagu()
        reccomendation = [] # mengosongkan the reccomendation
        
        # cari lagu lagi atau menghapus lagu yang sudah dipilih

# =============================================================================
#            MENU SETELAH SELESAI MENCARI LAGU DAN MENU PEMBAYARAN
# =============================================================================   
#      
        print("")
        print("========================================")
        print("            MENU KONFIRMASI")
        print("========================================")
        print("Apa yang ingin dilakukan?")
        print("1. Cari lagu")
        print("2. Hapus lagu dari keranjang")
        print("3. Pembayaran")
        print("4. Selesai")
        decision = int(input("Pilihan Anda: "))
        if decision == 1:     
            continue
        elif decision == 2:
            hapus_lagu()
        elif decision == 3:
            print("")
            print("========================================")
            print("            MENU PEMBAYARAN")
            print("========================================")
            print("Apakah Anda yakin ingin membayar?")
            print("1. Ya")
            print("2. Tidak")
            decision_beli = int(input("Pilihan Anda: "))
            if (decision_beli == 1):
                cost_generator()
                if (len(lagu_pilih) > 0):    
                    if (sum(saldo_total) >= sum(price_lagu_pilih)):
                        current_saldo = sum(saldo_total) - sum(price_lagu_pilih)
                        print("Sisa saldo Anda " +str(current_saldo))
                        print("Transaksi berhasil!")
                        print("Terima kasih sudah berbelanja di STEITUNES!")
                        main_menu()
                    else:   # saldo < price_lagu_pilih
                        print("Maaf! Saldo Anda tidak cukup")
                        print("")
                        print("Apakah Anda ingin melakukan top-up saldo?")
                        print("1. Ya")
                        print("2. Tidak")
                        decision_top_up = int(input("Pilihan Anda: "))
                        if (decision_top_up == 1):
                            print("========================================")
                            print("             MENU TOP UP")
                            print("========================================")
                            print("Berapakah saldo yang ingin Anda top-up?")
                            saldo_top_up = int(input("Saldo: "))
                            top_up(saldo_top_up)
                        elif (decision_top_up == 2):
                            main_menu()
                else:
                    print("Anda tidak membeli apa - apa")
                    print("Silahkan mencari lagu terlebih dahulu")
                    song_search()
            elif (decision_beli == 2):
                song_search()
        elif decision == 4:
            print("Yakin?")
            print("1. Ya")
            print("2. Tidak")
            yakin = int(input("Pilihan Anda: "))
            if yakin == 1:
                selesai_cari_lagu = True
                main_menu()
            elif yakin == 2:
                pass

menu_signup_login()
