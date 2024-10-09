import cv2  # For image processing
import pytesseract  # For OCR
import pickle  # To load the trained model

# Load your pre-trained ML model
model_path = 'path_to_your_model/nutrition_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

def process_image(image_path):
    # Open and read the image file
    image = cv2.imread(image_path)

    # Use OCR to extract text (e.g., nutrition information)
    extracted_text = pytesseract.image_to_string(image)

    # Pass the extracted text to your ML model
    prediction = model.predict([extracted_text])  # Assuming your model works on text input

    return prediction  # Return the prediction/output
