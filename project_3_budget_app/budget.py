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
        percent = (i.ledger[0]['amount'] - i.get_balance())
        #  / i.ledger[0]['amount'])*100
        # percent = round(percent / 10) * 10
        data.append(percent)
        names.append(i.name)
        # print(percent)
    add = sum(data)
    # print(add)
    for i in range(len(data)):
        data[i] = round(((data[i]/add)*100) / 10)*10
        # print(data[i])

    
    print_o = "Percentage spent by category\n"
    for i in range(100,-10,-10):
        print_o = print_o + "{:>3}|".format(i)
        for j in data:
            if j >= i:
                print_o = print_o +  " o "
            else:
                print_o = print_o + "   "
        print_o += ' \n'

    len_dash = 3*len(data)+1
    print_o += "    "
    for i in range(len_dash):
        print_o = print_o +  "-"
    print_o = print_o +  "\n"

    for i in range(len(max(names, key=len))):
        print_o += "     "
        for name in names:
            if i < len(name):
                print_o = print_o +  name[i] + "  "
            else:
                print_o = print_o + "   "
        print_o += "\n"
    print_o = print_o.rstrip("\n")
    return(print_o)



