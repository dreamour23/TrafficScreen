from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from time import gmtime, strftime
import os

cwd = os.getcwd()
service = Service(cwd + "\chromedriver.exe")
options = webdriver.ChromeOptions()
options = Options()
options.add_argument("start-maximized")
options.headless = True
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1920, 1080)

Input = input('Please give Coordinate and Zoom Level (e.g. 53.1234,14.6789,17): ').split(",")
Lat = Input[0]
Lon = Input[1]
Zoom = Input[2]
Zoom_TT_int = int(Input[2])-1.25
Zoom_TT = str(Zoom_TT_int)

def mydrive (Lat=Lat,Lon=Lon,Zoom_TT=Zoom_TT):
    url = 'https://mydrive.tomtom.com/en_gb/#mode=viewport+viewport=' + Lat +',' + Lon + ',' + Zoom_TT + ',0,-0+ver=3'
    driver.get(url)
    sleep(20)
    filename = 'TomTom_' + (strftime("%Y-%m-%d %H%M", gmtime()))
    driver.implicitly_wait(100)
    driver.get_screenshot_as_file(filename + '.png')   

def plan (Lat=Lat,Lon=Lon,Zoom=Zoom):
    url = 'https://plan.tomtom.com/en/?p=' + Lat +',' + Lon + ',' + Zoom + 'z'
    driver.get(url)
    sleep(10)
    filename = 'Plan_' + (strftime("%Y-%m-%d %H%M", gmtime()))
    driver.implicitly_wait(100)
    driver.get_screenshot_as_file(filename + '.png') 

def googlemaps (Lat=Lat,Lon=Lon,Zoom=Zoom):
    url = 'https://www.google.com/maps/@' + Lat + ',' + Lon + ',' + Zoom + 'z/data=!5m1!1e1'
    driver.get(url)
    sleep(10)
    filename = 'GoogleMaps_' + (strftime("%Y-%m-%d %H%M", gmtime()))
    driver.implicitly_wait(100)
    driver.get_screenshot_as_file(filename + '.png')    

def waze (Lat=Lat,Lon=Lon,Zoom=Zoom):
    url = 'https://embed.waze.com/iframe?' + 'zoom=' + Zoom + '&lat=' + Lat + '&lon=' + Lon + '&ct=livemap'
    driver.get(url)
    sleep(10)
    filename = 'Waze_' + (strftime("%Y-%m-%d %H%M", gmtime()))
    driver.implicitly_wait(100)
    driver.get_screenshot_as_file(filename + '.png')     

def here (Lat=Lat,Lon=Lon,Zoom=Zoom):
    url = 'https://wego.here.com/traffic/explore?map=' + Lat + ',' + Lon + ',' + Zoom + ',traffic'
    driver.get(url)
    sleep(10)
    filename = 'Here_' + (strftime("%Y-%m-%d %H%M", gmtime()))
    driver.implicitly_wait(100)
    driver.get_screenshot_as_file(filename + '.png')   

mydrive()
#plan()
googlemaps()
waze()
here()