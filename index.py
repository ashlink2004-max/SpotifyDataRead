import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv ('.env')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENNT_SECRET')

#creating token for token
def access_token():
    #combine client_id an dclient_secret
 try:
    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    #converts the credentials string into base64 format This is required for HTTP Basic Authentication
    encoded_credentials=base64.b64encode(credentials.encode()).decode()

    response=requests.post(
         'https://accounts.spotify.com/api/token',
          headers={"Authorization":f'Basic {encoded_credentials}'},
          data={'grant_type': 'client_credentials'})

 #    print("Token Generated Successfully...")
    return response.json()['access_token']
 except Exception as e:
    print("Error in Token Generation...",e)
# print(access_token())


#LATEST RELEASE IN SPOTIFY
def get_new_release():
   try:
    token = access_token()
    headers={"Authorization":f"Bearer {token}"}
    Param={'limit':50}
    response=requests.get('https://api.spotify.com/v1/browse/new-releases',headers=headers,
                           params=Param)
    # print(response)
    if response.status_code==200:
        # print (response.json())
       data=response.json()
       release=[]
       albums=data['albums']['items']
       for i in albums:
            a={
                'album_name':i['name'],
                'release_date':i['release_date'],
            }
            print(a)
   except Exception as e:
       print("Error in latest release data fetching...",e)
get_new_release()

