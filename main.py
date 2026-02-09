# Lab TIFC1-PF-3-3---Lab-Build-a-Better-Calculator

def addmultiplenumbers(nums): # Suma una lista de números
    total = 0
    for num in nums:
      total += num
    return total

def multiplymultiplenumbers(nums): # Multiplica una lista de números
    total = 1
    for num in nums:
      total *= num
    return total

def isiteven(num): # Define retornando un True o False si el número es par
   return num % 2 == 0

def isitaninteger(num): # Define retornando True o False si el número es un entero(int)
   if type(num) == int:
      return True
   else:
      return False

def main():
   print(f"El resultado de la suma es: {addmultiplenumbers([1, 2, 3])}")
   print(f"El resultado de la multiplicacion es: {multiplymultiplenumbers([1, 2, 3])}")
   print(isiteven(2))
   print(isitaninteger(2.5))


if __name__=="__main__":
  main()