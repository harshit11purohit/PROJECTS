import pandas as pd

def process_weather_data(raw):
    # Handle error case
    if "error" in raw:
        return {"error": raw["error"]}, pd.DataFrame()

    main = raw.get("main", {})
    weather = raw.get("weather", [{}])[0]

    processed = {
        "city": raw.get("name", "N/A"),
        "temperature": main.get("temp", "N/A"),
        "humidity": main.get("humidity", "N/A"),
        "weather": weather.get("description", "N/A")
    }

    df = pd.DataFrame([processed]).fillna("N/A")

    return processed, df

