import requests
from datetime import datetime

TOKEN = "qwertyuioplkjhgfdsazxcvbnm"
USERNAME = "mdazeem"
GRAPH_ID = "graph1619"

pixela_endpoint = "https://pixe.la/v1/users"

users_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# res = requests.post(url=pixela_endpoint,json=users_params)
# print(res.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "min",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
# print(today.strftime("%Y-%m-%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today?\n")
}
response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
new_pixel = {
    "quantity":"15"
}
# res = requests.put(url=update_endpoint,json=new_pixel,headers=headers)
# print(res.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# res = requests.delete(url=delete_endpoint,headers=headers)
# print(res.text)