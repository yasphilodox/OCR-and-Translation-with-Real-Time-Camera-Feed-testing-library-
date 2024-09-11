import cv2
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
