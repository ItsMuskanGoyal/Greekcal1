pip install mibian
import mibian
c = mibian.BS([Currentprice, Strikeprice, interestrate, Daysofexpiration], volatility= 14.18)
c = mibian.BS([17858, 17850, 4.24, 6], callPrice=162)

print("Delta is ", c.callDelta)
print("Theta is ", c.callTheta)
print("Price is ", c.callPrice)
print("Delta2 is ", c.callDelta2)
print("Rho is ", c.callRho)
print("Vega is ", c.vega)
print("Gamma is ", c.gamma)
print("IV Implied Volatiltiry is: ",c.impliedVolatility)

c = mibian.BS([1.7858, 1.7850, 4.24, 6], putPrice=0.126)
print(c.impliedVolatility)

# c = mibian.BS([underlying_asset, strike_price, interstrate4.24, daysof expiration, volatility= x, putPrice=y, callPrice= z])
c = mibian.BS([1.7858, 1.7850, 4.24, 6], putPrice=0.126, volatility= c.impliedVolatility)
print("Theta for this strike is : ",c.putTheta)
print("Price for this strike is : ",c.putPrice)
print("Delta for this strike is : ",c.putDelta)
print("Rho for this strike is : ",c.putRho)
print("Implied Volatility is: ", c.impliedVolatility)
print("Vega for this strike is : ",c.vega)
print("Gamma for this strike is : ",c.gamma)