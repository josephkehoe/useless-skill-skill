from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder
import mycroft.audio

class UselessSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.id="mud"
    @intent_handler(IntentBuilder("").require("skill.useless").require("Identity").build())
    def handle_skill_useless(self, message):
        id=message.data.get("Identity")
        self.speak_dialog('skill.useless',{"Name":id})


def create_skill():
    return UselessSkill()

