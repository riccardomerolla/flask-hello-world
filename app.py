import logging

logging.basicConfig(level=logging.DEBUG)

from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

slack_app = App()


@slack_app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()


@slack_app.event("app_mention")
def event_test(body, say, logger):
    logger.info(body)
    say("What's up?")


@slack_app.event("message")
def handle_message():
    pass


from flask import Flask, request, jsonify

from service.notifications import Notifications

app = Flask(__name__)
handler = SlackRequestHandler(slack_app)


@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


@app.route("/send-message", methods=["POST"])
def send_message():
    content = request.json
    print(Notifications().send_message_from_request(content))
    return jsonify({"result":"OK"})


@app.route("/echo", methods=["GET"])
def echo():
    return "Hello, SLACK-APP-BOLT!"
