from picamera import PiCamera
from time import sleep
from email.base64mime import body_encode
from urllib import response
import mux_python
import requests
import os
import json
from picamera import PiCamera
from time import sleep
from subprocess import call 

camera = PiCamera()

def convert(file_h264, file_mp4):
    # Record a 15 seconds video.
    camera.start_recording(file_h264)
    sleep(10)
    camera.stop_recording()
    print("Rasp_Pi => Video Recorded! \r\n")
    # Convert the h264 format to the mp4 format.
    command = "MP4Box -add " + file_h264 + " " + file_mp4
    call([command], shell=True)
    print("\r\nRasp_Pi => Video Converted! \r\n")
    

# Record a video and convert it (MP4).
convert('/home/rasberry/Desktop/video.h264', '/home/rasberry/Desktop/video.mp4')

from firebase_admin import credentials, initialize_app, storage
# Init firebase with your credentials

cred = credentials.Certificate("mini-project-dc97a-acb0bad81186.json")
initialize_app(cred, {'storageBucket': 'mini-project-dc97a.appspot.com'})

# Put your local file path 
fileName = "/home/rasberry/Desktop/video.mp4"
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)
print('firebse')

# Opt : if you want to make public access from the URL
blob.make_public()

print("your file url", blob.public_url)


configuration = mux_python.Configuration()
configuration.username = '63e178aa-4a4c-414e-8208-c9e8269ce9a1'
configuration.password = 'oosqBdi8q6jeBLOVgYBbCQMLmK2Hatu2FIk/CgO84wSul2Pq3tWV+H3UOQAQMWjqLX+7CG6VXiu'

uploads_api = mux_python.DirectUploadsApi(mux_python.ApiClient(configuration))
print("111")

create_asset_request = mux_python.CreateAssetRequest(playback_policy=[mux_python.PlaybackPolicy.PUBLIC])
create_upload_request = mux_python.CreateUploadRequest(timeout=7200, new_asset_settings=create_asset_request, cors_origin="*")
create_upload_response = uploads_api.create_direct_upload(create_upload_request)
print(create_upload_response)

def formatted_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

headers = {
}

json_data = {
    'input': blob.public_url,
    'playback_policy': [
        'public',
    ],
}

response = requests.post('https://api.mux.com/video/v1/assets', headers=headers, json=json_data, auth=('63e178aa-4a4c-414e-8208-c9e8269ce9a1', 'oosqBdi8q6jeBLOVgYBbCQMLmK2Hatu2FIk/CgO84wSul2Pq3tWV+H3UOQAQMWjqLX+7CG6VXiu'))
formatted_print(response.json())
if response.status_code == 200:
    print("sucessfully fetched the data")
    formatted_print(response.json())
else:
    print(f"Hello person, there's a {response.status_code} error with your request")





