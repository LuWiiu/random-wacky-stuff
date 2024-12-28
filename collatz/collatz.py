class collatz:
  num: int
  F_stop: bool
  def __init__(s, num: int)->None: 
    s.F_stop = False
    s.num=num
  def calc(s)->int:
    if s.num % 2 != 0: s.num=s.num*3+1 
    else: s.num /= 2
    return int(s.num)
  def calc(s)->int: # Faster method
    # This line is here so if the number will be even after another devision, we can conclude it will divide forever till 1
    # This means ending early will not effect the result!
    if s.num % 4 == 0: s.F_stop = True; return -0
    elif s.num % 2 != 0: s.num=s.num*3+1 
    else: s.num /= 2
    return int(s.num)
  def testCalc_(s)->int:
    """
    return 0: s.num is not in range
    return 1: test was succsesful
    return 2: test faild
    """
    expectOut: list = [[], [1], [10, 5, 16, 0]]
    currentTest: list
    ouputNums: list = []
    out: int

    if not s.num <= 3: return 0
    currentTest = expectOut[s.num - 1]
    while s.num != 1 and not s.F_stop:
      out = s.calc()
      ouputNums.append(out)
      print(f"debug out: {out}")
    if currentTest == ouputNums: return 1
    else: return 2

def debugMain_()->int:
  debugNum_: int = int(input("Starting number: "))
  debugC_ = collatz(debugNum_)
  return debugC_.testCalc_()

def main(debugMode: bool)->int:
  if debugMode: return debugMain_()
  new: int

  num: int = int(input("Starting number: "))
  c = collatz(num)
  while c.num != 1 and not c.F_stop:
    new = c.calc()
    print(f"out: {num} | {new}")
  return -1

mode: str
while True:
  mode = input("Debug mode y/n: ").lower()
  if input( f"main exited with code {main(mode == "y")}... enter to exit > " ) != ".ag": break
