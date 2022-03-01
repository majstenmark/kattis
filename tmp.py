import matplotlib.pyplot as plt
import random
import math
'''
		double t = dev * Math.sqrt(-2 * Math.log(Math.random()));
		if (Math.random() < 0.5)
			t = -t;
		return t;
'''
x = [i for i in range(-100, 101)]
y = []
dev = 20
for i in range(100):
    r = random.random()
    t = dev * math.sqrt(-2 * math.log(random.random()))
    if r < 0.5:
        y.append(-t)
    else:
        y.append(t)
plt.hist(y, 10)
plt.show()
