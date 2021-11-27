import requests
import io
import json

# import pdb;pdb.set_trace()
URL = 'http://127.0.0.1:8000/update/'


def show_student(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


def post_data():
    data = {
    'name': "ddh",
    'roll': 1000,
    'city': "patanr"
    }

    json_data = json.dumps(data)

    r = requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

    # data = {
    #     'name': 'raj',
    #     'city': 'goa',
    #     'roll': 106,
    # }
    #
    # json_data = json.dumps(data)
    # # import pdb;pdb.set_trace()
    #
    # r = requests.post(url=URL, data=json_data)
    # data = r.json()
    # print(data)


def update_data():
    data = {
        'id': 1,
        'name': 'raj',
        'city': 'goa',
        'roll': 106,
    }

    json_data = json.dumps(data)

    # r = requests.put(url=url, data=json_data, )
    res = requests.put(url = URL,data=json_data)
    import pdb;pdb.set_trace()
    data = res.json()
    print(data)

def delete_data(id):
    data = {'id':id}

    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    data = r.json()
    print(data)

delete_data(2)

# show_student(1)
# post_data()
# update_data()
