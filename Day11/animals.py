class Animal:
    noise = "Rrrrrrr"
    color = "Red"
    def make_noise(self):
        print(f"{self.noise}")
    
    #Funguje ale toto sa v tiredach nerobí, stráca sa význam triedy
    def rando():
        print("This")
    
    
    def set_noise (self, new_noise):
        self.noise = new_noise
        return self.noise
    def get_noise(self):
        return self.noise

    
    def set_color (self, new_color):
        self.color = new_color
        return self.color
    def get_color(self):
        return self.color



class Wolf(Animal):
    noise = "Grrrrr"


class BabyWolf(Wolf):
    color = "Yellow"