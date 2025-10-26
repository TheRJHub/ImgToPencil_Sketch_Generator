import cv2
import numpy as np

# --- Load Image ---
image_path = r"C:\Users\KIIT\OneDrive\Desktop\Project\FactoryDesignPattern\RRR.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found at", image_path)
    exit()

# --- Convert to Grayscale ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# --- Invert Grayscale ---
inv_gray = 255 - gray

# --- Apply Gaussian Blur for Pencil Effect ---
blur = cv2.GaussianBlur(inv_gray, (21, 21), 0)

# --- Create Pencil Sketch ---
sketch = cv2.divide(gray, 255 - blur, scale=256)

# --- Convert to BGR to Add Text ---
sketch_bgr = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

# --- Add Watermark ---
watermark_text = "Art By Rajat"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6  # small size
thickness = 1
color = (0, 0, 0)  # black text

(text_width, text_height), baseline = cv2.getTextSize(watermark_text, font, font_scale, thickness)
x = sketch_bgr.shape[1] - text_width - 10
y = sketch_bgr.shape[0] - 10

cv2.putText(sketch_bgr, watermark_text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)

# --- Display Result ---
cv2.imshow("Original", img)
cv2.imshow("Pencil Sketch", sketch_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()