# Check Python version
python --version

# Upgrade pip
python -m pip install --upgrade pip

# Create and activate a new virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install Flask dependencies
pip install Flask==3.0.3 Flask-SQLAlchemy==3.1.1 Flask-CORS==4.0.1 Pillow==9.0.0

# Install PyTorch
pip install torch torchvision torchaudio
# Or for CUDA support
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
