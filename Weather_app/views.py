import requests
from django.shortcuts import render
from requests.exceptions import Timeout, ConnectionError, RequestException
from django.conf import settings

API_KEY = settings.WEATHER_API_KEY



def home(request):
    city = None
    temp = None
    condition = None
    humidity = None
    icon = None
    wind = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")

        url = "http://api.weatherapi.com/v1/current.json"

        params = {
            "key": API_KEY,
            "q": city,
            "aqi": "no"
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()  # handles 4xx / 5xx

            data = response.json()

            # WeatherAPI specific error handling
            if "error" in data:
                error = data["error"]["message"]
            else:
                temp = data["current"]["temp_c"]
                condition = data["current"]["condition"]["text"]
                humidity = data["current"]["humidity"]
                wind = data["current"]["wind_kph"]
                icon = "https:" + data["current"]["condition"]["icon"]

        except Timeout:
            error = "Request timed out. Please try again."
        except ConnectionError:
            error = "No internet connection."
        except RequestException:
            error = "Something went wrong with the weather service."
        except KeyError:
            error = "Unexpected response from server."

    context = {
        "city": city,
        "temp": temp,
        "condition": condition,
        "humidity": humidity,
        "wind": wind,
        "icon": icon,
        "error": error
    }

    return render(request, "index.html", context)












