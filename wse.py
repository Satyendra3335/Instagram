import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
  print("exists")
else:
  print("The file does not exist")
  f=open("demofile.txt" , "x")
  f.write("Hello")
