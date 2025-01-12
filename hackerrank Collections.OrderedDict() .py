""" Collections.OrderedDict()
Task

You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item. """

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

order = OrderedDict()
for _ in range(int(input())):
    item, space, price = input().rpartition(' ')
    order[item] = order.get(item, 0) + int(price)
for item, price in order.items():
    print(item, price)