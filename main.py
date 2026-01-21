import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open camera.")
else: 
    print("Camera opened successfully.")

for i in range(31):
    ret, frame = cap.read()
    background_frame = frame 

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break
    
    hsv_image= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_green = [0, 120, 70]
    upper_green = [10, 255, 255]
    
    lower_green = np.array(lower_green, dtype="uint8")
    upper_green = np.array(upper_green, dtype="uint8")
    
    mask = cv2.inRange(hsv_image, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)
    
    masked_frame = cv2.bitwise_and(frame, frame, mask=mask_inv)
    masked_background = cv2.bitwise_and(background_frame, background_frame, mask=mask)

    result = cv2.add(masked_frame, masked_background)

    cv2.imshow('Invisible Frame', result)
    cv2.imshow("Original Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()