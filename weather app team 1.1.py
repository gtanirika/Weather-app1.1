import requests

def get_weather(city_name):
    try:
        # Construct URL for wttr.in (simple weather service)
        url = f"https://wttr.in/{city_name}?format=%C+%t+%h+%P+%r"
        
        # Send GET request to wttr.in
        response = requests.get(url)
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # The result is returned as plain text
            weather_info = response.text.split(' ')  # Split the response into separate items
            
            # Display each specification on a new line
            print(f"Weather information for {city_name}:")
            print(f"Condition: {weather_info[0]}")
            print(f"Temperature: {weather_info[1]}")
            print(f"Humidity: {weather_info[2]}")
            print(f"Pressure: {weather_info[3]}")
           
        else:
            print("Error: Unable to retrieve weather information.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Input city name and call the function
city_name = input("Enter city or country name: ")
get_weather(city_name)
