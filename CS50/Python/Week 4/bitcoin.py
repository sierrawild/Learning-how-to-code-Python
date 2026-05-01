import sys, requests

API =  "https://rest.coincap.io/v3/assets/bitcoin?apiKey=58bf743777eb5564aff08700f5df595e476fd4ecd7ab896ee0eb7e9353fd452a"

r = requests.get(API)
bitcoin = r.json()
price = float(bitcoin["data"]["priceUsd"])




try:
    buy = float(sys.argv[1])
    print(f'${buy * price:,.4f}')
except ValueError:
    print('Command-line argument is not a number')
    sys.exit(1)
except IndexError:
    print('Missing command-line argument')
    sys.exit(1)
