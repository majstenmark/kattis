D = input()
Rc= input()
Tc = input()

for t_age in range(0, 100):
    t_candles = max(0, (t_age - 2) * (t_age + 3)/2)

    r_age = t_age + D
    r_candles = max(0, (r_age - 3) * (r_age + 4)/2)
#    print 't age {}, t candles {}, r age {} r candles {}'.format(t_age, t_candles, r_age, r_candles)
    if t_candles + r_candles == Rc + Tc and r_candles <= Rc:
        rem = Rc- r_candles
        print rem
        exit()
