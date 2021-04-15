import requests
response = requests.get('https://google.com/')
print(type(response), response)
for x in response:
    print(x)
print("\n"*3, "*" * 50, "\n"*3)
print(response.status_code)