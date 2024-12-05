import requests

#url = "https://fakestoreapi.com/products?limit=5"
url = "https://fakestoreapi.com/products/category/jewelery"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exeptions.RequestExeption as e:
    print(f"Error fetching data: {e}")

