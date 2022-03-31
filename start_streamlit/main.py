import requests

from pydaisi import Daisi

def start(daisi_name):
    d = Daisi(daisi_name)

    my_id = str(d.id)
    r = requests.post("http://pebble-api/pebbles/streamlit", json={"id": my_id})
    result = r.json()

    return result
