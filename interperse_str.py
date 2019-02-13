
import sys

def interperse_strings(listA, listB):
  listC=[]
  n = max(len(listA), len(listB))
  #print n
  #j = 0
  for k in range(n):
      #print listA[k], listB[k]
      if k<len(listA):
          listC.append(listA[k])
      #j+=1
      if k<len(listB):
          listC.append(listB[k])
      #j+=1
    
  return listC

def main():
  A=["a","b"]
  B=["1","2"]
  B1=["x", "y", "z"]
  
  C=interperse_strings(A,B)
  print C

  D=interperse_strings(A,B1)
  print D

if __name__ == "__main__":
   main()
