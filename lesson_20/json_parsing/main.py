import json
from requests import get, post


# response = get("https://petstore.swagger.io/v2/store/inventory")
# print(response.json())

data = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2021-09-11T08:50:34.083Z",
  "status": "placed",
  "complete": True
}
response = post(url="https://petstore.swagger.io/v2/store/order", json=data)
print(response.json())