import pandas as pd



def readFile(filename):
    file = pd.read_excel(filename)
    # Use the rename function with a lambda to capitalize the first letter of each column
    file.columns = file.columns.map(lambda x: x.capitalize())
    
    return file

def split_columns(file):
    # Split the 'Name' column into 'First_Name' and 'Surname'
    split_names = file['Name'].str.split(expand=True)
    
    # Drop the original 'Name' column
    file.drop('Name', axis=1, inplace=True)

    # Insert the split columns at the desired position (in this case, at column 'A' and 'B')
    file.insert(0, 'First_Name', split_names[0])
    file.insert(1, 'Surname', split_names[1])

    return file

# A transformation that counts the occurrences of each unique value in the 'Answer' column 
# and creates a new column 'Answer_Count' in the DataFrame 'file' to store these counts.
def answer_count(file):
    file['Answer_Count'] = file.groupby('Answer')['Answer'].transform('size')
    # Name of the column next to which you want to insert 'Answer_Count'
    column_name_to_insert_next_to = 'Answer'
    # Find the index of the specified column
    index_to_insert_next_to = df.columns.get_loc(column_name_to_insert_next_to)
    # Use the insert method to insert the 'Answer_Count' column at the next index
    file.insert(index_to_insert_next_to + 1, 'Answer_Count', file.pop('Answer_Count'))
    return file


def rename_cols(file, new_cols):
    new_cols = {'Company_number':'Company_Number', 'Company_name':'Company_Name'}
    # Use the rename method to change column headers
    file.rename(columns=new_cols, inplace=True)
    return file


# Instance of the functions
if __name__ == "__main__":
    df = readFile("C:/Users/Jammie/OneDrive/Coders Bookshelf/Portfolio/Data Analyst/Python_EDA_1/data/mock_data.xlsx")
    
    df_1 = split_columns(df)
    df_2 = answer_count(df_1)
    df_3 = rename_cols(df_2, ['Company_Number', 'Company_Name'])
  
    # Specify the folder path where you want to save the Excel file and the filename
    output_path = "C:/Users/Jammie/OneDrive/Coders Bookshelf/Portfolio/Data Analyst/Python_EDA_1/data/survey_data.xlsx"
    # Save the DataFrame to Excel in the specified folder
    df.to_excel(output_path, index=False)

