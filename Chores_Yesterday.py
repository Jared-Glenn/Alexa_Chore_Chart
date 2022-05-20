import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from datetime import datetime

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "And of which legendary child do you wish to hear?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class Ethan_IntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Ethan_Intent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        date_format = '%m/%d/%Y'
        original_date = datetime.strptime('4/8/2022', date_format)
        now = datetime.now()
        day_b = now.strftime("%m/%d/%Y")
        today = datetime.strptime(day_b, date_format)
        diff = (today - original_date).days
        day_modifier = (diff - 2) % 4

        if day_modifier == 0:
            mod = "feed the cat, empty the surprise box, clean the table"
        if day_modifier == 1:
            mod = "clean the front room, do an extra chore for Mom"
        if day_modifier == 2:
            mod = "unload and load the dishwasher"
        if day_modifier == 3:
            mod = "clean the backyard"
        
        speak_output = (
            "Yesterday, Ethan's chores were to {}, clean his room, make his bed, and read for 20 minutes.".format(mod))

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class Ellie_IntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Ellie_Intent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        date_format = '%m/%d/%Y'
        original_date = datetime.strptime('4/8/2022', date_format)
        now = datetime.now()
        day_b = now.strftime("%m/%d/%Y")
        today = datetime.strptime(day_b, date_format)
        diff = (today - original_date).days
        day_modifier = (diff - 1) % 4

        if day_modifier == 0:
            mod = "feed the cat, empty the surprise box, clean the table"
        if day_modifier == 1:
            mod = "clean the front room, do an extra chore for Mom"
        if day_modifier == 2:
            mod = "unload and load the dishwasher"
        if day_modifier == 3:
            mod = "clean the backyard"
        
        speak_output = (
            "Yesterday, Ellie's chores were to {}, clean her room, make her bed, and read for 20 minutes.".format(mod))

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class Abbie_IntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Abbie_Intent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        date_format = '%m/%d/%Y'
        original_date = datetime.strptime('4/8/2022', date_format)
        now = datetime.now()
        day_b = now.strftime("%m/%d/%Y")
        today = datetime.strptime(day_b, date_format)
        diff = (today - original_date).days
        day_modifier = (diff + 0) % 4

        if day_modifier == 0:
            mod = "feed the cat, empty the surprise box, clean the table"
        if day_modifier == 1:
            mod = "clean the front room, do an extra chore for Mom"
        if day_modifier == 2:
            mod = "unload and load the dishwasher"
        if day_modifier == 3:
            mod = "clean the backyard"
        
        speak_output = (
            "Yesterday, Abbie's chores were to {}, clean her room, and make her bed.".format(mod))

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class Gennie_IntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Gennie_Intent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        date_format = '%m/%d/%Y'
        original_date = datetime.strptime('4/8/2022', date_format)
        now = datetime.now()
        day_b = now.strftime("%m/%d/%Y")
        today = datetime.strptime(day_b, date_format)
        diff = (today - original_date).days
        day_modifier = (diff + 1) % 4

        if day_modifier == 0:
            mod = "feed the cat, empty the surprise box, clean the table"
        if day_modifier == 1:
            mod = "clean the front room, do an extra chore for Mom"
        if day_modifier == 2:
            mod = "unload and load the dishwasher"
        if day_modifier == 3:
            mod = "clean the backyard"
        
        speak_output = (
            "Yesterday, Jenny's chores were to {}, clean her room, and make her bed.".format(mod))

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class Short_IntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Short_Intent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        date_format = '%m/%d/%Y'
        original_date = datetime.strptime('4/8/2022', date_format)
        now = datetime.now()
        day_b = now.strftime("%m/%d/%Y")
        today = datetime.strptime(day_b, date_format)
        diff = (today - original_date).days
        day_modifier = (diff - 1) % 4

        if day_modifier == 0:
            words = (
            "Ethan was on table duty, Ellie had Mom's extra chore, Abbie was on dishwasher, and Jenny was on the backyard.")
        if day_modifier == 1:
            words = (
            "Ethan had Mom's extra chore, Ellie was on dishwasher, Abbie was on the backyard, and Jenny was on table duty.")
        if day_modifier == 2:
            words = (
            "Ethan was on dishwasher, Ellie was on the backyard, Abbie was on table duty, and Jenny had Mom's extra chore.")
        if day_modifier == 3:
            words = (
            "Ethan was on the backyard, Ellie was on table duty, Abbie had Mom's extra chore, Jenny was on dishwasher.")

        speak_output = (
            "{}".format(words))

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "I have a list of chores for you today! Just tell me your name and I'll look them up."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure who you said. What lucky child wants to know his or her chores?"
        reprompt = "I'll check the list again. What was that name?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )



sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(Ethan_IntentHandler())
sb.add_request_handler(Ellie_IntentHandler())
sb.add_request_handler(Abbie_IntentHandler())
sb.add_request_handler(Gennie_IntentHandler())
sb.add_request_handler(Short_IntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()