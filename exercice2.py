import sys

def question1(beta,p,e_max):
    M =beta**(e_max+1) - beta**(e_max+1-p)
    M_tild = (M+beta**(e_max+1))//2
    return M,M_tild

def question2():
    M = sys.float_info.max
    return M
#test 
M,M_tild =question1(2,53,1023)
print(M)
print(M_tild)
print(format(M_tild-M,"56.54f"))
print("question 2")
print(M-question2())
print(float(M_tild-1)-M)