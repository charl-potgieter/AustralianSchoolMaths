---
weight: 8
---

## <span style="color:RGB(0,32,96"> Probability and Discrete Probability Distributions </span> 
<br>

### <span style="color:RGB(139,69,19)"> Concepts  </span>


* event
* complement
* independent events
* mutually exclusive events
* non-mutually exclusive events
* outcome
* equally likely outcomes
* theoretical probability
* conditional probability
* probability scale
* probability tree
* tree diagram
* array $($table$)$
* relative frequency
* population
* sample space
* set
* Venn diagram
* random variable
* discrete random variable
* continuous random variable
* uniform discrete random variables
* non-uniform discrete random variables
* expected value
* probability distribution
* discrete probability distribution
* uniform probability distribution
* mean or expected value
* variance
* standard deviation


### <span style="color:RGB(150,0,0)">  Notes </span>


* Probability trees: Use the product rule along branches to find $P( A \cap B )$   representing A and B
<BR><BR>
* Probability trees: Use the additional rule for different branches to find $P(A \cup B) $ representing A or B.
<BR><BR>
* $A \cup B $ is A union B
<BR><BR>
* $A \cap B $  is A intersection B
<BR><BR>
* The probability formula applies where each outcome is equally likely: $ P(E) = \dfrac{n(E)}{n(S)} $
<BR><BR>
* The sum of all mutually exclusive probabilities is 1
<BR><BR>
* $P(A \cup B) = P(A) + P(B) $ is the addition rule for mutually exclusive events
<BR><BR>
* $P(A \cup B) = P(A) + P(B) - P(A \cap B) $ is the addition rule 
<BR><BR>
* $P(A \cap B)  = P(A)P(B)$ is the product rule for independent events only
<BR><BR>
* Conditional probability is $ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) eq 0 $ while conditional probability for independent events is $ P(A|B) = P(A) $
<BR><BR>
* Capital letter, e.g. X is often used for a random variable
<BR><BR>
* Lower case letter such as x is used for the values of X
<BR><BR>
* Properties of discrete probability distributions:
    * All possible value of X are mutually exclusive
    * The sum of probabilities = 1
    * For each value of x: 0<=P(X=x)<=1
<BR><BR>
* A probability distribution can be drawn as a table with columns for x and P$($x$)$
<BR><BR>
* The expected values E(X) of a probability distribution measures the centre of the distribution  = mean or average
<BR><BR>
* $\overline{x} $ is the mean of a sample
<BR><BR>
* $\mu $ is the mean of the population
<BR><BR>
* $s$ is the sample standard deviation
<BR><BR>
* $\sigma$ is the poplulation standard deviation
<BR><BR>
* As the sample size increases $\overline{x} $ approaches  $\mu $
<BR><BR>
* The complement of A can be written as $\overline A$ or $ \text{A'}$ or $A^c$
<BR><BR>
* The formula sheet defines variance as follows:  $ Var(X) = E(X^2) - \mu^2$.  The following may be an easier format to understand though: $ Var(X) = \sum[x^2p(x)] - \mu^2$
<BR><BR>
* Know how to capture frequencies and calculate statistics on calculator
<BR><BR>



<br>


###  <span style="color:RGB(150,0,0)"> Formulas </span>
<br>
{{< tabs "d2967533-deb5-4dd7-b9db-619d825e8934" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_98b91 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_98b91 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_98b91">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_98b91_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_98b91_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_98b91_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_98b91_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_98b91_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_98b91_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_98b91_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_98b91_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_98b91_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_98b91_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_98b91_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_98b91_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_98b91_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_b9912 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_b9912 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_b9912_row0_col0, #T_b9912_row3_col0, #T_b9912_row5_col0, #T_b9912_row6_col0, #T_b9912_row8_col0, #T_b9912_row10_col0, #T_b9912_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_b9912_row1_col0, #T_b9912_row2_col0, #T_b9912_row4_col0, #T_b9912_row7_col0, #T_b9912_row9_col0, #T_b9912_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_b9912">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_b9912_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_b9912_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_b9912_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_b9912_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_b9912_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_b9912_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_b9912_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_b9912_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_b9912_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_b9912_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_b9912_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_b9912_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_b9912_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_3db9f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_3db9f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_3db9f_row0_col0, #T_3db9f_row2_col0, #T_3db9f_row4_col0, #T_3db9f_row5_col0, #T_3db9f_row6_col0, #T_3db9f_row7_col0, #T_3db9f_row8_col0, #T_3db9f_row9_col0, #T_3db9f_row10_col0, #T_3db9f_row11_col0, #T_3db9f_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_3db9f_row1_col0, #T_3db9f_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_3db9f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_3db9f_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_3db9f_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_3db9f_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_3db9f_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_3db9f_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_3db9f_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_3db9f_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_3db9f_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_3db9f_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_3db9f_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_3db9f_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_3db9f_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_3db9f_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Descriptive Statistics and Bivariate Data Analysis </span> 
<br>

### <span style="color:RGB(139,69,19)"> Concepts  </span>


* categorical data
* numerical data
* nominal data
* ordinal data
* discrete data
* continuous data
* frequency table
* histogram
* frequency polygon
* cumulative frequency histogram
* ogive $($cumulative frequency polygon$)$
* stem-and-leaf plot
* dot plot
* five-number summary
* box plot $($box-and-whisker-plot$)$
* two-way table
* bar chart
* pie chart
* Pareto chart
* mode
* median
* outlier
* quantile
* quartile
* decile
* percentile
* range
* interquartile range
* skewness
* symmetrical distribution
* modality
* unimodal
* bimodal
* multimodal
* bivariate data
* dependent and independent variables
* extrapolation
* interpolation
* least-squares regression line
* line of best fit
* Pearson's correlation coefficient
* scatterplot
* causality


### <span style="color:RGB(150,0,0)">  Notes </span>


* Categorical data can be nominal or ordinal
<BR><BR>
* Numerical data can be discrete or continuous
<BR><BR>
* Displaying numerical data:
    *Frequency table
    * histogram $($centre of column is lined up with value on x-axis.  No gap between columns$)$ 
    * frequency polygon $($line graph displaying frequency, starts and ends on x-axis$)$ 
    * cumulative frequency histogram 
    * ogive $($cumulative frequency polygon$)$ 
    * stem and leaf plot $[$graphical display of tens $($stems$)$ and units $($leaves$)]$
    * dot plot
    * five-number summary
    * box plot $($box-and-whisker-plot$)$
<BR><BR>
* 3 Measures of central tendency:
    * mean
    * mode
    * median
<BR><BR>
* If ranges are provided in a frequency table a class centre will generally need to be added as an additional column in order to calculate statistics such as mean, standard deviation etc.
<BR><BR>
* Grouped data has a modal class rather than a mode
<BR><BR>
* If there are two middle values. In other words an even number of values, the median is the average of these values.
<BR><BR>
* The median on an ogive is the halfway point on the cumulative frequency axis
<BR><BR>
* Recommended, but not universal, method for computing quartiles:
    * Use the median to divide the ordered set into 2 halves.  
    * If there is an odd number in the original set then do not include the median in either half.
    * If there is an even number in the original set then split the set exactly in half
    * Q1 and Q3 are the medians of the lower and upper halves respectively
<BR><BR>
* Quantile is a general term, quartiles divide set into 4 parts, deciles into 10 parts and percentiles into 100 parts
<BR><BR>
* Shapes of data: 
    * negatively skewed = more area to left of the centre = the tail points to low scores
    * positively skewed = more area to the right of the centre = the tail points to high scores
    * symmetrical
<BR><BR>
* Modality of data:
    * unimodal  = 1 peak
    * bimodal  = 2 peaks
    * multimodal = has many peaks
<BR><BR>
* Scatterplots are used to graph bivariate data
<BR><BR>
* Scatterplots can be:
    * linear
    * non-linear
    * have no shape
<BR><BR>
* Don't need to utilise a formula to calculate Pearson's correlation co-efficient $($r$)$ but need to be able to calculate using calculator
<BR><BR>
* Values of  Pearson's correlation co-efficient $($r$)$:
    * $ -1 \le r \le 1$
    * $ 0 \le r \le 1$ &emsp;&ensp;&nbsp;  scatterplot with positive direction
    * $r=1$ &emsp;&emsp;&emsp;&emsp; perfect positive correlation 
    * $ -1 \le r \le 0$ &ensp;&nbsp; scatterplot with negative direction 
    * $r=-1$ &emsp;&emsp;&emsp; perfect negative correlation
    * $r=0$ &emsp;&emsp;&emsp;&emsp; no correlation
<BR><BR>
* Need to be able to calculate least squares regression line on a calculator but don’t need to be able to manually calculate with formula
<BR><BR>



<br>


###  <span style="color:RGB(150,0,0)"> Formulas </span>
<br>
{{< tabs "428e8cf2-0ee7-4785-8193-a3229fe46192" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_8945a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8945a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_8945a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_8945a_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_8945a_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_8945a_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_8945a_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_8945a_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_8945a_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_214da th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_214da td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_214da_row0_col0, #T_214da_row1_col0, #T_214da_row2_col0, #T_214da_row3_col0, #T_214da_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_214da_row4_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_214da">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_214da_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_214da_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_214da_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_214da_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_214da_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_214da_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Random Variables </span> 
<br>

### <span style="color:RGB(139,69,19)"> Concepts  </span>


* random variable
* continuous random variable
* continuous probability distribution
* uniform probability distribution
* probability density function $($pdf$)$
* cumulative distribution function $($cdf$)$
* empirical rule
* normal distribution
* z-score


### <span style="color:RGB(150,0,0)">  Notes </span>


* The cumulative distribution function is the integral of the probability density function
<BR><BR>
* A continuous probability distribution is reported by a probability density function
<BR><BR>
* The probability of a single outcome of a continuous probability distribution cannot be calculated, in other words $P(X=x) = 0$.  The probability can only be calculated for a range
<BR><BR>
* Given $P(X=a) = 0$ and $P(X=b) = 0$, therefore $P(a < X < b) = P(a \leq X \leq b)$
<BR><BR>
* The area under a probability density function is 1 : $ {\Large\int}^\infty_{-\infty} f(x)dx = 1$
<BR><BR>
* Given probability density function $f(x)$ over domain [a,b] and cumulative distribution function $F(x)$ $F(a) = 0$ and $F(b) = 1$
<BR><BR>
* The median lies at point x where ${\Large\int}^x_a f(x)dx = \dfrac{1}{2}$ where $f(x)$ is a pdf defined on domain [a,b].  Alternatively $F(x)-F(a) = \dfrac{1}{2}$ Similiar rules apply to other quantiles.
<BR><BR>
* The mean, mode, and median are equal for a normal distribution
<BR><BR>
* Finding probability by integration in a normal distribution is complex, therefore use tables where $\mu = 0$ and $\sigma = 1$
<BR><BR>



<br>


###  <span style="color:RGB(150,0,0)"> Formulas </span>
<br>
{{< tabs "cb524721-4704-4fd3-8116-22303d435506" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_b373f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_b373f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_b373f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_b373f_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_b373f_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_b373f_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_b373f_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_b373f_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_b373f_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_dca85 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_dca85 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_dca85_row0_col0, #T_dca85_row1_col0, #T_dca85_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_dca85_row2_col0, #T_dca85_row3_col0, #T_dca85_row5_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_dca85">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_dca85_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_dca85_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_dca85_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_dca85_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_dca85_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_dca85_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> The Binomial Distribution </span> 
<br>

### <span style="color:RGB(139,69,19)"> Concepts  </span>


* Bernoulli random variable
* Binomial random variable
* Bernoulli trial
* Bernoulli distribution
* Binomial distribution
* population proportion
* sample proportion
* sampling distribution of proportions
* central limit theorem


### <span style="color:RGB(150,0,0)">  Notes </span>


* Properties of binomial distribution:
    * fixed number of trials
    * there are only 2 outcomes: success or failure
    * each trial is independent
    * Probabilities are the same for each trial
<BR><BR>
* Share of a binomial distribution:
    * p<0.5 : positively skewed
    * p=0.5 : normal / symmetrical
    * p>0.5 : negatively skewed
<BR><BR>
* Be able to represent a Bernoulli distribution as a :
    * piecewise function
    * distribution table
    * bar chart
<BR><BR>



<br>


###  <span style="color:RGB(150,0,0)"> Formulas </span>
<br>
{{< tabs "ddd9df80-e0b2-413e-886b-7945ff51e702" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_c4ce2 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c4ce2 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_c4ce2">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c4ce2_row0_col0" class="data row0 col0" >$ \text{Bernoulli distribution: } E(X) = p $</td>
    </tr>
    <tr>
      <td id="T_c4ce2_row1_col0" class="data row1 col0" >$ \text{Bernoulli distribution: } VAR(X) = p(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_c4ce2_row2_col0" class="data row2 col0" >$\text{Binomial distribution}: P(X=r) = ^nC_rp^r(1-p)^{n-r}$</td>
    </tr>
    <tr>
      <td id="T_c4ce2_row3_col0" class="data row3 col0" >$\text{Binomial distribution}: X\sim Bin(n,p) $
$ \Rightarrow P(X=x) $
$ = \bigl({n \atop x} \bigr)p^x(1-p)^{n-x}, x=0,1,...,n$</td>
    </tr>
    <tr>
      <td id="T_c4ce2_row4_col0" class="data row4 col0" >$ \text{binomial distribution: } E(X) = np $</td>
    </tr>
    <tr>
      <td id="T_c4ce2_row5_col0" class="data row5 col0" >$ \text{binmomial distribution: } VAR(X) = np(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_c4ce2_row6_col0" class="data row6 col0" >$ \hat{p} = \dfrac{x}{n} $</td>
    </tr>
    <tr>
      <td id="T_c4ce2_row7_col0" class="data row7 col0" >$ \text{sample proportions: } E(\hat{p}) = p $</td>
    </tr>
    <tr>
      <td id="T_c4ce2_row8_col0" class="data row8 col0" >$ \text{sample proportions: } \text{VAR} (\hat{p}) = \dfrac{p(1-p)}{n} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_5e1a9 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5e1a9 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_5e1a9_row0_col0, #T_5e1a9_row1_col0, #T_5e1a9_row7_col0, #T_5e1a9_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_5e1a9_row2_col0, #T_5e1a9_row3_col0, #T_5e1a9_row4_col0, #T_5e1a9_row5_col0, #T_5e1a9_row6_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_5e1a9">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_5e1a9_row0_col0" class="data row0 col0" >$ \text{Bernoulli distribution: } E(X) = p $</td>
    </tr>
    <tr>
      <td id="T_5e1a9_row1_col0" class="data row1 col0" >$ \text{Bernoulli distribution: } VAR(X) = p(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_5e1a9_row2_col0" class="data row2 col0" >$\text{Binomial distribution}: P(X=r) = ^nC_rp^r(1-p)^{n-r}$</td>
    </tr>
    <tr>
      <td id="T_5e1a9_row3_col0" class="data row3 col0" >$\text{Binomial distribution}: X\sim Bin(n,p) $
$ \Rightarrow P(X=x) $
$ = \bigl({n \atop x} \bigr)p^x(1-p)^{n-x}, x=0,1,...,n$</td>
    </tr>
    <tr>
      <td id="T_5e1a9_row4_col0" class="data row4 col0" >$ \text{binomial distribution: } E(X) = np $</td>
    </tr>
    <tr>
      <td id="T_5e1a9_row5_col0" class="data row5 col0" >$ \text{binmomial distribution: } VAR(X) = np(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_5e1a9_row6_col0" class="data row6 col0" >$ \hat{p} = \dfrac{x}{n} $</td>
    </tr>
    <tr>
      <td id="T_5e1a9_row7_col0" class="data row7 col0" >$ \text{sample proportions: } E(\hat{p}) = p $</td>
    </tr>
    <tr>
      <td id="T_5e1a9_row8_col0" class="data row8 col0" >$ \text{sample proportions: } \text{VAR} (\hat{p}) = \dfrac{p(1-p)}{n} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}