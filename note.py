# coding: utf-8
def main(): 
  note1 = int(input("Entrez la première note"))
  note2 = int(input("Entrez la seconde note"))
  note3 = int(input("Entrez la troisième note"))
  result = (note1 + note2 + note3) / 3
  print("Your average score is " + str(result))
  
if __name__ == '__main__':
  main()