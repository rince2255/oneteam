basicSalary = int(input("enter your basic salary"))
pf = 0
da = 0
hra = 0
nightAllowance = 500
if basicSalary < 10000:
    pf = 0.03 * basicSalary
    da = 0.04 * basicSalary
    hra = 0.025 * basicSalary
elif basicSalary >= 10001 and basicSalary <= 25000:
    pf = 0.05 * basicSalary
    da = 0.06 * basicSalary
    hra = 0.045 * basicSalary
elif basicSalary > 25000:
    pf = 0.07 * basicSalary
    da = 0.05 * basicSalary
    hra = 0.06 * basicSalary

netSalary = basicSalary + da + hra + pf + nightAllowance
grossSalary = netSalary-pf
print("Net salary : ", netSalary)
print(grossSalary)
