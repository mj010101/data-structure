#
# Decoder for the Morse alphabet
#

# The tree nodes

class Morse():
  def __init__(self, symbol=None, dot=None, dash=None):
    self.symbol = symbol
    self.dot = dot
    self.dash = dash

  def decode(self, morse):
    if morse == "":
      # 해석할 기호가 남아있지 않을시, 해당 시점의 노드에 저장된 symbol을 변환함.
      return self.symbol
    elif morse[0] == '.':
      # 만약 morse 문자열의 첫번째 기호가 '.'이면 self.dot을 참조하여 왼쪽 자식으로 향함.
      if self.dot is None:
        # 왼쪽 자식이 없다면 None을 반환.
        return None
      # 정상적으로 존재 한다면, 두번째 부호부터 다시 재귀적으로 반복함.
      return self.dot.decode(morse[1:])
    elif morse[0] == '-':
      # 마찬가지로 morse 문자열의 첫번째 기호가 '-'이면 self.dash를 참조하여 오른쪽 자식으로 향하고, 두번째 부호부터 재귀적으로 반복.
      if self.dash is None:
        return None
      return self.dash.decode(morse[1:])
    
    return
    raise NotImplementedError

# The decoding tree
# 0~9까지의 digit을 추가해야함.
# 1: ".----" 2: "..---" 3: "...--" 4: "....-" 5: "....."
# 6: "-...." 7: "--..." 8: "---.." 9: "----." 0: "-----"

# 다만, 위를 추가하기전에 해당 공간에 들어갈 '빈 노드'를 먼저 생성해줘야 한다.
# if morse_table.dot.dash.dash.dash is None:
#     morse_table.dot.dash.dash.dash = Morse()
# morse_table.dot.dash.dash.dash.dash = Morse('1')

morse_table = Morse(None, 
                    Morse('E', 
                          Morse('I',
                                Morse('S',
                                      Morse('H'),
                                      Morse('V')),
                                Morse('U',
                                      Morse('F'))),
                          Morse('A',
                                Morse('R',
                                      Morse('L')),
                                Morse('W',
                                      Morse('P'),
                                      Morse('J', 
                                            None, 
                                            Morse('1'))))),
                    Morse('T',
                          Morse('N',
                                Morse('D',
                                      Morse('B'),
                                      Morse('X')),
                                Morse('K',
                                      Morse('C'),
                                      Morse('Y'))),
                          Morse('M',
                                Morse('G',
                                      Morse('Z'),
                                      Morse('Q')),
                                Morse('O'))))

# 숫자 1 추가
if morse_table.dot.dash.dash.dash is None:
    morse_table.dot.dash.dash.dash = Morse()
morse_table.dot.dash.dash.dash.dash = Morse('1')

# 숫자 2 추가
if morse_table.dot.dot.dash.dash is None:
    morse_table.dot.dot.dash.dash = Morse()
morse_table.dot.dot.dash.dash.dash = Morse('2')

# 숫자 3 추가
if morse_table.dot.dot.dot.dash is None:
    morse_table.dot.dot.dot.dash = Morse()
morse_table.dot.dot.dot.dash.dash = Morse('3')

# 숫자 4 추가
if morse_table.dot.dot.dot.dot is None:
    morse_table.dot.dot.dot.dot = Morse()
morse_table.dot.dot.dot.dot.dash = Morse('4')

# 숫자 5 추가
if morse_table.dot.dot.dot.dot.dot is None:
    morse_table.dot.dot.dot.dot.dot = Morse('5')

# 숫자 6 추가
if morse_table.dash.dot.dot.dot is None:
    morse_table.dash.dot.dot.dot = Morse()
morse_table.dash.dot.dot.dot.dot = Morse('6')

# 숫자 7 추가
if morse_table.dash.dash.dot.dot is None:
    morse_table.dash.dash.dot.dot = Morse()
morse_table.dash.dash.dot.dot.dot = Morse('7')

# 숫자 8 추가
if morse_table.dash.dash.dash.dot is None:
    morse_table.dash.dash.dash.dot = Morse()
morse_table.dash.dash.dash.dot.dot = Morse('8')

# 숫자 9 추가
if morse_table.dash.dash.dash.dash is None:
    morse_table.dash.dash.dash.dash = Morse()
morse_table.dash.dash.dash.dash.dot = Morse('9')

# 숫자 0 추가
morse_table.dash.dash.dash.dash.dash = Morse('0')
# --------------------------------------------------------------------

def decode_transmission(s):
  rwords = []
  words = s.split("  ")
  for word in words:
    rword = ""
    letters = word.split(" ")
    for letter in letters:
      rword += morse_table.decode(letter)
    rwords.append(rword)
  return " ".join(rwords)

# --------------------------------------------------------------------

if __name__ == "__main__":
  tests = [ ('.-', 'A'), ('-...', 'B'), ('-.-.', 'C'), ('-..', 'D'),
          ('.---', 'J'), ('-.-', 'K'),
          ('.----', '1'),
          ('..---', '2'),
          ('...--', '3'),
          ('....-', '4'),
          ('... --- ...', 'SOS') ]

  for m, s in tests:
    print("Decoding %20s " % m, end="")
    decoded = decode_transmission(m)
    print("--> '%s': %s" % (decoded, "CORRECT" if decoded == s else "WRONG!"))

  examples = [ "-.-. ... ..--- ----- -....  .. ...  ..-. ..- -.",
               "--. --- --- -..  .-.. ..- -.-. -.-  --- -.  - .... .  ..-. .. -. .- .-..",
               "-....  - .. -- . ...  --...  .. ...  ....- ..---"
  ]
  
  print("A few more examples:")
  for m in examples:
    decoded = decode_transmission(m)
    print("%72s --> '%s'" % (m, decoded))

# --------------------------------------------------------------------
