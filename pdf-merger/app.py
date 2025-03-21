# Import required libraries
from flask import Flask, render_template, request, send_file, flash
from PyPDF2 import PdfMerger
import os
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flashing messages

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension
    Args:
        filename (str): Name of the uploaded file
    Returns:
        bool: True if file extension is allowed, False otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """
    Render the main page of the application
    Returns:
        rendered template: The index.html template
    """
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    """
    Handle PDF file upload and merging
    Returns:
        file: Merged PDF file for download
        or
        redirect: Back to index with error message
    """
    # Check if files were uploaded
    if 'pdfs' not in request.files:
        flash('No files uploaded')
        return render_template('index.html')
    
    files = request.files.getlist('pdfs')
    
    # Validate files
    if not files or files[0].filename == '':
        flash('No selected files')
        return render_template('index.html')
    
    # Initialize PDF merger
    merger = PdfMerger()
    
    try:
        # Process each uploaded file
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                merger.append(filepath)
                
                # Clean up uploaded file
                os.remove(filepath)
        
        # Save merged PDF
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.pdf')
        merger.write(output_path)
        merger.close()
        
        # Send merged file to user
        return send_file(
            output_path,
            as_attachment=True,
            download_name='merged.pdf'
        )
    
    except Exception as e:
        # Handle any errors during processing
        flash(f'Error merging PDFs: {str(e)}')
        return render_template('index.html')
    
    finally:
        # Clean up merged file
        if os.path.exists(output_path):
            os.remove(output_path)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)