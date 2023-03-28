# importing necessary libraries
import cv2

# reading image
img = cv2.imread("ronaldo.jpg")

# edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# cartoonization
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

# showing the outputs
cv2.imshow("image", img)
cv2.imshow("edges", edges)
cv2.imshow("cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllwindows()
