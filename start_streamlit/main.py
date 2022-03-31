import requests

from pydaisi import Daisi

def start(daisi_name, base_url="https://app.daisi.io"):
    d = Daisi(daisi_name, base_url=base_url)

    r = requests.get(f"{base_url}/pebble-api/pebbles/streamlit")
    result2 = r.json()

    my_id = str(d.id)
    r = requests.post(f"{base_url}/pebble-api/pebbles/streamlit", json={"id": my_id})
    result = r.json()

    mystr = f'Previous Streamlit App: {result2}<br>New Streamlit App: {result}<br><br>View it here: <a target="_blank" href="{base_url}/st">Click!</a>'

    return mystr
