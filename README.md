# sample-react-django-work
An easy-to-follow example integrating React with Django for building web applications.

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Frontend**: React, Axios

## Setup

### Backend (Django)
1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python manage.py runserver
   ```



### Frontend (React)
1. Navigate to the frontend folder:
   ```bash
   cd myapp
   ```
2. Install packages and start the server:
   ```bash
   npm install
   npm start
   ```

### API Endpoints
* **`GET /hello-world/`** : Returns the current server time.
* **`GET /cat-image/`** : Returns a random cat image URL.
   
