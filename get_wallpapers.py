import requests
import json
import ctypes
import sys
SPI_SETDESKWALLPAPER = 20 

if len(sys.argv) == 2:
	query_params = {'format': 'js', 'idx':str(sys.argv[1]), 'n':'1'}
else:
	query_params = {'format': 'js', 'idx':'0', 'n':'1'}
url = 'https://www.bing.com/HPImageArchive.aspx'
response = requests.get(url, params=query_params);
response_json = response.json()
base_url = 'https://bing.com'
for image in response_json['images']:
	full_url = base_url + image['url']
	wallpaper_response = requests.get(full_url, stream=True)
	if wallpaper_response.status_code == 200:
		file_path = 'E:\\workspace\\downloaded_wallpapers\\' + image['hsh'] + '.jpg'
		with open(file_path, 'wb') as file:
			for chunk in wallpaper_response:
				file.write(chunk)
		ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path , 0)