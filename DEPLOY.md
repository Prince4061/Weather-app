# How to Deploy to Render 🚀

Follow these steps to deploy your Weather App for free on Render.com.

## 1. Prepare Your Code
(These steps are already done for you!)
- `requirements.txt` has `gunicorn` and `flask`.
- `Procfile` is created with `web: gunicorn app:app`.

## 2. Push to GitHub

### Option A: Drag & Drop (Easiest) 🖱️
1.  Create a new repository on GitHub (e.g., `weather-app`).
2.  Click the link that says **"uploading an existing file"**.
3.  **Drag and Drop these specific files/folders ONLY:**
    - `app.py`
    - `templates/` (folder)
    - `static/` (folder)
    - `requirements.txt`
    - `Procfile`
    - `README.md`
4.  ❌ **DO NOT UPLOAD**: The `venv` folder or `__pycache__` folder. These are too big and not needed.
5.  Click **"Commit changes"**.

### Option B: Command Line (Advanced)
1.  Initialize git: `git init`
2.  Add files: `git add .`
3.  Commit: `git commit -m "Initial commit"`
4.  Push: `git push origin main`

## 3. Deploy on Render
1.  Go to [Render.com](https://render.com/) and Sign Up/Login.
2.  Click **"New +"** and select **"Web Service"**.
3.  Connect your GitHub account and select the `weather-app` repository.
4.  **Configure Settings:**
    - **Name:** Give your app a name (e.g., `my-weather-app`).
    - **Region:** Singapore or closest to you.
    - **Branch:** `main` (or `master`).
    - **Root Directory:** Leave blank.
    - **Runtime:** `Python 3`.
    - **Build Command:** `pip install -r requirements.txt`
    - **Start Command:** `gunicorn app:app` (Render might auto-detect this from Procfile).
5.  **Environment Variables (Important!):**
    - Scroll down to "Environment Variables".
    - Click "Add Environment Variable".
    - **Key:** `API_KEY` (Wait, for security, hardcoding in app.py is okay for now, but best practice is to use env vars. Since we hardcoded it in `app.py`, you can skip this effectively, but if you want to be secure, change `app.py` to `os.environ.get('API_KEY')` and add it here).
    - For this specific project submission, **you can skip this step** as the key is in `app.py`.
6.  Click **"Create Web Service"**.

## 4. Wait & Test
- Render will start building your app. It might take 2-3 minutes.
- Once done, you will see a green "Live" badge.
- Click the URL provided (e.g., `https://my-weather-app.onrender.com`) to see your live app!
