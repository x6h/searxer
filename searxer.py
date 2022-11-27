import json
import random

ignored_tlds = [
    ".i2p",
    ".onion"
]

instances_json_file = open("instances.json", "rt")

if not instances_json_file:
    print("failed to open instances.json file. please run update_instances.py.")
    exit(1)

instances_json = json.loads(instances_json_file.read())
instances = instances_json["instances"]
valid_instances = []

for instance in instances:
    if any(tld not in instance for tld in ignored_tlds):
        valid_instances.append(instance)

if len(valid_instances) < 1:
    print("no valid instances found.")
    exit(1)

print(random.choice(valid_instances))
