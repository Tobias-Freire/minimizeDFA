from getAutomaton import getAutomaton
from verifyAutomaton import verify

automato = getAutomaton("./automatos/automatoF.txt")
result = verify(automato["transicoes"])
print(result)
