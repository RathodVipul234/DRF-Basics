import json

import requests
import io
import json
URL = 'http://127.0.0.1:8000/update/'
def update():
    data = {
        'id': 1,
        'name': 'raj',
        'city': 'goa',
        'roll': 106,
    }
    import pdb;pdb.set_trace()
    json_data = json.dumps(data)
    res = requests.put(url=URL,data=json_data)
    data = res.json()
    print(data)

update()
