import sqlite3
import pandas as pd

# 1. Load the csv we just made
rfm_data = pd.read_csv('final_segmented_data.csv')

# 2. Connect to  (or create) a database file called 'ecommerce.db'
conn = sqlite3.connect('ecommerce.db')

# 3. Push the data into a table called 'customer_segments'
rfm_data.to_sql('customer_segments', conn, if_exists='replace', index=False)

print(f"Phase 2 Complete: 'ecommerce.db' created with {len(rfm_data)} rows!")

# Let's test a SQL Query right here in python!
query = "SELECT * FROM customer_segments WHERE Final_RFM_Score >= 12 LIMIT 5"
top_customers = pd.read_sql(query, conn)

print("\n--- Top 5 Champions (SQL Query Result) ---")
print(top_customers)

conn.close()