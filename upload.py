import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = {"Authorization": "Bearer auth token"}
para = {
    "name": "some.mp4",
}
files = {
    "data": ("metadata", json.dumps(para), "application/json; charset=UTF-8"),
    "file": open("./some.mp4", "rb"),
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files,
)
print(r.text)
