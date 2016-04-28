import probo

## Set up the market data
spot = 41.0
rate = 0.08
volatility = 0.30
dividend = 0.0
the_data = probo.marketdata.MarketData(rate, spot, volatility, dividend)

## Set up the option
expiry = 1.0
strike = 40.0
the_call = probo.payoff.VanillaPayoff(expiry, strike, probo.payoff.call_payoff)

## Set up the European Binomial pricer
steps = 200
pricer = probo.engine.EuropeanBinomialPricer
the_engine = probo.engine.BinomialPricingEngine(steps, pricer) 

## Calculate the price
the_option = probo.facade.OptionFacade(the_call, the_engine, the_data)
price = the_option.price()
print("The call price is: {0:.3f}".format(price))
