import streamlit as st
import pandas as pd
from PIL import Image

# Load your real estate listings data into a pandas DataFrame
data = pd.read_csv("real_estate_listings.csv")

# Create a main function to define the structure of your Streamlit app
def main():

    st.header("About Me")
    st.image("agent_photo.jpg", width=200)

    # Add your self-introduction
    st.write("""
    Hi, I'm your friendly real estate agent! I specialize in helping people find their dream homes.
    I have a wealth of experience in the real estate industry and I'm here to assist you with all your real estate needs.
    Feel free to contact me if you have any questions or if you'd like to schedule a viewing.
    """)
    st.title("Real Estate Listings")

    # Add self-instructions for using the app
    st.write("""
        Use the filters in the sidebar to refine your search.
        You can adjust the number of bedrooms, minimum and maximum price, and minimum and maximum area.
        The filtered results will be displayed below.
    """)

    # Show the data as a table
    st.dataframe(data)
    
    # Add a filter for location
    location_filter = st.sidebar.selectbox("Filter by location", ["All"] +     data["location"].unique().tolist())


    # Add filters for number of bedrooms, price, and area
    #bedrooms = st.sidebar.slider("Number of Bedrooms", 1, 10, 1)
    #min_price = st.sidebar.slider("Minimum Price", 50, 4000, 50)
    #max_price = st.sidebar.slider("Maximum Price", 50, 4000, 4000)
    #min_area = st.sidebar.slider("Minimum Area (sqft)", 100, 2000, 100)
    #max_area = st.sidebar.slider("Maximum Area (sqft)", 100, 2000, 2000)

    bedrooms = st.sidebar.slider("Number of Bedrooms", min_value=1, max_value=10, value=1)
    min_price = st.sidebar.slider("Minimum Price", min_value=int(data["price"].min()), max_value=int(data["price"].max()), value=int(data["price"].min()))
    max_price = st.sidebar.slider("Maximum Price", min_value=int(data["price"].min(), max_value=int(data["price"].max()), value=int(data["price"].max()))
    min_area = st.sidebar.slider("Minimum Area (sqft)", min_value=int(data["area"].min()), max_value=int(data["area"].max()), value=int(data["area"].min()))
    max_area = st.sidebar.slider("Maximum Area (sqft)", min_value=int(data["area"].min()), max_value=int(data["area"].max()), value=int(data["area"].max()))
    
# Filter the data based on the selected values

    filtered_data = data[(data["location"] == location_filter) | (location_filter == "All")]
    
    filtered_data = filtered_data[
        (data["bedrooms"] >= bedrooms) &
        (data["price"] >= min_price) &
        (data["price"] <= max_price) &
        (data["area"] >= min_area) &
        (data["area"] <= max_area)
    ]

    st.header("Filtered Result")
    # Show the filtered data
    st.dataframe(filtered_data)

    # Add the photos of the listings
    st.subheader("Photos")
    for i, row in filtered_data.iterrows():
        # Open the image file using PIL
        img = Image.open(row["photo"])

        # Display the image in the app
        st.image(img, width=300)

        # Display the caption for the image
        st.write("Caption:", row["caption"])

# Run the main function
if __name__ == "__main__":
    main()
