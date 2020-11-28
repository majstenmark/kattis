msg= raw_input()

best = len(msg)
for L in range(2, len(msg)//2):
    for startindex in range(len(msg)-L):
        macro = msg[startindex:startindex+L]
        repl = msg.replace(macro, 'M')
        best = min(best, len(repl) + len(macro))
print(best)
