from bs4 import BeautifulSoup
import requests

class get_image:

    def get_img(self, url):
        
        current_url = f'{url}'
        #print(current_url)    
        
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")   

        player_names = soup.findAll("img")
        temp_dict = {}
        
        if len(player_names) != 0:
            
            for i, image in enumerate(player_names):
                
                #print(image)
                try:

                    temp_dict[i] = image["data-srcset"]                  

                except:
                    try:

                        temp_dict[i] = image["data-src"]       
                        

                    except:
                        try:

                            temp_dict[i] = image["data-fallback-src"]  
                            
                                
                        except:
                            try:

                                temp_dict[i] = image["src"]   
                                
                            except:
                                pass

        return temp_dict