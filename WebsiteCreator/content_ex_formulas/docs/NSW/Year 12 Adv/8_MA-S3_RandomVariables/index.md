---
weight: 8
title: 'Random Variables'
---


###   Concepts 

 - random variable
 - continuous random variable
 - continuous probability distribution
 - uniform probability distribution
 - probability density function (pdf)
 - cumulative distribution function (cdf)
 - empirical rule
 - normal distribution
 - z-score



###   Notes 

 - The cumulative distribution function is the integral of the probability density function

 - A continuous probability distribution is reported by a probability density function

 - The probability of a single outcome of a continuous probability distribution cannot be calculated, in other words $P(X=x) = 0$.  The probability can only be calculated for a range

 - Given $P(X=a) = 0$ and $P(X=b) = 0$, therefore $P(a < X < b) = P(a \leq X \leq b)$

 - The area under a probability density function is 1 : $ {\Large\int}^\infty_{-\infty} f(x)dx = 1$

 - Given probability density function $f(x)$ over domain [a,b] and cumulative distribution function $F(x)$ $F(a) = 0$ and $F(b) = 1$

 - The median lies at point x where ${\Large\int}^x_a f(x)dx = \dfrac{1}{2}$ where $f(x)$ is a pdf defined on domain [a,b].  Alternatively $F(x)-F(a) = \dfrac{1}{2}$ Similiar rules apply to other quantiles.

 - The mean, mode, and median are equal for a normal distribution
 
 - Finding probability by integration in a normal distribution is complex, therefore use tables where $\mu = 0$ and $\sigma = 1$


###  Spreadsheets  


Click on below to open spreadsheet examples

[RandomVariables](https://github.com/charl-potgieter/AustralianSchoolMaths/raw/main/WebsiteCreator/spreadsheets/RandomVariables.xlsx)
