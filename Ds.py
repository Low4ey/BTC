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
        plt.plot_date(self.x_cords, self.y_cords, linestyle="solid")

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
        plt.plot_date(self.x_cords,self.y_cords,linestyle="solid",ms=0)
        plt.tight_layout()
    
    def animate(self):
        self.ani = FuncAnimation(plt.gcf(), self.Start, interval=1000)


while True:
    print("Press 1 for Get live data Crypto Currency : \n Press 2 to get VS Graph ")
    ch=input()
    if ch==1:
        crypto_curr=input("Enter Crypto Currency Code : ").upper()
        currency=input("Enter Country Currency : ").upper()
        crypt=crypto(crypto_curr,currency)
        crypt.animate()
        plt.show()
    if ch==2:
        crypto_curr=input("Enter Crypto Currency Code : ").upper()
        crypto_curr_2=input("Enter Second Crypto Currency Code : ").upper()
        currency=input("Enter Country Currency : ").upper()
        crypt=crypto(crypto_curr,currency)