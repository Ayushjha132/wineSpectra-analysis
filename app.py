import streamlit as st
import pandas as pd
import chardet
import plotly.express as px

st.set_page_config(page_title="WineSpectra Analysis", page_icon=":wine_glass:")

from function import overall_data, ml_available, ml_record, price

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
            |⣿⣿⣿ S ⣿⣿⣿|             A comprehensive glimpse into the world of 
            |⣿⣿⣿ U ⣿⣿⣿|             wines, featuring details scraped from wine.
            |⣿⣿⣿ L ⣿⣿⣿|             covers wine names, color types, prices, 
            |⣿⣿⣿ A ⣿⣿⣿|             capacities (in milliliters), ratings provided 
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
    
    st.markdown("## Wine-Varity Analysis")

    st.markdown("#### Distribution of Wine Prices")

    cost = price(df)

    fig = px.histogram(cost, nbins=20, title='Histogram Chat of Wine Prices', labels={'value': 'Prices (in $)', 'count': 'Frequency'})
    st.plotly_chart(fig)

    fig1 = px.line(df, x= 'Names', y='Prices', title='Line Graph of Wine Prices', labels={'Prices': 'Wine Prices (in $)'})
    
    st.plotly_chart(fig1)


#ML PAGE
if sideMenu == "ML Analysis":
    
    st.markdown("## Container Analysis")
    st.markdown("Standard amount of wine container size in ml (milliliter)")
    st.markdown("<br>", unsafe_allow_html=True)

    ml_value = ml_available(df)
    number = ml_record(ml_value, df)

    data = {'Container Size': ml_value, 'Total Number': number}
    df_plot = pd.DataFrame(data)

    st.bar_chart(df_plot.set_index('Container Size'))

    st.write(f"Average Size: {ml_value.mean()} ml")
    st.write(f"Minimum Size: {ml_value.min()} ml")
    st.write(f"Maximum Size: {ml_value.max()} ml")


# RED-WINE AGE
if sideMenu == "Red-Wine Analysis":
    
    st.markdown("## Red-Wine Analysis")
    red_wine = df[df["color_wine"] == 'Red Wine']

#? LINE 
    st.markdown("#### Rating Chart")
    ratings = red_wine[[ "Names","Ratings"]]

    fig_rating = px.scatter(ratings, x='Names', y='Ratings',title='Scatter Chart of Wine Ratings', labels={'Names': 'Red Wines'})
    st.plotly_chart(fig_rating)

#? HISTOGRAM
    st.markdown("#### Price Chart")

    cost = price(red_wine)
    fig = px.histogram(cost, nbins=20, title='Histogram Chat of Wine Prices', labels={'value': 'Prices (in $)', 'count': 'Frequency'})
    st.plotly_chart(fig)

    fig1 = px.line(red_wine, x= 'Names', y= 'Prices', title='Line Graph of Wine Prices', labels={'Prices': 'Wine Prices (in $)'})
    
    st.plotly_chart(fig1)

#? LINE
    st.markdown("#### ABV % In Red Wine")
    abv = red_wine[[ "Names","ABV %"]]

    fig_abv = px.line(abv, x= 'Names', y='ABV %', title='Line Chart of ABV by Wine Name', labels={'ABV %': 'Alcohol by Volume'})
    st.plotly_chart(fig_abv)

# WHITE-WINE PAGE
if sideMenu == "White-Wine Analysis":
    
    st.markdown("## White-Wine Analysis")
    white_wine = df[df["color_wine"] == 'White Wine']

#? LINE 
    st.markdown("#### Rating Chart")
    ratings = white_wine[[ "Names","Ratings"]]

    fig_rating = px.scatter(ratings, x='Names', y='Ratings',title='White Chart of Wine Ratings', labels={'Names': 'White Wines'})
    st.plotly_chart(fig_rating)

#? HISTOGRAM
    st.markdown("#### Price Chart")

    cost = price(white_wine)
    fig = px.histogram(cost, nbins=20, title='Histogram Chat of Wine Prices', labels={'value': 'Prices (in $)', 'count': 'Frequency'})
    st.plotly_chart(fig)

    fig1 = px.line(white_wine, x= 'Names', y= 'Prices', title='Line Graph of Wine Prices', labels={'Prices': 'Wine Prices (in $)'})
    
    st.plotly_chart(fig1)

#? LINE
    st.markdown("#### ABV % In Red Wine")
    abv = white_wine[[ "Names","ABV %"]]
    
    fig_abv = px.line(abv, x= 'Names', y='ABV %', title='Line Chart of ABV by Wine Name', labels={'ABV %': 'Alcohol by Volume'})
    st.plotly_chart(fig_abv)

# PINK & ROSE WINE PAGE
if sideMenu == "Pink & Rosé-Wine Analysis":
    
    st.markdown("### Pink & Rosé-Wine Analysis")
    pink_rose_wine = df[df["color_wine"] == 'Pink and Rosé']

#? LINE 
    st.markdown("#### Rating Chart")
    ratings = pink_rose_wine[[ "Names","Ratings"]]

    fig_rating = px.scatter(ratings, x='Names', y='Ratings',title='Scatter Chart of Wine Ratings', labels={'Names': 'Red Wines'})
    st.plotly_chart(fig_rating)

#? HISTOGRAM
    st.markdown("#### Price Chart")

    cost = price(pink_rose_wine)
    fig = px.histogram(cost, nbins=20, title='Histogram Chat of Wine Prices', labels={'value': 'Prices (in $)', 'count': 'Frequency'})
    st.plotly_chart(fig)

    fig1 = px.line(pink_rose_wine, x= 'Names', y= 'Prices', title='Line Graph of Wine Prices', labels={'Prices': 'Wine Prices (in $)'})
    
    st.plotly_chart(fig1)

#? LINE
    st.markdown("#### ABV % In Red Wine")
    abv = pink_rose_wine[[ "Names","ABV %"]]
    
    fig_abv = px.line(abv, x= 'Names', y='ABV %', title='Line Chart of ABV by Wine Name', labels={'ABV %': 'Alcohol by Volume'})
    st.plotly_chart(fig_abv)

#SPARKLING & CHAMPAGNE PAGE
if sideMenu == "Sparkling & Champagne Analysis":
    
    st.markdown("### Sparkling & Champagne Analysis")
    sparkling_champagne_wine = df[df["color_wine"] == 'Sparkling & Champagne']

#? LINE 
    st.markdown("#### Rating Chart")
    ratings = sparkling_champagne_wine[[ "Names","Ratings"]]

    fig_rating = px.scatter(ratings, x='Names', y='Ratings',title='Sparkling & Champagne Chart of Wine Ratings', labels={'Names': 'Sparkling & Champagne Wines'})
    st.plotly_chart(fig_rating)

#? HISTOGRAM
    st.markdown("#### Price Chart")

    cost = price(sparkling_champagne_wine)
    fig = px.histogram(cost, nbins=20, title='Histogram Chat of Wine Prices', labels={'value': 'Prices (in $)', 'count': 'Frequency'})
    st.plotly_chart(fig)

    fig1 = px.line(sparkling_champagne_wine, x= 'Names', y= 'Prices', title='Line Graph of Wine Prices', labels={'Prices': 'Wine Prices (in $)'})
    
    st.plotly_chart(fig1)

#? LINE
    st.markdown("#### ABV % In Red Wine")
    abv = sparkling_champagne_wine[[ "Names","ABV %"]]
    
    fig_abv = px.line(abv, x= 'Names', y='ABV %', title='Line Chart of ABV by Wine Name', labels={'ABV %': 'Alcohol by Volume'})
    st.plotly_chart(fig_abv)


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
        * chardet 
        * matplotlib''')
    
