from cgi import test
import unittest
from main import add, subtract, multiply, divide
from bigger_pockets import Bigger_Pockets, House 

class TestMath(unittest.TestCase):


   # number1=float(input("Enter first number: "))
   # number2=float(input("Enter second number: "))
   # def subtraction(a,b): 
   #     sub=a-b
    #    return sub
   # print("cash flow monthly is: ",subtraction(number1,number2))



    def cash_flow_subtract(self):
        cash_flow_test = Bigger_Pockets

        self.assertEquals(subtract(input(2500 - 1700) 800))

    def yearly_takeaway_multiply(self):
        yearly_takeaway_multiply = House

        self.assertEquals(multiply(input(800 * 12) 9600))

    def roi_divide(self):
        roi_divide = House

        self.assertEquals(divide(9600 / 60000)0.16)



if __name__ == '__main__':
    unittest.main()
