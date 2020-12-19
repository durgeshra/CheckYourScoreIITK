import json
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
import requests

username = "username"
password = "password"

cj = CookieJar()
opener = build_opener(HTTPCookieProcessor(cj))

login_data = urlencode({"name": username, "pass": password, "form_build_id":"form-xSwXpgQhmYTvWYD6viHi37fo4MlfZSuLS1aCd1Tde64","form_id":"user_login_form","op":"SIGN+IN"}).encode("utf-8")

opener.open("https://hello.iitk.ac.in/user/login", login_data)

cook = {}
cookie = ""
for entry in cj:
    if entry.name=="uid" or entry.name=="token":
        cook[entry.name] = entry.value
    cookie += entry.name+"="+entry.value+"; "
cook["Cookie"]=cookie

print(cook)