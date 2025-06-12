# movie-remmmended-cloud-credits
Movie Year Predictor App
Predict a movie’s release year using its genres with this interactive Streamlit app powered by machine learning.




📌 Description
This app uses a RandomForestRegressor to predict the likely release year of a movie based on its genre(s). It demonstrates the power of machine learning combined with an easy-to-use web interface built using Streamlit.

Users can:

Select one or more genres (e.g., Action, Romance, Horror)

Get an instant prediction of the movie’s release year

View example predictions

Explore genre popularity using a chart

📷 Preview
(Include a screenshot here once you've deployed or captured one)

🚀 Features
🎭 Multi-genre input with multi-select interface

🔮 Real-time movie year prediction

📊 Genre frequency bar chart

✅ Sample predictions for quick insights

💾 Model and encoder saved using joblib

🧠 Tech Stack
Python

Streamlit

scikit-learn

pandas

matplotlib

joblib

🔧 Setup Instructions
Clone the repo

bash
Copy
Edit
git clone https://github.com/your-username/movie-year-predictor.git
cd movie-year-predictor
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run movie_year_app.py
📁 File Structure
bash
Copy
Edit
├── movie_year_app.py           # Streamlit app
├── movie_year_predictor.joblib # Trained RandomForest model
├── genre_encoder.joblib        # MultiLabelBinarizer encoder
├── requirements.txt
└── README.md
