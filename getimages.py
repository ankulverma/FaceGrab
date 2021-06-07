
import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyAGwaYIE3eTwWEkNp_QvmvHpcvUEAvGiIw",
    "storageURL": "gs://facegrab-c82ff.appspot.com/",
    "databaseURL": "https://facegrab-c82ff-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "authDomain": "facegrab-c82ff.firebaseapp.com",
    "projectId": "facegrab-c82ff",
    "storageBucket": "facegrab-c82ff.appspot.com",
    "messagingSenderId": "414897340300",
    "appId": "1:414897340300:web:39698616f4a6c951fca0a9",
    "measurementId": "G-0F42EJJR32",
    "serviceAccount": "serviceAccountKey.json"
}
firebase = pyrebase.initialize_app(firebaseConfig)
path = "DownloadImages"
db = firebase.database()
storage = firebase.storage()

all_files = storage.child("ImageSourceDirectory").list_files() #Enter the name of the folder
for file in all_files:
    try:
        print(file.name+" Downloading")
        file.download_to_filename(file.name)
    except:
        print('Images Downloaded')
