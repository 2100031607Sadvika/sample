class Base:
    def display(self):
        print('panda')

class Derived(Base):
        def display(self):
            print("oink")
ob=Derived()
ob.display()