while True:

   print('welcome to python cashier')
   money = int(input('enter cashier current money\n'))


   prices = {"small popcorn" : 3, "medium popcorn" : 5,
             "large popcorn" : 8, "small drink" : 1,
              "medium drink" : 2, "large drink" : 3 }
# TODO == replace dict with db use 
  
   def calc(money, prices):
      try:
         itemchange = pay - itemvalue  
      except Exception as e:
        print(e)
      finally:
        print(f'change: {itemchange}') 

   def show(money, prices): 
     try:
         for key,value in prices.items():
            print (f'{key}: {value}')
     except Exception as e:
         print(e)
     finally:
         return False
   show(money, prices)

   def start(money, prices):
     try:
     
        for key, value in prices.items():
          global item
          item = str(input('enter what you want to buy:\n'))
          if (item in prices.keys()):
            global itemvalue
            itemvalue = prices.get(item)
            print(f'{item}: {itemvalue}')
            global pay
            pay = float(input('how much costumer pay?\n'))
            return calc(money, prices)
          else:
            print('item not found')
     except Exception as e:
           print(e)
     finally:
           moneybalance = money + itemvalue
           print(f'moneybalance: {moneybalance}')
              

   start(money, prices)





