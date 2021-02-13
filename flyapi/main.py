##Gak usah di recode engine
# -*- coding: utf-8 -*-
import os
import sys
import time
def nanyacoeg():
    nanya = raw_input("lanjut gak coeg[Y/N] ")
    if nanya == "Y" or nanya == "y":
        restartcoeg()
    elif nanya == "N" or nanya == "n":
        print "ada beberapa command termux-api yg blm gw tampilin krna gk ngrti coeg"
        time.sleep(0.4)
        print "makasih dah make nih tools"
        print "\033[1;33mloading..."
        time.sleep(0.3)
        exit()
    else:
        print "\033[1;33mkuanggap itu tidak.."
        time.sleep(0.4)
        exit()
def restartcoeg():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

logo="""\033[1;31m
 _                                                  _
| |_ ___ _ __ _ __ ___  _   ___  __      __ _ _ __ (_)
| __/ _ \ '__| '_ ` _ \| | | \ \/ /____ / _` | '_ \| | author = Mr. Stalker
\033[1;34m| ||  __/ |  | | | | | | |_| |>  <_____| (_| | |_) | | My channel youtube =
 \__\___|_|  |_| |_| |_|\__,_/_/\_\     \__,_| .__/|_| Mr. Stalker121
                                             |_|
\033[1;31m                                               _
  ___ ___  _ __ ___  _ __ ___   __ _ _ __   __| |
 / __/ _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |
\033[1;34m| (_| (_) | | | | | | | | | | | (_| | | | | (_| |
 \___\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|
 """
ayam="""
\033[1;31m0 keluar                  16 play musik               32 atur wifi
\033[1;32m1 info audio              17 scan musik               33 scan imfo wifi
\033[1;33m2 status batere           18 rekam suara
\033[1;34m3 kecerahan               19 buat notifikasi
\033[1;35m4 log panggilan           20 apus notifikasi
\033[1;36m5 info kamera             21 liat inbox
\033[1;37m6 photo                   22 kirim sms
\033[1;31m7 ambil klipboard         23 nelpon
\033[1;32m8 buat klipboard          24 info sel telepone
\033[1;33m9 liat kontak             25 info perangkat telepone
\033[1;34m10 dialog                 26 popup
\033[1;35m11 fingerprint            27 senter
\033[1;36m12 fix shebang            28 getar
\033[1;37m13 termux info            29 volume
\033[1;31m14 infrared frekuensi     30 ganti wallpaper
\033[1;32m15 lokasi                 31 info koneksi wifi
"""
os.system("clear")
print logo + ayam
makan = raw_input("\033[1;32mIni teks@#$= ")
if makan == "0" or makan == "keluar":
    time.sleep(0.4)
    print "makasih dah make nih tools"
    time.sleep(0.6)
    exit()
elif makan == "1" or makan == "01":
    os.system("termux-audio-info")
    time.sleep(0.5)
    nanyacoeg()
elif makan == "2" or makan == "02":
    os.system("termux-battery-status")
    time.sleep(0.5)
    nanyacoeg()
elif makan == "3" or makan == "03":
    kecerahan = raw_input("berapa kecerahannya[0 sampe 255] ")
    os.system('termux-brightness %s'%(kecerahan))
    restartcoeg()
elif makan == "4" or makan == "04":
    log="termux-call-log"
    print """
    -g gak usah
    -l membatasi  batas dalam daftar log panggilan(default: 10)
    -o mengimbangi  diimbangi dalam daftar log panggilan(default: 0)"""
    coeg = raw_input("pilih coeg[-l][-o][-g] ")
    if coeg == "-l -o" or coeg == "-o -l":
        batas = raw_input("batasnya coeg#> ")
        imbang = raw_input("imbangnya coeg#> ")
        os.system('%s -l %s -o %s'%(log, batas, imbang))
        nanyacoeg()
    elif coeg == "-l" or coeg == "-o":
        berapa = raw_input("berapa coeg#> ")
        os.system('%s %s %s'%(log, coeg, berapa))
        nanyacoeg()
    elif coeg == "-g":
        os.system('%s'%(log))
        nanyacoeg()
elif makan == "5" or makan == "05":
    os.system("termux-camera-info")
    nanyacoeg()
elif makan == "6" or makan == "06":
    print "pastikan ditempat terang coeg"
    time.sleep(0.3)
    print "otomatis kesimpen di sdcard dan berformat jpeg"
    poto = raw_input("nama filenya coeg #> ")
    hmm = raw_input("0/1 [note 0 kamera belakang 1 kamera depan] ")
    os.system("termux-camera-photo -c %s /sdcard/%s.JPEG"%(hmm, poto))
    nanyacoeg()
elif makan == "7" or makan == "07":
    os.system("termux-clipboard-get")
    nanyacoeg()
elif makan == "8" or makan == "08":
    cuih = raw_input("masukin kata kata untuk disimpen #> ")
    os.system("termux-clipboard-set %s"%(cuih))
    nanyacoeg()
elif makan == "9" or makan == "09":
    os.system("termux-contact-list")
    nanyacoeg()
elif makan == "10":
    nanya = raw_input("beberapa baris[b]/mode nomor[n]/mode password[p]/gk usah[g]? ")
    if nanya == "b":
        multiple="-m"
        baris = raw_input("kasih judul[Y/N] ")
        if baris == "Y" or baris == "y":
            judul = raw_input("judulnya@> ")
            title='-t "%s"'%(judul)
            os.system('termux-dialog -i "isi coeg" %s %s'%(multiple, title))
            nanyacoeg()
        elif baris == "N" or baris == "n":
            os.system('termux-dialog -i "isi coeg" %s'%(multiple))
            nanyacoeg()
    elif nanya == "n":
        numbers="-n"
        nomor = raw_input("mode password[Y/N] ")
        if nomor == "Y" or nomor == "y":
            password="-p"
            nanya = raw_input("kasih judul[Y /N] ")
            if nanya == "Y" or nanya == "y":
                judul = raw_input("judulnya@> ")
                title='-t "%s"'%(judul)
                os.system('termux-dialog -i "isi coeg" %s %s %s'%(numbers, password, title))
                nanyacoeg()
            elif nanya == "N" or nanya == "n":
                os.system('termux-dialog -i "isi coeg" %s %s'%(numbers, password))
                nanyacoeg()
        elif nomor == "N" or nomor == "n":
            nanya = raw_input("kasih judul[Y/N] ")
            if nanya == "Y" or nanya == "y":
                judul = raw_input("judulnya@> ")
                title='-t "%s"'%(judul)
                os.system('termux-dialog -i "isi coeg" %s %s'%(numbers, title))
                nanyacoeg()
            elif nanya == "N" or nanya == "n":
                os.system('termux-dialog -i "isi coeg" %s'%(numbers))
                nanyacoeg()
    elif nanya == "p":
        password="-p"
        numbers="-n"
        nanya = raw_input("mode pin[p]/mode sandi[s] ")
        if nanya == "p":
            os.system('termux-dialog -i "isi coeg" %s %s'%(password, numbers))
            nanyacoeg()
        elif nanya == "s":
            os.system('termux-dialog -i "isi coeg" %s'%(password))
            nanyacoeg()
    elif nanya == "g":
        judul = raw_input("kasih judul[Y/N] ")
        if judul == "Y" or judul == "y":
            nanya = raw_input("judulnya=} ")
            title='-t "%s"'%(nanya)
            os.system('termux-dialog -i "isi coeg" %s'%(title))
            nanyacoeg()
        elif judul == "N" or judul == "n":
            os.system("termux-dialog -i 'isi coeg'")
            nanyacoeg()
elif makan == "11":
    print """
    Use fingerprint sensor on device to check for authentication
    NOTE: Only available on Marshmallow and later
    """
    os.system("termux-fingerprint")
    nanyacoeg()
elif makan == "12":
    pile = raw_input("filenya coeg[contoh /sdcard/ayam.py] @#> ")
    os.system('termux-fix-shebang "%s"'%(pile))
    print "dah coeg"
    nanyacoeg()
elif makan == "13":
    os.system("termux-info")
    nanyacoeg()
elif makan == "14":
    os.system("termux-infrared-frequencies")
    nanyacoeg()
elif makan == "15":
    provider = raw_input("penyedia lokasi[gps/network/passive] ")
    request = raw_input("permintaan[once/last/updates] ")
    print "selovv coeg"
    os.system('termux-location -p "%s" -r "%s"'%(provider, request))
    print "loading.."
    time.sleep(0.4)
    nanyacoeg()
elif makan == "16":
    media="termux-media-player"
    print """
    info        Menampilkan informasi pemutaran saat ini
    play        Melanjutkan pemutaran jika dijeda
    play <file> Memutar file media yang ditentukan
    pause       Jeda pemutaran
    stop        Keluar dari pemutaran"""
    coeg = raw_input("[info/play/play<file>/pause/stop] ")
    cuih='"%s"'%(coeg)
    if coeg == "info":
        os.system("%s %s"%(media, cuih))
        nanyacoeg()
    elif coeg == "play":
        os.system("%s %s"%(media, cuih))
        nanyacoeg()
    elif coeg == "play<file>":
        tempat = raw_input("filenya[contoh /sdcard/ayam.mp3] ")
        disini='"%s"'%(tempat)
        os.system("%s play %s"%(media, disini))
        nanyacoeg()
    elif coeg == "pause":
        os.system("%s %s"%(media, cuih))
        nanyacoeg()
    elif coeg == "stop":
        os.system("%s %s"%(media, cuih))
        nanyacoeg()
elif makan == "17":
    print """Pindai file yang ditentukan dan tambahkan ke penyedia konten media.
    -r memindai direktori secara rekursif
    -v mode verbose"""
    scan="termux-media-scan"
    ayam = raw_input("pilih coeg[-v/-r/-v -r] ")
    if ayam == "-v" or ayam == "-r":
        bakar = raw_input("filenya[contoh /sdcard/ntah.mp3] ")
        os.system('%s "%s" "%s"'%(scan, ayam, bakar))
        nanyacoeg()
    elif ayam == "-v -r" or ayam == "-r -v":
        gosong='"%s"'%(ayam)
        bakar = raw_input("filenya[contoh /sdcard/ntah.mp3] ")
        os.system('%s "%s" "%s"'%(scan, gosong, bakar))
        nanyacoeg()
elif makan == "18":
    rekam="termux-microphone-record"
    print """otomatis kesimpen di sdcard
    Rekam menggunakan mikrofon di perangkat Anda
    -d mulai rekaman / default
    -f mulai rekaman / file spesifik
    -l mulai rekaman / ditentukan batas (dalam detik)
    -i Dapatkan info tentang rekaman saat ini
    -q hentikan rekaman"""
    nasi = raw_input("[-d/-f/-l/-i/-q] ")
    if nasi == "-d" or nasi == "-i" or nasi == "-q":
        os.system("%s %s"%(rekam, nasi))
        nanyacoeg()
    elif nasi == "-f":
        nama = raw_input("namanya$=> ")
        basi = raw_input("kasih batasan waktu[Y/N] ")
        if basi == "Y" or basi == "y":
            detik = raw_input("berapa detik? ")
            os.system('%s "%s".3gp %s'%(rekam, nama, detik))
            nanyacoeg()
        elif basi == "N" or basi == "n":
            os.system('%s "%s".3gp'%(rekam, nama))
            nanyacoeg()
    elif nasi == "-l":
        detik = raw_input("berapa detuk? ")
        os.system("%s %s"%(rekam, detik))
        nanyacoeg()
elif makan == "19":
    print '''command paling dasar --content basing
    Tampilkan pemberitahuan sistem. Teks konteks dibaca dari stdin atau ditentukan menggunakan --content
  --action action  tindakan untuk dijalankan saat menekan pemberitahuan
  --button1 text  teks untuk ditampilkan pada tombol notifikasi pertama
  --button1-action action  aksi untuk mengeksekusi pada tombol notifikasi pertama
  --button2 text  teks untuk ditampilkan pada tombol pemberitahuan kedua
  --button2-action action  aksi untuk mengeksekusi pada tombol notifikasi kedua
  --button3 text  teks untuk ditampilkan pada tombol pemberitahuan ketiga
  --button3-action action  aksi untuk mengeksekusi pada tombol pemberitahuan ketiga
  --content content  konten untuk ditampilkan dalam pemberitahuan. Baca dari stdin tidak ditentukan di sini.
  --id id  pemberitahuan id (akan menimpa pemberitahuan sebelumnya dengan id yang sama)
  --warna rrggbb warna terang dari blinking dipimpin sebagai RRGGBB (default: ffffff)
  --led-on milidetik  jumlah milidetik untuk LED menyala saat berkedip (default: 800)
  --led-off milidetik  jumlah milidetik untuk LED mati sementara berkedip (default: 800)
  --on-delete action  aksi untuk dieksekusi ketika notifikasi dihapus
  --priority prio  prioritas notifikas(high/low/max/min/default)
  --sound  bunyikan suara dengan notifikasi
  --title title  judul pemberitahuan untuk ditampilkan
  --vibrate pattern  pola getar, koma dipisahkan seperti dalam 500,1000,200
  kalian tinggal tulis command yg diatas, dikasih id jga, krna penting
  untuk bagian button, content, title.teks diawali dan diakhiri dengan tanda "
  sisanya tinggal kalian anuin sendiri, kalo gk ngerti baca ulang coeg, tpi klo gk mau make yg laen aja'''
    kucing = raw_input("isi coeg@_ ")
    os.system('termux-notification %s'%(kucing))
    nanyacoeg()
elif makan == "20":
    tulis = raw_input("tulis idnya@#$> ")
    os.system('termux-notification-remove %s'%(tulis))
    nanyacoeg()
elif makan == "21":
    cemees="termux-sms-inbox"
    print """
    -l membatasi  batasi dalam daftar sms(default: 10)
    -o keseimbangan  seimbangi dalam daftar sms(default: 0)
    """
    duh = raw_input("pilih coeg[-l][-o][-g] ")
    if duh == "-l -o" or duh == "-o -l":
        batas = raw_input("batasannya=> ")
        sebambang = raw_input("keseimbangannya=> ")
        os.system('%s -l %s -o %s'%(cemees, batas, sebambang))
        nanyacoeg()
    elif duh == "-l" or duh == "-o":
        laper = raw_input("isicoeg&> ")
        os.system('%s %s %s'%(cemees, duh, laper))
        nanyacoeg()
    elif duh == "-g":
        os.system('%s'%(cemees))
        nanyacoeg()
elif makan == "22":
    sms="termux-sms-send -n"
    print """make pulsa coeg
    cara sms ke lebih dari 1 nomor
    nomor1[,nomor2,nomor3,dan seterusnya]"""
    argh = raw_input("nomornya=} ")
    sakit = raw_input("isi pesan=~ ")
    os.system('%s %s "%s"'%(sms, argh, sakit))
    nanyacoeg()
elif makan == "23":
    print "make pulsa coeg"
    sweet = raw_input("nomornyacoeg+> ")
    os.system("termux-telephony-call %s"%(sweet))
    nanyacoeg()
elif makan == "24":
    os.system("termux-telephony-cellinfo")
    nanyacoeg()
elif makan == "25":
    os.system("termux-telephony-deviceinfo")
    nanyacoeg()
elif makan == "26":
    tos="termux-toast"
    print """Tampilkan teks dalam Toast (popup sementara). Teks untuk ditampilkan disediakan sebagai argumen atau dibaca dari stdin jika tidak ada argumen yang diberikan.
     -b mengatur warna latar belakang (default: gray)
     -c mengatur warna teks (default: white)
     -g mengatur posisi toast: [top, middle, or bottom] (default: middle)
     -s hanya menunjukan toast untuk sementara waktu
NOTE: warna dapat berupa nama standar (yaitu red) atau nilai hex 6/8 digit (yaitu "# FF0000" atau "# FFFF0000") di mana urutannya (AA)RRGGBB. Warna yang tidak valid akan kembali ke nilai default, untuk warna yg laen selain warna standard, make nilai hex aja klo mau nih linknya https://pastebin.com/BH3fA4e9
command -s gk bsa gabung sama -b -c -g karena mereka musuhan, jdi klo dah milih -b -c -g jangan ditambahin -s dan sebaliknya"""
    wek = raw_input("pilih satu atau lebih[-b][-c][-g]/[-s] ")
    if wek == "-b -c -g" or wek == "-c -b -g" or wek == "-g -b -c" or wek == "-g -c -b":
        latar = raw_input("warna background?=> ")
        teks = raw_input("warna teks?=> ")
        di = raw_input("letaknya?=> ")
        isi = raw_input("isi teks?=> ")
        os.system('%s -b "%s" -c "%s" -g %s %s'%(tos, latar, teks, di, isi))
        nanyacoeg()
    elif wek == "-b -c" or wek == "-c -b":
        latar = raw_input("warna background?= ")
        teks = raw_input("warna teks?= ")
        isi = raw_input("isi teks?= ")
        os.system('%s -b "%s" -c "%s" %s'%(tos, latar, teks, isi))
        nanyacoeg()
    elif wek == "-b -g" or wek == "-g -b":
        warna = raw_input("warnanya=? ")
        di = raw_input("letaknya=? ")
        isi = raw_input("isi teks=? ")
        os.system('%s -b "%s" -g %s %s'%(tos, warna, di, isi))
        nanyacoeg()
    elif wek == "-c -g" or wek == "-g -c":
        warna = raw_input("warnanya@> ")
        di = raw_input("letaknya#> ")
        isi = raw_input("isi teks@> ")
        os.system('%s -c "%s" -g %s %s'%(tos, warna, di, isi))
        nanyacoeg()
    elif wek == "-g":
        di = raw_input("letaknya$> ")
        isi = raw_input("isi teks#> ")
        os.system('%s %s %s %s'%(tos, wek, di, isi))
        nanyacoeg()
    elif wek == "-s":
        isi = raw_input("isi teks@> ")
        os.system('%s %s %s'%(tos, wek, isi))
        nanyacoeg()
elif makan == "27":
    senter = raw_input("[on | off] ")
    os.system('termux-torch %s'%(senter))
    nanyacoeg()
elif makan == "28":
    bzz="termux-vibrate"
    print """Getar perangkat
    -d durasi   untuk bergetar dalam ms (default: 1000)
    -f  memaksa getaran dalam mode senyap"""
    durasi = raw_input("durasinya coeg&> ")
    senyap = raw_input("mode senyap[Y/N]Â> ")
    if senyap == "Y" or senyap == "y":
        os.system('%s -d %s -f'%(bzz, durasi))
        nanyacoeg()
    elif senyap == "N" or senyap == "n":
        os.system('%s -d %s'%(bzz, durasi))
        nanyacoeg()
elif makan == "29":
    print """Ubah volume aliran audio 
    Aliran audio yang valid adalah: alarm, music, notification, ring, system, call"""
    valid = raw_input("aliran audio=> ")
    berapa = raw_input("volumenya (0-100) ")
    os.system('termux-volume %s %s'%(valid, berapa))
    nanyacoeg()
elif makan == "30":
    print """
    -f  ubah wallpaper dari file
    -u  ubah wallpaper dari sumber url"""
    kucing = raw_input("dari file[-f] atau dari link[u] ")
    print """contoh dari file
    /sdcard/ayam.png
contoh dari link
    https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS112W4xt1bQZ4_N3mZb7HFo5zZ4ygMjCv1Qk0QZHEUB3a9YUGsilq5U6AMEw"""
    mana = raw_input("tuliscoeg@#> ")
    os.system('termux-wallpaper %s "%s"'%(kucing, mana))
    nanyacoeg()
elif makan == "31":
    os.system("termux-wifi-connectioninfo")
    nanyacoeg()
elif makan == "32":
    print """true = idupin wifi
false = matiin wifi"""
    wifi = raw_input("[true | false] ")
    os.system("termux-wifi-enable %s"%(wifi))
    nanyacoeg()
elif makan == "33":
    print "Dapatkan informasi tentang pemindaian wifi terakhir"
    time.sleep(0.7)
    os.system("termux-wifi-scaninfo")
    nanyacoeg()
else:
    print "\033[1;31msalah coeg.."
    time.sleep(0.6)
    restartcoeg()
