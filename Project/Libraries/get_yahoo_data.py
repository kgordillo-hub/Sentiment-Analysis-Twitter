import yfinance as yf
import datetime
from datetime import timedelta

class YahooData:
    def __init__(self, givenDate, daysBack=180):
        self.endDate = datetime.datetime.strptime(givenDate,'%Y-%m-%d')
        dateDiff = timedelta(days=-daysBack+1)
        newDate = self.endDate + dateDiff
        self.startDate = newDate
        self.endDate = self.endDate + timedelta(days=1)

    def getYahooData(self, keyword):
        historical_data = yf.download(keyword, start=self.startDate, end=self.endDate, progress=False)
        #historical_data = yahoo.get_historical(self.startDate, self.endDate)
        return historical_data