import requests
import logging


download_path = "./"

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)


def get_file_name(url):
 image_name = url.split("?")
 image_name = image_name[0].split("/")
 image_name = image_name[len(image_name)-1]
 return image_name
 

path = input("Enter the complete source path\n")

try:
 with open(path,"r") as source_file:
  data = source_file.read()
  data = data.split("display_resources")
 for i in range(1,len(data)):
  src = data[i].split("src")
  src = src[3].split("config_width")
  image_url = src[0][3:(len(src[0])-3)].replace("\\","")
  logging.info("Downloading : "+image_url)
  response = requests.get(image_url, stream=True)
  if response.status_code == 200:
   open(download_path+get_file_name(image_url), 'wb').write(response.content)
   logging.info("Download Successful "+image_url)
  else:
   logging.error("Unable to download the file.Please check the URL "+image_url)
except FileNotFoundError:
 logging.error("Unable to locate the file : "+path)
except Exception as e:
 logging.error(e)



 
