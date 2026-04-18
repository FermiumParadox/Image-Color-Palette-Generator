from flask import Flask, render_template, request, session
from utils import get_dominant_colors  # import your function from utils.py
import io
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs('static/uploads', exist_ok=True)
load_dotenv()

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Folder where uploaded images will be stored
UPLOAD_FOLDER = 'static/uploads'

# Save this folder path in app configuration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for homepage
# Allows both:
# - GET → when user visits the page
# - POST → when user uploads an image
@app.route('/', methods=['GET', 'POST'])
def index():
    colors = []
    image_url = None
    k = 5

    error = None

    if request.method == 'POST':
        k = int(request.form.get('k', 5))
        file = request.files.get('image')

        if not file or file.filename == '':
            error = "Please select an image file."

        elif not allowed_file(file.filename):
            error = "Only image files (png, jpg, jpeg, gif) are allowed."

        else:
            try:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                session['image_path'] = filepath

                with open(filepath, 'rb') as f:
                    image_stream = io.BytesIO(f.read())

                colors = get_dominant_colors(image_stream, k=k)
                image_url = '/' + filepath

                def rgb_to_hex(color):
                    return '#%02x%02x%02x' % tuple(int(c) for c in color)

                colors = [(c, rgb_to_hex(c)) for c in colors]

            except Exception:
                error = "Invalid image file. Please upload a valid image."

    return render_template('index.html', colors=colors, image_url=image_url, k=k, error=error)

# Run the app
if __name__ == '__main__':
    # debug=True → auto reload + shows errors clearly
    app.run(debug=True)