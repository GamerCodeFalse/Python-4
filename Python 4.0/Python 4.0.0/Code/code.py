class Code:
  def PrintStatement(line,input_,v):
    if(line == "/print:"):
      print(input_)
    if(line == "/print:v"):
      print(v)

  def DefineVaraibleStatment(line,input_):
    if(line == "/var:"):
      v = input_
      return v
    else:
      return None
  def RandomIntegerStatment(line,input_,v):
    if(line == "/randint:"):
      import random
      print(random.randint(0,int(input_)))
