# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:58:19 2018

@author: RBPandya
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"#1"
"Calculating mean and variance for uniform continuous distribution between 0 and 1"
a=0
b=1
mean1=a+b/2
var1=(b-a)**2/12

"#2"
"Generating 1000 random numbers between 0 and 1"
x2=np.random.random_sample((1000,1))
"Calculating mean and variance for x2"
mean2=sum(x2)/len(x2)
var2=sum([(xi-mean2)**2 for xi in x2])/(len(x2)-1)
"Computing theoritical values of mean and variance for x2"
meant=0.5
vart2=sum([(xi-meant)**2 for xi in x2])/(len(x2)-1)
"Cross-verifying values with in-built function"
m2=np.mean(x2)
v2=np.var(x2,axis=0,ddof=1)
"Repeating the experiment for 80 times for finding variance of sample means"
x22=np.random.random_sample((1000,80))
"Calculating mean and variance for x22"
mean22=np.mean(x22,axis=0)
varm22=np.var(mean22,ddof=1)

"Generating 10000 random numbers between 0 and 1"
x3=np.random.random_sample((10000,1))
"Calculating mean and variance for x3"
mean3=sum(x3)/len(x3)
var3=sum([(xi-mean3)**2 for xi in x3])/(len(x3)-1)
"Computing theoritical values of mean and variance for x3"
meant=0.5
vart3=sum([(xi-meant)**2 for xi in x3])/(len(x3)-1)
"Cross-verifying values with in-built function"
m3=np.mean(x3)
v3=np.var(x3,axis=0,ddof=1)
"Repeating the experiment for 800 times for finding variance of sample means"
x32=np.random.random_sample((1000,80))
"Calculating mean and variance for x32"
mean32=np.mean(x32,axis=0)
varm32=np.var(mean32,ddof=1)


"#3"
"Central Limit Theorem"
"Generating 1000 random numbers and repeating the process for 50 times"
x4=np.random.random_sample((1000,50))
"Computing mean and variance for x4"
m4=np.mean(x4,axis=0)
v4=np.var(x4,axis=0,ddof=1)
"Ploting Distribution Curves"
f1 = plt.figure()
sns.distplot(m4)
plt.xlabel('Value of sample means')
plt.ylabel('Number of samples')
f2=plt.figure()
sns.distplot(v4)
plt.xlabel('Value of sample variances')
plt.ylabel('Number of samples')
"Generating 10000 random numbers and repeating the process for 50 times"
x5=np.random.random_sample((10000,50))
"Computing mean and variance for x5"
m5=np.mean(x4,axis=0)
v5=np.var(x4,axis=0,ddof=1)
"Ploting Distribution Curves"
f3=plt.figure()
sns.distplot(m5)
plt.xlabel('Value of sample means')
plt.ylabel('Number of samples')
f4=plt.figure()
sns.distplot(v5)
plt.xlabel('Value of sample variances')
plt.ylabel('Number of samples')

"#4"
"Generating 10000 random numbers between 0 and 1 for sequences"
x6=np.random.random_sample((1000,1))
A=sum([x6[i]*x6[i+1] for i in range(0,999)])/(len(x6)-1)
B=sum([(x6[i]) for i in range(0,999)])/(len(x6)-1)-sum([x6[i] for i in range (1,1000)])/(len(x6)-1)
"Computing co-variance for two sequences"
Z=A-B
"test case of two similar sequences for verification"
x7=np.random.random_integers(1,size=(1000,1))
A2=sum([x7[i]*x7[i+1] for i in range(0,999)])/(len(x7)-1)
B2=sum([(x7[i]) for i in range(0,999)])/(len(x7)-1)-sum([x7[i] for i in range (1,1000)])/(len(x7)-1)
Z2=A2-B2

"#5"
"Generating 10000 random numbers between 0 and 1"
x8=np.random.random_sample((1000,1))
"Computing mean and variance for x8"
m8=np.mean(x8)
v8=np.var(x8,ddof=1)
bins_dis=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
counts, edges = np.histogram(x8, bins=bins_dis)
print(counts)
"Computing the values of Z2 to find the probability and degree of freedom"
Zsq=sum([((ci -100)**2)/100 for ci in counts])







