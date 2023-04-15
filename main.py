import json
import os
import random

def readJson():
  with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "questions.json"), "r") as f:
    file = json.loads(f.read())
  return file

def updateWeights(newQuestion, file):
  breaker = False
  for section in file.values():
    for topic in section.values():
      for question in topic.values():
        if question["q"] == newQuestion["q"]:
          question["weight"] = newQuestion["weight"]
          breaker = True
          break
      if breaker: break
    if breaker: break
  with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "questions.json"), "w") as f:
    f.write(json.dumps(file, indent=2))
  return file

  #update weights of questions

def getQuestion(file):
  totalWeight = 0
  for section in file.values():
    for topic in section.values():
      for question in topic.values():
        totalWeight += question["weight"]

  rand = random.randint(1, totalWeight)
  for section in file.values():
    for topic in section.values():
      for question in topic.values():
        rand -= question["weight"]
        if rand <= 0:
          return question

def askQuestion(question):
  input(f"{question['q']} ")
  marks = int(input("Enter the number of marks you got: "))
  question["weight"] += int((0.75) * question["marks"] - marks)
  return question

def main():
  file = readJson()
  while True:
    question = getQuestion(file)
    question = askQuestion(question)
    file = updateWeights(question, file)

if __name__ == "__main__":
  main()