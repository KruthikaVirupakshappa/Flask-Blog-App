# Flask-Blog-App
Flask web app for managing blog posts which includes Create, Read, Update, and Delete functionality.
The purpose of this project is to develop a simple yet fully functional blog application using Flask, a lightweight web framework in Python. The application demonstrates the fundamental principles of web development including routing, database integration, and template rendering while keeping the structure minimal and easy to understand. This Flask Blog allows users to create, read, update, and delete (CRUD) blog posts stored in a SQLite database. It uses Flask-SQLAlchemy for database interactions for dynamic web pages. The user interface is designed to be clean and intuitive, enabling seamless navigation between posts, editing, and creation pages.
Tools and Technologies
● Flask - Python micro web framework used to build the backend
● Flask -SQLAlchemy- ORM for interacting with SQLite database
● SQLite - Lightweight file-based database used to store posts
● HTML - For dynamic templates and UI rendering
● CSS - To style the pages and provide a responsive layout
● VS Code/Terminal - Development environment and testing tool
The application supports full CRUD functionality:
● Create: Users can add new blog posts using a simple form with a title and content field.
● Read: Posts are displayed dynamically on the homepage and can be viewed individually.
● Update: Existing posts can be edited and updated directly from the browser.
● Delete: Posts can be removed permanently with a single click.
The Flask Blog application is made up of several interconnected web pages that together form a complete blogging system. Each page has a specific purpose and is dynamically rendered using Flask’s Jinja2 templating engine, which allows the content to update in real time based on the data stored in the SQLite database.
