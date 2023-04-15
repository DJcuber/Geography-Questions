import json
import os
import random

def readJson():
  with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "questions.json")) as f:
    file = json.loads(f.read())
  return file

def updateWeights(question):
  pass
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
    askQuestion(question)

if __name__ == "__main__":
  main()