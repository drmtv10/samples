
def left_aligned_text(input_str):
  asterisks = ''
  i=0
  for i in range(len(input_str)):
    if input_str[i] is not ' ':
      asterisks += '*'
    else:
      print asterisks
      asterisks = ''
  print asterisks #last word of the sentance captured here.
     
def right_aligned_text(input_str):
  wlist = input_str.split()
  right_just_width = 0
  for w in wlist:
    rjw = len(w)
    if right_just_width < rjw: 
      right_just_width = rjw
      
  for w in wlist:
    print ("*"*len(w)).rjust(right_just_width)

def main():
    inputSrt = "This is a sample text"
    print "1. Left Aligned Output"
    left_aligned_text(inputSrt)
    print "2. Right Aligned Output"
    right_aligned_text(inputSrt)

if __name__ == "__main__":
   main()
