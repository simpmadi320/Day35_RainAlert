import requests
from twilio.rest import Client

# Weather API Info
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = "ACa3b7696505534de4059e02d2326f0ee8"
auth_token = "ef000d968ecc5f8444b627e06a126bc5"

# SMS API Info


weather_params_Stratford = {
    "lat": 3.3700,
    "lon": -80.9822,
    "cnt": 4,
    "appid": "b99d28e7ae96031250f2d043b9e88521"
}
"""

weather_params_Rock_River = {
    "lat": 49.46692,
    "lon": -83.33312,
    "cnt": 4,
    "appid": "b99d28e7ae96031250f2d043b9e88521"
}
"""
response = requests.get(OMW_Endpoint, params=weather_params_Stratford)
#print(response.status_code)
response.raise_for_status()
weather_data = response.json()
#print(weather_data)

condition_code = weather_data["cod"]

if (int(condition_code) == 200):

    weather_list = weather_data["list"]

    print(weather_list)

    bring_umbrella = False

    for i in range(0, len(weather_list)):
        weather_code = weather_list[int(i)]["weather"][0]["id"]
        print(weather_code)
        if (weather_code < 700):
            bring_umbrella = True
            break

    if (bring_umbrella):

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an ☔",
            from_="+19283252781",
            to="+12262366722"
        )
        print(message.status)
    else:
        print("No umbrella needed")
else:
    print("Condition Code Error: " + str(condition_code))