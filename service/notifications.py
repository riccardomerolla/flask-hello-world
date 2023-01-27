import os
from slack_sdk import WebClient

class Notifications:
    """Logic to handle notifications to our Slack App"""

    def send_message_from_request(self, content):
        try:
            user_id = content['userid']
            notification_type = content['type']
            payload = content['payload']
        except KeyError as ex:
            error_message = 'Mandatory parameter is missing: %s' % str(ex)
            return error_message
        self._send_message(user_id, notification_type, payload)
        return content

    def _send_message(self, user_id, notification_type, payload):
        try:
            # ID of the channel you want to send the message to
            channel_id = user_id
            bot_access_token = os.environ["SLACK_BOT_TOKEN"]
        
            client = WebClient(token=bot_access_token)
            response = client.chat_postMessage(
                channel=channel_id,
                blocks=[
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "Hello, Assistant to the Regional Manager Dwight! *Michael Scott* wants to know where you'd like to take the Paper Company investors to dinner tonight.\n\n *Please select a restaurant:*"
                                }
                            },
                            {
                                "type": "divider"
                            },
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "*Farmhouse Thai Cuisine*\n:star::star::star::star: 1528 reviews\n They do have some vegan options, like the roti and curry, plus they have a ton of salad stuff and noodles can be ordered without meat!! They have something for everyone here"
                                },
                                "accessory": {
                                    "type": "image",
                                    "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/c7ed05m9lC2EmA3Aruue7A/o.jpg",
                                    "alt_text": "alt text for image"
                                }
                            },
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "*Kin Khao*\n:star::star::star::star: 1638 reviews\n The sticky rice also goes wonderfully with the caramelized pork belly, which is absolutely melt-in-your-mouth and so soft."
                                },
                                "accessory": {
                                    "type": "image",
                                    "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/korel-1YjNtFtJlMTaC26A/o.jpg",
                                    "alt_text": "alt text for image"
                                }
                            },
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "*Ler Ros*\n:star::star::star::star: 2082 reviews\n I would really recommend the  Yum Koh Moo Yang - Spicy lime dressing and roasted quick marinated pork shoulder, basil leaves, chili & rice powder."
                                },
                                "accessory": {
                                    "type": "image",
                                    "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/DawwNigKJ2ckPeDeDM7jAg/o.jpg",
                                    "alt_text": "alt text for image"
                                }
                            },
                            {
                                "type": "divider"
                            },
                            {
                                "type": "actions",
                                "elements": [
                                    {
                                        "type": "button",
                                        "text": {
                                            "type": "plain_text",
                                            "text": "Farmhouse",
                                            "emoji": True
                                        },
                                        "value": "click_me_123"
                                    },
                                    {
                                        "type": "button",
                                        "text": {
                                            "type": "plain_text",
                                            "text": "Kin Khao",
                                            "emoji": True
                                        },
                                        "value": "click_me_123",
                                        "url": "https://google.com"
                                    },
                                    {
                                        "type": "button",
                                        "text": {
                                            "type": "plain_text",
                                            "text": "Ler Ros",
                                            "emoji": True
                                        },
                                        "value": "click_me_123",
                                        "url": "https://google.com"
                                    }
                                ]
                            }
                        ]
            )
            print(response)
            if not response['ok']:
                raise Exception('Slack API call chat.postMessage returned with ok=False.')

        # TODO: handle error responses from Slack
        except Exception as ex:
            raise Exception('Unhandled error: %s' % str(ex))
        
        print(user_id, notification_type, payload)