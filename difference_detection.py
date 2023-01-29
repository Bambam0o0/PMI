
# Imports
import cv2, os
import numpy as np

# Loading files
ref_pathfile = "no_car.jpg"
reference_image = cv2.imread(os.getcwd()+"\\"+ref_pathfile)
reference_image = cv2.resize(reference_image, (450, 580)) #resizing the ref picture if too large
gray_reference = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

curr_pathfile = "car.jpg"
current_image = cv2.imread(os.getcwd()+"\\"+curr_pathfile)
current_image = cv2.resize(current_image, (reference_image.shape[1], reference_image.shape[0])) #resizing to the ref picture size
gray_current = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)

# Displaying both pictures
cv2.imshow("reference image", reference_image) 
cv2.imshow("current image", current_image)

# Getting absolute difference between both grayscale pictures
difference = cv2.absdiff(gray_reference, gray_current)

# Set a treshold value to fix a tolerance
threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]

# Appliquer un morphologie pour enlever les bruits
kernel = np.ones((5,5),np.uint8)
threshold = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
threshold = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)

# Identify differences pixels 
contours = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

# Draw rectangle around the detected difference
for contour in contours:
    if cv2.contourArea(contour) > 1000:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(current_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("Place occupée")
    else:
        print("Place libre")

# Dispaly final picture with detected object
cv2.imshow("Difference", current_image)

# End keybind
cv2.waitKey(0)
cv2.destroyAllWindows()
