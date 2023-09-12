import yaml
import os
with open('docker-compose.yml') as f:
    compose = yaml.safe_load(f)

keys = [key for key in compose["services"].keys()]
s = ''
for key in range(len(keys)):
    s += f"{key}. {keys[key]}\n"
s += "q. Exit\n"
key = input(s)
if key == "q": exit()
os.system("clear")
print(f'Starting: {keys[int(key)]} ')
os.system(f'docker-compose exec {keys[int(key)]} bash')
exit()

