from faker import Faker
import random
from database.connection import get_connection, close_connection

fake = Faker()

# Categories, device types, and example device names
categories = {
    "HouseHold": {
        "Lighting": ["Philips LED Bulb", "Syska LED Tube", "Havells CFL Lamp", "Wipro Desk Lamp"],
        "HVAC": ["LG Split AC", "Voltas Room AC", "Usha Ceiling Fan", "Bajaj Room Heater"],
        "Kitchen Appliance": ["Samsung Refrigerator", "IFB Microwave Oven", "Bajaj Toaster", "Prestige Electric Kettle", "Philips Mixer Grinder"],
        "Electronics": ["Sony TV", "Dell Laptop", "HP Desktop", "Canon Printer", "Bose Sound System"]
    },
    "Industrial": {
        "Motors": ["Siemens Conveyor Motor", "ABB Water Pump Motor", "Kirloskar Cooling Fan Motor"],
        "Machinery": ["CNC Lathe", "Milling Machine", "Hydraulic Press"],
        "Factory Lighting": ["Philips LED Floodlight", "Havells High Bay Lamp", "Syska Strip Light"],
        "HVAC": ["Blue Star Industrial AC", "Voltas Chiller", "Crompton Ventilation Fan"],
        "Sensors and IOT": ["Honeywell Temperature Sensor", "Siemens Pressure Sensor", "Bosch Humidity Sensor", "Proximity Sensor"]
    },
    "Renewable Energy": {
        "Solar Panels": ["Trina Solar 250W", "Canadian Solar 350W", "Vikram Solar 300W"],
        "Battery Storage": ["Exide Li-ion Battery Bank", "Luminous Lead-Acid Battery Pack"],
        "Charging Stations": ["Tata EV Charger Level 1", "ABB EV Charger Level 2"]
    },
    "Transport": {
        "Engine Components": ["Bosch Alternator", "Delphi Fuel Pump", "Garrett Turbocharger"],
        "Auxiliary Devices": ["Car AC Compressor", "Philips Headlights", "Sony Infotainment System"],
        "EV Devices": ["Tesla Battery Management System", "BYD EV Motor Controller", "Onboard Charger"]
    },
    "IoT Devices": {
        "Smart Plugs": ["TP-Link WiFi Smart Plug", "Wipro Zigbee Smart Plug"],
        "Wearables": ["Apple Watch", "Mi Fitness Band", "Fitbit Charge"],
        "Automation Sensors": ["Nest Motion Sensor", "Ecobee Smart Thermostat", "Xiaomi Door/Window Sensor"]
    }
}

# Function to generate realistic power ratings per type
power_ranges = {
    "Lighting": (5, 50),
    "HVAC": (50, 5000),
    "Kitchen Appliance": (100, 2000),
    "Electronics": (10, 500),
    "Motors": (200, 5000),
    "Machinery": (500, 10000),
    "Factory Lighting": (50, 500),
    "Sensors and IOT": (1, 10),
    "Solar Panels": (100, 500),
    "Battery Storage": (500, 5000),
    "Charging Stations": (1000, 7000),
    "Engine Components": (50, 500),
    "Auxiliary Devices": (50, 1500),
    "EV Devices": (200, 2000),
    "Smart Plugs": (10, 2500),
    "Wearables": (1, 20),
    "Automation Sensors": (1, 50)
}

def generate_fake_devices(total=50):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    count = 0

    while count < total:
        category = random.choice(list(categories.keys()))
        device_type = random.choice(list(categories[category].keys()))
        name = random.choice(categories[category][device_type])
        location = fake.city()
        min_power, max_power = power_ranges.get(device_type, (10, 1000))
        power_rating = round(random.uniform(min_power, max_power), 2)
        status = random.choice(["Active", "Inactive"])

        cursor.execute("""
            INSERT INTO devices (name, category, location, power_rating, status)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, category, location, power_rating, status))

        count += 1

    conn.commit()
    cursor.close()
    close_connection(conn)
    print(f"✅ Inserted {total} fake devices successfully.")

if __name__ == "__main__":
    generate_fake_devices()  # Generates 500 devices
