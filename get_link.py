from bs4 import BeautifulSoup
import requests

class get_link:

    def __init__(self) -> None:
        pass
 
    def all_link_get(self,url):

            req = requests.get(url)
            soup = BeautifulSoup(req.text, "lxml")   

            links = soup.find_all("a")
            temp_dict = {} 
            counter = 0
            for a in links:
                link_temp = str(a.get('href'))
                if link_temp.startswith('https:'):
                    
                    temp_dict[str(counter)] = str(a.get('href'))
                    
                else:
                    temp_dict[str(counter)] = (url + str(a.get('href')))

                counter = counter + 1
            return temp_dict


    def deneme(self,temp_dict:dict):
        
        gecici = self.ekleme(temp_dict.values())

        temp_dict.clear()

        temp_dict = gecici

        #print(temp_dict)

        with open("linkler.txt", "w+") as f:
            f.write(str(temp_dict))

        return temp_dict


    def ekleme(self,gelen):
        
        temp_dict = {}
        counter = 0
        for a in gelen:
            dizi = self.all_link_get(a)
            for b in (dizi.values()):
                if b not in temp_dict.values():
                    temp_dict[str(counter)] = b
                    counter = counter + 1
            
        return temp_dict
