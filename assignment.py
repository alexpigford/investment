# to do - add a feature that calculates the interest for each year

InvestmentAmount = int(input("Enter the Investment Amount: "))
InterestRate = float(input("Enter the Interest Rate: "))
Years = int(input("Enter the number of years: "))
FutureValue = InvestmentAmount*((1+(0.01*InterestRate)) ** Years)
 
if InvestmentAmount >= 1000 and InterestRate < 15 and Years >= 5 and Years <= 10 :
   print("The initial investment was: ",InvestmentAmount)
   print("The future value is: ",(round(FutureValue, 2)))
   print("The interest gained over",Years,"years is",(round(FutureValue - InvestmentAmount, 2)))
else :
   print("Error: Investment must be $1000 or more with an interest rate below 15 for 5-10 years.")

