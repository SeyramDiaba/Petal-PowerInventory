import codecademylib
import pandas as pd

# Load DataFrame 
inventory = pd.read_csv('inventory.csv')
# Inspecting First 10 rows
inventory.head(10)

# First 10 rows saved to 'staten_island'
staten_island = inventory.iloc[:10]

#Products sold at Staten Island
product_request = staten_island['product_description']

#Types of seeds sold at the Brooklyn location
seed_request = inventory[(inventory.location=='Brooklyn') | (inventory.product_type== 'seeds')]
print seed_request

# Add a column to inventory when is True when quantity is >0
inventory['in_stock']= inventory.quantity.apply(lambda x: True if x > 0 else False )
print inventory['in_stock']

# How Valuable is Petal Power
inventory['total_value'] = inventory.price * inventory.quantity
print inventory

# Description of each product for Marketing Catalog

combine_lambda = lambda row:\
'{}-{}'.format(row.product_type,row.product_description)

#Column that has complete description of each product
inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)
print inventory
