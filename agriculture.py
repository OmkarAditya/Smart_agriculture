import serial
import requests
import time

# Open the serial connection
ser = serial.Serial('COM6', 9600)  # Replace 'COM8' with your Arduino's serial port

# Create an empty list to store the values
values_list = []

# Read values from Arduino
while True:
    # Read the line from serial
    line = ser.readline()
    
    # Convert the line to float and append it to the list
    try:
        value = float(line.strip())
        values_list.append(value)
    except ValueError:
        pass
    
    # Check if the desired number of values is reached
    if len(values_list) >= 4:  # Adjust this condition according to your array size
        # Print the received values
        print(values_list)
        
        # Send data to ThingSpeak
        api_key = 'YOUR_API_KEY'  # Put your ThingSpeak API key here
        url = f'https://api.thingspeak.com/update?api_key=YOUR_API_KEY'

        # Prepare the data payload
        data = {"api_key": api_key}
        
        for i, value in enumerate(values_list):
            field_name = f"field{i+1}"
            data[field_name] = value
    
        # Send the data using HTTP GET request
        response = requests.get(url, params=data)

        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print("Data sent to ThingSpeak successfully.")
        else:
            print("Failed to send data to ThingSpeak.")
            print("Response:", response.text)
        
        # Clear the values list
        values_list = []
    
    # # Wait for 5 seconds
    # time.sleep(5)

# Close the serial connection
ser.close()
