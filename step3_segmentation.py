import sqlite3
import pandas as pd

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# 1. We create a new column called 'Segment' in our table
try:
    cursor.execute("ALTER TABLE customer_segments ADD COLUMN Segment TEXT;")
except:
    print("Column 'Segment' already exists, proceeding to update...")

# 2. The SQL CASE Statement: This is the 'Core Logic'
segment_query = """
UPDATE customer_segments
SET Segment = CASE
    WHEN Final_RFM_Score >= 13 THEN 'Champions'
    WHEN Final_RFM_Score >= 10 THEN 'Loyal Customers'
    WHEN Final_RFM_Score >= 7 THEN 'Potential Loyalists'
    WHEN Final_RFM_Score >= 4 THEN 'At Risk'
    ELSE 'Lost'
END;
"""

cursor.execute(segment_query)
conn.commit()

# 3. Verify the results
print("Phase 3 Complete: Customers have been segmented!")
final_view = pd.read_sql("SELECT Customer_ID, Final_RFM_Score, Segment FROM customer_segments LIMIT 10", conn)
print(final_view)


# Fetch everything from the SQL table back into a Pandas DataFrame

# Save the final labeled data for Power BI
all_data = pd.read_sql("SELECT * FROM customer_segments", conn)
all_data.to_csv('final_for_powerbi.csv', index=False)
print("📂 'final_for_powerbi.csv' is ready for your dashboard!")


conn.close()