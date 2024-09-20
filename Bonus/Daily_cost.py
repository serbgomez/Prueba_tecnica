# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:38:26 2024

@author: serbg
"""

import pandas as pd
import pycountry
import numpy as np

path = 'DatosProyecto/'
out_path = 'Output/'
deli = ';'

# Extract all data to dataframes
currency = pd.read_csv(path+'daily_currencies.csv', delimiter=deli)
sup = pd.read_csv(path+'suppliers.csv', delimiter=deli)
head = pd.read_csv(path+'invoices_header.csv', delimiter=deli)
prod = pd.read_csv(path+'invoices_products.csv', delimiter=deli)

# Compute the total cost of each product order
prod['Cost'] = prod['PurchasePrice (Unit)']*prod['Quantity']


# Merge the dataframes to get a big one containing all the data
# Some columns have been renamed for the purpose of this merging

# 1 - Merge invoice_head with invoice_prod  on the Invoice ID column
prod_2 = pd.merge(prod, head, on='Invoice', how='left')
prod_2.rename(columns={'Supplier': 'IDSupplier'}, inplace=True)

# 2 - Merge with Supplier on the Supplier ID
prod_3 = pd.merge(prod_2, sup, on='IDSupplier', how='left')
prod_3.rename(columns={'InvoiceDate': 'Date'}, inplace=True)

# 3 - Merge with the currency excahnge data
# I manually checked that the company only worked with EUR and USD
prod_4 = pd.merge(prod_3, currency, on='Date', how='left')

# There are some missing values in the currency exchange. Fill those with the 
    #latest knwon value (Close was used as reference value for the exchange)

# Reorder the dataframe on date order
prod_4['Dates'] = pd.to_datetime(prod_4['Date'])
prod_4.set_index('Dates', inplace=True)
prod_4.sort_index(inplace=True)
prod_4['Close'].ffill(inplace=True)
# To make sure the first values are filled as well, do a backwards fill (they take the earliest knwon value)
prod_4['Close'].bfill(inplace=True)

# Adjust the currency when necesary
prod_4['Adj_Cost'] = prod_4.apply(lambda row: row['Cost'] if row['Currency_x'] == 'EUR' else row['Cost']*row['Close'], axis=1)

# Save the wanted data
daily_cost = prod_4.groupby('Date', as_index=False)['Adj_Cost'].sum()
daily_cost.to_csv(out_path+'Daily_cost.csv')
