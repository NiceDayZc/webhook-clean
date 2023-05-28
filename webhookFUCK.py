import os
import re
import requests

def find_discord_webhooks(folder_path):
    u = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
                urls = re.findall(r"https?://(?:www\.)?discord(?:app)?\.com/api(?:/v\d)?/webhooks/\d+/[^\"\s]+", text)
                print(F"scan in {file_path}")
                u.extend(urls)

    return u

folder = "./141.98.19.51"

webhook = find_discord_webhooks(folder)
c = [url.rstrip('"') for url in webhook]

for x in c:
    print(x)
    s = requests.delete(x)
    if s.status_code == 204:
        print(f"Delete {x}")
    else:
        print(f"Failed {x} {s.text}")

print("all webhook i clean")
