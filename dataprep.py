
# %%
import os
import pandas as pd
import numpy as np

data = pd.read_csv('./sentiment/data/Women-Dresses-Reviews-Dataset.csv', index_col=0) # ignore 1st col
df = data[:1200]
df

# %%
sentiment = pd.read_csv('./sentiment/data/combined.csv', index_col=False)
sentiment

# %%
merged = pd.concat([df, sentiment], axis=1)
merged

# %%
# Check NaN values
a = merged.isna().any(axis=1)
if len(a>=2): # check more than 2 times NaN in cols
    b = merged[merged.isna().any(axis=1)]
    print(b.head())

# %%
import calendar

total_rows = 1200

month_rows = {
    1: int(total_rows * 0.06),   # January
    2: int(total_rows * 0.03),   # February (Reduced)
    3: int(total_rows * 0.05),  
    4: int(total_rows * 0.075),   # April (Reduced)
    5: int(total_rows * 0.06),  # May
    6: int(total_rows * 0.105),  # June
    7: int(total_rows * 0.155),  # July
    8: int(total_rows * 0.035),  # August (Reduced)
    9: int(total_rows * 0.045),  # September (Reduced)
    10: int(total_rows * 0.085),  # October
    11: int(total_rows * 0.135),  # November
    12: int(total_rows * 0.165),  # December
}

start_date = pd.to_datetime('2022-01-01')
end_date = pd.to_datetime('2022-12-31')
dates = []


for month, rows in month_rows.items():
    # Calculate the number of days in the current month
    _, last_day = calendar.monthrange(start_date.year, month)
    
    # Generate date values within the current month
    date_range = pd.date_range(
        start=start_date.replace(month=month, day=1),
        end=end_date.replace(month=month, day=last_day),
        periods=rows
    )
    
    # Append date values to the list
    dates.extend(date_range)

date_df = pd.DataFrame({'date': dates})

df1 = merged.merge(date_df, left_index=True, right_index=True)

#%%
# Display the first few rows of the DataFrame
df1

# %%
import matplotlib.pyplot as plt
# Create a histogram to show the distribution of dates
plt.figure(figsize=(10, 6))
plt.hist(df1['date'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Dates')
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the histogram
plt.show()

#%%
df1.to_csv('./sentiment/data/merged.csv', index=False)

# %%
df1.describe()
# %%
print(df1.department_name.astype('category'))
print(df1.class_name.astype('category'))
# %%
