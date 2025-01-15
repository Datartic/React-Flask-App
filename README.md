## React-Flask-App
Fully functioning App with React on front end and Flask on Backend. Allows to store user data and authenticate.

<img width="742" alt="Screenshot 2025-01-15 at 2 47 33 PM" src="https://github.com/user-attachments/assets/e84188c8-069a-4196-9b22-d26f093e1a52" />
<img width="737" alt="Screenshot 2025-01-15 at 2 47 40 PM" src="https://github.com/user-attachments/assets/c59cc760-253a-4cf6-ab3a-8ef567a30515" />


### Project Description
Tax Filing Portal is a web application designed to provide secure, efficient, and professional tax filing services. The portal allows users to sign up, log in, and access their personalized dashboard to manage their tax filing activities. The application ensures that only authenticated users can access sensitive information and perform tax-related tasks.

### Features
User Authentication:

### Sign up with a username, full name, email, and password.
Log in with email and password.
Session management with session tokens to maintain user authentication.
Dashboard:

### Personalized dashboard for authenticated users.
Access to tax filing services and user-specific information.
Navigation:

### Navbar with conditional rendering based on authentication status.
Options to navigate to Home, Sign Up, Login, Dashboard, and Logout.
Responsive Design:

User-friendly interface with responsive design using Material-UI components.

### Tech Stack
Frontend:

React: JavaScript library for building user interfaces.
React Router: Library for routing in React applications.
Material-UI: React component library for implementing Google's Material Design.
Axios: Promise-based HTTP client for making API requests.
Backend:

Flask: Micro web framework for building the backend API.
Flask-SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) for Flask.
Flask-CORS: Extension for handling Cross-Origin Resource Sharing (CORS) in Flask applications.
Database:

PostgreSQL: Relational database for storing user information and session tokens.
Project Structure
Frontend:

src/App.js: Main application component with routing logic.
src/pages/Home.jsx: Home page component.
src/pages/SignUp.jsx: Sign-up page component.
src/pages/Login.jsx: Login page component.
src/pages/Dashboard.jsx: Dashboard page component.
src/components/Navbar.jsx: Navbar component with conditional rendering.
src/index.js: Entry point for the React application.
Backend:

app.py: Main Flask application with API endpoints for sign-up and login.
How to Run
Backend:

Set up a PostgreSQL database and configure the connection in app.py.
Install the required Python packages using pip install -r requirements.txt.
Run the Flask application using python app.py.
Frontend:

Install the required Node.js packages using npm install.
Start the React application using npm start.
