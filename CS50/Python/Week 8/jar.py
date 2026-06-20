class Jar:
    def __init__(self, capacity=12):

        self.capacity = capacity
        self.cookies = 0
        
    def __str__(self):
        return r"🍪" * self.cookies

    def deposit(self, n):
        self.cookies += n
        if self.cookies > self._capacity:
            raise ValueError("Cookies do not fit the jar")
        
        
    def withdraw(self, n):
        self.cookies -= n
        if self.cookies < 0:
            raise ValueError("You are taking to many cookies")

    @property
    def capacity(self):
        return self.capacity
    
    @capacity.setter
    def capacity(self, capacity):
        try:
            if capacity < 0:
                raise ValueError("Capacity below 0")
            self._capacity = capacity
        except TypeError:
            raise ValueError("Invalid number")

    @property
    def size(self):
        return self.cookies
        
jar = Jar()
jar.deposit(3)
print(jar)
jar.withdraw(3)
jar.deposit(1)
print(jar)
print(jar.size)
jar.withdraw(2)