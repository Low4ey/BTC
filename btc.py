import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import cryptocompare as cc


class crypto:
    def __init__(self, crypto, currency):
        self.x_cords = []
        self.y_cords = []
        self.crypto_curr = crypto
        self.vs_currency = currency
        plt.title(self.crypto_curr)

    def get_crypto_price(self):
        return cc.get_price(self.crypto_curr,self.vs_currency)[self.crypto_curr][self.vs_currency]
   
    def plotting(self):
        plt.plot_date(self.x_cords, self.y_cords, linestyle="solid",ms=0)

    def start(self):
        plt.gcf().canvas.manager.set_window_title(
            f"Live Plotting {self.crypto_curr}")
        plt.tight_layout()
        anim = FuncAnimation(plt.gcf(), self.plotting, interval=1000)
        plt.show()

    def Start(self,i):
        self.x_cords.append(datetime.now())
        self.y_cords.append(self.get_crypto_price())

        plt.cla()
        plt.gcf().canvas.manager.set_window_title(f"Live Plotting {self.crypto_curr}")
        plt.xlabel('Date')
        plt.ylabel(f'{self.crypto_curr} in {self.vs_currency}')
        self.plotting()
        plt.tight_layout()
    
    def animate(self):
        self.ani = FuncAnimation(plt.gcf(), self.Start, interval=1000)

print("Press Y/y if you want watch supported Crypto currencies , Press any key to move to Next step : ")
ch=input()
if ch=="Y" or ch=="y":    
    print(cc.get_coin_list(format=True))
else:
    pass
crypto_curr=input("Enter Crypto Currency Code : ").upper()
currency=input("Enter Country Currency : ").upper()
crypt=crypto(crypto_curr,currency)
crypt.animate()
plt.show()
