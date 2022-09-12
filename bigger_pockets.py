class Bigger_Pockets():
    def __init__(self, income, expenses, cash_in, cash_flow, yearly_takeaway, roi):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.cash_in = cash_in
        self.yearly_takeaway = yearly_takeaway
        self.roi = roi

class House:
    def __init__(self):
        self.rental = []
        
        
        
    def print_rental(self):
        print("=~" * 15)
        print("RENTAL INFORMATION:")
        
        for rental in self.rental:
            print(rental.income, rental.expenses, rental.cash_in, rental.roi)
            print(self.yearly_takeaway)
            print(self.cash_flow)
            print(self.roi)
                  
        print("=~" * 15)
        
    def run(self):
        while True:
            income = input("total income monthly: ")
            expenses = input("total expenses monthly: ")
            cash_in = input("total cash put in property: ")
            
            #self.add_rental(income, expenses, cash_in, roi)
                    
            cont = input("would you like to 'show data', or 'restart'? ")
    
            if cont == 'show data':
                print(self.rental)
                break
            if cont == 'restart':
                income = input("total income monthly: ")
                expenses = input("total expenses monthly: ")
                cash_in = input("total cash put in property: ")
                roi = input("Is it a series?(yes/no): ") #### annual cash flow divided by cash in
            
                self.add_rental(income, expenses, cash_in, roi)

                        
                cont = input("would you like to 'show data', or 'restart'? ")
                if cont == 'show data':
                    print(self.rental)
                    break
            
                if cont == 'n':
                    break
                

                
        self.print_rental()


my_rental = House()
my_rental.run()