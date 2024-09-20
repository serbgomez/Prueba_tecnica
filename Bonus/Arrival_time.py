# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:05:08 2024

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

# Create an auxiliar dataframe with the theoretical arrival times (I just did it manually looking at the countries,
    # there may some mistakes with eastern Europe countries)
count = sup['Country'].unique().tolist()
theor = [10, 20, 20, 45, 45, 20, 20, 45, 45, 45, 45, 45, 45, 20, 20, 20, 20, 20, 45, 20, 20, 20, 20, 20, 20]

time = pd.DataFrame({'Country': count, 'Exp_time': theor})

# Merging

# Merge the expected times to the suppliers
sup_2 = pd.merge(sup, time, on='Country', how='left')

# Merge everything to the product DataFrame
prod_2 = pd.merge(prod, head, on='Invoice', how='left')
prod_2.rename(columns={'Supplier': 'IDSupplier'}, inplace=True)

prod_3 = pd.merge(prod_2, sup_2, on='IDSupplier', how='left')

# Convert dates to datetime objects and get the real arrival time in days
prod_3['OrderDate'] = pd.to_datetime(prod_3['OrderDate'])
prod_3['InboundDate'] = pd.to_datetime(prod_3['InboundDate'])

real_time = prod_3['InboundDate']-prod_3['OrderDate']

prod_3['Real_time'] = [i.days for i in real_time]
prod_3['Year'] = prod_3['OrderDate'].dt.year

# Create the output dataframe with the requested data
df = prod_3.groupby(['Year', 'IDSupplier', 'SupplierName', 'Product'], as_index=False).agg({
    'Real_time': 'mean',
    'Exp_time': 'mean'
})

# Compute the difference between true arrival time and expectation
# Positive values indicate that the arrival took longer than expected
df['Time_dif'] = df['Real_time'] - df['Exp_time']

df.to_csv(out_path+'Arrival_times.csv')