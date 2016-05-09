from probo.marketdata import MarketData
from probo.payoff import VanillaPayoff, call_payoff
from probo.engine import BinomialPricingEngine, EuropeanBinomialPricer, BlackScholesPricingEngine, BlackScholesPricer
from probo.facade import OptionFacade

## Set up the market data
spot = 41.0
rate = 0.08
volatility = 0.30
dividend = 0.0
the_data = MarketData(rate, spot, volatility, dividend)

## Set up the option
expiry = 1.0
strike = 40.0
the_call = VanillaPayoff(expiry, strike, call_payoff)

## Set up the European Binomial pricer
steps = 3 
pricer = EuropeanBinomialPricer
bi_engine = BinomialPricingEngine(steps, pricer) 

## Calculate the price
option1 = OptionFacade(the_call, bi_engine, the_data)
price1 = option1.price()
print("The call price via Binomial is: {0:.3f}".format(price1))

## Set up the Black-Scholes pricer
#bs_engine = BlackScholesPricingEngine(BlackScholesPayoffType.call, BlackScholesPricer)
bs_engine = BlackScholesPricingEngine("call", BlackScholesPricer)
option2 = OptionFacade(the_call, bs_engine, the_data)
price2 = option2.price()
print("The call price via Black-Scholes is: {0:.3f}".format(price2))


