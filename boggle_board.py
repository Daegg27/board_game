import random
class BoggleBoard:
  
  def __init__(self):
    self.board = ("""    ________
    ________
    ________
    ________""")
    print(self.board)

  def shake(self):
    # alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    board_string = ""
    available_dice = ["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO", "EHRTVW", "CIMOTU", "DISTTY", "EIOSST", "DELRVY", "ACHOPS", "HIMNQU", "EEINSU","EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"]
    # Loops through each dice, selects a letter randomly, then removes dice after use
    for i in range(0,16):
      random_index = random.randrange(0,len(available_dice))
      board_string += available_dice[random_index][random.randrange(0, 5)]
      available_dice.pop(random_index)
    
    # Converts string to list, checks for Q, and rejoins string
    string_to_list = list(board_string)
    print(string_to_list)
    for char in string_to_list:
      if char == "Q":
        print("totally is working")
        string_to_list[string_to_list.index(char)] = "Qu"
    print(string_to_list)
    board_string = "".join(string_to_list)

    self.board = f"""    {board_string[0:4]}
    {board_string[4:8]}
    {board_string[8:12]}
    {board_string[12:16]}"""
    print(self.board)


game_one = BoggleBoard()
game_one.shake()
