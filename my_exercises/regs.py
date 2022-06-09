import re

price = 'Price: $18,569.50'
expression = 'Price: \$([0-9,]*\.[0-9]*)'

matches = re.search(expression, price)
# print(matches.group(0))
# print(matches.group(1))

price_without_coma = matches.group(1).replace(',', '')
print(price_number := float(price_without_coma))
