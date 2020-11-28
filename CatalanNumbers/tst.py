# (2n)! / (n+1)! n!
val  = 1
for n in range(1, 20):
  val = val * 2 * n * (2 * n - 1) /((n + 1)*n)
  print('{}: {}'.format(n, val))
