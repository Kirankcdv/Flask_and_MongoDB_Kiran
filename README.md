
# Flask & MongoDB — DevOps Assignment

**Submitted by:** Kiran K.

## 1. Project Objective

The objective is to build a Flask web application that provides a JSON API and a frontend form for submitting user information to MongoDB Atlas.

## 2. Technologies Used

- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML and CSS
- JSON
- Visual Studio Code

## 3. Project Structure

```text
Flask_and_MongoDB_Kiran/
├── app.py
├── data.json
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── screenshots/
│   ├── api_response.png
│   ├── frontend_form.png
│   └── database_error.png
├── static/
│   └── style.css
└── templates/
    ├── index.html
    └── success.html
```

## 4. Task 1 — JSON API Route

The Flask application provides a GET endpoint at `/api`.

The endpoint reads data from `data.json` and returns it as a JSON response. It returns an error response if the file cannot be read or parsed.

**Test URL:** `http://127.0.0.1:5000/api`

**Screenshot:** See `screenshots/api_response.png`.

## 5. Task 2 — Frontend Form

The home page contains a form with fields for name, email and message.

The form submits data to the Flask backend using the POST method.

The application validates that all fields are completed before attempting database insertion.

## 6. MongoDB Atlas Integration

The application uses PyMongo to connect to MongoDB Atlas. Submitted form data is intended to be stored in the `flask_assignment` database and `submissions` collection.

The connection URI is configured through an environment variable named `MONGO_URI` in `.env`.

Database credentials must not be included in source control.

## 7. Success and Error Handling

On a successful database insertion, the application redirects the user to `/success`, where the message "Data submitted successfully" is displayed.

If validation or database insertion fails, the application displays an error on the form page.

**Current test status:** The `/api` endpoint and frontend form have been tested. MongoDB Atlas connectivity is still failing with a DNS/TLS connection error. Successful database insertion has not yet been verified.

## 8. Screenshots

- `screenshots/api_response.png`: JSON API response.
- `screenshots/frontend_form.png`: Frontend form.
- `screenshots/database_error.png`: Database connection error during testing.

## 9. GitHub Repository

**Repository URL:** (https://github.com/Kirankcdv/Flask_and_MongoDB_Kiran.git).

## 10. Conclusion

The Flask application and JSON API have been implemented. MongoDB Atlas connectivity must be resolved and a successful form submission verified before the project can be considered fully complete.
