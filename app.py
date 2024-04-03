import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# header
st.header('AirBnB')

# Displaying an image
image = Image.open('data/image.jpg')
st.image(image, caption='AirBnB')

# load data
PATH_DATA = "data/Airbnb_Data.csv"

@st.cache_data
def load_data(path):
    """Load data from path"""
    data = pd.read_csv(path)
    data = data.sample(500)
    return data

df = load_data(PATH_DATA)
st.write(df[:5])

st.write("""This dashboard will present the spread of AirBnB in the USA (in 6 cities).""")

# Titles and Mode selections
st.sidebar.title("About")
st.sidebar.info(
    """
    AIRBNB
    """
)

# Load data
show_data = st.sidebar.checkbox('Show raw data')
if show_data == True:
    st.subheader('Raw data')
    st.markdown(
        "#### AIRBnB")
    st.write(df)

# create map
st.map(data=df, latitude="geo_lat", longitude="geo_lon")

# create sidebar
city = st.sidebar.multiselect(
    'Show cities?',
    df['city'].unique()
)
filtred = df[(df['city'].isin(city))]
st.write(filtred)

# Create distplot with custom bin_size
fig = px.scatter(filtred, x='log_price', y='review_scores_rating', color='city')

# Plot!
st.plotly_chart(fig)

# Описание полей
st.markdown(
    """
    ### Описание полей
        - id
        - log_price
        - property_type
        - room_type
        - amenities
        - accommodates
        - bathrooms
        - bed_type
        - cancellation_policy
        - cleaning_fee
        - city
        - description
        - first_review
        - host_has_profile_pic
        - host_identity_verified
        - host_response_rate
        - host_since
        - instant_bookable
        - last_review
        - latitude
        - longitude
        - name
        - neighbourhood
        - number_of_reviews
        - review_scores_rating
        - thumbnail_url
        - zipcode
        - bedrooms
        - beds
    
    """

)