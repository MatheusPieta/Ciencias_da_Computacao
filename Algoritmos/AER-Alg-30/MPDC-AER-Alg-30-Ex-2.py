def fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibonacci(n-1) + fibonacci(n-2))  
nterms = int(input("bote um numero: ")) 
  
if nterms <= 0:
   print("Numero invalido")  
else:  
   print("sequencia de fibonacci:")  
   for i in range(nterms):  
       print(fibonacci(i))