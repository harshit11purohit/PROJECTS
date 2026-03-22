import pandas as pd
import xml.etree.ElementTree as ET

CSV_FILE = "weather_data.csv"
EXCEL_FILE = "weather_data.xlsx"
XML_FILE = "weather_data.xml"

import pandas as pd

def to_csv(df, filename="weather.csv"):
    df.to_csv(filename, index=False)
    print(f"\nCSV saved as: {filename}")

def to_excel(df, filename="weather.xlsx"):
    df.to_excel(filename, index=False)
    print(f"\nExcel saved as: {filename}")

def to_xml(df, filename="weather.xml"):
    df.to_xml(filename, index=False)
    print(f"\nXML saved as: {filename}")


# Convert DataFrame → CSV
def convert_to_csv(df):
    df.to_csv(CSV_FILE, index=False)
    return CSV_FILE


# Convert DataFrame → Excel
def convert_to_excel(df):
    df.to_excel(EXCEL_FILE, index=False)
    return EXCEL_FILE


# Convert DataFrame → XML
def convert_to_xml(df):
    root = ET.Element("WeatherData")

    for index, row in df.iterrows():
        city_element = ET.SubElement(root, "City")

        ET.SubElement(city_element, "Name").text = str(row.get("city", ""))
        ET.SubElement(city_element, "Temperature").text = str(row.get("temperature", ""))
        ET.SubElement(city_element, "Humidity").text = str(row.get("humidity", ""))
        ET.SubElement(city_element, "Weather").text = str(row.get("weather", ""))

    tree = ET.ElementTree(root)
    tree.write(XML_FILE, encoding="utf-8", xml_declaration=True)

    return XML_FILE
