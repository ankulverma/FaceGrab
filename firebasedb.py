import pyrebase

firebaseConfig = {
    "apiKey": " ",
    "storageURL": " ",
    "databaseURL": " ",
    "authDomain": " ",
    "projectId": " ",
    "storageBucket": " ",
    "messagingSenderId": " ",
    "appId": " ",
    "measurementId": " ",
    "serviceAccount": " "
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage = firebase.storage()

#TO DOWNLOAD STORAGE DIRECTORY
#path = "DownloadImages"
#all_files = storage.child("ImageSourceDirectory").list_files() #Enter the name of the folder
#for file in all_files:
#    try:
#        print(file.name+" Downloading")
#        file.download_to_filename(file.name)
#    except:
#       print('Images Downloaded')

# download photo_download = input("enter the name of the file to be downloaded : ") storage.child(
# "ImageSourceDirectory").child(photo_download).download("",photo_download) storage.child(
# "ImageSourceDirectory").child(photo_download).download(filename="umeed",path=os.path.basename(photo_download))

#RETURN VALUE TO SEARCH

from Search import *
def returnValues(id):
    flag = False
    result = db.child("csvTable").get()
    for res in result.each():
        if res.key() == id:
            flag = True
    return flag

#result = db.child("csvTable").get()
#for res in result.each():
#    db.child("csvTable").remove()


# INSERT DATA db
# data={'result_name':"PRIYANSH VERMA",'result_cam_id':"0",'result_time':"08:59:20",'result_loc':"Local Place",'result_date':"2021-06-05"}
# db.child("csvTable").child("0206cs181118").set(data)

# GET DATA db
# print("Realtime DB")
# result=db.get()
# for res in result.each():
#    print(res.val())

# UPLOAD FILE storage
# file=input("Name of file") #local
# cloudfilename=input("File name in storage") #remote
# storage.child(cloudfilename).put(file)

# GET URL storage
# print(storage.child(cloudfilename).get_url(none))

# DOWNLOAD FILE storage
# cloudfilename=input("File name in storage: ")
# print(storage.child(cloudfilename).get_url(None))
# downloadlink=input("URL: ")
# storage.child(downloadlink).download(img)

# READ FILE storage
# path=input("enter the path want to read")
# url=storage.child(path).get_url(None)
# f=urllib.request.urlopen(url).read(url)
# print(f)
