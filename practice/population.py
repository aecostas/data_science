import pandas
import pandasql
import numpy

FILENAME = 'world_population_series.csv'



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

  df.drop('World', inplace=True)

  # maybe replace by the last one?
  df.replace('..',0, inplace=True)

  return df;

def population_evolution(df):
  for key in df.keys():
    print key, numpy.array(df[key]).astype('int').sum()

def population_growing(df):    
  # most growing countries during 10 years
  interval = 10
  first_year = 1967
  last_year = 2016
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
  df_population = wrangling(FILENAME)
  population_evolution(df_population)
#  df_grow = population_growing(df_population)
  
#  print df_grow[df_grow['start_population'] > 1000000].sort_values(['grow'], ascending=False)



# TODO: remove not classified, European Union, Euro area?


