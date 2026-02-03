Project Name: SkyScript CLI Weather
Description
SkyScript is a lightweight Python command-line tool that fetches real-time weather data for any city or country in the world. By utilizing the requests library to interface with the wttr.in service, it provides a clean, text-based breakdown of current atmospheric conditions, temperature, humidity, and pressure.

Key Features
Simple Interface: Just enter the city name to get instant results.

Zero API Keys: Uses the wttr.in service, so no complex registration or API keys are required for basic use.

Structured Output: Parses raw plain-text data into a readable format for the user.

Error Handling: Includes basic try-except blocks to handle network issues or invalid city names.

How it Works: The Data Flow
The script follows a classic Client-Server Request-Response cycle:

User Input: The user provides a city/country name via the terminal.

Request: Python's requests library sends a GET request to the server.

Processing: The server returns a formatted string containing weather specifications.

Parsing: The script splits the response string into a list and prints individual components (Condition, Temp, etc.).

Installation & Usage
Clone the repository:

Bash
git clone https://github.com/your-username/SkyScript.git
Install dependencies:

Bash
pip install requests
Run the script:

Bash
python weather_script.py
Technical Stack
Language: Python 3.x

Library: requests

API Service: wttr.in
