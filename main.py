import pandas as pd

# Read the CSV files into DataFrames
df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')

# Concatenate the DataFrames into a single DataFrame
combined_df = pd.concat([df1, df2, df3])

# Clean and filter the rows
combined_df['product'] = combined_df['product'].str.strip().str.lower()
filtered_df = combined_df[combined_df['product'] == 'pink morsel']
filtered_df.loc[:,'sales'] = filtered_df['quantity'] * filtered_df['price']

# Select and reorder the desired columns
output_df = filtered_df[['sales', 'date', 'region']]

# Save the output DataFrame to a CSV file
output_df.to_csv('output.csv', index=False)
