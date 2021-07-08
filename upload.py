import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Authorization": "Bearer ya29.a0ARrdaM93nmqj7eRns_ZzeKkjlHtZdkgEeYARKYtyYdZwTmtvZJqR-PcymbLXJIqkdZaK_pwVx_8_3_NUATWVHkaS1Z_K6cC8awCpIkInayj718hnStM1iU_s9hr330CusCcb01s0mKj93pN1E8K0tCHWi0Cl"
}
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
