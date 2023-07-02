import requests, json

url = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
text = url.text

quiz_api_data = json.loads(text)

question_data = quiz_api_data["results"]


# question_data = [
#     {"text": "'A' is the most common letter used in the English language.", "answer": "False"},
#     {"text": "There is only 1 part of the body that can't heal themselves", "answer": "True"},
#     {"text": "Coffee is made from berries", "answer": "True"},
#     {"text": "The five rings on the Olympic flag are interlocking", "answer": "True"},
#     {"text": "You can sneeze during your sleep.", "answer": "False"},
#     {"text": "Before becoming queen, Queen Elizabeth II trained as a mechanic.", "answer": "True"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "The first animal sent into space was a monkey.", "answer": "False"},
#     {"text": "In the English language there is no word that rhymes with orange.", "answer": "True"},
#     {"text": "In a deck of cards, the king has a mustache.", "answer": "False"},
#     {"text": "Linux operating system is denoted by a seal.", "answer": "False"},
#     {"text": "The world’s largest island is Greenland.", "answer": "True"}
# ]
