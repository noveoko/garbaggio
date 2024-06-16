from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
import torch
from torchvision import models, transforms
from PIL import Image
import io

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)

class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

db.create_all()

# Load the pre-trained model
model = models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        image = Image.open(filename)
        transform = transforms.Compose([
            transforms.ToTensor()
        ])
        image = transform(image).unsqueeze(0)

        with torch.no_grad():
            prediction = model(image)

        # Assuming prediction is a list of dictionaries
        objects = []
        for element in prediction[0]['labels']:
            label = element.item()
            # Converting labels (integers) to class names
            class_name = models.detection._utils.label_to_name(label)
            objects.append(class_name)

        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')

        for obj in objects:
            new_object = Object(name=obj, latitude=latitude, longitude=longitude)
            db.session.add(new_object)
        db.session.commit()

        return jsonify({'success': 'File uploaded and objects detected', 'objects': objects})

if __name__ == '__main__':
    app.run(debug=True)
