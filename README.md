
Image Duplicator GUI – Batch Duplicate and Rename Images Easily
===============================================================

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-yellowgreen)

A user-friendly Python desktop application to batch duplicate and rename image files using custom codes. The GUI interface, built with Tkinter, simplifies image management for photographers, data annotators, researchers, and developers.

Key Features
------------
- Upload multiple image files in bulk
- Input unique codes to rename duplicated images
- Preview output filenames before processing
- Reorder uploaded images via drag buttons (Move Up / Down)
- Automatically saves renamed files in an `output` folder
- Built using Python and Pillow for image handling

System Requirements
-------------------
- Python 3.6 or later
- pip (Python package installer)
- OS: Windows, macOS, or Linux

Installation Guide
------------------

### Step 1: Clone or Download the Repository

If using Git:
    git clone https://github.com/yourusername/image-duplicator-gui.git
    cd image-duplicator-gui

Or simply download the `image_duplicator_gui.py` file into a folder.

### Step 2: Install Dependencies

Make sure Pillow is installed:

    pip install pillow

Running the Application
-----------------------

Launch the app by running the script in your terminal or command prompt:

    python image_duplicator_gui.py

Usage Instructions
------------------

### 1. Upload Images
Click "Upload Images" and select one or more `.jpg`, `.png`, `.jpeg`, or `.bmp` image files.

### 2. Enter Codes
Type or paste the desired codes into the textbox. Use commas or new lines to separate codes.

Examples:

    A001, A002, A003

    or

    A001
    A002
    A003

### 3. Preview Filenames (Optional)
Click "Preview Output Filenames" to see how each image will be renamed.

### 4. Duplicate and Rename Images
Click "Duplicate and Rename". The app will create renamed copies of the uploaded images for every code.

Files are saved in the newly created folder:

    output/

### 5. Reorder Images (Optional)
Use "Move Up" and "Move Down" buttons to reorder the uploaded image list before duplication. This affects the filename suffix (_1, _2, etc.) order.

How the Image Duplication Works
-------------------------------

For each code you enter:
- The app duplicates every uploaded image.
- It renames them in the format:

      04-CODE.jpg
      04-CODE_1.jpg
      04-CODE_2.jpg
      ...

If you upload 3 images and enter 2 codes (e.g., `X001` and `X002`), you will get 6 output files:

    04-X001.jpg
    04-X001_1.jpg
    04-X001_2.jpg
    04-X002.jpg
    04-X002_1.jpg
    04-X002_2.jpg

Search Engine Optimization (SEO) Notes
--------------------------------------

This tool is ideal for:
- Bulk image duplication and renaming
- Dataset preparation for machine learning and computer vision
- Renaming images with batch codes for filing or archival
- GUI tools for image management
- Open-source batch image processing tools in Python

License
-------
MIT License – Free to use, modify, and distribute.

Support and Contributions
-------------------------

For feature requests, issues, or contributions, please open a GitHub issue or pull request.
