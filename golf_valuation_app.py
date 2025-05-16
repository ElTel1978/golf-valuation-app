
import streamlit as st
import pandas as pd

# Load Excel data
df = pd.read_excel("golf_club_data.xlsx")

# Clean and convert price column
df["Prices"] = df["Prices"].replace('[£,]', '', regex=True).astype(float)

# Streamlit UI
st.title("Golf Club Trade-In Valuation")

# Dropdowns
club_type = st.selectbox("Select Club Type", sorted(df["Type"].dropna().unique()))
brand = st.selectbox("Select Brand", sorted(df["Brand"].dropna().unique()))

# Filter models based on brand
models = df[df["Brand"] == brand]["Model"].dropna().unique()
model = st.selectbox("Select Model", sorted(models))

# Condition input (scale 1–10)
condition = st.slider("Select Club Condition (1 = Poor, 10 = Like New)", 1, 10, 5)

# Estimate value
filtered = df[
    (df["Type"] == club_type) &
    (df["Brand"] == brand) &
    (df["Model"] == model)
]

if not filtered.empty:
    base_price = filtered.iloc[0]["Prices"]
    value = round(base_price * (condition / 10), 2)
    st.success(f"Estimated Trade-In Value: £{value}")
else:
    st.warning("Club not found. Try adjusting your selections.")
