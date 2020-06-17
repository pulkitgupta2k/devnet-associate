import requests

link = "https://postman-echo.com/basic-auth"

response = requests.get(link, auth = ("postman","password"))

print(response)
print(response.text)