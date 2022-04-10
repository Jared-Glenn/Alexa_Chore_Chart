#class ChoreIntentHandler(AbstractRequestHandler):
#    def can_handle(self, handler input):
#        return ask_utils.is_intent_name("ChoreIntent")(handler_input)
#
#    def handle(self, handler_input):
#        speak_output = "Let's take a look at today's chores."
#
#        return (
#            handler_input.response_builder
#            .speak(speak_output)
#            .ask(speak_output)
#            .response
#        )
#
#sb.add_request_handler(ChoreIntentHandler())
#
#

from datetime import date

measure_from = date(2022, 4, 8)
tday = date.today()
diff = (tday - measure_from).days

day_mod = None

x = 0

def chore(x):
    if x == 0:
        return """Feed the cat,
Empty the Surprise box,"""
    elif x == 1:
        return """Clean the front room,
Do an extra chore for Mom,"""
    elif x == 2:
        return """Unload the Dishwasher,
Load the Dishwasher,"""
    elif x == 3:
        return """Wipe the bathrooms down,
Clear and clean the table,"""

inp = input("Whose chores do you want to know?")

if inp == "Ethan":
    day_mod = (diff + 0) % 4
    chores = chore(day_mod)
    print("""
Today, Ethan needs to:
"""+
chores,"""
Make his bed,
And read for 30 minutes.""")
elif inp == "Ellie" or inp == "Elloise":
    day_mod = (diff + 1) % 4
    chores = chore(day_mod)
    print("""
Today, Ellie needs to:
"""+
chores,"""
Make her bed,
And read for 30 minutes.""")
elif inp == "Abbie" or inp == "Abigail":
    day_mod = (diff + 2) % 4
    chores = chore(day_mod)
    print("""
Today, Abbie needs to:
"""+
chores,"""
Make her bed,
And read for 30 minutes.""")
elif inp == "Gennie" or inp == "Genevieve":
    day_mod = (diff + 3) % 4
    chores = chore(day_mod)
    print("""
Today, Gennie needs to:
"""+
chores,"""
Make her bed,
And read for 30 minutes.""")
