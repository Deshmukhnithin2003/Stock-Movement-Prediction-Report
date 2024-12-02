# Stock-Movement-Prediction-Report
A Machine learning model that predicts stock movements by scraping data from social media platforms like Twitter, Reddit, or Telegram

## Overview
This project predicts stock movements by analyzing sentiment from Reddit discussions. 
The pipeline involves data scraping, preprocessing, sentiment analysis, and model training.

---

## Project Structure

```
|-- data/                         # Directory for raw and processed data files
|-- notebooks/                    # Jupyter notebooks for each project stage
    |-- 1_data_scraping.ipynb     # Scraping data from Reddit using PRAW
    |-- 2_data_preprocessing.ipynb# Preprocessing and sentiment analysis
    |-- 3_model_training.ipynb    # Training and evaluating the prediction model
|-- scripts/                      # Standalone Python scripts for automation
    |-- scraper.py                # Script for data scraping
    |-- preprocess.py             # Script for preprocessing and feature extraction
    |-- train_model.py            # Script for model training and evaluation
|-- requirements.txt              # List of dependencies for the project
|-- README.md                     # Documentation (this file)
```

---

## Setup Instructions

### 1. **Clone the Repository**
Clone this repository to your local system:
```bash
git clone https://github.com/your-repo-name/stock-movement-prediction.git
cd stock-movement-prediction
```

### 2. **Install Dependencies**
Ensure you have Python 3.8+ installed. Install the required dependencies using:
```bash
pip install -r requirements.txt
```

### 3. **Set Up API Keys**
- Obtain Reddit API credentials (`client_id`, `client_secret`, `user_agent`) by creating a new app at [Reddit App Preferences](https://www.reddit.com/prefs/apps).
- Create a `.env` file in the project root with the following structure:
```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
USER_AGENT=your_user_agent
```

### 4. **Run Jupyter Notebooks**
Execute the Jupyter notebooks in the following sequence for full project execution:
1. **`1_data_scraping.ipynb`**: Scrapes data from Reddit subreddits like `r/stocks`.
2. **`2_data_preprocessing.ipynb`**: Preprocesses scraped data and performs sentiment analysis.
3. **`3_model_training.ipynb`**: Trains and evaluates the prediction model.

To launch Jupyter notebooks:
```bash
jupyter notebook
```

### 5. **Run Scripts Directly (Optional)**
You can also execute the process using the Python scripts provided:
```bash
# Scraping data
python scripts/scraper.py

# Preprocessing and sentiment analysis
python scripts/preprocess.py

# Model training and evaluation
python scripts/train_model.py
```

---

## Dependencies
The required dependencies are listed in the `requirements.txt` file. Install them using:
```bash
pip install -r requirements.txt
```

Key libraries include:
- `praw` for Reddit scraping
- `pandas`, `numpy` for data manipulation
- `scikit-learn` for machine learning
- `nltk`, `textblob` for NLP and sentiment analysis

---

## Contributing
Feel free to fork the repository and submit pull requests for improvements.

---

## Contact
For questions or feedback, reach out to [Your Email/Contact Information].

---

