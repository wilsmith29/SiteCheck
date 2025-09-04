import requests
from selenium import webdriver

def check_site_status(url):
    response = requests.get(url)
    return response.status_code

def run_tests(url):
    pass

url = input("Copy URL here: ")

status = check_site_status(url)

if 200 <= status < 300:
   #run_tests(url)
   print("Website active")

else:
   print("Website is down, cannot run tests")


