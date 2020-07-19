from django.shortcuts import render, redirect
import json
import requests
import re

## Função para buscar os dados da url da Obrazul
def bringProductList():
    ## Realizando o GET e atribuindo o array
    resultJson = requests.get('https://www.obrazul.com.br/api/recruitment/products/')
    if(resultJson.status_code == 200):
        resultJson = json.loads(resultJson.content)
        listProducts = resultJson["products"]
    
    return listProducts


# -----------------------------------

## Função para renderizar todos produtos
def allProduct(request):

    ## Definindo variaveis e arrays
    objPosition = 0
    allProducts = []

    ## Buscando url e atribuindo ela a variavel
    listProducts = bringProductList() 
    
    ## Percorredendo o Array de objetos e buscando os dados de acordo com o input do usuario
    for obj in listProducts:
        eachProduct = listProducts[objPosition]

        store = eachProduct["store"]
        storeLocation = store["location"]
        storeAddress = "Rua: " + storeLocation["address"] + ", " + "Nº " + storeLocation["address_number"] + ", Bairro: " + storeLocation["neighborhood"] + " " + storeLocation["city"] + "-" + storeLocation["state"]

        eachProduct = {
        'name' : eachProduct["name"],
        'price' : eachProduct["price"],
        'picture' : eachProduct["picture"],
        'price' : eachProduct["price"],
        'storeName' : store["name"],
        'storePhone' : store["phone"],
        'storeAddress' : storeAddress
        }

        ## Nova lista com todos os produtos que correspondem com o input do usuario
        allProducts.append(eachProduct)
        objPosition += 1
            
    return render(request, 'allProducts.html', {'allProducts': allProducts})


# -----------------------------------

## Função para filtrar os produtos de acordo com o input do usuario
def filteringProduct(request):

    ## Definindo variaveis e arrays
    objPosition = 0
    searchResult = []

    ## Pegando o valor inserido pelo usuario
    userInput = request.GET.get('searchField', None)
    print("Essa foi a pesquisa -->> ", userInput) 

    ## Buscando url e atribuindo ela a variavel
    listProducts = bringProductList() 
    
    ## Percorredendo o Array de objetos e buscando os dados de acordo com o input do usuario
    for obj in listProducts:
        selectedObject = listProducts[objPosition]

        ## É verificado se o input do usuario corresponde com algo do fullname do produto ou com name da store e então o atribui a nova lista
        if(re.search(str(userInput), selectedObject["fullname"], re.IGNORECASE) 
            or re.search(str(userInput), selectedObject["store"]["name"], re.IGNORECASE)):

            store = selectedObject["store"]
            storeLocation = store["location"]
            storeAddress = "Rua: " + storeLocation["address"] + ", " + "Nº " + storeLocation["address_number"] + ", Bairro: " + storeLocation["neighborhood"] + " " + storeLocation["city"] + "-" + storeLocation["state"]

            eachProduct = {
            'name' : selectedObject["name"],
            'price' : selectedObject["price"],
            'picture' : selectedObject["picture"],
            'price' : selectedObject["price"],
            'storeName' : store["name"],
            'storePhone' : store["phone"],
            'storeAddress' : storeAddress
            }

            ## Nova lista com todos os produtos que correspondem com o input do usuario
            searchResult.append(eachProduct)
            objPosition += 1

        else:
            objPosition += 1
            
    return render(request, 'searchResult.html', {'searchResult': searchResult})