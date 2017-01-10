#
# This file is a try to learn how to
# modify values within a DataFrame
#
import pandas as pd
import numpy as np

data = {
    'day1' : pd.Series([1., 1., 1.2], index=['a', 'b', 'c']),
    'day2' : pd.Series([1.2, 1., 2., 2.4], index=['a', 'b', 'c', 'd']),
    'day3' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])
}

data_unsorted = {
    'day1' : pd.Series([1., 1., 1.2], index=['a', 'b', 'c']),
    'day2' : pd.Series([1.2, 1., 2., 2.4], index=['a', 'b', 'c', 'd']),
    'day3' : pd.Series([1., 4., 3., 2.], index=['a', 'd', 'c', 'b'])
}


data_noindex = {
    'day1' : pd.Series([1., 1., 1.2]),
    'day2' : pd.Series([1.2, 1., 2., 2.4]),
    'day3' : pd.Series([1., 4., 3., 2.])
}




df = pd.DataFrame(data)
df_unsorted = pd.DataFrame(data_unsorted)
df_noindex = pd.DataFrame(data_noindex)


# print(df_unsorted);
# print(df);

# for i, row in df_noindex.iterrows():
#     print i

print(df)
print("--------------------------")

print("\ndf['day1']")
print(df['day1'])
print("--------------------------")
print("\n\ndf[df['day1'] == 1]")
print(df[df['day1'] == 1]);
print("--------------------------")

print("df.loc['a']")
print(df.loc['a'])



print(np.mean(df.loc['a']))

print("--------------------")


df['average_wrong'] = pd.Series()
df['average_ok'] = pd.Series()


# this loop goes over all the entries
# in the dataframe and sets the column 'one'
# of each row to the average


# Outside the loop, the dataframe remains unchanged
for i, row in df.iterrows():
    # this line does not work, row will remain unchanged
    # outside the loop
    row.loc[('average_wrong')] = np.mean(row)

# Outside the loop the dataframe show the correct
# average in the average_ok column
for i, row in df.iterrows():
    df.loc[i,('average_ok')] = np.mean(row)


    

    
print(df)


#for i, row in df.iterrows():
 #   print i

exit(0)

# how to add a new column to an existent DataFrame
df['newcolumn'] = pd.Series([1,2,3,4], index=['a','b','c','d'])

# this loop goes over all the entries
# in the dataframe and sets the column 'one'
# of each row to 4
# Outside the loop, the dataframe remains unchanged
for i, row in df.iterrows():
    # this line does not work, row will remain unchanged
    row.loc[('day1')] = 4

    # however, printing row looks ok
    print(row)

print(df) # column 'one' unchanged

# this loop goes over all the entries
# in the dataframe and sets the column 'one'
# of each row to 7
# Outside the loop, the dataframe remains unchanged
for i, row in df.iterrows():
    df.loc[i,('day1')] = 7
    print(row);

print(df)


