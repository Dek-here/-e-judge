def nToKBit(n, K=64):
   output = [0]*K

   def loop(n, i):
       if n == 0: 
           return output
       output[-i] = n & 1
       return loop(n >> 1, i+1)

   return loop(n, 1)
nToKBit(int(input()))