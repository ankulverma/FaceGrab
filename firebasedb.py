import pyrebase
import urllib
import sys

firebaseConfig={
    "apiKey": "AIzaSyAGwaYIE3eTwWEkNp_QvmvHpcvUEAvGiIw",
    "storageURL":"gs://facegrab-c82ff.appspot.com/",
    "databaseURL" : "https://facegrab-c82ff-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "authDomain": "facegrab-c82ff.firebaseapp.com",
    "projectId": "facegrab-c82ff",
    "storageBucket": "facegrab-c82ff.appspot.com",
    "messagingSenderId": "414897340300",
    "appId": "1:414897340300:web:39698616f4a6c951fca0a9",
    "measurementId": "G-0F42EJJR32"
}
firebase= pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
storage=firebase.storage()

all_files = storage.child("ImageSourceDirectory").list_files()
for file in all_files:
    storage.child("ImageSourceDirectory").download(filename=file, path=os.path.basename(file))

#INSERT DATA db
#data={'result_name':"PRIYANSH VERMA",'result_cam_id':"0",'result_time':"08:59:20",'result_loc':"Local Place",'result_date':"2021-06-05"}
#db.child("csvTable").child("0206cs181118").set(data)

#GET DATA db
#print("Realtime DB")
#result=db.get()
#for res in result.each():
#    print(res.val())

#UPLOAD FILE storage
#file=input("Name of file") #local
#cloudfilename=input("File name in storage") #remote
#storage.child(cloudfilename).put(file)

#GET URL storage
#print(storage.child(cloudfilename).get_url(none))

#DOWNLOAD FILE storage
#cloudfilename=input("File name in storage: ")
#print(storage.child(cloudfilename).get_url(None))
#downloadlink=input("URL: ")
#storage.child(downloadlink).download(img)

#READ FILE storage
#path=input("enter the path want to read")
#url=storage.child(path).get_url(None)
#f=urllib.request.urlopen(url).read(url)
#print(f)

