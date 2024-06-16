# Garbaggio Web Application

Garbaggio is a web application designed to facilitate the collection and sharing of free items available around town. Users can upload photos of items, which are then automatically analyzed using a machine learning model to detect objects. Detected objects are stored in a database along with their location and timestamp information.

## Features

- **Object Detection**: Utilizes a pre-trained Mask R-CNN model from PyTorch to detect objects in uploaded photos.
- **Database Storage**: Stores detected objects in an SQLite database (`database.db`) with attributes including object name, latitude, longitude, and timestamp.
- **Web Interface**: Provides a user-friendly web interface where users can upload photos and view detected objects.
- **Responsive Design**: Built with Flask (backend) and Vue.js (frontend) for a modern and responsive user experience.

## Tech Stack

- **Backend**: Flask (Python)
  - Flask-SQLAlchemy: ORM for database management
  - Flask-CORS: Handling Cross-Origin Resource Sharing
- **Frontend**: Vue.js
  - Axios: HTTP client for making requests to the Flask backend
- **Machine Learning**: PyTorch (Torchvision)
  - Used for object detection with a Mask R-CNN model

## Installation

### Prerequisites

- Python 3.8+ installed on your system
- Node.js and npm (Node Package Manager) installed for Vue.js frontend development

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd Garbaggio
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**:
   ```bash
   cd frontend
   npm install
   ```

5. **Run the application**:
   - Start the Flask backend:
     ```bash
     python backend/app.py
     ```
   - Start the Vue.js frontend (in a separate terminal):
     ```bash
     cd frontend
     npm run serve
     ```

6. **Access the application**:
   Open a web browser and go to `http://localhost:8080` (or the URL shown in the terminal after running `npm run serve`) to use the Garbaggio web application.

### Usage

1. **Upload Photo**:
   - Click on the upload button and select a photo of an item available for pickup.
   - Enter the latitude and longitude coordinates of the item's location.

2. **Object Detection**:
   - The uploaded photo is processed using a pre-trained Mask R-CNN model.
   - Detected objects are displayed on the screen.

3. **Database Storage**:
   - Detected objects, along with their location and timestamp, are stored in the SQLite database (`backend/database.db`).

### Contributing

Contributions are welcome! If you'd like to enhance the Garbaggio web application, please fork the repository and create a pull request with your proposed changes. Ensure your code follows the project's coding style and includes relevant tests.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- The Mask R-CNN model used for object detection is based on the torchvision library from PyTorch.
- Flask and Vue.js communities for their excellent documentation and resources.
