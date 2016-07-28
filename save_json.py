import io
import json


## Saving data to a json file   
def save_json(filename,data):
    with io.open('resource/{0}.json'.format(filename),'w',encoding='utf-8') as f:
         f.write(json.dumps(data,indent=1))