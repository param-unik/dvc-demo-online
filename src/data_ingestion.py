import numpy as np
import pandas as pd
import os

url = "https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv"
df = pd.read_csv(url)

df = df.iloc[:, 3:]

df = df[df["Length of Membership"] > 1]

df.drop(columns=["Avg. Session Length"], inplace=True)
df.to_csv(os.path.join("data", "customer.csv"))
