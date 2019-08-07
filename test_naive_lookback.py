from probo.marketdata import MarketData
from probo.payoff import VanillaPayoff, call_payoff, put_payoff
from probo.payoff import ExoticPayoff, lookbackCallPayoff, lookbackPutPayoff
from probo.engine import MonteCarloEngine, NaiveMonteCarloPricer, PathwiseNaiveMonteCarloPricer
from probo.facade import OptionFacade

## Set up the market data
spot = 41.0
rate = 0.08
volatility = 0.30
dividend = 0.0
thedata = MarketData(rate, spot, volatility, dividend)

## Set up the option
expiry = 1.0
strike = 40.0
thecall = ExoticPayoff(expiry, strike, lookbackCallPayoff)
theput = ExoticPayoff(expiry, strike, lookbackPutPayoff)

## Set up Naive Monte Carlo
nreps = 100000
steps = 252
pricer = NaiveMonteCarloPricer
#pricer = PathwiseNaiveMonteCarloPricer
mcengine = MonteCarloEngine(nreps, steps, pricer)

## Calculate the price
option1 = OptionFacade(thecall, mcengine, thedata)
price1 = option1.price()
print("The call price via Naive Monte Carlo is: {0:.3f}".format(price1[0]))

option2 = OptionFacade(theput, mcengine, thedata)
price2 = option2.price()
print("The put price via Naive Monte Carlo is: {0:.3f}".format(price2[0]))



