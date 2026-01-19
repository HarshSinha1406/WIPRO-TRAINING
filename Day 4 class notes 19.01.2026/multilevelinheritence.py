class A:
    def showA(self):
        print("showA")
class B(A):
    def showB(self):
        print("showB")
class C(B):
    def showC(self):
        print("showC")
c=C()
c.showA()
c.showB()
c.showC()