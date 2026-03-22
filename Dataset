# 2. LOAD DATASET
# ================================
df = pd.read_csv("insurance_data_linear.csv")

print("First 5 rows:")
display(df.head())

print("\nDataset Info:")
# Capture df.info() output to filter it
old_stdout = sys.stdout
sys.stdout = new_stdout = io.StringIO()
df.info()
sys.stdout = old_stdout # Restore stdout

filtered_output = [line for line in new_stdout.getvalue().splitlines() if "memory usage" not in line and "dtypes" not in line]
print("\n".join(filtered_output))

print("\nStatistical Summary:")
display(df.describe())
