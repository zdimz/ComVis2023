import cv2
import numpy as np

def detect_copy_move(image_path):
    # Load image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Apply threshold to create binary image
    threshold = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)[1]

    # Find contours in binary image
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over contours
    for contour in contours:
        # Calculate contour area
        area = cv2.contourArea(contour)

        # Ignore small contours
        if area < 1000:
            continue

        # Create mask for contour
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [contour], 0, 255, -1)

        # Calculate mean color of pixels inside contour
        mean = cv2.mean(img, mask=mask)[:3]

        # Search for similar pixels in image
        matches = cv2.matchTemplate(img, mask, cv2.TM_CCOEFF_NORMED)
        locations = np.where(matches >= 0.99)

        # Draw rectangles around matching areas
        for location in zip(*locations[::-1]):
            x, y = location
            w, h = contour.shape[0], contour.shape[1]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display result
    cv2.imshow('result', img)
    cv2.waitKey(0)

# Example usage
detect_copy_move('image.jpg')
