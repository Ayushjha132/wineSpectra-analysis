import pandas as pd

def overall_data(df):
    production_loc = df['Countrys'].nunique()
    wine_varieties = df['Names'].nunique()
    color_varieties = df['color_wine'].nunique()
    rated_wines = (df['Ratings'] > 0).sum()
    over_df = pd.DataFrame([production_loc, wine_varieties, color_varieties, rated_wines], index=['Total Producation Location', 'Total Wine Varities', 'Total Color Availability', 'Total Number of Rated Wines'], columns=['Overall Data'])
    
    return over_df


def ml_available(df):
    df = df[df['ML'] != 0]
    unique_values_ml = df['ML'].unique()
    return unique_values_ml

def ml_record(ml_available, df):
    df = df[df['ML'] != 0]
    ml_counts_array = df['ML'].value_counts().reindex(ml_available, fill_value=0).values
    return ml_counts_array

def price(df):
    # df = df[df['Prices'] != 0]
    cost_of_wine = df['Prices']
    return cost_of_wine