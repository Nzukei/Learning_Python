import pandas as pd
date_list = [{'yyyy-mm-dd : 2000-06-27'}, {'yyyy-mm-dd : 2000-09-24'}, {'yyyy-mm-dd : 2000-12-20'}]
df = pd.DataFrame(date_list, columns = {'yyyy-mm-dd'})
print(df)

def extact_year(column):
    return column.split("_")[0]
df['year'] = df['yyyy-mm-dd'].apply(extact_year)
print(df)

def get_age(year, current_year):
    return current_year - int(year)
# df['age'] = df['year'].apply(get_age, current_year=2018)'
print(df)
