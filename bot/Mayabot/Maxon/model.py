from chatterbot import ChatBot



maxon = ChatBot(name='Maxon', read_only=False,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
