# Mental Health Prediction

This is a machine learning-based application that predicts mental health risk levels based on various lifestyle factors. The application uses FastAPI for the backend API, SQLite for the database and Streamlit for the frontend interface.

## Demo Link 
https://mentalhealthprediction-ftyuxwnvfvntz8ptdrhtwi.streamlit.app/

Note: The History and Predict api's don't come up immediatly you visit the site it takes atleast 1 min for the backend server to comeback on after going to sleep due to inactivity 
- Frontend is hosted on Streamlit.io
- Backend is hosted on Render

## Features

- Predicts mental health risk levels (Low Risk, Medium Risk, High Risk)
- Takes into account various lifestyle factors:
  - Sleep hours
  - Exercise hours
  - Stress level
  - Social activity
  - Work hours
  - Screen time
- REST API backend with FastAPI
- Interactive web interface using Streamlit
- SQLite database for data storage

## Prerequisites

- Python 3.12 or higher
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Newbie4newthings/Mental_health_prediction.git
cd Mental_health_prediction
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
.\venv\Scripts\activate.ps1
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Chnage the api's point in the Frontend.py file:
   - for hosting on your local machine use `http://localhost:8000`
   - for hosting on the internet use your hostinng server endpoints

## Usage

The application consists of two main components that need to be started separately:

1. Start the FastAPI backend server:
```bash
uvicorn src.app:app --reload
python main.py
```
The API will be available at `http://localhost:8000`

2. In a new terminal, start the Streamlit frontend:
```bash
streamlit run src/frontend.py
```
The web interface will open automatically in your default browser.

## API Endpoints

- `POST /predict`: Predicts mental health risk based on input parameters
  - Request body should include:
    - sleep_hours (float)
    - exercise_hours (float)
    - stress_level (integer)
    - social_activity (integer)
    - work_hours (float)
    - screen_time (float)

## Project Structure

```
Mental_health_prediction/
├── health_predictions.db    # SQLite database
├── main.py                 # Main application entry point
├── models.py              # Database models
├── requirements.txt       # Project dependencies
└── src/
    ├── __init__.py
    ├── app.py            # FastAPI backend
    └── frontend.py       # Streamlit frontend
```

## Dependencies

- FastAPI: Web framework for building APIs
- Uvicorn: ASGI server for FastAPI
- Streamlit: Frontend framework
- Pandas: Data manipulation
- Scikit-learn: Machine learning functionality
- NumPy: Numerical computations
- SQLAlchemy: Database ORM
- Python-multipart: Form data handling

## License

Unknown

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

[Makanjuolamartin@gmail.com]
