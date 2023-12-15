def sign(sigma):
  res = 0
  for i in sigma[1]:
    for j in sigma[1]:
      if i>j:
        res += (sigma[2][sigma[1].indexof(i)]-sigma[2][sigma[1].indexof(j)])/(i-j)

# aus 4.a)
kappa = [[1,2,3,4],[3,4,2,1]]

# aus 4.b)
sigma = [[1,2,3,4,5,6,7],[2,1,5,6,4,3,7]]
tau = [[1,2,3,4,5,6,7],[1,3,4,2,5,7,6]]
