import requests
import json

def bypass_url(short_url):
    try:
        # Use bypass.city API
        api_url = f"https://bypass.city/api/bypass?apikey=free&url={short_url}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise error for bad status
        
        data = response.json()
        direct_url = data.get('destination') or data.get('url')
        
        if direct_url:
            print(f"Direct URL: {direct_url}")
            return direct_url
        else:
            print("No direct URL found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON response from API.")
        return None

# Example Usage
test_url = "https://lksfy.com/demo"  # Replace with your URL
bypass_url(test_url)
