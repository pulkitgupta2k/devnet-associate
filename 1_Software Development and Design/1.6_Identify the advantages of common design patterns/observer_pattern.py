class Observer():
    def update(self, subject):
        print("OBSERVER: Observer state is now: " + str(subject._state))

class subject():

    _state = 0
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    def updateState(self, n):
        self._state = n
        self.notify()



s = subject()
ob1 = Observer()
ob2 = Observer()

s.attach(ob1)
s.attach(ob2)

s.updateState(5)