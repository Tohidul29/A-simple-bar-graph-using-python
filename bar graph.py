import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [1,2,3,4,5,6,7,8,9,10]
y = [60,20,33,45,39,40,29,35,40,42]

plt.bar(x, y, label = 'student numbers in the class', color = 'red')

plt.title('A simple bar graph')
plt.xlabel('class')
plt.ylabel('students')
plt.legend()

plt.show()