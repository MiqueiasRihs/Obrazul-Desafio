from django.shortcuts import render
import json
import requests
# from django.template.defaultfilters import register

# @register.filter(name='dict_key')
# def dict_key(d, k):
#     '''Returns the given key from a dictionary.'''
#     return d[k]

def show_index(request):
    obj_num = 0
    resultJson = requests.get('https://www.obrazul.com.br/api/recruitment/products/')
    if(resultJson.status_code == 200):
        resultJson = json.loads(resultJson.content)
        products = resultJson["products"]

    for obj in products:
        obj_num += 1
        objSelected = products[obj_num]
        if(objSelected["name"] == "RIPA PRATA REFERÊNCIA 466"):
            name = objSelected["name"]
            price = objSelected["price"]
            picture = objSelected["picture"]
            price = objSelected["price"]
            store = objSelected["store"]
            storeName = store["name"]
            storePhone = store["phone"]
            storeLocation = store["location"]

            storeAddress = "Rua: " + storeLocation["address"] + ", " + "Nº " + storeLocation["address_number"] + ", Bairro: " + storeLocation["neighborhood"] + storeLocation["city"] + "-" + storeLocation["state"]

            print(name)
            print(price)
            print(picture)
            print(price)
            print(storeName)
            print(storeAddress)
 
            break
        else:
            continue

    return render(request, 'index.html', {'dictionary': resultJson})