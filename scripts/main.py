import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

# A Sub-rountine that takes in filenames
# and merges data from these files
# and cleans the data and returns a clean dataframe
def merge_all_data(filenames_pattern):
    #Load the files from data directory
    try: 
        files = glob.glob(filenames_pattern)
        print("Files found: ", files)
    except FileNotFoundError(filenames_pattern):
        print("Files Not found!")
    
    #Load the datasets from the csv files
    df_list = []
    for file in files:
        df = pd.read_csv(file)
        df_list.append(df)
    
    #Read the dataframes from the list of files

    try:
        experiments_df = df_list[0]
        supplements_df = df_list[1]
        health_df = df_list[2]
        users_df = df_list[3]
    except IndexError(df_list):
        print("Index Bound out Error")

    #Merge User Profiles data with User Health data
    user_health_DF = users_df.merge(health_df, on = "user_id", how = "left")

    #Merge Supplements Data with Experiments data
    supp_experi_DF = supplements_df.merge(experiments_df, on = "experiment_id", how = "left")

    #View Info of Mergers
    #print(user_health_DF.info())
    #print(supp_experi_DF.info())

    #Merge the results together
    final_merge_DF = user_health_DF.merge(supp_experi_DF, on = ["user_id","date"], how = "left")
    

    #Drop duplicate rows
    final_merge_DF = final_merge_DF.drop_duplicates(subset=["user_id","date"])
    #print(final_merge_DF.info())

    #Clean Age by checking the type of column and categorizing by age-group
    #18-25, 26-35, 36-45, 46-55, 56-65, Over 65
    def categorize_age(age):
        if pd.isna(age):
            return 'Unknown'
        age = float(age)
        if age < 18:
            return 'Under 18'
        elif age < 26:
            return '18 - 25'
        elif age < 36:
            return '26 - 35'
        elif age < 46:
            return '36 - 45'
        elif age < 56:
            return '46 - 55'
        elif age < 65:
            return '56 - 65'
        else:
            return 'Over 65'
        
    final_merge_DF['user_age_group'] = final_merge_DF['age'].apply(categorize_age)
    final_merge_DF['user_age_group'] = final_merge_DF['user_age_group'].astype('category')
    print(final_merge_DF.info())
    print(final_merge_DF['user_age_group'].head(40))

    


    #print(type(df_list[0]))    

merge_all_data("data/*.csv")