'''
CREATE a new repl by "TOWER of HANOI" and then upload the project community in dashboard
'''
print("*** TOWER OF HANOI ***\n")

def TOH(n,source,destination,auxillary):
  if n==1:
    print("Move disk 1 from source",source,"to destination",destination)
    return
  TOH(n-1,source,auxillary,destination)
  print("Move disk 1 from source",source,"to destination",destination)
  TOH(n-1,auxillary,destination,source)

n = 4
TOH(n,"A","B","C")