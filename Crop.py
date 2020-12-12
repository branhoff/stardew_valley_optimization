

class Crop:
    
    _season_duration = 28
    
    def __init__(self, crop, cost, sell_price, growth_duration, intial_grow=None):
        self._crop = crop
        self._cost = cost
        self._sell_price = sell_price
        self._growth_duration = growth_duration
        self._intial_grow = intial_grow
    
    def get_crop(self):
        return self._crop
    
    def get_cost(self):
        return self._cost
    
    def get_sell_price(self):
        return self._sell_price
    
    def get_growth_duration(self):
        return self._growth_duration
    
    def get_intial_grow(self):
        return self._intial_grow
            
    def shop_closed(self, start=0):
        end = Crop._season_duration
        
        return [x + 1 for x in range(start-1,end) if (x + 1) % 7 == 3]
    

class NonRenewCrop(Crop):
        
    def __init__(self, _crop, _cost, _sell_price, _growth_duration):
        super().__init__(_crop, _cost, _sell_price, _growth_duration)

        self._leftover_days = Crop._season_duration % self._growth_duration
        self._harvest_count = int((Crop._season_duration - self._leftover_days) / self._growth_duration + 1)
        
    def pay_days(self, start=1):
        end = Crop._season_duration
        
        isharvest = lambda x: x % (self._growth_duration + 1) == 0
        isclosed = lambda x: x % 7 == 3
        
        return [x+start-1 if isharvest(x) and not isclosed(x+1) else x+start for x in range(start,end+1) if isharvest(x)]        

    def compound(self, account=500):
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
        
    def __init__(self, crop, cost, sell_price, growth_duration, intial_grow):
        super().__init__(crop, cost, sell_price, growth_duration, intial_grow)

        self.leftover_days = Crop._season_duration % self._growth_duration
        self.harvest_count = int((Crop._season_duration - self.leftover_days) / self._growth_duration + 1)
        
    def compound(self, account=500):
        #for x in 
        
        pass
