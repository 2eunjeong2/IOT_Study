# MQTT 메세지를 주고받는 스크립트 파일
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("device/01/temperature")

def on_message(client, userdata, msg):
    print(msg.topic+": "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)
client.loop_forever()