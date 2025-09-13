import requests
import json

def uni(url):
    try:
        res = requests.post(
            "https://freeseptemberapi.vercel.app/bypass",
            json={"url": url},
            headers={'User-Agent': 'Mozilla/5.0'}  # To avoid blocks
        )
        _data = res.text
        print(f"Raw Response: {_data[:200]}...")  # Debug
        
        if "message" in _data or "error" in _data.lower():
            print(f"API Error: {_data}")
            return None
        
        _j = json.loads(_data)
        return _j.get("url")
    except requests.exceptions.RequestException as e:
        print(f"Request Error (API down or network issue): {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON Parse Error: {e}")
        return None

# Example Usage
test_url = "https://lksfy.com/demo"  # Replace with your URL
result = uni(test_url)
if result:
    print(f"Direct URL: {result}")
else:
    print("Bypass failed. API may be unavailable.")
