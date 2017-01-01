#
# This file is a try to learn how to
# modify values within a DataFrame
#
import pandas as pd
import numpy as np

d = {
    'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])
}

df = pd.DataFrame(d)

# how to add a new column to an existent DataFrame
df['newcolumn'] = pd.Series([1,2,3,4], index=['a','b','c','d'])

# this loop goes over all the entries
# in the dataframe and sets the column 'one'
# of each row to 4
# Outside the loop, the dataframe remains unchanged
for i, row in df.iterrows():
    # this line does not work, row will remain unchanged
    row.loc[('one')] = 4

    # however, printing row looks ok
    print(row)

print(df) # column 'one' unchanged

# this loop goes over all the entries
# in the dataframe and sets the column 'one'
# of each row to 7
# Outside the loop, the dataframe remains unchanged
for i, row in df.iterrows():
    df.loc[i,('one')] = 7
    print(row);

print(df)


