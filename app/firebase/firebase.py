import firebase_admin
from firebase_admin import credentials
from google.cloud import storage

class FireBase:
  def __init__(self):
    cred = credentials.Certificate("app/firebase/customed-links.json")
    self.firebase_app = firebase_admin.initialize_app(cred)
    self.storage_client = storage.Client.from_service_account_json('app/firebase/customed-links.json')
    self.bucket = self.storage_client.bucket(bucket_name="customed-links.appspot.com")
  
  def add_image(self, link):
    blob = self.bucket.blob(link)
    blob.upload_from_filename('app/databases/images/{}'.format(link))
    blob.make_public()
    return blob.public_url
