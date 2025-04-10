import pyttsx3
import pyaudio
import webbrowser
# import speech_recognition
import speech_recognition as sr

class Jarvis:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.set_voice(0)  # Default to first voice
        self.set_rate(120)  # Default speech rate

    def set_voice(self, voice_id):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice_id].id)

    def set_rate(self, rate):
        self.engine.setProperty('rate', rate)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                print('Recognizing...')
                return self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                print("Could not understand audio")
                return None
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service")
                return None

    def handle_command(self, command):
        if command is None:
            return

        command = command.lower()
        if "jarvis" in command:
            self.speak("Yes sir, I am here. How may I help you?")
            self.process_user_input()
        elif 'your age' in command:
            self.speak("I have no age. I was created on December 6, 2023.")
        elif any(platform in command for platform in ['google', 'youtube', 'facebook', 'whatsapp', 'instagram']):
            self.open_website(command)
        elif any(exit_word in command for exit_word in ['exit', 'quit', 'leave']):
            self.speak("Goodbye!")
            return True  # Signal to exit the loop
        else:
            self.speak("Sorry, I didn't understand that. Please try again.")
        return False  # Continue the loop

    def process_user_input(self):
        user_input = self.listen()
        return self.handle_command(user_input)

    def open_website(self, command):
        platforms = {
            'google': 'https://www.google.com',
            'youtube': 'https://www.youtube.com',
            'facebook': 'https://www.facebook.com',
            'whatsapp': 'https://www.whatsapp.com',
            'instagram': 'https://www.instagram.com'
        }
        for platform, url in platforms.items():
            if platform in command:
                webbrowser.open_new(url)
                self.speak(f"Opening {platform}. What should I search for?")
                return

if __name__ == '__main__':
    jarvis = Jarvis()
    while True:
        if jarvis.process_user_input():
            break  # Exit the loop if the user says exit, quit, or leave



