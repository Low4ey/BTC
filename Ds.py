from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import cryptocompare as cc
cg = CoinGeckoAPI()


class crypto:
    def __init__(self, crypto, currency):
        self.x_cords = []
        self.y_cords = []
        self.crypto_curr = crypto
        self.vs_currency = currency
        plt.title(self.crypto_curr)

    def insertion(self):
        self.x_cords.append(datetime.now())
        self.y_cords.append(cc.get_price(self.crypto_curr,self.vs_currency)[self.crypto_curr][self.vs_currency])
    
    def get_crypto_price(self):
        return cc.get_price(self.crypto_curr,self.vs_currency)[self.crypto_curr][self.vs_currency]
   
    def plotting(self):
        plt.plot_date(self.x_cords, self.y_cords, linestyle="solid")

    def start(self):
        plt.gcf().canvas.manager.set_window_title(
            f"Live Plotting {self.crypto_curr}")
        plt.tight_layout()
        anim = FuncAnimation(plt.gcf(), self.plotting, interval=1000)
        plt.show()

    def Start(self):
        self.x_cords.append(datetime.now())
        self.y_cords.append(self.get_crypto_price())

        plt.cla()
        plt.gcf().canvas.manager.set_window_title(f"Live Plotting {self.crypto_curr}")
        plt.xlabel('Date')
        plt.ylabel('Price($)')
        plt.plot_date(self.x_cords,self.y_cords,linestyle="solid",ms=0)
        plt.tight_layout()

Btc=crypto("BTC","USD")
Btc.Start()
# ani = FuncAnimation(plt.gcf(), Btc.Start, interval=1000)
plt.show()

# Btc.insertion()
# Btc.plotting()
# Btc.start()
# print(Btc.x_cords)
# print(Btc.y_cords)
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import cryptocompare
# from datetime import datetime 

# plt.style.use('seaborn')

# x_vals = []
# y_vals = []

# def get_crypto_price(cryptocurrency,currency):
#     return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]

# def get_crypto_name(cryptocurrency):
#     return cryptocompare.get_coin_list()[cryptocurrency]['FullName']

# def animate(i):
#     x_vals.append(datetime.now())
#     y_vals.append(get_crypto_price('BTC','USD'))

#     plt.cla()
#     plt.title(get_crypto_name('BTC') + ' Price Live Plotting')
#     plt.gcf().canvas.manager.set_window_title('Live Plotting Cryptocurrency')
    
#     plt.xlabel('Date')
#     plt.ylabel('Price($)')
#     plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
#     plt.tight_layout()
    
   
# ani = FuncAnimation(plt.gcf(), animate, interval=1000)

# plt.show()