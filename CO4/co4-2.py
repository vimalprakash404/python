class bank:
    def __init__(self, acNo, acName, acType, acBal):
        self.acNo = acNo
        self.acName = acName
        self.acType = acType
        self.acBal = acBal
    def acDepo(self,dep):
        self.acBal = self.acBal + dep
        print("successfully Deposited ")
        return self.acBal
    def acWithdraw(self,am):
        if am > self.acBal:
            print("insufficient balance")
        else:
            self.acBal = self.acBal - am
            print("Successfully Withdraw",am,"from your account")
            print("current Balance =",self.acBal)
            return self.acBal

k = bank(419852025, "Tom Cruise", "Current", 97562144)
deposit = int(input("enter amount to deposit="))
ba = k.acDepo(deposit)
print("current balance = ", ba)
withdraw = int(input("enter amount to withdraw"))
wi = k.acWithdraw(withdraw)
