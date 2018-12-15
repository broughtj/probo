from probo.marketdata import MarketData
from probo.payoff import VanillaPayoff, call_payoff, put_payoff
from probo.engine import MonteCarloEngine, lsmPricer
from probo.facade import OptionFacade

## Set up the market data
spot = 1.0
rate = 0.06
volatility = 0.30
dividend = 0.0
thedata = MarketData(rate, spot, volatility, dividend)

## Set up the option
expiry = 3.0
strike = 1.10 
thecall = VanillaPayoff(expiry, strike, call_payoff)
theput = VanillaPayoff(expiry, strike, put_payoff)

## Set up Naive Monte Carlo
nreps = 8
steps = 3
pricer = lsmPricer
mcengine = MonteCarloEngine(nreps, steps, pricer)

## Calculate the price
option2 = OptionFacade(theput, mcengine, thedata)
price2 = option2.price()
print("The put price via Least Squares Monte Carlo is: {0:.3f}".format(price2))



