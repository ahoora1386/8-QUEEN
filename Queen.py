import random
from colorama import init , Fore
import os
path = os.path.dirname(__file__)
from turtle import done
rand_1=[1,2,3,4,5,6,7,8]
rand_2=[]
r_1=[]
test=[]
test_2=[]


Queen=str(rand_1)
Queen2=rand_2
os.system("pip install colorama")  
os.system("cls") 
class Queens():
    
    
            
            def __init__(self):
                self.make_number_a()

            def make_number_a(self):
                while len(rand_2)!=8:
                    rand=random.randint(1,8)
                    if rand_2.count(rand) > 2:
                        del rand_2[0:]
                        self.make_number_a()
                    elif rand_2.count(rand) == 0:
                        rand_2.append(rand)
                init()
                print(Fore.YELLOW,rand_2)
                self.test_a()
            def test_a(self):
                for i in range(0,8):
                    r_1.append(rand_2[i]+rand_1[i])
                for i in range(2,17):
                    if r_1.count(i) == 2 or r_1.count(i) > 2:
                        del rand_2[0:]
                        del r_1[0:]
                        del test[0:]
                        self.make_number_a()
                    else:
                        test.append(i)
                if len(test)==15:
                    pass

                    
                else:
                    del rand_2[0:]
                    del r_1[0:]
                    del test[0:]
                    self.make_number_a()
                    
                    
    # |0|0|0|0|0|0|0|0|
    # |0|0|0|0|0|0|0|0|              
    # |0|0|0|0|0|0|0|0|              
    # |0|0|0|0|0|0|0|0|
    # |0|0|0|0|0|0|0|0|
    # |0|0|0|0|0|0|0|0|
    # |0|0|0|0|0|0|0|0|
    # |0|0|0|0|0|0|0|0|
    
                    
                
                self.test_b()
                
                
            def test_b(self):
                
                
                for name in range(0,8):
                    num=rand_2[name]-name+1
                    
    
                    if test_2.count(num) == 1 or test_2.count(num) > 1:
                        del rand_2[0:]
                        del r_1[0:]
                        del test[0:]
                        del test_2[0:]
                        self.make_number_a()
                    else:
                        test_2.append(num)

                    
                init()
                print("\n")
                print(Fore.LIGHTBLUE_EX,"********* Done *********")
                print(Fore.LIGHTGREEN_EX,"\n")
                
                print(""" -------------------------""")
                print("",rand_1)
                print("",rand_2) 
                print(""" -------------------------""") 
         
                print("\n")
 
                
                        
                while True:
                    pass  

            
                    
            
                
            
  
                
try:     
      
    Queens()                                
except:
    os.system(f"start {path}\Queen.py")    
                
        
        


            
                
        

        
        
        
        

          
        

            
        