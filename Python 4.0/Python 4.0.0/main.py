from Code.code import Code as code

statements = [code.PrintStatement,code.DefineVaraibleStatment,code.RandomIntegerStatment]

print("Python 4.0\n")

def Run(statments): 
  lineNumber = 1
  line = input("line "+str(lineNumber)+":")
  lineNumber += 1
  input_ = input("line "+str(lineNumber)+":")
  RunStatements(line,input_,statements)
  

def RunStatements(line,input_,statements):
  v = statements[1](line,input_)
  statements[0](line,input_,v)
  statements[2](line,input_,v)

while True:
  Run(statements)

