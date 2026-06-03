READ = 4 #100 in binary
WRITE = 2 #010 in binary
EXECUTE = 1 #001 in binary
permission = 5 #110 in binary

if (permission & WRITE) == WRITE:
    print("WRITE enabled")
else:
    print("WRITE not enabled")