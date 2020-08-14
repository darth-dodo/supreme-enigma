import yfinance as yf
from pprint import pprint

symbols = ["MSFT", "GOOG", "AAPL", "FB", "PG"]

for sym in symbols:
    print("====================")
    print(sym)
    data = yf.Ticker(sym)
    pprint(data.info)
    print("====================")


"""
sample data

GOOG
{'52WeekChange': 0.28944457,
 'SandP52WeekChange': 0.1678102,
 'address1': '1600 Amphitheatre Parkway',
 'algorithm': None,
 'annualHoldingsTurnover': None,
 'annualReportExpenseRatio': None,
 'ask': 1527.32,
 'askSize': 900,
 'averageDailyVolume10Day': 1636387,
 'averageVolume': 1680273,
 'averageVolume10days': 1636387,
 'beta': 1.036263,
 'beta3Year': None,
 'bid': 1509.12,
 'bidSize': 1200,
 'bookValue': 304.342,
 'category': None,
 'circulatingSupply': None,
 'city': 'Mountain View',
 'companyOfficers': [],
 'country': 'United States',
 'currency': 'USD',
 'dateShortInterest': 1596153600,
 'dayHigh': 1537.25,
 'dayLow': 1508.005,
 'dividendRate': None,
 'dividendYield': None,
 'earningsQuarterlyGrowth': -0.3,
 'enterpriseToEbitda': 20.155,
 'enterpriseToRevenue': 5.588,
 'enterpriseValue': 927857442816,
 'exDividendDate': None,
 'exchange': 'NMS',
 'exchangeTimezoneName': 'America/New_York',
 'exchangeTimezoneShortName': 'EDT',
 'expireDate': None,
 'fiftyDayAverage': 1494.7865,
 'fiftyTwoWeekHigh': 1586.99,
 'fiftyTwoWeekLow': 1013.536,
 'fiveYearAverageReturn': None,
 'fiveYearAvgDividendYield': None,
 'floatShares': 610861762,
 'forwardEps': 56.35,
 'forwardPE': 26.946762,
 'fromCurrency': None,
 'fullTimeEmployees': 127498,
 'fundFamily': None,
 'fundInceptionDate': None,
 'gmtOffSetMilliseconds': '-14400000',
 'heldPercentInsiders': 0.05746,
 'heldPercentInstitutions': 0.7062,
 'industry': 'Internet Content & Information',
 'isEsgPopulated': False,
 'lastCapGain': None,
 'lastDividendValue': None,
 'lastFiscalYearEnd': 1577750400,
 'lastMarket': None,
 'lastSplitDate': 1430092800,
 'lastSplitFactor': '10000000:10000000',
 'legalType': None,
 'logo_url': 'https://logo.clearbit.com/abc.xyz',
 'longBusinessSummary': 'Alphabet Inc. provides online advertising services in '
                        'the United States, Europe, the Middle East, Africa, '
                        'the Asia-Pacific, Canada, and Latin America. It '
                        'offers performance and brand advertising services. '
                        'The company operates through Google and Other Bets '
                        'segments. The Google segment offers products, such as '
                        'Ads, Android, Chrome, Google Cloud, Google Maps, '
                        'Google Play, Hardware, Search, and YouTube, as well '
                        'as technical infrastructure. It also offers digital '
                        'content, cloud services, hardware devices, and other '
                        'miscellaneous products and services. The Other Bets '
                        'segment includes businesses, including Access, '
                        'Calico, CapitalG, GV, Verily, Waymo, and X, as well '
                        'as Internet and television services. Alphabet Inc. '
                        'was founded in 1998 and is headquartered in Mountain '
                        'View, California.',
 'longName': 'Alphabet Inc.',
 'market': 'us_market',
 'marketCap': 1032170962944,
 'maxAge': 1,
 'maxSupply': None,
 'messageBoardId': 'finmb_29096',
 'morningStarOverallRating': None,
 'morningStarRiskRating': None,
 'mostRecentQuarter': 1593475200,
 'navPrice': None,
 'netIncomeToCommon': 31534000128,
 'nextFiscalYearEnd': 1640908800,
 'open': 1510.34,
 'openInterest': None,
 'payoutRatio': 0,
 'pegRatio': 5.65,
 'phone': '650-253-0000',
 'previousClose': 1506.62,
 'priceHint': 2,
 'priceToBook': 4.989288,
 'priceToSalesTrailing12Months': 6.216774,
 'profitMargins': 0.18993,
 'quoteType': 'EQUITY',
 'regularMarketDayHigh': 1537.25,
 'regularMarketDayLow': 1508.005,
 'regularMarketOpen': 1510.34,
 'regularMarketPreviousClose': 1506.62,
 'regularMarketPrice': 1510.34,
 'regularMarketVolume': 1401861,
 'revenueQuarterlyGrowth': None,
 'sector': 'Communication Services',
 'sharesOutstanding': 333631008,
 'sharesPercentSharesOut': 0.0036000002,
 'sharesShort': 2437191,
 'sharesShortPreviousMonthDate': 1593475200,
 'sharesShortPriorMonth': 2384162,
 'shortName': 'Alphabet Inc.',
 'shortPercentOfFloat': None,
 'shortRatio': 1.53,
 'startDate': None,
 'strikePrice': None,
 'symbol': 'GOOG',
 'threeYearAverageReturn': None,
 'toCurrency': None,
 'totalAssets': None,
 'tradeable': False,
 'trailingAnnualDividendRate': None,
 'trailingAnnualDividendYield': None,
 'trailingEps': 45.492,
 'trailingPE': 33.378395,
 'twoHundredDayAverage': 1378.0566,
 'volume': 1401861,
 'volume24Hr': None,
 'volumeAllCurrencies': None,
 'website': 'http://www.abc.xyz',
 'yield': None,
 'ytdReturn': None,
 'zip': '94043'}

 """
