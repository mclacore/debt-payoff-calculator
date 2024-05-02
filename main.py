def main():
  """
  Info needed to calculate payoff:
  - current balance
  - current APR
  - minimum payment
  
  Ideas for output:
  - minimum payment time taken, interest paid
  - minimum payment + 10% time taken, interest paid
  - minimum payment + 20% time taken, interest paid
  """
  current_balance = int(input("Input current credit card balance: "))
  current_interest = int(input("Input current credit card interest rate: "))
  minimum_payment = int(input("Input current credit card minimum payment: "))
  
  
  
  print("Minimum payment payoff time is %s months and interest paid is $%s")
  print("Minimum payment + 10% payoff time is %s months and interest paid is $%s")
  print("Minimum payment + 20% payoff time is %s months and interest paid is $%s")
  
main()