class collatz:
  num: int
  F_stop: bool
  F_fastCalc: bool
  def __init__(s, num: int, fastCalc: bool = False)->None: 
    s.F_stop = False
    s.num = num
    s.F_fastCalc = fastCalc
  def calc(s)->int:
    if s.num % 4 == 0 and s.F_fastCalc: s.F_stop = True; return -0
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

def debugMain_(fastCalc: bool = False)->int:
  debugNum_: int = int(input("Starting number: "))
  debugC_ = collatz(debugNum_, fastCalc)
  return debugC_.testCalc_()

def main(debugMode: bool, fastCalc: bool = False)->int:
  if debugMode: return debugMain_(fastCalc)
  new: int

  num: int = int(input("Starting number: "))
  c = collatz(num, fastCalc)
  while c.num != 1 and not c.F_stop:
    new = c.calc()
    print(f"out: {num} | {new}")
  return -1

mode: str
fastCalc: str
mainArgs: list
while True:
  mode     = input("Debug mode y/n: ").lower()
  fastCalc = input("fastCalc mode y/n: ").lower()
  mainArgs = [mode == "y", fastCalc == "y"]
  if input( f"main exited with code {main(*mainArgs)}... enter to exit > " ) != ".ag": break
