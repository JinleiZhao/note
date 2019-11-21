
#a=list(range(10))
#print(a)


#for n in range(10):
#	print (n)
#print("done")


#for n in range(10):
	#print ("the square of",n,"is",n*n)
	#pass
#print("done")

#function that takes 2 numbers as input
#and outputs their average 
#def avg(x,y):
#	print("first input is",x)
#	print("second input is",y)
#	a=(x+y)/2.0
#	print("average is",a)
#	return a

#avg(200,301)

import numpy
#a=numpy.zeros([3,2])
#print(a)


import pandas as pd
import numpy as np

from graphviz import Digraph
# data=pd.read_data("iris.data")
# print(data)

dot = Digraph(comment='The Round Table')
# digraph G{
# { a b c} -> { d e f }
# }

digraph abc {

	a -> b;
	b -> d;
	c -> d;

}