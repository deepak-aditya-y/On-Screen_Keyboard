# On-Screen Keyboard Project

This project allows users to input text using the tip of their fingers on any required input fields. It utilizes computer vision techniques to recognize finger positions and translate them into text input.

## Requirements

- **Python Version**: Python 3.8 is required for compatibility with the libraries used.
- **Libraries**:
  - `cvzone` (version 1.4.1)
  - `mediapipe` (version 0.8.7)
  - `pynput`

To install the required libraries, run:

pip install cvzone==1.4.1 mediapipe==0.8.7 pynput

## Project Structure

The project includes scripts and modules that enable finger position detection and text input functionality.

- **Finger Detection Script**: Captures finger movements and detects their positions for text input.
- **Input Handling Script**: Translates detected finger positions into corresponding text inputs on the screen.

## Working Example

Here’s an example of the on-screen keyboard in action:

![image](https://github.com/user-attachments/assets/a0636a31-f7bb-40e2-8d82-7a148735c92b)


---

This project demonstrates the capabilities of using computer vision for interactive input methods. Feel free to add more details or modify the structure as needed.

To install the required libraries, run:

```bash
pip install cvzone==1.4.1 mediapipe==0.8.7 pynput
