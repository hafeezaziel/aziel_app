import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

# Google Gemini API Key (Replace with your actual key)
API_KEY = "AIzaSyCGyHTASn5v2rpo1KUZXr0Qx47L_Ia5A3Q"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateText?key={API_KEY}"

class AzielApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Input field
        self.input_box = TextInput(hint_text="Ask something...", size_hint_y=None, height=50)
        self.add_widget(self.input_box)

        # Submit button
        self.submit_button = Button(text="Ask", size_hint_y=None, height=50)
        self.submit_button.bind(on_press=self.get_response)
        self.add_widget(self.submit_button)

        # Output label
        self.response_label = Label(text="Response will appear here", size_hint_y=None, height=100)
        self.add_widget(self.response_label)

    def get_response(self, instance):
        user_input = self.input_box.text.strip()
        if not user_input:
            self.response_label.text = "Please enter a question."
            return

        # Send request to Google Gemini API
        payload = {
            "prompt": {"text": user_input},
            "temperature": 0.7
        }
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(API_URL, json=payload, headers=headers)
            response_data = response.json()

            if "candidates" in response_data:
                self.response_label.text = response_data["candidates"][0]["output"]
            else:
                self.response_label.text = "Error: Invalid response."

        except Exception as e:
            self.response_label.text = f"Error: {str(e)}"

class AzielAI(App):
    def build(self):
        return AzielApp()

if __name__ == "__main__":
    AzielAI().run()
