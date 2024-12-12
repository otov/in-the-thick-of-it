import requests

api_url="https://restcountries.com/v3.1/all"

try:
    response = requests.get(api_url)
    if response.status_code==200:
        countries_data = response.json()
        print("Visu valstu nosaukumi: ")

        for country in countries_data:
            country_name = country.get("name", {}).get("common","Nezināms nosaukums")
            print(country_name)

        total_countries=len(countries_data)
        print(f"\nKopējais valstu skaits: {total_countries}")

        total_population=sum(country.get("population",0) for country in countries_data)
        average_population = total_population / total_countries if total_countries else 0
        print(f"\nVidējais iedzīvotāju skaits visās valstīs: {average_population:,.0f}")

        largest_pop_c=max(countries_data, key=lambda x: x.get("population",0))
        largest_pop_n=largest_pop_c.get("name",{}).get("common","Nezināmis nosaukums")
        largest_pop = largest_pop_c.get("population",0)
        print(f"\nValsts ar vislielāko iedzīvotāju skaitu: {largest_pop_n} ({largest_pop:,.0}) iedzīvotāji")

        total_area = sum(country.get("area",0) for country in countries_data)
        print(f"\nVisu valstu kopējā platība; {total_area} kvadrātkilometri.")

        latvia_info = next((country for country in countries_data if country.get("name",{}).get ("common") =="Latvia"), None)

        if latvia_info:
            

