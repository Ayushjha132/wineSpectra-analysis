import pandas as pd



def overall_data(df):
    production_loc = df['Countrys'].nunique()
    wine_varieties = df['Names'].nunique()
    color_varieties = df['color_wine'].nunique()
    rated_wines = (df['Ratings'] > 0).sum()
    
    over_df = pd.DataFrame([production_loc, wine_varieties, color_varieties, rated_wines], index=['Total Producation Location', 'Total Wine Varities', 'Total Color Availability', 'Total Number of Rated Wines'], columns=['Overall Data'])
    
    return over_df

