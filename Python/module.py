#what is module: a package of set of files such that it can be used again 
# Import datetime from datetime below:
from datetime import datetime

current_time = datetime.now()
print(current_time)

##random module
# Import random below:
import random

# Create random_list below:
random_list = [random.randint(0, num) for num in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

##namespaces
import codecademylib3_seaborn

# Add your code below:
from matplotlib import pyplot as plt
import random

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
print(numbers_b)

plt.plot(numbers_a, numbers_b)
plt.show()

##Decimals
# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
num1 = Decimal('0.2')
num2 = Decimal('0.69')
two_decimal_points = num1 + num2
print(two_decimal_points)

num3 = Decimal('0.53')
num4 = Decimal('0.65')
four_decimal_points = num3 * num4
print(four_decimal_points)

"""#Modules Python Review
You’ve learned:

what modules are and how they can be useful
how to use a few of the most commonly used Python libraries
what namespaces are and how to avoid polluting your local namespace
how scope works for files in Python
Programmers can do great things if they are not forced to constantly reinvent tools that have already been built. With the power of modules, we can import any code that someone else has shared publicly.

In this lesson, we covered some of the Python Standard Library, but you can explore all the modules that come packaged with every installation of Python at the Python Standard Library documentation.

This is just the beginning. Using a package manager (like conda or pip3), you can install any modules available on the Python Package Index.

The sky’s the limit!"""

