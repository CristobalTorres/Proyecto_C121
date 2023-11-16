import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)


finger_tips = [8, 12, 16, 20]
thumb_tip = 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)
    finger_fold_status = []

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            # Acceder a los puntos de referencia por su posición
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

             # El código va aquí  
               # Comprobar si la posición X de las puntas es más pequeña que la otra posición X del punto de referencia del dedo
            for tip in finger_tips:
                if lm_list[tip].x < lm_list[tip - 3].x:
                    # Si la condición es verdadera, crea un círculo de color verde en las puntas
                    x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)
                    cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
                    # Agregar el valor True a la matriz finger_fold_status
                    finger_fold_status.append(True)
                else:
                    # Agregar False si la condición no se cumple
                    finger_fold_status.append(False)
        
        if all(finger_fold_status):
            if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y:
                print("Me gusta")
                cv2.putText(img,"megusta",(20,30),cv2.FONT_HERSHEY_SIMMPLEX,1,(0,225,0),3)
        if all(finger_fold_status):
            if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y:
                print("Me gusta")
                cv2.putText(img,"megusta",(20,30),cv2.FONT_HERSHEY_SIMMPLEX,1,(0,0,255),3)

        mp_draw.draw_landmarks(img, hand_landmark,
        mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
        mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("Rastreo de manos", img)
    cv2.waitKey(1)
finger_fold_status = []



