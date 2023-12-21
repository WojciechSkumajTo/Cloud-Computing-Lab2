import paho.mqtt.client as mqtt
import time

broker_address = "broker.hivemq.com"
port = 1883

client = mqtt.Client("mqtt_pub_client")

def on_publish(client, userdata, mid):
    print(f"Wysłano wiadomość o ID: {mid}")


client.on_publish = on_publish

client.connect(broker_address, port, 60)
client.loop_start()

# Publikacja wiadomości na różnych topic'ach z różnymi QoS
client.publish("add_data", "test", qos=1)  # QoS 0 - np. odczyt stanu
time.sleep(1)
client.publish("get_data", 23, qos=1)  # QoS 1 - np. ustawienie stanu
time.sleep(1)

client.loop_stop()
client.disconnect()


#! docker-compose build --no-cache projectMQTTpub
#! docker-compose up projectMQTTpub