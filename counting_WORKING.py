import cv2
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    numbersUP = 0


    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:


        # Get hand index to check label (left or right)
        index = results.multi_hand_landmarks.index(hand_landmarks)
        check_hand_LR = results.multi_handedness[index].classification[0].label

        # Set variable to keep landmarks positions (x and y)
        hand_mark_points = []

        # Fill list with x and y positions of each landmark
        for landmarks in hand_landmarks.landmark:
          hand_mark_points.append([landmarks.x, landmarks.y])

        # This rule applies to thumb

        # program checks if thumb is considered "raised" 
        # based on the position of its tip and intermediate point (IP)

        # if TIP[0] (xcoord) is greater than IP[0], then tip of thumb is further out on x axis than Phalanx. therefore left hand
        # if TIP[0] (xcoord) is less than IP[0], then Phalanx of thumb is further out on x axis than tip. therefore right hand

        if check_hand_LR == "Left" and hand_mark_points[4][0] > hand_mark_points[3][0]:
          numbersUP = numbersUP+1
        elif check_hand_LR == "Right" and hand_mark_points[4][0] < hand_mark_points[3][0]:
          numbersUP = numbersUP+1

        # ycoord of the fingertip compared to the ycoord of PIP
        # y axis increase when moving down
        # fingertip ycoord less than PIP, finger "raised"

        #Index finger
        if hand_mark_points[8][1] < hand_mark_points[6][1]:       
          numbersUP = numbersUP+1

        #Fuck finger
        if hand_mark_points[12][1] < hand_mark_points[10][1]:     
          numbersUP = numbersUP+1
        
        #Ring finger
        if hand_mark_points[16][1] < hand_mark_points[14][1]:     
          numbersUP = numbersUP+1

        #Pinky
        if hand_mark_points[20][1] < hand_mark_points[18][1]:     
          numbersUP = numbersUP+1


        # Draw hand landmarks 
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    # Display finger count
#    numbersUP = cv2.flip(numbersUP, 1)
    cv2.putText(image, str(numbersUP), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)

    #print string in console
#    print(numbersUP)

    # Flip the image horizontally so you look normal
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()






################################################################
#   Refrences
#https://google.github.io/mediapipe/solutions/hands
#https://colab.research.google.com/drive/1FvH5eTiZqayZBOHZsFm-i7D-JvoB9DVz
#https://ai.googleblog.com/2019/08/on-device-real-time-hand-tracking-with.html
#https://blog.tensorflow.org/2020/03/face-and-hand-tracking-in-browser-with-mediapipe-and-tensorflowjs.html
#