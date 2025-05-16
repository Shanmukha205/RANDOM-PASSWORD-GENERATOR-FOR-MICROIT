# Random Password Generator

A modern web application that generates secure random passwords based on user preferences. Built with Flask and vanilla JavaScript, featuring a clean and responsive user interface.

## Features

- Generate passwords with customizable length (4-128 characters)
- Choose character types to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special symbols (!@#$%^&*...)
- Copy password to clipboard with one click
- Responsive design that works on both desktop and mobile
- Modern UI with smooth animations and transitions

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the files to your local machine.

2. Create a virtual environment (recommended):
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure your virtual environment is activated (if you created one).

2. Start the Flask development server:
   ```bash
   python app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
random-password-generator/
├── app.py              # Flask application and password generation logic
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # CSS styles
└── templates/
    └── index.html     # HTML template
```

## How It Works

1. The frontend provides a user-friendly interface for selecting password preferences.
2. When the "Generate Password" button is clicked, the preferences are sent to the backend.
3. The Flask backend uses Python's `secrets` module to generate a cryptographically secure random password.
4. The generated password is sent back to the frontend and displayed to the user.
5. Users can easily copy the password to their clipboard using the copy button.

## Security Features

- Uses Python's `secrets` module for cryptographically secure random number generation
- Input validation on both frontend and backend
- No password storage or logging
- HTTPS recommended for production deployment

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License. 