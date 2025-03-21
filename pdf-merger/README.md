# PDF Merger

This project is a simple web application built with Flask that allows users to merge multiple PDF files into a single document. The application features a modern user interface and is designed to be user-friendly.

## Features

- Upload multiple PDF files
- Merge PDF files into a single document
- Download the merged PDF file

## Technologies Used

- Flask: A lightweight WSGI web application framework in Python.
- HTML/CSS: For the front-end user interface.
- JavaScript: For client-side interactivity.
- PyPDF2: A Python library for PDF manipulation.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pdf-merger.git
   ```

2. Navigate to the project directory:
   ```
   cd pdf-merger
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Create required directories:
   ```
   mkdir temp
   mkdir static
   mkdir templates
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your web browser and navigate to `http://127.0.0.1:5000`

## Creating the User Interface

1. Create a `templates` directory in the project root and add an `index.html` file:
   ```html
   <!-- filepath: c:\Users\Xpert\Desktop\copilot_demo\pdf-merger\templates\index.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>PDF Merger</title>
       <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
   </head>
   <body>
       <div class="container">
           <h1>PDF Merger</h1>
           <form action="/merge" method="post" enctype="multipart/form-data">
               <input type="file" name="pdfs" multiple required>
               <button type="submit">Merge PDFs</button>
           </form>
       </div>
   </body>
   </html>
   ```

2. Create a `static` directory in the project root and add a `styles.css` file:
   ```css
   /* filepath: c:\Users\Xpert\Desktop\copilot_demo\pdf-merger\static\styles.css */
   body {
       font-family: Arial, sans-serif;
       background-color: #f4f4f4;
       display: flex;
       justify-content: center;
       align-items: center;
       height: 100vh;
       margin: 0;
   }

   .container {
       background: white;
       padding: 20px;
       border-radius: 8px;
       box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);