# coding: utf-8
wallet = 5000
computer_price = 1200


# Computer price < than 1000
print(computer_price < 1000) #output true or false 
if computer_price < 1000:
  print("The price is less than 1000")
else:
  print("The price is greater than 1000")

  # Condition ternaire, [] = ? and ('', '') = '' :''; 
  text = ("First result", "second result") [computer_price <= 1000]