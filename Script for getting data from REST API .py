import requests
import sys
import dateutil.parser 

print ("KALKULATOR WALUT")

try:
    currency = sys.argv[1]
except IndexError:
    currency = input("Podaj walutę: ")

currency = currency.upper()

try:
    date_as_str = sys.argv[2]
except IndexError:
    date_as_str = input("Podaj datę: ")

try:
    date = dateutil.parser.parse(date_as_str)
except ValueError:
    print("Invalid date format")
    sys.exit(1)

date_for_url = date.strftime('%Y-%m-%d')

# Utworzenie adresu URL
URL = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date_for_url}/?format=json"

# Pobranie kursu waluty z danego dnia 
response = requests.get(URL)
if response.status_code == 404:
    print("Brak danych")
    sys.exit(2)
if not response.ok:
    print("Unexpected server response")
    sys.exit(3)

json = response.json()
try:
    rate = json['rates'][0]['mid']
except (ValueError, KeyError):
    print("Invalid server response")
    sys.exit(4)

print(f"1{currency} = {rate} PLN w dniu {date.day}/{date.month}/{date.year}")