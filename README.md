# 🌍 Terminal Globe
A small Python project that renders a rotating globe directly in the terminal using ASCII characters.

The program converts a world map image into a character-based representation by sampling its pixels and comparing RGB color distances. The resulting map is then continuously shifted to simulate the globe rotating.

# Demo
<img width="320" height="320" alt="Hello World Demo" src="https://github.com/user-attachments/assets/5d7a044c-3196-47fd-8aab-5ac2aead3c5c"/>

# Features
ASCII-style globe rendering in the terminal
Image-based map generation using Pillow
RGB color-distance based pixel classification
Adjustable image quality
Adjustable rotation speed

# Requirements
- Python 3.x
- Pillow

Install Pillow with: `pip install Pillow`

# Usage
Place WorldMap.jpg in the project directory and run: `python main.py`

The program will ask for:
- Image Quality — controls the size/detail of the generated map
- Rotation Speed — controls how quickly the globe moves

# How It Works
1. The world map image is loaded using Pillow.
2. Pixels are sampled at intervals based on the selected image quality.
3. Each sampled pixel is classified by comparing its RGB distance to the defined empty and block colors.
4. The resulting map is represented using spaces and # characters.
5. The map is shifted horizontally and vertically each frame to create the rotation effect.
6. A circular distance check limits the visible area to the shape of a globe.

# Purpose
This project was created as a small programming experiment to explore basic image processing, coordinate calculations, and terminal rendering in Python.
