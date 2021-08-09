class ATM:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    
    def checkbalance(self):
        print("Your balance is 50k")
    
    def withdrawal(self,amount):
        newAmount=50000-amount
        print("Ypu have withdrawn "+str(amount)+". Your remaining balance is "+str(newAmount))

def main():
    cardNumber=input("Enter your card number:")
    pin=input("Enter your PIN number:")
    user1=ATM(cardNumber,pin)
    print("Choose your activity")
    print("1.Balance enquiry 2.Withdrawal ")
    activity=int(input("Enter activity number"))
    if(activity==1):
        user1.checkbalance()
    elif(activity==2):
        amount=int(input("Enter the amount"))
        user1.withdrawal(amount)
    else:
        print("Enter a valid number")

    
main()