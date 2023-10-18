import requests
import random
import time

# URL of the transit information system where data will be sent
TRANSIT_INFO_URL = "https://your-transit-info-api.com/data-endpoint"

# Simulated IoT Sensor for Ridership
class RidershipSensor:
    def get_ridership_data(self):
        # Simulate ridership data (e.g., number of passengers)
        riders = random.randint(0, 100)
        return {"passenger_count": riders}

# Main loop
def main():
    ridership_sensor = RidershipSensor()

    try:
        while True:
            ridership_data = ridership_sensor.get_ridership_data()
            print(f"Sending Ridership Data: {ridership_data}")

            # Send ridership data to the transit information system via HTTP POST request
            response = requests.post(TRANSIT_INFO_URL, json=ridership_data)

            if response.status_code == 200:
                print("Data sent successfully")
            else:
                print(f"Failed to send data. HTTP status code: {response.status_code}")

            time.sleep(30)  # Simulate sending data every 30 seconds

    except KeyboardInterrupt:
        pass

if __name__ == "__main":
    main()
