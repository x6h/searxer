import urllib.request
import json

url = urllib.request.urlopen("https://searx.space/data/instances.json")
data = json.dumps(json.loads(url.read()), indent=4)

data_file = open("instances.json", "wt")
data_file.write(str(data))
data_file.close()

print("pulled searx instances")
