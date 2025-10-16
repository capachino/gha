import os
from flask import Flask, request, abort

app = Flask(__name__)

# The directory where user files are stored
UPLOAD_DIR = "/app/user_uploads/"

@app.route('/download')
def download_file():
    # Get the filename from a URL parameter (e.g., /download?file=report.pdf)
    filename = request.args.get('file')

    if not filename:
        return "Missing 'file' parameter", 400

    # !!! VULNERABLE LINE !!!
    # The user's input is directly joined to the directory path.
    file_path = os.path.join(UPLOAD_DIR, filename)

    try:
        # The server attempts to read and return the file
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        abort(404, "File not found.")
    except Exception:
        abort(500, "An error occurred.")

if __name__ == '__main__':
    # Note: This is a dev server, not for production.
    app.run(debug=True)
