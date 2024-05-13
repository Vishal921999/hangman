
# 0th -> inital hangman
# 6th -> final hangman

hanged_man = [
r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",

r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",

r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",

r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",

r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",

r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

totalChances = 6

def fetchHangman(currChances):
    return hanged_man[totalChances - currChances]