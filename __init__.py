from mycroft import MycroftSkill, intent_file_handler


class UselessSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.useless.intent')
    def handle_skill_useless(self, message):
        self.speak_dialog('skill.useless')


def create_skill():
    return UselessSkill()

