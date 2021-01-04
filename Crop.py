

class Crop:
    
    _season_duration = 28
    
    def __init__(self, crop, cost, sell_price, first_growth_rate, second_growth_rate=None):
        self._crop = crop
        self._cost = cost
        self._sell_price = sell_price
        self._first_growth_rate = first_growth_rate
        self._second_growth_rate = second_growth_rate
    
    def get_crop(self):
        return self._crop
    
    def get_cost(self):
        return self._cost
    
    def get_sell_price(self):
        return self._sell_price
    
    def get_first_growth_rate(self):
        return self._first_growth_rate
    
    def get_second_growth_rate(self):
        return self._second_growth_rate
            
    def shop_closed(self, start=1):
        """

        """
        end = Crop._season_duration
        
        return [x for x in range(start,end+1) if x % 7 == 3]
    

class NonRenewCrop(Crop):
        
    def __init__(self, _crop, _cost, _sell_price, _first_growth_rate):
        super().__init__(_crop, _cost, _sell_price, _first_growth_rate)

        self._leftover_days = Crop._season_duration % self._first_growth_rate
        self._harvest_count = int((Crop._season_duration - self._leftover_days) / self._first_growth_rate + 1)
        
    def pay_days(self, start=1):
        """
        returns a list of days that you can harvest crops and sell it back to the shop
        i.e. crop is mature and store is not closed
        """
        end = Crop._season_duration
        
        isharvest = lambda x: x % (self._first_growth_rate + 1) == 0
        isclosed = lambda x: x % 7 == 3
        
        return [x+start-1 if isharvest(x) and not isclosed(x+1) else x+start for x in range(start,end+1) if isharvest(x)]        

    def compound_return(self, account=500):
        for _x in self.pay_days():
            remainder = account % self._cost
            revenue = ((account - (remainder))/self._cost)*self._sell_price
            account = revenue + remainder
            
        return account
    
    def harvest(self):
        #print(self.period)
        #print(self.harvest_count)
        pass


class RenewCrop(Crop):
        
    def __init__(self, _crop, _cost, _sell_price, _first_growth_rate, _second_growth_rate):
        super().__init__(_crop, _cost, _sell_price, _first_growth_rate, _second_growth_rate)

        self.leftover_days = Crop._season_duration % self._first_growth_rate
        self.harvest_count = int((Crop._season_duration - self.leftover_days) / self._first_growth_rate + 1)
        
    def compound_return(self, account=500):
        """

        """
        pass
