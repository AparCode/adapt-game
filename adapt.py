import random
import time

def display_points(s,c):
  print("----------------------")
  print("Stress Level: " + str(s))
  print("Confidence Level: " + str(c))
  print("----------------------")

def label_day(n):
  print("Day " + str(n))
  print("--------------")

time.sleep(1)
print("Welcome to ADAPT!")
time.sleep(1)
print("You're an Asian women who just moved into the United States, considered a country of diversity. So, you never need to worry about it, right?")
time.sleep(1)
startGame = int(input("Let's see how you can survive living in the United States for a month. Press \'1\' to prove it: "))
if startGame == 1:
  s = 0
  c = 50
  display_points(s,c)

  

  #Day 1
  label_day(1)
  time.sleep(1)
  print("You step out of a plance to LA, excited about your new endeavors there.")
  time.sleep(1)
  print("You were greeted by a group of few citizens. But these weren't the usual citizens you see in Asia.")
  time.sleep(1)
  print("One greeted you with \"Hey there, Geisha Girl\".\nAnother citizen said \"Hey, look, it's that fine china they've been talking about\".")
  time.sleep(1)
  print("What do you do?")
  day1Choice = int(input("Press \'1\' to Do Nothing. Press \'2\' to Respond: "))

  if day1Choice == 2:
    print("You tell them that they are a bunch of jerks.")
    time.sleep(1)
    c += int(random.randint(1,3))
    s += int((random.randint(15,25)/100) *(20-s))

  else:
    time.sleep(1)
    c -= int(random.randint(1,10))
    s += int((random.randint(1,5)/100) * (20-s))

  display_points(s,c)

  #Day 2
  label_day(2)
  time.sleep(1)
  print("After settling down at your new apartment, you decided to apply for a job. You have proficiency in data analytics, so you decided to apply to an economic business.")
  time.sleep(1)
  print("When you went to a job interview, the boss asks \"Aren't you better off, I dunno, painting nails or cleaning a home?\"")
  time.sleep(1)
  print("Do you agree with him?")
  day2Choice = int(input("Press \'1\' to Agree or Press \'2\' to Disagree: "))

  if day2Choice == 2:
    print("You glance at him and take out your resume with data analysis expertise on it.")
    time.sleep(1)
    print("The boss approves and you got selected for the job. You've never been so proud to get a job in a competitive country.")
    time.sleep(1)
    c += int(random.randint(1,3))
    s += int((random.randint(15,25)/100) *(20-s))

    display_points(s,c)

    #Day 3
    label_day(3)
    time.sleep(1)
    print("Today's your first day at the job! Your first task as a data analyzer person is to work on soloutions for traffic jams with a team.")
    time.sleep(1)
    print("You are assigned with three other \"veteran\" workers at the office, and despite no experience at the company you have a revolutionary data model strategy that can really help the issue.")
    time.sleep(1)
    print("However, when you speak, your collegues tend to ignore you or speak louder.")
    print("What will you do?")
    day3Choice = int(input("Press \'1\' to remain quiet or Press \'2\' to try to speak up: "))
    if day3Choice == 2:
      print("WIP")
    else:
      print("WIP")

  else:
    time.sleep(1)
    c -= int(random.randint(1,10))
    s += int((random.randint(1,5)/100) * (20-s))

    display_points(s,c)

    #Day 3
    label_day(3)
    time.sleep(1)
    print("After the horrible job interview, you decided to find a job at a nail salon")
    time.sleep(1)
    print("The procedure towards being able to paint nails for a living isn't as bad as that of a economic business, but the salary is quite low: $9 per hour.")
    time.sleep(1)
    print("You then start to question the legality of that number before you.")
    time.sleep(1)
    print("What would you do?")
    day3Choice = int(input("Press \'1\' to accept the salary as it is. Press \'2\' to request the manager that you get paid more."))
    if day3Choice == 2:
      print("You attempt to bargain with the manager for a higher salary.")
      time.sleep(1)
      print("However, the manager said no. You will have to accept the salary as it is.")
      time.sleep(1)
      c += int(random.randint(1,3))
      s += int((random.randint(15,25)/100) *(20-s))
    
    else:
      time.sleep(1)
      c -= int(random.randint(1,10))
      s += int((random.randint(1,5)/100) * (20-s))

    display_points(s,c)

    display_points(s,c)
    print("WIP")


    

  