
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
cg=CoinGeckoAPI()

class crypto:
    def __init__(self,crypto,currency):
        self.x_cords=[]
        self.y_cords=[]
        self.crypto_curr=crypto
        self.vs_currency=currency
        plt.title(self.crypto_curr)
    
    def insertion(self):
        self.x_cords.append(datetime.now())
        self.y_cords.append(cg.get_price(ids=self.crypto_curr,vs_currencies=self.vs_currency)[self.crypto_curr][self.vs_currency])
    
    def plotting(self):
        plt.plot_date(self.x_cords,self.y_cords,linestyle="solid")
    
    def start(self):
        plt.gcf().canvas.manager.set_window_title(f"Live Plotting {self.crypto_curr}")
        plt.tight_layout()
        anim=FuncAnimation(plt.gcf(),self.plotting,interval=1000)
        plt.show()
        

# Btc=crypto("bitcoin","usd")
# Btc.insertion()
# Btc.plotting()
# Btc.start()
# print(Btc.x_cords)
# print(Btc.y_cords)

plt.plot_date(datetime.now(),cg.get_price(ids="bitcoin",vs_currencies="eth")["bitcoin"]["eth"])
plt.show()

    


    


# def plotting(crypto_curr,currency):
#     x_cords.append(datetime.now())
#     y_cords.append(cg.get_price(ids=crypto_curr,vs_currencies=currency)[crypto_curr][currency])

#     plt.title()



# plotting("bitcoin","eth")
# print(x_cords)
# print(y_cords)



# plt.plot(x_cords,y_cords)
# plt.show()