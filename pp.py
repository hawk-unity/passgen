import random
import string
print(""" 
██   ██  █████  ██     ██ ██   ██      ██████  ███████  ██████ ██   ██ 
██   ██ ██   ██ ██     ██ ██  ██      ██    ██ ██      ██       ██ ██  
███████ ███████ ██  █  ██ █████       ██    ██ █████   ██        ███   
██   ██ ██   ██ ██ ███ ██ ██  ██      ██    ██ ██      ██       ██ ██  
██   ██ ██   ██  ███ ███  ██   ██      ██████  ██       ██████ ██   ██ 
                                                                       
                                                                      
""")
def rastgele_sifre_uret(uzunluk):
    harfler =  string.ascii_letters + string.digits + string.punctuation
    sonuc = ''.join(random.choice(harfler) for i in range(uzunluk))
    return sonuc
try : 
    karakter_sayı = int(input("KAC KARAKTER OLSUN İSTERSİN : "))
    print("ŞİFRENİZ : " + rastgele_sifre_uret(karakter_sayı)) 
    print("ŞİFRENİZ : " + rastgele_sifre_uret(karakter_sayı))
except ValueError:
    print("Lütfen sadece sayı girin!")