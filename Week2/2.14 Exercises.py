response = input("What is your initial investment?")
r = float(response)
growth = (1+(0.01/2))
square = (2*5)
growth_year = (growth **square)
print ("The total amount is", r * growth_year)

#compute as less variables

response = input("What is your initial investment?")
r = float(response)
actual_growth = ((1+(0.01/2))**(2*5))
print ("The total amount is ", r * actual_growth)

#Ask both investment and number of years

response = input("What is your initial investment?")
r = float(response)
response_two = input("How many years will you invest?")
n = float(response_two)
exponential_growth = ((1+(0.01/2))**(2*n))
print ("The total amount will be ", r * exponential_growth)

