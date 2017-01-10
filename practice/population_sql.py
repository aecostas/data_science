import pandas
import pandasql
import numpy

FILENAME = 'world_population_series2.csv'

data = pandas.read_csv(FILENAME, encoding='latin-1');

# set Country Name as index to make easier the lecture
# of the data
data.set_index(data['Country Name'], inplace=True)

# remove:
#   - last five rows, which are not relevant for
#     our purposes (world bank metadata)
#   - World row
#   - Columns with meta info
#   - column corresponding to year 2016, which has no data
data = data.drop(['Series Name', 'Series Code', 'Country Name', 'Country Code','2016 [YR2016]'], axis=1)
data = data[:-5]

data.drop('World', inplace=True)


q = """
   select * from data;
"""
result = pandasql.sqldf(q.lower(), locals())

print result

