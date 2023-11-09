import get_image
import get_link
import image_download
import os
import shutil
def remove_folder(path):
    if os.path.exists(path):
         shutil.rmtree(path)
try: 
    with open("dosyalar.txt","r") as r:
                        daTATA = r.read()
                        split = daTATA.split("//")
                        for i in split:
                            remove_folder(i)

           
    os.remove("dosyalar.txt")
except:
     pass

derinlik = int(input("Derinlik giriniz: "))

first_url = input("URL giriniz: ")

main_dictionary = {}

# Tanımlama
f_image = get_image.get_image()
f_url = get_link.get_link()

url = {0: first_url}

if derinlik <= 1:
    image = f_image.get_img(url[0])
    os.mkdir("0_dosya")
    with open("dosyalar.txt","a") as f:
            f.write("0_dosya//")
    image_download.d_img(image,"0")
    
else:
    for i in range(1,derinlik):
        url = f_url.deneme(url)
    for i in url:
        print("link " + i)
        image = f_image.get_img(url[i])
        os.mkdir(str(i)+"_dosya")
        with open("dosyalar.txt","a") as f:
            f.write(str(i)+"_dosya//")
        
        image_download.d_img(image,i)


