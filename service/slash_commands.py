
class SlashCommands:
    """Logic for the different Slash commands our Slack App supports"""

    def get_video_payload(self):
        return "Create your Prezi video here: " + "https://prezi.com/v/create/"

    def get_present_payload(self):
        return "Create your Prezi present here: " + "https://prezi.com/p/create-prezi/"

    def get_shared_payload(self):
        return "TO DO"