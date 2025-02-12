# Camarrow

Camarrow is a gesture-based control system that enables users to navigate applications using hand movements detected via a webcam. This project utilizes **MediaPipe Hands** for real-time hand tracking and **PyAutoGUI** for simulating keyboard interactions. Designed to enhance accessibility and provide a hands-free experience, Camarrow is particularly useful for gaming and touchless UI navigation.

## Features

- **Real-Time Hand Tracking**: Detects full palm gestures using MediaPipe Hands.
- **Gesture-Based Navigation**: Move left, right, up, or down by simply swiping your hand.
- **Optimized for Sensitivity & Accuracy**: Fine-tuned detection for smooth response.
- **Hands-Free Gaming**: Play games like Subway Surfers without touching the screen.
- **Minimal Dependencies**: Requires only a webcam and basic Python libraries.

## Installation

Ensure you have Python 3.7+ installed, then run the following command to install dependencies:

```bash
pip install mediapipe opencv-python pyautogui
```

## Usage

1. **Run the script**:
   ```bash
   python main.py
   ```
2. **Ensure proper lighting** for better gesture recognition.
3. **Raise your full palm** to activate gesture mode.
4. **Move your hand** left, right, up, or down to simulate keyboard swipes.
5. **Press 'q'** to exit the application.

## Usage Method

- **Swipe Right**: Moves right in the application.
- **Swipe Left**: Moves left in the application.
- **Swipe Up**: Moves up in the application.
- **Swipe Down**: Moves down in the application.
- **Palm Not Raised**: Gesture mode remains inactive.

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- PyAutoGUI
- Webcam

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance functionality.

## License

This project is licensed under the **MIT License**.
