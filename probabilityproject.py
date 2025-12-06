import pandas as pd
from scipy.stats import ttest_ind

# File paths
file_path = r'D:\probpro\GenderBasedEmploymentInPakistan2023.csv'

# Load data
data = pd.read_csv(file_path)

# Filter data for employment in rural and urban areas
rural_employment = data[(data['Indicator'] == 'Employed') & (data['Area Type'] == 'Rural')]
urban_employment = data[(data['Indicator'] == 'Employed') & (data['Area Type'] == 'Urban')]

# Extract Male and Female employment rates
rural_male = rural_employment['Male']
rural_female = rural_employment['Female']
urban_male = urban_employment['Male']
urban_female = urban_employment['Female']

# Perform t-tests
t_rural, p_rural = ttest_ind(rural_male, rural_female, nan_policy='omit')
t_urban, p_urban = ttest_ind(urban_male, urban_female, nan_policy='omit')

# Output results
print("T-test results for Rural Employment:")
print(f"T-statistic: {t_rural}, P-value: {p_rural}")

print("\nT-test results for Urban Employment:")
print(f"T-statistic: {t_urban}, P-value: {p_urban}")
