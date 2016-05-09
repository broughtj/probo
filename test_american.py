from probo.marketdata import MarketData
from probo.payoff import VanillaPayoff, call_payoff, put_payoff
from probo.engine import BinomialPricingEngine, AmericanBinomialPricer 
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
thecall = VanillaPayoff(expiry, strike, call_payoff)
theput = VanillaPayoff(expiry, strike, put_payoff)

## Set up the European Binomial pricer
steps = 3 
pricer = AmericanBinomialPricer
binomengine = BinomialPricingEngine(steps, pricer) 

## Calculate the price
option1 = OptionFacade(thecall, binomengine, thedata)
price1 = option1.price()
print("The call price via American Binomial is: {0:.3f}".format(price1))
option2 = OptionFacade(theput, binomengine, thedata)
price2 = option2.price()
print("The put price via American Binomial is: {0:.3f}".format(price2))


