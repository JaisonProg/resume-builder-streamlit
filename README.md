 # Resume Builder (Streamlit Version)

A simple web-based resume builder written in Python using [Streamlit](https://streamlit.io/).

## Features

- Interactive form to enter resume data
- Instantly generates and downloads a `.txt` resume file
- No need to install anything beyond Streamlit
- No email or account setup required

## How to Run Locally

1. Clone this repository:

```
git clone https://github.com/yourusername/resume-builder-streamlit.git
cd resume-builder-streamlit
```

2. Install Streamlit:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## How to Deploy Online (Free)

You can host this app for free using [Streamlit Cloud](https://streamlit.io/cloud):

1. Push this folder to a GitHub repository
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and sign in
3. Click "New app" and select your repo
4. Set the file path to `app.py`
5. Click "Deploy"

Done! You now have a live resume builder you can share with anyone.

## Requirements

- Python 3.7+
- Streamlit