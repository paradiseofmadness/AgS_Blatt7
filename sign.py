def sign(sigma):
  res = 1
  for i in sigma[0]:
    for j in sigma[0]:
      if i<j:
        res *= (sigma[1][sigma[0].index(i)]-sigma[1][sigma[0].index(j)])/(i-j)
  return res

# aus 4.a)
kappa = [[1,2,3,4],[3,4,2,1]]

# aus 4.b)
sigma = [[1,2,3,4,5,6,7],[2,1,5,6,4,3,7]]
tau = [[1,2,3,4,5,6,7],[1,3,4,2,5,7,6]]

print(sign(kappa))
print(sign(sigma))
print(sign(tau))
