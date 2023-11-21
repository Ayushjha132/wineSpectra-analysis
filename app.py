import streamlit as st
import pandas as pd
import chardet
from function import overall_data

# decoding csv file format any unknown encoder. 
def read_csv_auto_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    data = pd.read_csv(file_path, encoding=result['encoding'])
    return pd.DataFrame(data)

df = read_csv_auto_encoding('dataset/wine_dataset.csv')

# sidebar
st.sidebar.markdown('# :rainbow[WineSpectra Analysis]')

# sidebar menu
sideMenu = st.sidebar.radio(
    "Select an option",
    ("Overall Analysis", "Wine-Varity Analysis", "ML Analysis", "Red-Wine Analysis", "White-Wine Analysis", "Pink & Rosé-Wine Analysis", "Sparkling & Champagne Analysis", "About")
)

# OVERALL ANALYSIS PAGE
if sideMenu == "Overall Analysis":
    st.title("Overall Analysis")

    st.text(r'''
              [⠀⡄⣾⣿⠀]
               |⣿⣿⣿|
               |⣿⣿⣿|
               |⣿⣿⣿|
               |⣿⠉⢹|
              |⢸⣿⣿⣿⡇|
             |⠀⣿⣿⣿⣿⣿⡀|
            |⠀⣸⣿⣿⣿⣿⣿⣇⠀|
            |⢠⣿⣿⣿⣿⣿⣿⣿⡄|             WineSpectra Analysis:
            |⣼⣿⣿⣿ ⣿⣿⣿⣷|
            |⣿⣿⣿ W ⣿⣿⣿|             A comprehensive glimpse into the world of 
            |⣿⣿⣿ I ⣿⣿⣿|             wines, featuring details scraped from wine.
            |⣿⣿⣿ N ⣿⣿⣿|             covers wine names, color types, prices, 
            |⣿⣿⣿ E ⣿⣿⣿|             capacities (in milliliters), ratings provided 
            |⣿⣿⣿⣿⣿⣿⣿⣿⣿|             by site users, the number of ratings received,
            |⣿⣿⣿⣿⣿⣿⣿⣿⣿|             country of origin, alcohol content (ABV), and 
            |⣿⣿⣿⣿⣿⣿⣿⣿⣿|             a list of top wine experts who have reviewed.
            |⣿⣿⣿⣿⣿⣿⣿⣿⣿|
            |⣿⣿⣿⣿⣿⣿⣿⣿⣿|
            |⣿⣿⣿⣁⣿⣿⣿⣿⡏|
           [⠈⠛⠛⠛⠛⠛⠛⠛⠋⠁⠉]
    ''')

    overall,cost,ratings,ratingsnum,abv = st.tabs(["Overall","Cost","Ratings","RatingsNum", "ABV %"])

    #overall tab
    over_df = overall_data(df)
    overall.table(over_df)

    #cost tab
    cost.markdown("### 5 most costly wines")
    costly = df[['Names', 'Prices']].sort_values(by='Prices', ascending=False).head()
    cost.table(costly)

    cost.markdown("### 5 least costly wines")
    costly = df[['Names','Prices']].sort_values(by='Prices', ascending=True).head()
    cost.table(costly)

    #ratings tab
    ratings.markdown("#### Top 5 highly rated wines")
    rating = df[['Names','Ratings']].sort_values(by='Ratings', ascending=False).head()
    ratings.table(rating)
    ratings.markdown("*Least rated are not included because of zero ratings.*")

    #ratingsnum
    ratingsnum.markdown("#### Top 5 wines with highest ratingsnum")
    ratednum = df[['Names','Ratingsnum']].sort_values(by='Ratingsnum', ascending=False).head()
    ratingsnum.table(ratednum)
    ratingsnum.markdown('''*Least ratednum are not included because of zero ratings.*''')

    #abv %
    abv.markdown("#### Top 5 wines with highest ratingsnum")
    top_abv = df[['Names','ABV %']].sort_values(by='ABV %', ascending=False).head()
    abv.table(top_abv)
    abv.markdown('''*Least ABV% are not included because there are wines with zero alcohol.*''')

# VARITY PAGE
if sideMenu == "Wine-Varity Analysis":
    
    st.markdown("### Wine Spectra Analysis")

#ML PAGE
if sideMenu == "ML Analysis":
    
    st.markdown("### Wine Spectra Analysis")

# RED-WINE AGE
if sideMenu == "Red-Wine Analysis":
    
    st.markdown("### Wine Spectra Analysis")

# WHITE-WINE PAGE
if sideMenu == "White-Wine Analysis":
    
    st.markdown("### Wine Spectra Analysis")

# PINK & ROSE WINE PAGE
if sideMenu == "Pink & Rosé-Wine Analysis":
    
    st.markdown("### Wine Spectra Analysis")

#SPARKLING & CHAMPAGNE PAGE
if sideMenu == "Sparkling & Champagne Analysis":
    
    st.markdown("### Wine Spectra Analysis")



# ABOUT PAGE
if sideMenu == "About":
    
    st.markdown("### Wine Spectra Analysis")

    st.markdown(''' ##### This dataset offers a comprehensive glimpse into the world of wines, featuring details scraped from :rainbow[wine.com]. With a rich assortment of information, it covers wine names, color types, prices, capacities (in milliliters), ratings provided by site users, the number of ratings received, country of origin, alcohol content (ABV), and a list of top wine experts who have reviewed the wines ''')

    st.markdown("#### Data Source:")
    st.markdown('''This dataset was meticulously scraped from wine.com, a popular source for wine enthusiasts and connoisseurs.''')

    st.markdown("#### Key-points about data:")

    st.markdown('''
        * Name: Name of the wine
        * Color_wine: The color type of the wine
        * Prices: Price of the wine
        * ML: Capacity in milliliters
        * Rating: User-generated rating on the site
        * Ratingsnum: The number of user ratings
        * Countrys: Country of production
        * ABV: Alcohol by volume (ABV) content
        * Retes: List of top wine experts who have reviewed the wines ''')

    st.markdown("### Used Library:")
    st.markdown('''
        * numpy
        * pandas
        * streamlit
        * plotly 
        * chardet ''')
    