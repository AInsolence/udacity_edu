correct = [[1,2,8],
           [2,3,1],
           [7,1,5]]

def check(data):
  new = []
  for e in data:
    new.append([])
  for i in range (0, len(data)):
    for j in range (0, len(data)):
      new[i].append(data[j][i])
  return new
 
print check(correct)