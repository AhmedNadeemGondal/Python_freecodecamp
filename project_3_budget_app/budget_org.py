class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = [] 

    def deposit(self,amount,description=''):
        self.ledger.append({'amount': amount, 'description': description})
        # print(self.ledger[0]['amount'],type(self.ledger[0]))

    def withdraw(self,amount,description=''):
        if self.check_funds(amount):   
            self.ledger.append({'amount': -amount, 'description': description})
            return(True)
        else:
            return(False)   

    def get_balance(self):
        if len(self.ledger) == 0:
            int = 0
            return(int)
        else:    
            balance = self.ledger[0]['amount']
            for i in range(1, len(self.ledger)):
                    balance += self.ledger[i]['amount']
            return (balance)

    def transfer(self,amount,cat):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': "Transfer to " + cat.name})
            cat.deposit(amount,'Transfer from '+ self.name)
            return(True)
        else:
            return(False)

    def check_funds(self,amount):
        return amount <= self.get_balance()

    def __str__(self):
        a = ''
        a = a + "{:*^30s}\n".format(self.name)
        for i in range( len(self.ledger)): 
            a = a + "{0:<23}".format(self.ledger[i]['description'][:23])
            a = a + "{0:>7.2f}\n".format(self.ledger[i]['amount'])
        a = a + "Total: {0:.2f}".format(self.get_balance())
        return(a)


def create_spend_chart(categories):
    data = []
    names =[]
    for i in categories:
        percent = ((i.ledger[0]['amount'] - i.get_balance()) / i.ledger[0]['amount'])*100
        percent1 = round(percent / 10) * 10
        data.append(percent1)
        names.append(i.name)
        # print(percent)
    

    for i in range(100,-10,-10):
        print("{:>3}|".format(i), end="")
        for j in data:
            if j >= i:
                print(' o ', end="")
            else:
                print('   ', end="")
        print()
    len_dash = 3*len(data)+1
    print('    ', end='')
    for i in range(len_dash):
        print('-',end='')
    print()

    for i in range(len(max(names, key=len))):
        print('     ', end='')
        for name in names:
            if i < len(name):
                print(name[i], end="  ")
            else:
                print("   ", end="")
        print()    



