import pandas as pd

# File paths
file_path = r'D:\probpro\GenderBasedEmploymentInPakistan2023.csv'  # Update with your actual file path
cleaned_file_path = r"D:\probpro\cleaned_data.csv"  # Update with your actual save path

# Load data
data = pd.read_csv(file_path)

# Print unsorted data
print("Unsorted Data:")
print(data)

# Replace hyphen ("-") and None with NaN in the relevant columns
columns_to_fill = ['Total', 'Male', 'Female']

# Replace hyphen ("-") and None with NaN
data.replace({"-": pd.NA, None: pd.NA}, inplace=True)

# Cast columns to integer type and handle missing values
for col in columns_to_fill:
    if col in data.columns:  # Check if the column exists
        
        # Convert to numeric, handling NA values
        data[col] = pd.to_numeric(data[col], errors='coerce')
        # Cast to nullable integer type
        data[col] = data[col].astype('float')
       
        # Calculate mean, ignoring NaN
        mean_value = data[col].mean(skipna=True)
        
        # Fill missing values with the mean and cast back to integer
        data[col] = data[col].fillna(mean_value).round().astype(int)

# Print cleaned data
print("\nCleaned Data:")
print(data)

# Save cleaned data to a new CSV
data.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned data saved to: {cleaned_file_path}")
