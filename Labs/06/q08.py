#name: ibrahim johar farooqi
#date: 25 september 2024
#lab: 06
#task: 8

import pandas as pd

products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')

print("first 5 rows of products dataframe:\n")
print(products_df.head(5))

print("\nfirst 5 rows of orders dataframe:\n")
print(orders_df.head(5))

print("last 10 rows of products dataframe:\n")
print(products_df.tail(10))

print("\nlast 10 rows of orders dataframe:\n")
print(orders_df.tail(10))

merged_df = pd.merge(orders_df, products_df, on='ProductID')
merged_df['Revenue'] = merged_df['Price'] * merged_df['Quantity']
total_revenue = merged_df['Revenue'].sum()
print(f"\ntotal revenue generated from all orders: ${total_revenue}")

#top 5 best & low selling
product_sales = merged_df.groupby('ProductID')['Quantity'].sum()

#best-selling products
best_selling_products = product_sales.nlargest(5)
print("\ntop 5 best-selling products (by quantity):")
print(best_selling_products)

#low selling products
low_selling_products = product_sales.nsmallest(5)
print("\ntop 5 low-selling products (by quantity):")
print(low_selling_products)

top_selling_product_ids = best_selling_products.index
top_selling_products_df = products_df[products_df['ProductID'].isin(top_selling_product_ids)]

most_common_category = top_selling_products_df['Category'].mode()[0]
print(f"\nmost common product category in the top 5 best-selling products is: {most_common_category}")

#average price of products in each category.
average_price_by_category = products_df.groupby('Category')['Price'].mean()
print("\naverage price of products in each category:")
print(average_price_by_category)

#convert 'OrderDate' to datetime
merged_df['Order Date'] = pd.to_datetime(merged_df['Order Date'], format='%m-%d-%Y')

merged_df['Day'] = merged_df['Order Date'].dt.day
merged_df['Month'] = merged_df['Order Date'].dt.month
merged_df['Year'] = merged_df['Order Date'].dt.year

#calculate total revenue (day, month, year)
total_revenue_by_day = merged_df.groupby('Day')['Revenue'].sum()
total_revenue_by_month = merged_df.groupby('Month')['Revenue'].sum()
total_revenue_by_year = merged_df.groupby('Year')['Revenue'].sum()

#day, month, year with highest revenue
best_day = total_revenue_by_day.idxmax()
best_month = total_revenue_by_month.idxmax()
best_year = total_revenue_by_year.idxmax()

print(f"\nday with highest total revenue: {best_day}")
print(f"month with highest total revenue: {best_month}")
print(f"year with the highest total revenue: {best_year}")

#total revenue for each month.
monthly_revenue_df = merged_df.groupby('Month')['Revenue'].sum().reset_index()
print("\ntotal revenue for each month:")
print(monthly_revenue_df)

#check for null vals/invalid chars
print("\ncheck for null values in Products DataFrame:")
print(products_df.isnull().sum())

print("\ncheck for null values in Orders DataFrame:")
print(orders_df.isnull().sum())

products_df = products_df.dropna()
orders_df = orders_df.dropna()