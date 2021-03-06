import requests 
import random

def hangman(LowerLimitOfPopulation, UpperLimitOfPopulation):  
  p = requests.get("http://restcountries.eu/rest/v2/all")
  new_list_country = []
  dash_list = []
  country_array = []
  data = p.json()
  first_display = 0
  
  for i in data:                                      # set difficulty by specifying the population
    if len(i["name"]) < 15 and LowerLimitOfPopulation < i["population"] < UpperLimitOfPopulation :                         
      country_array.append(i)                         #appending the selected countries to a list 
  for j in country_array :     # we are filtering out those countires that have space in their name to avoid complications in the game
    if j["name"].find(" ") > 0 :                     
      continue
    new_list_country.append(j)                        #appending the filtered countries to a new list 

  country = random.choice(new_list_country)           #selecting a country from the list
  word = country["name"].lower()
  chance = 5   
  flag = 0
  word_list = list(word)
  
  if flag==0:                                         # initially print dashes to reveal the length of the word to the user
    dash_incrementor = 0
    while dash_incrementor < len(word):
      dash_list.append("_")
      dash_incrementor = dash_incrementor + 1
    flag = flag+1 
    print (" ".join(dash_list),"\n")    
    
  if flag==1:
    while (chance >-2 and chance <6):
      user_try = input("enter a letter")
      if user_try not in word:
        print ("your chance is ",chance)
        if chance == 3:
          print ("region is ", country["region"])
        if chance == 2:
          print ("subregion is ", country["subregion"])
        elif chance == 1:
          print ("Capital is", country["capital"])
        chance = chance - 1                           #if user_try is not in word thrn chance gets decremented
        if chance == -1:
          print("Better luck next time :)")
          print ("The correct answer is", word)
          break
      else:
        start = 0                                     #start variable to check for repetition
        idx = 0  
        idx = word.find(user_try,start)               #finds the location of the letter
        while(idx>-1):
          dash_list[idx] = user_try                   #inserting the correct guess at the correct place
          start = idx +1                              # initializing the start variable
          idx = word.find(user_try,start)             #check for repetition
        print (" ".join(dash_list))                   # printing the current status
        if dash_list == word_list : 
          if chance == -1 :                           #if the user runs out of chance then he loses
            print ("Better luck next time :)")
            print ("The correct answer is", word)
            break
 #if all the guesses are correct and he guessed it with less than 5 mistakes then he wins
          elif "_" not in dash_list :                
            print ("Congrats! you won!! ") 
            break
try:
  print ("Hello user!\nWelcome to hangman!\n ")
  choiceOfDifficulty = int(input("To choose you difficulty PRESS\n1 for easy \n2 for medium \n3 for hard \n"))
  if choiceOfDifficulty == 1:
    LowerLimitOfPopulation = 150000000
    UpperLimitOfPopulation = 1377422166
    hangman(LowerLimitOfPopulation, UpperLimitOfPopulation)
  elif choiceOfDifficulty == 2:
    LowerLimitOfPopulation = 20000000
    UpperLimitOfPopulation = 150000000
    hangman(LowerLimitOfPopulation, UpperLimitOfPopulation)
  elif choiceOfDifficulty == 3:
    LowerLimitOfPopulation = 0
    UpperLimitOfPopulation = 20000000
    hangman(LowerLimitOfPopulation, UpperLimitOfPopulation)
  else:
    print("Invalid response") 
except ValueError:
  print ("Invalid response")
