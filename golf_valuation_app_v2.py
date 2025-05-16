
import streamlit as st
import pandas as pd

# Load Excel data
df = pd.read_excel("golf_club_data.xlsx")
df["Prices"] = df["Prices"].replace('[£,]', '', regex=True).astype(float)

st.title("Golf Club Trade-In Valuation Tool")

# Dropdowns for full filtering
club_type = st.selectbox("Select Club Type", sorted(df["Type"].dropna().unique()))
brand = st.selectbox("Select Brand", sorted(df["Brand"].dropna().unique()))
model = st.selectbox("Select Model", sorted(df[df["Brand"] == brand]["Model"].dropna().unique()))
handed = st.selectbox("Select Handedness", sorted(df["Handed"].dropna().unique()))
shaft = st.selectbox("Select Shaft Type", sorted(df["Shaft"].dropna().unique()))
gender = st.selectbox("Select Gender", sorted(df["Gender"].dropna().unique()))
headcover = st.selectbox("Matching Headcover Included?", sorted(df["Matching Headcover"].dropna().unique()))

# Condition slider
condition = st.slider("Select Club Condition (1 = Poor, 10 = Like New)", 1, 10, 5)

# Filter the dataframe based on all inputs
filtered = df[
    (df["Type"] == club_type) &
    (df["Brand"] == brand) &
    (df["Model"] == model) &
    (df["Handed"] == handed) &
    (df["Shaft"] == shaft) &
    (df["Gender"] == gender) &
    (df["Matching Headcover"] == headcover)
]

# Show value
if not filtered.empty:
    base_price = filtered.iloc[0]["Prices"]
    value = round(base_price * (condition / 10), 2)
    st.success(f"Estimated Trade-In Value: £{value}")
else:
    st.warning("No exact match found. Please check your selections.")
