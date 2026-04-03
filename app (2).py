import streamlit as st
import pickle
import pandas as pd

# Page Config
st.set_page_config(page_title="AI Recommender", layout="wide")

# Load Data
df = pickle.load(open('products.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation Function
def recommend(product_name):
    idx = df[df['product_name'] == product_name].index[0]
    distances = similarity[idx]
    
    product_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_products = []
    for i in product_list:
        recommended_products.append(df.iloc[i[0]].product_name)
    
    return recommended_products

# UI Title
st.title("🛍️ AI Product Recommendation System")

# Layout
col1, col2 = st.columns(2)

with col1:
    selected_product = st.selectbox(
        "🔍 Select a Product",
        df['product_name'].values
    )

with col2:
    if st.button("🚀 Recommend"):
        recommendations = recommend(selected_product)
        
        st.subheader("✨ Recommended Products:")
        for product in recommendations:
            st.success(product)