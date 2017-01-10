import pandas
import pandasql
import numpy

FILENAME = 'world_population_series.csv'

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

# maybe replace by the last one?
data.replace('..',0, inplace=True)

# evolution of the population from 1967
for key in data.keys():
  print key, numpy.array(data[key]).astype('int').sum()

# most growing countries during 10 years
interval = 10
first_year = 1967
last_year = 2016
countries = {}
for country in data.index:
  max_growing_data = {}
  max_growing_data['grow'] = 0

  for year in range(first_year, last_year-interval):
    start_population = float(data["%d [YR%d]" % (year, year)][country])
    end_population = float(data["%d [YR%d]" % (year + interval, year + interval)][country])

    if start_population == 0:
      continue;
    
    grow = ((end_population - start_population) / start_population)*100;

    if grow > max_growing_data['grow']:
      max_growing_data['year'] = year
      max_growing_data['grow'] = grow
      max_growing_data['start_population'] = start_population
      max_growing_data['end_population'] = end_population
      
  countries[country] = max_growing_data

growing_data = pandas.DataFrame(countries).transpose()

print growing_data.sort_values(['grow'], ascending=False)

#  for year in data.loc[(country),:]:
#    print country, year

# TODO: remove not classified, European Union, Euro area?
