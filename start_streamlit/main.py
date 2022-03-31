import requests

from pydaisi import Daisi

def start(daisi_name, base_url="https://app.daisi.io"):
    d = Daisi(daisi_name, base_url=base_url)

    my_id = str(d.id)
    r = requests.post("http://pebble-api/pebbles/streamlit", json={"id": my_id})
    result = r.json()

    r = requests.get("http://pebble-api/pebbles/streamlit")
    result2 = r.json()

    return [result, result2]
