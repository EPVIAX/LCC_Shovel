# Lifecycle Cost App

## Overview
The Lifecycle Cost App is a web application designed to calculate the lifecycle costs of equipment. It provides a user-friendly interface for inputting data and retrieving calculated results through a backend API.

## Project Structure
```
lifecycle-cost-app
├── backend
│   ├── app.py                # Entry point of the backend application
│   ├── models
│   │   └── database.py       # Database models and connection logic
│   ├── routes
│   │   └── api.py            # API endpoints for the application
│   └── services
│       └── calculations.py    # Business logic for lifecycle cost calculations
├── frontend
│   ├── static
│   │   ├── css               # CSS files for styling
│   │   └── js                # JavaScript files for client-side functionality
│   ├── templates
│   │   └── index.html        # Main HTML template for the web application
│   └── app.js                # JavaScript code for interacting with the backend API
├── requirements.txt          # Python dependencies for the backend
├── config.py                 # Configuration settings for the application
└── README.md                 # Documentation for the project
```

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/lifecycle-cost-app.git
   cd lifecycle-cost-app
   ```

2. **Install dependencies:**
   Make sure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure the application:**
   Update the `config.py` file with your database connection details and any other necessary environment variables.

4. **Run the backend server:**
   Start the backend application by running:
   ```
   python backend/app.py
   ```

5. **Access the frontend:**
   Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage
- Input the necessary data regarding the equipment in the provided fields.
- Submit the form to calculate the lifecycle costs.
- The results will be displayed on the same page.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.