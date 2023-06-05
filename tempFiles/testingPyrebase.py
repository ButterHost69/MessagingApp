import pyrebase

firebaseConfig = {
    
    "apiKey"            : "AIzaSyD4LK-KwRyO5B-SE7H5UECi1y8dXX1lA7o",
    "authDomain"        : "chatapp-903c2.firebaseapp.com",
    "projectId"         : "chatapp-903c2",
    "storageBucket"     : "chatapp-903c2.appspot.com",
    "messagingSenderId" : "596064841458",
    "appId"             : "1:596064841458:web:2713287c8b72349806aa6b"    

}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()