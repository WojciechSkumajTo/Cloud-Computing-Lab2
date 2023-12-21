import paho.mqtt.client as mqtt
import httpx


broker_address = "broker.hivemq.com"
api_url = "http://projectFastAPI:8000"

counter = 1

port = 1883

def add_data(item_id, data):
    client = httpx.Client()
    try:
        response = client.post(f"{api_url}/add_data/{item_id}?data={data}")
        return response.json()
    finally:
        client.close()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Połączono z brokerem")
    else:
        print(f"Błąd połączenia, kod: {rc}")

def on_message(client, userdata, msg):
    global counter
    add_data(counter, msg.payload.decode('utf-8'))
    counter += 1


client = mqtt.Client("mqtt_subscriber")

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port, 60)

client.subscribe("add_data", qos=1)  # QoS 1
client.subscribe("get_data", qos=0)  # QoS 0

client.loop_forever()
