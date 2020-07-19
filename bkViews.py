from django.shortcuts import render, redirect
import json
import requests
import re
# from django.template.defaultfilters import register

# @register.filter(name='dict_key')
# def dict_key(d, k):
#     '''Returns the given key from a dictionary.'''
#     return d[k]

def show_index(request):
    prodprod = request.GET.get('searchField')
    print(prodprod)
    obj_num = 0
    allProducts = []
    resultJson = requests.get('https://www.obrazul.com.br/api/recruitment/products/')
    if(resultJson.status_code == 200):
        resultJson = json.loads(resultJson.content)
        products = resultJson["products"]
    
    for obj in products:
        objSelected = products[obj_num]
        if(re.search(str(prodprod), objSelected["fullname"], re.IGNORECASE)):
        # if(str(prodprod) in objSelected["fullname"] or str(prodprod) in objSelected["name"]):
            store = objSelected["store"]
            storeLocation = store["location"]
            storeAddress = "Rua: " + storeLocation["address"] + ", " + "Nº " + storeLocation["address_number"] + ", Bairro: " + storeLocation["neighborhood"] + " " + storeLocation["city"] + "-" + storeLocation["state"]

            eachProduct = {
            'name' : objSelected["name"],
            'price' : objSelected["price"],
            'picture' : objSelected["picture"],
            'price' : objSelected["price"],
            'storeName' : store["name"],
            'storePhone' : store["phone"],
            'storeAddress' : storeAddress
            }

            allProducts.append(eachProduct)
            obj_num += 1

        else:
            obj_num += 1

    return render(request, 'index.html', {'allProducts': allProducts})