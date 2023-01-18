<<<<<<< HEAD
import itertools

# itertools is an built-in module that is available for performing certain heavy operations on iterators with the help of its functions that are generally time consuming and it is also resource intensive to do it manually.   

"Infinite iterators: "
"count()"
# it takes two arguments the first one is the starting int and the second one is the optional argument that is steps
n=10
i=n
infinite_count= list(itertools.count(n))
while i >= 0: 
    print(infinite_count)
=======
import itertools

# itertools is an built-in module that is available for performing certain heavy operations on iterators with the help of its functions that are generally time consuming and it is also resource intensive to do it manually.   

"Infinite iterators: "
"count()"
# it takes two arguments the first one is the starting int and the second one is the optional argument that is steps
n=10
i=n
infinite_count= list(itertools.count(n))
while i >= 0: 
    print(infinite_count)
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
    i-=1