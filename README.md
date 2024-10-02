CSV Table Management Web Application
**Project Overview:**
 This project is a web-based application that allows users to upload, view, edit, save, and export CSV data in a user-friendly interface. It is built with Python (Flask) as the backend, a SQLite database for   data storage, and a frontend powered by HTML, JavaScript, and Bootstrap for responsiveness. The application ensures seamless interaction with CSV files, making it easier to manage data in real-time.

Features:
 CSV Upload: Users can upload CSV files to the application.
 Data Display: The uploaded CSV data is displayed in a responsive table format.
 Editability: The table cells can be edited directly in the browser.
 Save Functionality: After editing, users can save the changes, and the data will be stored in the SQLite database.
 Export to CSV: The edited data can be exported back to a CSV file.
 Sorting and Filtering: Users can sort and filter the table data for better management.
How It Works:
 Upload CSV: Users upload a CSV file using the file input form.
 Display Data: The application reads the CSV file and displays it as an editable HTML table.
 Edit Data: The user can edit any table cell. Once the changes are made, the user clicks the "Save" button, which sends the data to the backend to be saved in the SQLite database.
 Export Data: The user can download the current data in the table as a CSV file by clicking the "Export" button.
 Sorting & Filtering: The user can filter or sort the data using the provided filter input and table sorting options.
Technologies Used
 Flask (Python): Serves the backend and handles routing and data processing.
 SQLite: Lightweight database for storing the CSV data.
 Pandas: Used to handle CSV file operations in the backend.
 HTML/CSS (Bootstrap): Provides the structure and styling of the web interface.
 JavaScript: Adds dynamic functionality for editing, saving, sorting, and filtering the table data. 


Installation:
1/Clone the repository: git clone https://github.com/y0ss4f/csv-uploader.git
2/Run the Flask App: python app.py
3/Access the application via: http://localhost:5000
