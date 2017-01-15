import pandas
import pandasql
import numpy
import re

FILENAME = 'world_population_series_217.csv'

def wrangling(filename):
  df = pandas.read_csv(FILENAME, encoding='latin-1');  

  # set Country Name as index to make easier the lecture
  # of the data
  df.set_index(df['Country Name'], inplace=True)

  # remove:
  #   - last five rows, which are not relevant for
  #     our purposes (world bank metadata)
  #   - World row
  #   - Columns with meta info
  #   - column corresponding to year 2016, which has no data
  df = df.drop(['Series Name', 'Series Code', 'Country Name', 'Country Code','2016 [YR2016]'], axis=1)
  df = df[:-5]

#  df.drop('World', inplace=True)
#  df.drop('European Union', inplace=True)
#  df.drop('Euro area', inplace=True)

  # maybe replace by the last one?
  df.replace('..',0, inplace=True)

  return df;

def population_growth(df):
  total = 0
  for key in df.keys():
    print key, numpy.array(df[key]).astype('int').sum()

def population_growing(df, interval):
  first_year = int(df.keys()[-1].split(' ')[0])
  last_year = int(df.keys()[0].split(' ')[0])

  countries = {}
  for country in df.index:
    max_growing_data = {}
    max_growing_data['grow'] = 0

    for year in range(first_year, last_year-interval):
      start_population = float(df["%d [YR%d]" % (year, year)][country])
      end_population = float(df["%d [YR%d]" % (year + interval, year + interval)][country])

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
  return growing_data


if __name__ == "__main__":
  MIN_POPULATION = 1000000
  df_population = wrangling(FILENAME)

#  population_growth(df_population)
  df_grow_countries = population_growing(df_population, 10)

  filtered =  df_grow_countries[df_grow_countries['start_population'] > MIN_POPULATION].sort_values(['grow'], ascending=False)

  print filtered.head(n=10).round(decimals=2)[['start_population','end_population', 'year', 'grow']]

  print filtered.tail(n=10).round(decimals=2)[['start_population','end_population', 'year', 'grow']]

  print filtered.loc['Spain']
  
# TODO: remove not classified
