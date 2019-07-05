paises = ["Colombia", "Suiza", "Peru", "Qatar"]

def country_delete_duplicate(country):

    if paises.count(country) > 0:
        
        paises.remove(country)
        print("pais eliminado")
    else:
        paises.append(country)
        print("agregado pais")
