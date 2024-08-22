
# Voice-Based Email System

A Python-based project that allows users to send emails using voice commands. This project utilizes various libraries to recognize and process speech, enabling hands-free email composition and sending.

## Features

- Voice recognition using `SpeechRecognition`.
- Email sending functionality through `smtplib`.
- Text-to-speech for responses and confirmations.
- Simple and intuitive voice-based interaction.

## Requirements

Make sure you have the following Python libraries installed:

pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
pip install smtplib
pip install email-validator


## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Rohit-222/Voice-Based-Email-Sender
   cd Voice-Based-Email-System
   ```

2. **Install the required libraries**:

   Run the following command to install the necessary Python libraries:

   ```bash
   pip install SpeechRecognition
   pip install pyttsx3
   pip install pyaudio
   pip install smtplib
   pip install email-validator
   ```

   > **Note:** If you do not have `pip` installed, refer to the official [pip installation guide](https://pip.pypa.io/en/stable/installation/).

3. **Configuration**:

    Add your sender's email and reciever's address and give it a nickname so that when sending you can call in short name.(This has to be done in line 28,30,31 of voice_basic_imp.py file)

4. **Running the Project**:

   To start the voice-based email system, run:

   ```bash
   python voice_based_email.py
   ```

   Follow the voice prompts to send an email.

## Usage

1. Run the project using the command provided above.
2. Speak clearly when prompted to dictate the recipient's email address, subject, and body of the email.
3. The system will confirm your inputs before sending the email.

## Contributing

Feel free to fork this project, submit pull requests, or open issues for any bugs or feature requests.


## Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)
