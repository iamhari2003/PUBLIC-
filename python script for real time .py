import paho.mqtt.client as mqtt
import random
import time

# MQTT Broker (You should replace this with your broker's information)
MQTT_BROKER = "mqtt.eclipse.org"
MQTT_PORT = 1883

# MQTT Topics
TOPIC = "iot/location"

# Simulated IoT Sensor
class GPSSensor:
    def get_location(self):
        latitude = round(random.uniform(0, 90), 6)  # Simulate latitude data
        longitude = round(random.uniform(0, 180), 6)  # Simulate longitude data
        return f"Latitude: {latitude}, Longitude: {longitude}"

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print(f"Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message {mid} published")

# Create MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the Broker
client.connect(MQTT_BROKER, MQTT_PORT)

# Start the MQTT loop
client.loop_start()

# Initialize the GPS Sensor
gps_sensor = GPSSensor()

try:
    while True:
        location_data = gps_sensor.get_location()
        print(f"Sending Location: {location_data}")
        # Publish location data to the MQTT topic
        client.publish(TOPIC, location_data)
        time.sleep(5)  # Simulate sending data every 5 seconds

except KeyboardInterrupt:
    pass

# Disconnect from the Broker
client.disconnect()
