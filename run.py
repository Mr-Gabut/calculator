# Yang mau recode tolol gakmau belajar dulu cobain tulis sendiri bangsadd!!!
# fungsi cek
# use: python kalkulator.py
# Guah masih enuub anjimm
import time
# Pilihan buat pemakai
def pil():
  print("[1]. perkalian")
  print("[2]. perjumlahan")
  print("[3]. kembali")
# perkalian
def kali():
  n1=int(input("Angka "))
  n2=int(input("Dikali "))
  kal=n1*n2
  print(n1, "x", n2, "= ", kal)
  time.sleep(2.1)
# Pertambahan
def tambah():
  n1=int(input("Angka "))
  n2=int(input("Ditambah "))
  kal=n1+n2
  print(n1, "+", n2, "= ", kal)
  time.sleep(2.1)
def loads():
  nama=input("Nama Kamu :> .. ")
  print("Welcome ", nama)
  print("Loading...")
  time.sleep(2.1)
def salah():
  menu()
# Eksekusi anjim!!!!!
def menu():
  pil()
  Q=input("Pilih.. ")
  if(Q=='1'):
    kali()
    salah()
  elif(Q=="2"):
    tambah()
    salah()
  elif(Q=='3'): 
    print("Thanks for use")
    time.sleep(3.1)
  else:salah()
# Manggil
banner='''
	     <---------------->
	    <<== Kalkulator ==>>
	     <---------------->
|| ========================================= |
|| -------------->> AUTHOR : Mr-Gabut        |
|| -------------->> Youtube: F i r e M e     |
|| ========================================= |
   Copy here:    https://github.com/Mr-Gabut
'''
print(banner)
loads()
menu()
