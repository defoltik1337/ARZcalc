import requests
import subprocess
import os

GITHUB_VERSION_URL = "https://raw.githubusercontent.com/defoltik1337/ARZcalc/main/utils/version.txt"
UPDATE_SCRIPT_URL = "https://github.com/defoltik1337/ARZcalc/archive/refs/heads/master.zip"
LOCAL_VERSION_FILE = "utils/version.txt"
UPDATE_FOLDER = "update"

def read_local_version():
    if not os.path.exists(LOCAL_VERSION_FILE):
        return "0.0.0"
    with open(LOCAL_VERSION_FILE, "r") as file:
        return file.read().strip()

def fetch_github_version():
    try:
        response = requests.get(GITHUB_VERSION_URL, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
    except requests.RequestException:
        pass
    return None

def is_update_available(local_version, github_version):
    return local_version < github_version

def download_and_update():
    print("Загружаем обновление...")
    os.makedirs(UPDATE_FOLDER, exist_ok=True)
    zip_path = os.path.join(UPDATE_FOLDER, "update.zip")
    
    response = requests.get(UPDATE_SCRIPT_URL, stream=True)
    if response.status_code == 200:
        with open(zip_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print("Обновление загружено. Распаковываем...")
        subprocess.run(["unzip", "-o", zip_path, "-d", UPDATE_FOLDER])
        print("Обновление завершено! Перезапустите программу.")
    else:
        print("Ошибка загрузки обновления.")

local_version = read_local_version()
github_version = fetch_github_version()

if github_version and is_update_available(local_version, github_version):
    print(f"Доступна новая версия {github_version} (у вас {local_version}).")
    choice = input("Хотите обновиться? (y/n): ")
    if choice.lower() == "y":
        download_and_update()
    else:
        print("Обновление отменено.")
else:
    print("У вас актуальная версия.")
