class Smartphone:
    def _init_(self,brand,model,storage_gb):
        self.brand =brand
        self.model =model
        self.storage_gb =storage_gb
        self.is_on =False
        def turn_on(self):
            if not self.is_on:
                self.is_on =True
                print(f"The {self.brand} {self.model}is already on.")
                def make_call(self,number):
                    if self.is_on:
                        print(f"Calling {number} from the {self.brand} {self.model}.")
                    else:
                        print("The phone is off. Please turn it on to make a first call."
                              def _str_(self):
                                return self.get_info():
                                return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage_gb}GB"
                                
#Create two different Smartphone Objects
#Phone1 =Smartphone("Samsung","Galaxy S23",256)
#Phone2 =Smartphone("Apple","iPhone 16",512)
# 
#Use the methods on each object print(phone1.get_info()) 
#phone1.turn_on()
#phone1.make_call("0207923266")
#print("\n" + Phone2.get_info())
#phone2.turn_on()
#phone2.make_call("0248735445")

