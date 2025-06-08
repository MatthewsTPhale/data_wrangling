# data_wrangling
In this project, I create a method named merge_all_data
This method takes in a filepath and read a pattern of filenames
of type .csv. And then it appends them to a List to create a List of DataFrames

We then traverse the created List of DataFrammes, and extract each from the List;
assigning each respective DataFrame from the List to its named DataFrame, for example,
users_df is assigned to the users DataFrame from the List and so on..

Our next step is to merge the data together, taking the user_profiles dataset and merging it with user_health dataset, then taking the supplements dataset and merging it with the experiments data.
The resulting data sets are then merged together to produce a single large DataFrame.

We continue our process of data wrangling first cleaning all the dirty columns, then dropping 
dupliates to ensure we only have quality clean data.

This sub-rountine can be adopted and the algorithm improved to handle different types of scenarios or
to make the process of data cleaning to completely run as an automated process using this kind of wrangling sub-routines.

How The Project Works:
Clone the project into your environment

