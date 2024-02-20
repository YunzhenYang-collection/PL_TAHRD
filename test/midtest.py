import pandas as pd
import csv

df = pd.read_csv("https://github.com/41171119H/PL_TAHRD/blob/main/test/adult.csv")

# If df is successfully defined, proceed
if 'Income' in df.columns:
    # Calculate the mean, standard deviation, and median for the Income column
    Income_mean = np.mean(df['Income'])
    Income_std = np.std(df['Income'], ddof=1)
    Income_median = np.median(df['Income'])

    # Print the result
    print(f"平均值: {Income_mean}")
    print(f"標準差: {Income_std}")
    print(f"中位數: {Income_median}")

else:
    print("找不到薪資列 'Income'")

df
