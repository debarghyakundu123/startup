import rasa
from rasa.nlu.components import (
    NaturalLanguageProcessor,
    IntentMapper,
    EntityExtractor,
)

# Define the intents and entities
intents = ["order", "cancel_order", "track_order"]
entities = ["food_item", "delivery_address"]

# Create a natural language processor
nlp = NaturalLanguageProcessor(
    intents=intents,
    entities=entities,
    language="en",
)

# Create an intent mapper
intent_mapper = IntentMapper(intents)

# Create an entity extractor
entity_extractor = EntityExtractor(entities)

# Define the actions for each intent
actions = {
    "order": lambda: print("Order placed!"),
    "cancel_order": lambda: print("Order cancelled."),
    "track_order": lambda: print("Tracking your order..."),
}

# Define the chatbot's responses
responses = {
    "order": ["Your order has been placed. We will deliver it shortly."],
    "cancel_order": ["Your order has been cancelled."],
    "track_order": ["Tracking your order..."],
}

# Define the conversation flow
conversations = [
    {
        "start": {
            "intent": intent_mapper.map_intent("order"),
            "response": responses["order"],
        },
        "cancel_order": {
            "intent": intent_mapper.map_intent("cancel_order"),
            "response": responses["cancel_order"],
        },
        "track_order": {
            "intent": intent_mapper.map_intent("track_order"),
            "response": responses["track_order"],
        },
    }
]

# Create a chatbot instance
chatbot = rasa.ChatBot(nlp=nlp, actions=actions, conversations=conversations)

# Run the chatbot
chatbot.run()