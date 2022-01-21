# fungsi cek
# use: python kalkulator.py
# Guah masih enuub anjimm
import os,sys,time

time.sleep(2)
os.system('clear')
# Pilihan buat pemakai
def pil():
  print("[1]. perkalian")
  print("[2]. perjumlahan")
  print("[3]. pembagian")
  print("[4]. pengurangan")
  print("[5]. kembali")
# perkalian
def kali():
  n1=int(input("Angka "))
  n2=int(input("Dikali "))
  kal=n1*n2
  print(n1, "x", n2, "= ", kal)
  time.sleep(2.1)
def bagi():
  n1=int(input("Angka "))
  n2=int(input("Dibagi "))
  kal=n1/n2
  print(n1, ":", n2, "= ", kal)
  time.sleep(2.1)
# Pertambahan
def tambah():
  n1=int(input("Angka "))
  n2=int(input("Ditambah "))
  kal=n1+n2
  print(n1, "+", n2, "= ", kal)
  time.sleep(2.1)
def kurang():
  n1=int(input("Angka "))
  n2=int(input("Dikurang "))
  kal=n1-n2
  print(n1, "-", n2, "= ", kal)
  time.sleep(2.1)
def loads():
  nama=input("Nama Kamu :> .. ")
  print("Welcome ", nama)
  print("Loading...")
  time.sleep(2.1)
def salah(): # Supaya kalo milih lebih dari lima gak error cuk
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
  elif(Q=="3"):
    bagi()
    salah()
  elif(Q=="4"):
    kurang()
    salah()
  elif(Q=='5'):
    kontol='''
    =---------------------------------|
    |||== Thanks For Use ==|||>>> :)  |
    =---------------------------------|
    '''
    print(kontol)
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
