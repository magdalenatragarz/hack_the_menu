import json
import argparse

from pizza import Pizza

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--cheese', nargs='+', help='List of cheese ingredients')
parser.add_argument('-o', '--others', nargs='+', help='List of other ingredients')
parser.add_argument('-v', '--vege', nargs='+', help='List of vegetable ingredients')
parser.add_argument('-m', '--meat', nargs='+', help='List of meat ingredients')
parser.add_argument('-s', '--size', choices=['big', 'medium', 'small'], help='Size', required=True)
args = parser.parse_args()

meat = []
vege = []
others = []
cheese = []
size = "big"

with open('prices.json', 'r') as f:
    prices = json.load(f)

with open('ingredients.json', 'r') as f:
    menu = json.load(f)

for kind, value in parser.parse_args()._get_kwargs():
    if value is not None:
        if kind == "meat":
            meat = value
        elif kind == "others":
            others = value
        elif kind == "vege":
            vege = value
        elif kind == "cheese":
            cheese = value
        elif kind == "size":
            size = value

result = {}

for pizza in menu:
    pizza_obj = Pizza(
        menu[pizza][size]['price'],
        menu[pizza]['ingredients']['meat'],
        menu[pizza]['ingredients']['vegetables'],
        menu[pizza]['ingredients']['cheese'],
        menu[pizza]['ingredients']['others'],
        size,
        prices)
    pizza_obj.swap(meat, vege, cheese, others)
    result[pizza] = pizza_obj.get_final_price()

for name, price in sorted(result.items(), key=lambda item: item[1])[:1]:
    print(name.capitalize() + ":", price)



