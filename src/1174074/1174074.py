# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:37:02 2019

@author: Aspire E15
"""
#3.2 Pemahaman Teori
#no 1
def perkalian(x, y):
    z = x * y
    return z
x = 2
y = 3
hasil = perkalian(x, y)

#no 2
import halo
a = ("Silahkan Menyapa, ")
b = ("Halo Semua")
hasil = halo.halo (a, b)

#no 3
class pakan:
    jumlahpakan = 0
    def __init__(self, kode, jenis):
        self.kode = kode
        self.jenis = jenis
        pakan.jumlahpakan +=12
    def DataPakan(self):
        print("Kode pakan :", self.kode)
        print("jenis pakan :", self.jenis)
        print()
pakan1 = pakan("P001", "Berkonsentrat")
pakan2 = pakan("P002", "Tidak Berkonsentrat")
pakan1.DataPakan()
pakan2.DataPakan()
print("Total Pemesanan Pakan Sebanyak:", pakan.jumlahpakan, "pakan")

#no 4
from pakan import pakan
pakan1 = pakan("P001", "Berkonsentrat")
pakan2 = pakan("P002", "Tidak Berkonsentrat")
pakan1.DataPakan()
pakan2.DataPakan()
print("Total Pemesanan Pakan Sebanyak:", pakan.jumlahpakan, "pakan")

#no 5
from kalkulator import Penambahan
hasilnya = Penambahan(2, 5)
print(hasilnya)

#no 6
from folder import kalkulator

a=2
b=5

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

#no 7
from folder.pakan import pakan
pakan1 = pakan("P001", "Berkonsentrat")
pakan2 = pakan("P002", "Tidak Berkonsentrat")
pakan1.DataPakan()
pakan2.DataPakan()
print("Total Pemesanan Pakan Sebanyak:", pakan.jumlahpakan, "pakan")


#3.3 Keterampilan Pemograman
#no 1
print(1174074%3)
#mod3 = 0

def printNPM(npm):
    
    npm = list(str(npm))
    
    angka1 = {"0":" ****** ", "1":"  **", "2":" ******* ", "3":" ******* ", "4":"     ***", "5":"********", "6":" ******* ", "7":"*********", "8":" ******* ", "9":" *******"}
    angka2 = {"0":"***  ***", "1":"****", "2":"**    ***", "3":"**    ***", "4":"   *****", "5":"**      ", "6":"***      ", "7":"     *** ", "8":"***   ***", "9":"**    ***"}
    angka3 = {"0":"***  ***", "1":" ***", "2":"     *** ", "3":"    **** ", "4":" ***  **", "5":"******* ", "6":"******** ", "7":"    ***  ", "8":" *** *** ", "9":"**    ***"}
    angka4 = {"0":"***  ***", "1":" ***", "2":"    ***  ", "3":"    **** ", "4":"********", "5":"     ***", "6":"***   ***", "7":"   ***   ", "8":" *** *** ", "9":" ********"}
    angka5 = {"0":"***  ***", "1":" ***", "2":"  ****   ", "3":"**    ***", "4":"     ***", "5":"**   ***", "6":"***   ***", "7":"  ***    ", "8":"***   ***", "9":"      ***"}
    angka6 = {"0":" ****** ", "1":" ***", "2":"*********", "3":" ******* ", "4":"     ***", "5":" ****** ", "6":" ******* ", "7":" ***     ", "8":" ******* ", "9":" ******* "}
              
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []
              
    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')
    
printNPM(input("Masukkan NPM Anda: "))


#no 2
def printNPMDuaDijit(npm):
    ulang = 1
    sampai = int(npm[5:7])
    while(ulang <= sampai):
        print("Halo, "+str(npm)+" apa kabar?")
        ulang += 1

printNPMDuaDijit(input("Masukkan NPM Anda: "))        

#no 3
def tigadijitNPM(npm):
    ulang = 1
    sampai = list(map(int, npm[4:7]))
    sampai = sum(sampai)    
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        ulang += 1
    
tigadijitNPM(input("Masukkan NPM Anda: "))

#no 4
def DijitKetigaNPM(npm):
    print("Output:")
    print("Halo, "+str(npm[-3])+" apa kabar?")
    
DijitKetigaNPM(input("Masukkan NPM Anda"))

#no 5
def KarakterNPM(npm):
    npm = list(map(int, npm))  
    for n in npm:
        print(n)
        
KarakterNPM(input("Masukkan NPM Anda: "))

#no 6
def PenjumlahanNPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x
    
    print(hasil)
    
PenjumlahanNPM(input("Masukkan NPM Anda: "))
    
#no 7
def PerkalianNPM(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x
    
    print(hasil)
    
PerkalianNPM(input("Masukkan NPM Anda: "))

#no 8
def DijitGenapNPM(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end = "")
    
DijitGenapNPM(input("Masukkan NPM Anda: "))

#Jawaban No. 9
def DijitGanjilNPM(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
            print(n, end = "")
    
DijitGanjilNPM(input("Masukkan NPM Anda: "))

#no 10
def DijitPrimaNPM(npm):
    npm = list(map(int, npm))
    prima = []
    for n in npm:
        isPrime = True
        if n == 0 or n == 1:
            isPrime = False
        for x in range(2, n):
            if n % x == 0:
                isPrime = False
        if isPrime:
            prima.append(n)

    for p in prima:
        print(p, end = "")
    
DijitPrimaNPM(input("Masukkan NPM Anda: "))

#no 11

#no 12

#Ketrampilan Penanganan Error
#Jawaban No. 1
def sapa(nama):
    try:
        print("Hallo, "+str(nama))
    except:
        print("Terjadi error") 

sapa(input("Masukkan Nama Anda: "))
