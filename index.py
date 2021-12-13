import requests
from PIL import Image
# using time module
import time
from time import ctime

#range replace 1 to any...
ra = int(input("Starts From :"))
i = int(input("Ends Till :"))
imagelist = []

def download_img_total(time):
   
    for i in range(ra,time) :
        
        ####### post man requiest ############
        # past your request url
        url = "https://image.slidesharecdn.com/datareportal20200130gd001digital2020globaldigitaloverviewjanuary2020v01-200130025629/95/digital-2020-global-digital-overview-january-2020-v01-"+str(i)+"-638.jpg?cb=1596755441"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
               ##############
            
        with open('temp image_\/{0}.jpg'.format(i),'wb') as f:
            f.write(response.content)


def img_2_pdf_total(time):
    for i in range(ra ,time) :
        # create temp image_ folder and past path below
        image1 = Image.open(r'C:\Users\kiran\push github\temp image_\/'+str(i)+'.jpg') 
        im1 = image1.convert('RGB')
        imagelist.append(im1)
        
download_img_total(i)    
img_2_pdf_total(i)

# ts stores the time in seconds
ts = time.time()
ts = str(ctime(ts)).replace(":","-")
 # create  PDF Here folder and past path below
imagelist[0].save(r'C:\Users\kiran\push github\PDF Here\/'+str(ts)+'_from_'+str(ra)+'_total_'+str(i)+'.pdf',save_all=True, append_images=imagelist)
imagelist = []

#delete images
#-------------------------------#
#importing os module
import os

#providing the path of the folder
#r = raw string literal
folder_path = (r'C:\Users\kiran\push github\temp image_')

#using listdir() method to list the files of the folder
test = os.listdir(folder_path)

#taking a loop to remove all the images
#using ".png" extension to remove only png images
#using os.remove() method to remove the files

for images in test:
    if images.endswith(".jpg"):
        os.remove(os.path.join(folder_path, images))
#------------------------------------------------------#
print("done")
