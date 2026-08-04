'''smart home device may have both WiFi connectivity and Voice control features.
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that
inherits from both using multiple inheritance'''

class WiFiDevice :
    def connect_wifi(self):
        print("connected to wifi")

class VoiceAssistant :
    def voice_command(self):
        print("voice command recognized")

class SmartSpeaker(WiFiDevice, VoiceAssistant) :
    def play_music(self):
        print("playing music")

speaker = SmartSpeaker()

speaker.connect_wifi()
speaker.voice_command()
speaker.play_music()