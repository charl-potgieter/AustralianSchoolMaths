---
weight: 5
---

## <span style="color:RGB(0,0,150"> Probability and Discrete Probability Distributions </span> 
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
{{< tabs "d991684f-d81f-4a61-b406-94965ed9e7bf" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_ec783 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ec783 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_ec783">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ec783_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_ec783_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_ec783_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_ec783_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_ec783_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_ec783_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_ec783_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_ec783_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_ec783_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_ec783_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_ec783_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_ec783_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_ec783_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_64885 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_64885 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_64885_row0_col0, #T_64885_row3_col0, #T_64885_row5_col0, #T_64885_row6_col0, #T_64885_row8_col0, #T_64885_row10_col0, #T_64885_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_64885_row1_col0, #T_64885_row2_col0, #T_64885_row4_col0, #T_64885_row7_col0, #T_64885_row9_col0, #T_64885_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_64885">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_64885_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_64885_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_64885_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_64885_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_64885_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_64885_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_64885_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_64885_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_64885_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_64885_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_64885_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_64885_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_64885_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_4870d th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_4870d td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_4870d_row0_col0, #T_4870d_row2_col0, #T_4870d_row4_col0, #T_4870d_row5_col0, #T_4870d_row6_col0, #T_4870d_row7_col0, #T_4870d_row8_col0, #T_4870d_row9_col0, #T_4870d_row10_col0, #T_4870d_row11_col0, #T_4870d_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_4870d_row1_col0, #T_4870d_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_4870d">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_4870d_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_4870d_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_4870d_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_4870d_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_4870d_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_4870d_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_4870d_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_4870d_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_4870d_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_4870d_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_4870d_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_4870d_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_4870d_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,0,150"> Descriptive Statistics and Bivariate Data Analysis </span> 
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
* extrapolation
* interpolation
* least-squares regression line
* line of best fit
* Pearson's correlation coefficient
* scatterplot
* Causality


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
    *$ -1 \le r \le 1$
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
{{< tabs "a091881d-a080-4bc1-a5ff-6b2d0e2328f4" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_91d2f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_91d2f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_91d2f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_91d2f_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_91d2f_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_91d2f_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_91d2f_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_91d2f_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_91d2f_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_0f5eb th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_0f5eb td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_0f5eb_row0_col0, #T_0f5eb_row1_col0, #T_0f5eb_row2_col0, #T_0f5eb_row3_col0, #T_0f5eb_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_0f5eb_row4_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_0f5eb">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_0f5eb_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_0f5eb_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_0f5eb_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_0f5eb_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_0f5eb_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_0f5eb_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,0,150"> Random Variables </span> 
<br>

## <span style="color:RGB(0,0,150"> The Binomial Distribution </span> 
<br>