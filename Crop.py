

class Crop:
    
    season_duration = 28
    
    def __init__(self, crop, cost, sell_price, growth_duration, intial_grow=None):
        self.crop = crop
        self.cost = cost
        self.sell_price = sell_price
        self.growth_duration = growth_duration
        self.intial_grow = intial_grow
    
    def get_crop(self):
        return self.crop
    
    def get_cost(self):
        return self.cost
    
    def get_sell_price(self):
        return self.sell_price
    
    def get_growth_duration(self):
        return self.growth_duration
    
    def get_intial_grow(self):
        return self.intial_grow
            
    def shop_closed(self, start=0):
        end = Crop.season_duration
        
        return [x + 1 for x in range(start-1,end) if (x + 1) % 7 == 3]
    

class NonRenewCrop(Crop):
        
    def __init__(self, crop, cost, sell_price, growth_duration):
        super().__init__(crop, cost, sell_price, growth_duration)

        self.leftover_days = Crop.season_duration % self.growth_duration
        self.harvest_count = int((Crop.season_duration - self.leftover_days) / self.growth_duration + 1)
        
    def pay_days(self, start=1):
        end = Crop.season_duration
        
        isharvest = lambda x: x % (self.growth_duration + 1) == 0
        isclosed = lambda x: x % 7 == 3
        
        return [x+start-1 if isharvest(x) and not isclosed(x+1) else x+start for x in range(start,end+1) if isharvest(x)]        

    def compound(self, account=500):
        for _x in self.pay_days():
            remainder = account % self.cost
            revenue = ((account - (remainder))/self.cost)*self.sell_price
            account = revenue + remainder
            
        return account
    
    def harvest(self):
        #print(self.period)
        #print(self.harvest_count)
        pass

class RenewCrop(Crop):
        
    def __init__(self, crop, cost, sell_price, growth_duration, intial_grow):
        super().__init__(crop, cost, sell_price, growth_duration, intial_grow)

        self.leftover_days = Crop.season_duration % self.growth_duration
        self.harvest_count = int((Crop.season_duration - self.leftover_days) / self.growth_duration + 1)
        
    def compound(self, account=500):
        #for x in 
        
        pass
