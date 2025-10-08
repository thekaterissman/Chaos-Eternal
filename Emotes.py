class Emote:
    def __init__(self):
        self.emotes = {
            "wave": "You wave your hand in a friendly gesture.",
            "nod": "You nod your head in agreement.",
            "shake_head": "You shake your head in disagreement.",
            "point": "You point towards something in the distance.",
            "think": "You stroke your chin thoughtfully.",
            "celebrate": "You pump your fist in the air triumphantly."
        }

    def perform_emote(self, emote_name):
        return self.emotes.get(emote_name, "You try to perform an emote, but nothing comes to mind.")

    def get_available_emotes(self):
        return list(self.emotes.keys())