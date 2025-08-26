# User Authentication Platform

This project is a full-stack web application for user registration and login, built with Flask for the backend and React for the frontend. It features JWT authentication and a simple user dashboard.

## Online System

You can access the live application at: [Your Live Application Link Here]

## Screenshots

### Registration Process
![Registration Screenshot](path/to/registration_screenshot.png)

### Login Process
![Login Screenshot](path/to/login_screenshot.png)

## Getting Started

### Prerequisites

- Node.js and npm installed for the frontend
- Python 3.x and pip installed for the backend
- A SQL database (SQLite is used in this project)

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

### Backend Setup

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on the `.env.example` file and set your environment variables.

4. Run the Flask application:
   ```
   python app.py
   ```

## CI/CD

This project uses GitHub Actions for continuous integration and deployment. You can view the status of the CI/CD pipeline in the GitHub Actions tab of the repository.

![GitHub Actions Badge](https://github.com/yourusername/user-auth-platform/workflows/CI/badge.svg)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.