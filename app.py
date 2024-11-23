import streamlit as st
import util

def main():
    st.title("Home Price Prediction")

    # Load saved artifacts
    util.load_saved_artifacts()

    # Get location names 
    locations = util.get_location_names()

    # Input fields
    location = st.selectbox("Select Location", locations)
    total_sqft = st.number_input("Total Square Feet", min_value=0)
    bhk = st.number_input("Number of Bedrooms (BHK)", min_value=0)
    bath = st.number_input("Number of Bathrooms", min_value=0)

    # Predict button
    if st.button("Predict Price"):
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        estimated_price = estimated_price*100
        st.success(f"The estimated price per sq feet is: ₹{estimated_price}")

if __name__ == "__main__":
    main()
