import os
import time

def sgy_otomasyon():
    print("SGY Otomasyon Robotu Başlatıldı...")
    while True:
        # Manyetik veriyi tazele
        os.system('termux-sensor -s "Magnetometer" -n 1 > sensor_verisi.txt')
        
        # GitHub'a mühürle
        os.system('git add .')
        os.system('git commit -m "SGY Otomatik Mühür: ' + time.ctime() + '"')
        os.system('git push origin main')
        
        print(time.ctime() + " - Veriler GitHub'a uçuruldu. 10 dakika mola...")
        time.sleep(600)

sgy_otomasyon()
