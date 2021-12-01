import requests
import io
import json

# import pdb;pdb.set_trace()
URL = 'http://127.0.0.1:8000/third_party_crud_app/'


def show_student(id=None):

    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    header = {'content-type' : 'application/json'}
    r = requests.get(url=URL, data=json_data,headers=header)
    data = r.json()
    print(data)


def post_data():
    data = {
    "name": "abc",
    "roll": 199,
    "city": "rgoa"
    }

    json_data = json.dumps(data)
    header = {'content-type' : 'application/json'}
    r = requests.post(url=URL,data=json_data,headers=header)
    data = r.json()
    print(data)

def update_data():
    data = {
        'id': 1,
        'name': 'raj',
        'city': 'goa',
        'roll': 106,
    }

    json_data = json.dumps(data)

    res = requests.put(url = URL,data=json_data)
    data = res.json()
    print(data)

def delete_data(id):
    data = {'id':id}

    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    data = r.json()
    print(data)

# show_student()
# post_data()
update_data()
delete_data(1)
