from mycroft import MycroftSkill, intent_file_handler


class Sinaisdealerta(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sinaisdealerta.intent')
    def handle_sinaisdealerta(self, message):
        self.speak_dialog('sinaisdealerta')


def create_skill():
    return Sinaisdealerta()

