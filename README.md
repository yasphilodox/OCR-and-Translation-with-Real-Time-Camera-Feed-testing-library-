# OCR and Translation with Real-Time Camera Feed

This project demonstrates real-time Optical Character Recognition (OCR) using Tesseract and translates detected English text into French using the Google Translate API.

## How to Use

1. **Install Dependencies**: Install the necessary libraries using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Code**:

   - For using a computer camera:
     ```bash
     python real_time_ocr.py
     ```

   - For using an IP camera (e.g., your phone): Change the `ip_camera_url` in the code to match your phone's IP camera URL and run:
     ```bash
     python real_time_ocr.py
     ```

## Dependencies

- OpenCV
- pytesseract
- googletrans
