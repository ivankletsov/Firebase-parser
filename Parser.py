import os
import time
import pyrebase
import urllib.request

config = {"apiKey": "AIzaSyDCbGOM-TkhBRN7zunbyXAUUGzwBrhsWOc",
          "databaseURL": "",
          "authDomain": "test-a3be5.firebaseapp.com",
          "projectId": "test-a3be5",
          "storageBucket": "test-a3be5.appspot.com",
          "messagingSenderId": "378270106860",
          "serviceAccount": "test-a3be5-firebase-adminsdk-wtxtg-407da47c29.json"}
#пароль от созданой почты
password = '456758'
#Сама почта
mail = 'parser1@gmai.com'
# Все что надо для работы скрипта
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
auth = firebase.auth()
auth.sign_in_with_email_and_password(mail, password)
bucket = storage.bucket
blob = bucket.blob('113bf76b-2480-456c-b2f3-ece9a1d0476d-2-QYOR1.zip')
cc = blob.bucket.time_created
print(cc)
#получение списка файлов
files = storage.list_files()
#получение названия файла из пути на него и добавление в список

folder = []
for file in files:
    for i in str(file):
        if i =='<' or '>':
            unscope = str(file).replace('<', '')
            unscope2 = unscope.replace('>', '')
    file_for_list = unscope2[:0]+unscope2[30:]
    folder.append(file_for_list)
print(len(folder))
dir_path = r'/Users/egor/Documents/data'

directory = os.listdir(dir_path)
count = 0
for path in directory:
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
num = count - 1
a = 0
for a in range(0, num):
    folder.pop(0)


for file_name in folder:
    print(file_name)
    time.sleep(2)
    storage.child(file_name).download(file_name, f'/Users/egor/Documents/data/{file_name}')
    print('successed download')



