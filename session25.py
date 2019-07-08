import cv2
import pytesseract

image = cv2.imread("data.png", 1)
print(image)

text = pytesseract.image_to_string(image)
print(text)

# Scan an Image : eg:Blood Report Sample
# See h.w




