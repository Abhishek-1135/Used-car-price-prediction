# Used Car Price Prediction

Complete runnable reconstructed workspace based on the screenshot.

**Important:** Original source files, training data, and model were not supplied. This workspace uses **synthetic demonstration data** and a trained demo model. Predictions are **not real market valuations**. `app2.py`, `carapp.py`, `new_.py`, and `lamp.py` are launch-compatible placeholders because their original content was not visible.

## Setup (Windows / VS Code)

```powershell
py -3.11 -m venv venv
.\\venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If Python 3.11 is unavailable, use a supported installed Python version.

## Files
- `app.py`: main Streamlit app
- `app2.py`, `carapp.py`, `new_.py`, `lamp.py`: alternative entry points
- `models/car_price_pipeline.pkl`: fitted demonstration pipeline
- `data/raw_data/used_cars_raw.csv`: synthetic input dataset
- `data/cleaned_data/used_cars_cleaned.csv`: cleaned demonstration dataset
- `Notebooks/01_data_cleaning_eda_ipynb.ipynb`: EDA notebook
- `Notebooks/02_model_training.ipynb`: model training notebook
- `assets/car_background.jpg`: placeholder graphic
- `venv/`: create locally, not distributed

To train on real car data, replace the CSV and rerun the training notebook.
