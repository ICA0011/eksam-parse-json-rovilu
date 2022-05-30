import json
import requests

URL = 'http://upload.itcollege.ee/~aleksei/eksam.json'


def parse_json(url):
    for course in json.loads(requests.get(url).text)["courses"]:
        if course["name"] == "Scripting languages":
            return course["code"]


if __name__ == "__main__":
    print("Scripting languages code is " + parse_json(URL))
