import json
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
import requests

cook = <paste_your_cookie_here>

uid = cook["uid"]

subjects = ["course1", "course2", "course3", "course4", "course5"]

for subject in subjects:

    print(subject)
    print()

    r = requests.get('https://hello.iitk.ac.in/api/'+subject+'/users/stats/'+uid, headers=cook)
    response = json.loads(r.content)

    for item in response['imported_marks']:
        print(item["title"], ":", item["marks"])
    print("-----------------------------------------------------------")
