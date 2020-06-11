class Singleton:
   __instance = None

   @staticmethod  # execute getInstance before even instantiate an object
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self


s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton() # not allowed
print(s) 