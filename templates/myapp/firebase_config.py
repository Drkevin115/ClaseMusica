import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("clase-de-musica-3591c-firebase-adminsdk-e8y4a-0f76b59b29.json")
firebase_admin.initialize_app(cred)



