class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def BalanceEnquiry(self):
        print("the card number", self.cardNumber, "the pin number", self.pinNumber, "has avaliable balance of 32000")

    def CashWithdrawl(self):
        print("you have successfully withdrawl 5000 rupees")

card1 = Atm (4219/1206/9808/2638,1206)
card2 = Atm (6500/3455/1234/5678,1234)
card1.BalanceEnquiry()
card2.CashWithdrawl()