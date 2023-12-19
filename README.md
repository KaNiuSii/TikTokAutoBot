
# TikTok Automation Project

## Overview
This project is a Python-based TikTok automation tool, leveraging the Selenium library for web automation. It allows users to upload videos to TikTok with custom captions.

## Features
- **Automated TikTok Login**: Log into TikTok through an automated Chrome browser window.
- **Video Upload**: Upload a selected video file to TikTok.
- **Custom Captions**: Write and attach custom captions to the video from a text file.

## Prerequisites
- Python 3.x
- PyQt5
- Selenium
- Chrome WebDriver

## Installation
1. **Clone the repository**:
   ```bash
   git clone [repository URL]
   ```

2. **Set up a Python virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Structure
- `main.py`: The main GUI application script using PyQt5.
- `bot.py`: Contains the core functionality for interacting with TikTok using Selenium.
- `caption.txt`: A placeholder file for the user to input custom captions.
- `venv/`: Virtual environment folder (if used).
- `__pycache__/`: Python cache files.

## Usage
1. **Launch the Application**:
   Run `main.py` to start the GUI application.
   ```bash
   python main.py
   ```

2. **Select a Video File**:
   Use the 'Browse' button in the application to select a video file for upload.

3. **Enter Caption**:
   In the 'Enter Caption' box, type the caption you wish to accompany your video on TikTok. Write Description first, then every tag in a new line.

4. **Run the Bot**:
   Click the 'Run' button to start the upload process. The bot will open a Chrome window, log into TikTok, and perform the upload.
<br>![image](https://github.com/KaNiuSii/TikTokAutoBot/assets/123270897/7a5c34e8-b06a-421b-b1c0-6be5ad805a51)<br>

## Important Notes
- Ensure you have Chrome browser installed.
- The application might face issues due to unforeseen web element changes on TikTok; restart the application in such cases.
- The application requires manual login to TikTok.

## Troubleshooting
- If you encounter any issues, check if TikTok's website structure has changed and update the XPath selectors in `bot.py` accordingly.
- For issues related to Selenium or WebDriver, ensure your Chrome version is compatible with the installed ChromeDriver version.

## Contributing
Contributions, issues, and feature requests are welcome.

---

*For more information or help, please refer to the documentation or contact the repository owner.*
