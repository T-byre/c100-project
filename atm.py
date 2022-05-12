class ATM:
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
    
    def cashWithdrawal(self):
        print("cash withdrawal successful")
    
    def balanceInquiry(self):
        print("checking balanace from your bank account")

bankofAmerica = ATM("001","1007")
chase = ATM("345","1337")

bankofAmerica.cashWithdrawal()
bankofAmerica.balanceInquiry()
chase.cashWithdrawal()
chase.balanceInquiry()
print(bankofAmerica.cardnumber)
        