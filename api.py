# # import requests

# # # We need coordinates to get weather data
# # latitude = 48.85   # Paris latitude
# # longitude = 2.35   # Paris longitude

# # # Build the API URL with our parameters
# # url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# # # Make the request
# # response = requests.get(url)
# # data = response.json()

# # print(data)


# import requests
# latitude = 42.3609
# longitude = -71.0579
# url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
# response=requests.get(url)
# data=response.json()
# print(data)


# import requests

# latitude = 42.3601
# longitude = -71.0589

# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# print(url)

# response = requests.get(url)
# data = response.json()

# print(data)