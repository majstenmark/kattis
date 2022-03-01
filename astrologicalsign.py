astro = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius','Capricorn', 'Aquarius', 'Pisces']
jan = 'Jan'
feb = 'Feb'
mar = 'Mar'
apr = 'Apr'
may = 'May'
jun = 'Jun'
jul = 'Jul'
aug = 'Aug'
sep = 'Sep'
oct = 'Oct'
nov = 'Nov'
dec = 'Dec'

dates = [(21, mar, 20, apr), 
(21, apr, 20, may),
(21, may,21,jun),
(22, jun, 22,jul),
(23, jul, 22, aug), 
(23, aug, 21, sep),
(22, sep, 22, oct),
(23, oct, 22, nov),
(23, nov, 21, dec),
(22, dec, 20, jan),
(21, jan, 19, feb),
(20, feb, 20, mar)]

def getsign(day, mo):

    for i in range(12):
        startday, startmonth, endday, endmonth = dates[i]
        #print(i, dates[i], astro[i])
        if mo == startmonth and day >= startday:
            return astro[i]
        if mo == endmonth and day <= endday:
            return astro[i]
    
            

N = int(input())
for _ in range(N):
    day, mo = input().split()
    day = int(day)
    s = getsign(day, mo)
    print(s)

