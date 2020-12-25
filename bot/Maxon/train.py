from model import maxon

from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

small_talk = ['hi there!',
                  'hi!',
                  'how do you do?',
                  'how are you?',
                  'i\'m cool.',
                  'fine, you?',
                  'always cool.',
                  'i\'m ok',
                  'glad to hear that.',
                  'i\'m fine',
                  'glad to hear that.',
                  'i feel awesome',
                  'excellent, glad to hear that.',
                  'not so good',
                  'sorry to hear that.',
                  'what\'s your name?',
                  'i\'m pybot. ask me a math question, please.']
love_me = ['love',
                'My only beloved.. HSK! :D',
                'I love you onii sama~~ HSK',
                'HSK is my unrequitted love!']
math_talk_2 = ['sex',
                'I dont mind one night stand but HSK is my only true lob!',
                'Y kno wat? I like you d@ck! Lemme ride on you!',
                'Drive me like a bitch, give me the pleasures']


list_trainer = ListTrainer(maxon)
for item in (small_talk, love_me, math_talk_2):
    list_trainer.train(item)


trainer = ChatterBotCorpusTrainer(maxon)
trainer.train("chatterbot.corpus.english")

