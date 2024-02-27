from faker import Faker
import pandas as pd

fake = Faker()

# Headers
headers = [
    "Name", "email","answer", "comment", "sent", "responded", "Company_Number", "Company_Name", "region"
]

# Generate mock data
data = []
for _ in range(50):
    row = [
        fake.name(), fake.email(), fake.random_int(min=1, max=10), fake.text(), 
        fake.date(), fake.date(), fake.random_int(min=1000, max=9999), fake.company(), 
        fake.state()
    ]
    data.append(row)
    
# Create DataFrame
df = pd.DataFrame(data, columns=headers)

# Specify the folder path where you want to save the Excel file and the filename
output_path = "C:/Users/Jammie/OneDrive/Coders Bookshelf/Portfolio/Data Analyst/Python_EDA_1/data/mock_data.xlsx"
# Save the DataFrame to Excel in the specified folder
# df.to_excel(output_path, index=False)


# # Save DataFrame to Excel
# excel_file = 'mock_data.xlsx'
# df.to_excel(excel_file, index=False)
