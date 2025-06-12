
import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load model and encoder
model = joblib.load("movie_year_predictor.joblib")
encoder = joblib.load("genre_encoder.joblib")

# Streamlit configuration
st.set_page_config(page_title="Movie Year Predictor", layout="centered")
st.title("🎬 Movie Year Predictor")
st.markdown("Use genres to predict the release year of a movie.")

# Sidebar: Genre selection
st.sidebar.header("🎭 Genre Selection")
selected_genres = st.sidebar.multiselect("Choose genres:", encoder.classes_)

# Main: Display selected genres
st.subheader("🎯 Selected Genres")
if selected_genres:
    st.success(f"You selected: {', '.join(selected_genres)}")
else:
    st.info("Please select one or more genres from the sidebar.")

# Predict and display result
if st.button("🔮 Predict Release Year"):
    if selected_genres:
        try:
            X_input = encoder.transform([selected_genres])
            predicted_year = int(model.predict(X_input)[0])
            st.subheader("📅 Predicted Release Year")
            st.success(f"The predicted release year is **{predicted_year}**.")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
    else:
        st.warning("⚠️ Please select at least one genre.")

# Feature: Show example genre combinations and predictions
st.markdown("---")
st.subheader("🧪 Example Genre Predictions")
example_genres = [
    ["Action", "Adventure"],
    ["Romance", "Drama"],
    ["Comedy"],
    ["Horror", "Thriller"],
    ["Animation", "Family"],
]

for genres in example_genres:
    try:
        X = encoder.transform([genres])
        year = int(model.predict(X)[0])
        st.write(f"Genres: {', '.join(genres)} → Predicted Year: **{year}**")
    except:
        pass

# Feature: Genre popularity chart (based on encoder frequency)
st.markdown("---")
st.subheader("📊 Genre Popularity")
genre_counts = pd.Series(encoder.classes_).value_counts().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(6, 6))
genre_counts.plot(kind="barh", ax=ax, color="skyblue")
ax.set_title("Available Genres in Encoder")
st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Model: RandomForestRegressor | Features: Genre Encoding + Prediction + Charts")
