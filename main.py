import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

cap = cv2.VideoCapture(0)

prev_x, prev_y = 0, 0
gesture_active = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = [(int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])) for lm in hand_landmarks.landmark]

            if len(lm_list) >= 21:
                palm_base = lm_list[0]
                fingers_up = sum(lm_list[i][1] < lm_list[i - 2][1] for i in [8, 12, 16, 20])
                if fingers_up >= 4:
                    if not gesture_active:
                        prev_x, prev_y = palm_base
                        gesture_active = True
                    else:
                        curr_x, curr_y = palm_base

                        if curr_x - prev_x > 20:  #change sensitivity here
                            pyautogui.press("right")
                        elif prev_x - curr_x > 20: #change sensitivity here
                            pyautogui.press("left")
                        elif prev_y - curr_y > 20:  #change sensitivity here
                            pyautogui.press("up")
                        elif curr_y - prev_y > 20:  #change sensitivity here
                            pyautogui.press("down")

                        prev_x, prev_y = curr_x, curr_y
                else:
                    gesture_active = False

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
