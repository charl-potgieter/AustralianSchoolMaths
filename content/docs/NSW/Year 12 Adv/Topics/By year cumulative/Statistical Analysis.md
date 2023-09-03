---
weight: 6
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
* $A \cup B = P(A) + P(B) $ is the addition rule for mutually exclusive events
<BR><BR>
* $A \cup B = P(A) + P(B) - P(A \cap B) $ is the addition rule 
<BR><BR>
* $A \cap B  = P(A)P(B)$ is the product rule for independent events only
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
{{< tabs "880585b9-71c7-47ce-ae99-2cfc13963dbd" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_bce48 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_bce48 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_bce48">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_bce48_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_bce48_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_bce48_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_bce48_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_bce48_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_bce48_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_bce48_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_bce48_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_bce48_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_bce48_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_bce48_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_bce48_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_bce48_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_26f67 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_26f67 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_26f67_row0_col0, #T_26f67_row3_col0, #T_26f67_row5_col0, #T_26f67_row6_col0, #T_26f67_row8_col0, #T_26f67_row10_col0, #T_26f67_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_26f67_row1_col0, #T_26f67_row2_col0, #T_26f67_row4_col0, #T_26f67_row7_col0, #T_26f67_row9_col0, #T_26f67_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_26f67">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_26f67_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_26f67_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_26f67_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_26f67_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_26f67_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_26f67_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_26f67_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_26f67_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_26f67_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_26f67_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_26f67_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_26f67_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_26f67_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_026af th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_026af td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_026af_row0_col0, #T_026af_row2_col0, #T_026af_row4_col0, #T_026af_row5_col0, #T_026af_row6_col0, #T_026af_row7_col0, #T_026af_row8_col0, #T_026af_row9_col0, #T_026af_row10_col0, #T_026af_row11_col0, #T_026af_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_026af_row1_col0, #T_026af_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_026af">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_026af_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_026af_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_026af_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_026af_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_026af_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_026af_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_026af_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_026af_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_026af_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_026af_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_026af_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_026af_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_026af_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
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
    * negatively skewed = more data to left of the centre
    * positively skewed = more data to the right of the centre
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
{{< tabs "80b4d862-4a01-4efd-9135-66d76b9e8748" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_461c3 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_461c3 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_461c3">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_461c3_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_461c3_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_461c3_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_461c3_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_461c3_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_461c3_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_47011 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_47011 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_47011_row0_col0, #T_47011_row1_col0, #T_47011_row2_col0, #T_47011_row3_col0, #T_47011_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_47011_row4_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_47011">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_47011_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_47011_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_47011_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_47011_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_47011_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_47011_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
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
* The probability of a single outcome of a continuous probability distribution cannot be calculated, in other words P(X=x) = 0.  The probability can only be calculated for a range
<BR><BR>
* Given $P(X=a) = 0$ and $P(X=b) = 0$, therefore $P(a < X < b) = P(a \leq X \leq b)$
<BR><BR>
* The area under a probability density function is 1 : $ {\int}^\infty_{-\infty} f(x)dx = 1$
<BR><BR>
* Given probability density function $f(x)$ over domain [a,b] and cumulative distribution function $F(x)$ $F(a) = 0$ and $F(b) = 1$
<BR><BR>



<br>


###  <span style="color:RGB(150,0,0)"> Formulas </span>
<br>
<style type="text/css">
#T_fe21b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_fe21b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_fe21b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_fe21b_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_fe21b_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = \int^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_fe21b_row2_col0" class="data row2 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
  </tbody>
</table>
