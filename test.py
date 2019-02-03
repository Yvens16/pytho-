# coding: utf-8
def hello():
  # Création d'un variable 'username' ayant pour valeur Yvens
  username = "Yvens"
  # Création d'un variable 'age' ayant pour valeur 19
  age = 19
  # Change the value of age 
  age = 25
  age = age + 10 #The age should be 35
  # print("Hello world")
  # print(username, age)
  print("Hello " + username + " you are " + str(age))

if __name__ == '__main__':
  hello()