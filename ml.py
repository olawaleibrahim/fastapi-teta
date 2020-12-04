import spacy

nlp = spacy.load("en_core_web_sm")

spacy.__version__
nlp

doc = nlp("Facebook buys US startup for $23 billion")
doc = nlp("Apple is going to start the next DeepMind")
type(doc)

for ent in doc.ents:
    print(ent.text, ent.label_)


'''
[
  {
    "content": "Apple to buy UK startup for $1 billion",
    "number": 0,
    "comments": ["Impressive", "Nice buy out"]
  },
 {
    "content": "Conoco Philips purchase tech AI tech startup in Nigeria",
    "number": 0,
    "comments": ["Never saw that coming!", "Absolutely well deserved, congratulations!"]
  }
]
'''