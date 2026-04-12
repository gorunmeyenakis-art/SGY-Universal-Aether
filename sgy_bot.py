import os
import shutil
import time

SENSOR_COMMAND = "termux-sensor"
GIT_COMMAND = "git"


def _require_command(command_name):
    if shutil.which(command_name):
        return True
    print(f"Eksik sistem bagimliligi: {command_name}")
    return False


def _run(command):
    return os.system(command) == 0


def sgy_otomasyon():
    print("SGY Otomasyon Robotu Baslatildi...")
    if not _require_command(SENSOR_COMMAND):
        print("Termux:API kurulu olmadan sensor verisi toplanamaz.")
        return
    if not _require_command(GIT_COMMAND):
        print("Git kurulu olmadigi icin veri gonderimi yapilamiyor.")
        return

    while True:
        sensor_ok = _run('termux-sensor -s "Magnetometer" -n 1 > sensor_verisi.txt')
        if not sensor_ok:
            print("Sensor verisi alinamadi, bir sonraki deneme bekleniyor.")
            time.sleep(60)
            continue

        commit_message = f'SGY Otomatik Muhur: {time.ctime()}'
        _run("git add sensor_verisi.txt")
        _run(f'git commit -m "{commit_message}"')
        _run("git push origin main")

        print(time.ctime() + " - Veriler GitHub'a ucuruldu. 10 dakika mola...")
        time.sleep(600)


if __name__ == "__main__":
    sgy_otomasyon()
