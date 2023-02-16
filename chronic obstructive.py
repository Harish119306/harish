import matplotlib.pyplot as plt
plt.bar([40,50,60,70],[13,18,31,43],width=2, label='men')
plt.bar([45,55,65,75],[4,8,12,17],width=3, label='women',color='g')
plt.legend
plt.xlabel('Age(years)')
plt.ylabel('Prevalence of COPD(%)')
plt.title('COPD diseases')
plt.show()