from flask import Flask, render_template, request, send_file
from fetch_data import fetch_weather_data
from process_data import process_weather_data
from convert_data import to_csv, to_excel, to_xml

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    data = None
    df = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        raw = fetch_weather_data(city)
        data, df = process_weather_data(raw)

    return render_template("index.html", data=data, df=df)

@app.route("/download/<fmt>")
def download(fmt):
    city = request.args.get("city")

    if not city:
        return "City not provided", 400

    raw = fetch_weather_data(city)
    _, df = process_weather_data(raw)

    if df.empty:
        return "No data to download", 400

    fmt = fmt.lower()
    if fmt == "csv":
        path = to_csv(df)
    elif fmt == "excel":
        path = to_excel(df)
    elif fmt == "xml":
        path = to_xml(df)
    else:
        return "Unsupported format", 400

    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
