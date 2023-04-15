import json
import os

def readJson():
  with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "questions.json")) as f:
    questions = json.loads(f.read())
  return questions


def main():
  questions = readJson()
  print(questions)

if __name__ == "__main__":
  main()