import json
import requests
import os
import sys
import time
import crontab
import pandas

# getting JSON file and saving it 
df = pandas.read_json('https://data.nasa.gov/resource/y77d-th95.json')

# Save df to as local csv file
df.to_csv('crontab/data/data.csv')

# create a new file in the current working directory
cwd = os.getcwd()
print(cwd)
now = time.time()
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

with open(cwd + '/file1_' + nowStr + '.txt', 'w') as f:
    f.write(str(df))
