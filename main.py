# HomeWork about JSON and XML by Igor Golovin
import json
import xml.etree.ElementTree as ET
from pathlib import Path

data_folder = Path("files/")
xmlFile = data_folder / "newsafr.xml"

data_folder = Path("files/")
jsonFile = data_folder / "newsafr.json"

minSymbols = 6

def loadJSONFile(fName):
    with open(fName, encoding="utf8") as f:
        jsonData = json.load(f)
    return jsonData

def findWordsJSON(data):
    for x in data["rss"]["channel"]["items"]:
        lst = ''.join(x['description']).split(' ')
        lstMT6 = []
        for el in lst:
            if len(el) > minSymbols:
                lstMT6.append(el)
    newLine = "\n"
    print(f"JSON file. Count of words > 6 symbols: {len(lstMT6)}{newLine}{lstMT6}")

def loadXMLFile(fName):
    tree = ET.parse(fName)
    root = tree.getroot()
    return root

def findWordsXML(data):
    for el in data.iter("description"):
        lst = ''.join(el.text).split(' ')
        lstMT6 = []
        for el in lst:
            if len(el) > minSymbols:
                lstMT6.append(el)
    newLine = "\n"
    print(f"XML file. Count of words > 6 symbols: {len(lstMT6)}{newLine}{lstMT6}")

if __name__ == '__main__':
    print("let's start!")
    print()
    findWordsJSON(loadJSONFile(jsonFile))
    findWordsXML(loadXMLFile(xmlFile))
    print("Done")
