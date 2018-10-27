# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(tin,num):
    summ = 1000000
    for x in tin:
        en = len(x)
        if en < num or en = num and "X" in x  :
            continue
        for i in x:
            i = 0
            count = 0
            summm = 0
            while  count < num :
                if i == en:
                    summm = summ
                    break
                if x[i] == "X":
                    count = 0
                    summm = 0
                else:
                    count += 1
                    summm += x[i]
                i += 1
            if summm < summ:
                summ = summm
    if summ == 1000000:
        return 0
    return summ
