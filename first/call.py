import httpx

def fetch_data():
    return httpx.get("https://httpbin.org/uuid").text