Se connecter

S'inscrire
Vous avez dit :
give me a readme for tis project and a title " import cv2
import pytesseract
from googletrans import Translator

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust this path as needed

# Initialize the Google Translator
translator = Translator()

def translate_text(text):
    try:
        if text.strip():  # Check if the text is not empty
            translation = translator.translate(text, src='en', dest='fr')
            return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
    return ""

def wrap_text(text, font, max_width):
    """Wrap text to fit within the specified width."""
    lines = []
    words = text.split(' ')
    current_line = ""

    for word in words:
        # Measure the width of the current line with the new word
        test_line = f"{current_line} {word}".strip()
        (width, _), _ = cv2.getTextSize(test_line, font[0], font[1], font[2])
        
        if width <= max_width:  # If it fits, add the word to the line
            current_line = test_line
        else:  # Otherwise, start a new line
            if current_line:  # Only add if current line is not empty
                lines.append(current_line)
            current_line = word  # Start a new line with the current word

    if current_line:  # Add any remaining text
        lines.append(current_line)
    
    return lines

def ocr_and_translate(frame):
    # Use pytesseract to do OCR on the frame
    text = pytesseract.image_to_string(frame)
    
    # Translate the text to French
    translated_text = translate_text(text)
    
    return text, translated_text

"""1- if you want to test it with cmputer cam use this """
"""
def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    font = (cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)  # Font, scale, thickness
    max_width = 600  # Maximum width for wrapping

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Perform OCR and translation
        text, translated_text = ocr_and_translate(frame)

        # Wrap the text
        wrapped_text = wrap_text(text, font, max_width)
        wrapped_translated_text = wrap_text(translated_text, font, max_width)

        # Display the detected text and the translated text on the frame
        y_offset = 30  # Starting y position
        for line in wrapped_text:
            cv2.putText(frame, line, (10, y_offset), font[0], font[1], (255, 0, 0), font[2])
            y_offset += 30  # Move down for the next line
        
        y_offset += 10  # Add a small space between detected and translated text
        for line in wrapped_translated_text:
            cv2.putText(frame, line, (10, y_offset), font[0], font[1], (0, 255, 0), font[2])
            y_offset += 30  # Move down for the next line

        # Show the frame with the detected and translated text
        cv2.imshow('Camera', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
"""

"""2- if you wnt to use it with your phone cam use this and downlad the app ipwebcam andoid app store"""
def main():
    # Set the URL of the IP camera stream
    ip_camera_url = 'http://192.168.1.10:8080/video'  # Adjust this with your phone's IP address and port
    cap = cv2.VideoCapture(ip_camera_url)
    font = (cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)  # Font, scale, thickness
    max_width = 600  # Maximum width for wrapping

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Perform OCR and translation
        text, translated_text = ocr_and_translate(frame)

        # Wrap the text
        wrapped_text = wrap_text(text, font, max_width)
        wrapped_translated_text = wrap_text(translated_text, font, max_width)

        # Display the detected text and the translated text on the frame
        y_offset = 30  # Starting y position
        for line in wrapped_text:
            cv2.putText(frame, line, (10, y_offset), font[0], font[1], (255, 0, 0), font[2])
            y_offset += 30  # Move down for the next line
        
        y_offset += 10  # Add a small space between detected and translated text
        for line in wrapped_translated_text:
            cv2.putText(frame, line, (10, y_offset), font[0], font[1], (0, 255, 0), font[2])
            y_offset += 30  # Move down for the next line

        # Show the frame with the detected and translated text
        cv2.imshow('Camera', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
" 
ChatGPT a dit :
ChatGPT
OCR and Translation with Real-Time Camera Feed
This project demonstrates how to use Optical Character Recognition (OCR) and translation services to process and display text in real-time from a camera feed. The application captures video from either a computer's webcam or an IP camera, performs OCR to extract text from the video frames, translates the extracted text from English to French, and displays both the original and translated text on the video feed.

Prerequisites
Python: Ensure Python is installed on your system.

Libraries:

opencv-python for handling video capture and display.
pytesseract for performing OCR.
googletrans for translating text.
Install these dependencies using pip:

bash
Copier le code
pip install opencv-python pytesseract googletrans==4.0.0-rc1
Tesseract-OCR: Download and install Tesseract-OCR from Tesseract's official repository. Update the pytesseract.pytesseract.tesseract_cmd path in the code to match the location where Tesseract is installed.

Code Overview
OCR and Translation Functions
translate_text(text): Translates the given English text into French using Google Translate.
wrap_text(text, font, max_width): Wraps the given text to fit within a specified width for display purposes.
ocr_and_translate(frame): Extracts text from the given video frame using OCR and translates it to French.
Main Execution
There are two options for capturing video: from a computer's webcam or from an IP camera.

1. Using a Computer Webcam
Uncomment the following main() function to use the webcam:

python
Copier le code
def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    font = (cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)  # Font, scale, thickness
    max_width = 600  # Maximum width for wrapping

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Perform OCR and translation
        text, translated_text = ocr_and_translate(frame)

        # Wrap the text
        wrapped_text = wrap_text(text, font, max_width)
        wrapped_translated_text = wrap_text(translated_text, font, max_width)

        # Display the detected text and the translated text on the frame
        y_offset = 30  # Starting y position
        for line in wrapped_text:
            cv2.putText(frame, line, (10, y_offset), font[0], font[1], (255, 0, 0), font[2])
            y_offset += 30  # Move down for the next line
        
        y_offset += 10  # Add a small space between detected and translated text
        for line in wrapped_translated_text:
            cv2.putText(frame, line, (10, y_offset), font[0], font[1], (0, 255, 0), font[2])
            y_offset += 30  # Move down for the next line

        # Show the frame with the detected and translated text
        cv2.imshow('Camera', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()
2. Using an IP Camera
Uncomment the following main() function to use an IP camera:

python
Copier le code
def main():
    # Set the URL of the IP camera stream
    ip_camera_url = 'http://192.168.1.10:8080/video'  # Adjust this with your phone's IP address and port
    cap = cv2.VideoCapture(ip_camera_url)
    font = (cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)  # Font, scale, thickness
    max_width = 600  # Maximum width for wrapping

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Perform OCR and translation
        text, translated_text = ocr_and_translate(frame)

        # Wrap the text
        wrapped_text = wrap_text(text, font, max_width)
        wrapped_translated_text = wrap_text(translated_text, font, max_width)

        # Display the detected text and the translated text on the frame
        y_offset = 30  # Starting y position
        for line in wrapped_text:
            cv2.putText(frame, line, (10, y_offset), font[0], font[1], (255, 0, 0), font[2])
            y_offset += 30  # Move down for the next line
        
        y_offset += 10  # Add a small space between detected and translated text
        for line in wrapped_translated_text:
            cv2.putText(frame, line, (10, y_offset), font[0], font[1], (0, 255, 0), font[2])
            y_offset += 30  # Move down for the next line

        # Show the frame with the detected and translated text
        cv2.imshow('Camera', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()
Running the Code
Ensure all prerequisites are installed.
Adjust the Tesseract executable path and IP camera URL as necessary.
Uncomment the appropriate main() function for your setup.
Run the script using Python:
bash
Copier le code
python script_name.py
Notes
Press 'q' to exit the video feed window.
For IP camera usage, ensure that the IP address and port are correct and that the camera stream is accessible.
Feel free to customize the font settings, translation languages, and other parameters as needed for your specific use case.



Vous avez dit :
readme please for my githu repository
ChatGPT a dit :
ChatGPT
Here's a structured README.md file for your GitHub repository:

markdown
Copier le code
#Setup
Clone the repository:

bash
Copier le code
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
Adjust Tesseract Path: Edit the script to set the correct path for the Tesseract executable:

python
Copier le code
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Change the path according to your installation directory.

IP Camera Configuration (if using an IP camera): Set the correct URL for your IP camera stream in the main() function:

python
Copier le code
ip_camera_url = 'http://192.168.1.10:8080/video'
Usage
Using a Computer Webcam
Uncomment the main() function for webcam use in the script:

python
Copier le code
def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    ...
Using an IP Camera
Uncomment the main() function for IP camera use in the script:

python
Copier le code
def main():
    # Set the URL of the IP camera stream
    ip_camera_url = 'http://192.168.1.10:8080/video'
    ...
Run the script:

bash
Copier le code
python your_script_name.py
Exit the video feed: Press 'q' while the video window is active to quit.

Code Overview
translate_text(text): Translates English text to French.
wrap_text(text, font, max_width): Wraps text to fit within a specified width for display.
ocr_and_translate(frame): Performs OCR on the frame and translates the text.
main(): Captures video from the webcam or IP camera, performs OCR and translation, and displays the results.
Troubleshooting
No video feed: Ensure the camera is properly connected and accessible. For IP cameras, verify the URL and network settings.
Text not detected: Ensure the Tesseract-OCR installation is correct and the path is set properly.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Tesseract-OCR: Open-source OCR engine.
Google Translate API: Used for text translation.
OpenCV: Library used for video capture and display.