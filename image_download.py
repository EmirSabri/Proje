import requests

def d_img(dict,url=None):
    
    for key, value in dict.items():
        try:
            
            response = requests.get(value).content

            with open(str(url) + "_dosya\image_" + str(key) + ".jpg", "wb+") as f:
                f.write(response)
        except:
            pass