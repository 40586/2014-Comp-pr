# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

import random
from datetime import *

NO_OF_RECENT_SCORES = 3

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = '' #task 5

Deck = [None]
RecentScores = [None]
Choice = ''

def GetRank(RankNo,Ace):
  Rank = ''
  if RankNo == Ace[0]:
    Rank = 'Ace'
  elif RankNo == Ace[1]:
    Rank = 'Two'
  elif RankNo == Ace[2]:
    Rank = 'Three'
  elif RankNo == Ace[3]:
    Rank = 'Four'
  elif RankNo == Ace[4]:
    Rank = 'Five'
  elif RankNo == Ace[5]:
    Rank = 'Six'
  elif RankNo == Ace[6]:
    Rank = 'Seven'
  elif RankNo == Ace[7]:
    Rank = 'Eight'
  elif RankNo == Ace[8]:
    Rank = 'Nine'
  elif RankNo == Ace[9]:
    Rank = 'Ten'
  elif RankNo == Ace[10]:
    Rank = 'Jack'
  elif RankNo == Ace[11]:
    Rank = 'Queen'
  elif RankNo == Ace[12]:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  Choice = Choice[:1].lower()
  print()
  return Choice

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard,Ace):
  print()
  print('Card is the', GetRank(ThisCard.Rank,Ace), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  print()
  cont = True
  while cont == True:
    PlayerName = input('Please enter your name: ')
    if PlayerName != "":
      cont = False
  print()
  return PlayerName

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  Choice = Choice[:1].lower()
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    REcentScores[Count].Date = ''

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print(" {0:<9} {1:<6} {2:<9}".format("Names","Scores","Dates"))
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print(" {0:<9} {1:<6} {2:<9}".format(RecentScores[Count].Name,RecentScores[Count].Score,RecentScores[Count].Date)) #Task 5
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score, date):
  check = input("Do you want to ad your score to the high score table?(Y-N): ")
  if check[:1].lower() == "y":
    PlayerName = GetPlayerName()
    FoundSpace = False
    Count = 1
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
      if RecentScores[Count].Name == '':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
        RecentScores[Count].Date = RecentScores[Count + 1].date# task 5
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    RecentScores[Count].Date = date
    BubbleSortScores(RecentScores)

def PlayGame(Deck, RecentScores,Ace):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard,Ace)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard,Ace)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    date_ = datetime.now()#task 5
    date = datetime.strftime(date_,'%d/%m/%Y')
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2,date)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

def DisplayOptions():
  print()
  print('1. Ace Value')
  print()
  OptionsChoice = GetOptionsChoice()
  Ace = SetOptions(OptionsChoice)
  return Ace

def GetOptionsChoice():
  cont = False
  while cont == False:
    OptionsChoice = input('Please select from the menu: ')
    print()
    if OptionsChoice == '1':
      cont = True
    else:
      print('Please enter a valid value: ')
  return OptionsChoice

def SetOptions(OptionsChoice):
  if OptionsChoice == '1':
    Ace = SetAceHighOrLow()
  return Ace

def SetAceHighOrLow():
  cont = False
  Ace = []
  while cont == False:
    temp = input('Would you like to set Ace to (H)igh or (L)ow?: ')
    if temp[:1].lower() == 'h':
      Ace = [13,1,2,3,4,5,6,7,8,9,10,11,12]
      cont = True
    elif temp[:1].lower() == 'l':
      Ace = [1,2,3,4,5,6,7,8,9,10,11,12,13]
      cont = True
    else:
      print('Please enter a valid value')
  return Ace

def BubbleSortScores(RecentScores):
  swaps = True
  while swaps == True:
    swaps = False
    for index in range(1,len(RecentScores)-1):
      if RecentScores[index].Score<RecentScores[index+1].Score:
        swaps = True
        temp = RecentScores[index]
        RecentScores[index] = RecentScores[index+1]
        RecentScores[index+1] = temp


if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  Ace = [1,2,3,4,5,6,7,8,9,10,11,12,13]
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores,Ace)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores,Ace)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      Ace = DisplayOptions()
