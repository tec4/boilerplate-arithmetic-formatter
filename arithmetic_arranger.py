import re


def arithmetic_arranger(problems, showAnswers = False):

    if len(problems) > 5: 
      return "Error: Too many problems."

    line1 = []
    line2 = []
    line3 = []
    answers = []
    for problem in problems:
        match = re.match('^(.+) (.) (.+)$', problem)
        if match:
            top = match.group(1)
            operator = match.group(2)
            bottom = match.group(3)
            maxLenTop = len(top) if len(top) > len(bottom) else len(bottom)
            maxLenBottom = 0

            if not re.search('^[0-9]+$', top):
              return "Error: Numbers must only contain digits."

            if not re.search('^[0-9]+$', bottom):
              return "Error: Numbers must only contain digits."

            if operator not in ['+', '-']:
              return "Error: Operator must be '+' or '-'."

            if maxLenTop > 4:
              return "Error: Numbers cannot be more than four digits."

            answer = None
            if showAnswers and operator == '+':
              answer = int(top) + int(bottom)

            if showAnswers and operator == '-':
              answer = int(top) - int(bottom)

            if answer != None:
              answerStr = str(answer)
              maxLenBottom = len(answerStr)
          
            paddedLen = maxLenTop + 2
            line1.append(top.rjust(paddedLen, ' '))
            line2.append(
              # Add padding to the left of the operator if the bottom number is bigger than the top
              # Subtract 1 to take into account the one character operator
              "".rjust(0 if maxLenTop >= maxLenBottom else maxLenBottom - maxLenTop - 1, ' ') 
              + operator 
              + " " 
              + bottom.rjust(maxLenTop if maxLenTop >= maxLenBottom else maxLenBottom - maxLenTop, ' ')
            )
            line3.append("".rjust(paddedLen, "-"))

            if showAnswers:
              answers.append(str(answer).rjust(paddedLen, ' '))

    output = (
      "    ".join(line1) + "\n" + 
      "    ".join(line2) + "\n" +
      "    ".join(line3))

    if showAnswers:
      output = output + "\n" + "    ".join(answers)

    return output
