from jproperties import Properties

def readProperties(key):
   import sys 
   sys.path.append(".")
   
   configs = Properties()
   with open("app.properties", 'rb') as config_file:
     configs.load(config_file)
   #print(f'Property Value: {configs.get(key).data}') 
   return configs.get(key).data
