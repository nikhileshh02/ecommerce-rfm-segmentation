import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- Part A: GENERATE SYNTHETIC DATA ---
np.random.seed(42)
num_customers = 10000
num_transaction = 50000     # More transaction than customers ensures repetition

# Generate 10,000 unique Customer IDs
customers_pool = np.arange(10001, 10001 + num_customers)

# Randomly assign those IDs to 50,000 transactions
customer_ids = np.random.choice(customers_pool, num_transaction)
dates = [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 420)) for _ in range(num_transaction)]
amounts = np.random.uniform(5, 1000, num_transaction)

df = pd.DataFrame({'CustomerID': customer_ids, 'Date': dates, 'Amount': amounts})

# --- PART B: RFM CALCULATION ---
# we'll pretend today is one after the latest date in our data 
today = df['Date'].max() + timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'Date': lambda x: (today - x.max()).days, # Recency   => days_since_Last_Purchase
    'CustomerID': 'count',                    # Frequency => total_orders
    'Amount': 'sum'                           # Monetary  => total_spent
})

rfm.columns = ['Days_Since_Last_Purchase', 'Total_Orders', 'Total_Spent']

# --- PART C: SCORING (1 TO 5)--- (The Brains of the Project)
# 5 is best (low recency, high frequency, high monetary)
rfm['R_Score'] = pd.qcut(rfm['Days_Since_Last_Purchase'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Total_Orders'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Total_Spent'], 5, labels=[1, 2, 3, 4, 5])

#Total Score
rfm['Total_score'] = rfm['R_Score'].astype(int) + rfm['F_score'].astype(int) + rfm['M_score'].astype(int)

# 1. We already renamed the metrics in Part B. 
# 2. Now let's rename the Total_score to something more professional.
rfm = rfm.rename(columns={'Total_score': 'Final_RFM_Score'})

# 3. CRITICAL STEP: Turn the ID into a real column and rename it
rfm_final = rfm.reset_index() 
rfm_final = rfm_final.rename(columns={'CustomerID': 'Customer_ID'})

# 4. Save the high-quality CSV
rfm_final.to_csv('final_segmented_data.csv', index=False)

print(f"Phase 1 Scaling Complete!")
print(f"File saved with {len(rfm_final)} unique customers.")
print(rfm_final.head()) # Look at your beautiful clean headers!