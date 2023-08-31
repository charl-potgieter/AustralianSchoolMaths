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
{{< tabs "67bf2c57-d27f-48fa-8e2b-0022dfdfc4d8" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_acb79 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_acb79 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_acb79">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_acb79_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_acb79_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_acb79_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_acb79_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_acb79_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_acb79_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_acb79_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_acb79_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_acb79_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_acb79_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_acb79_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_acb79_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_acb79_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_2428d th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2428d td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_2428d_row0_col0, #T_2428d_row3_col0, #T_2428d_row5_col0, #T_2428d_row6_col0, #T_2428d_row8_col0, #T_2428d_row10_col0, #T_2428d_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_2428d_row1_col0, #T_2428d_row2_col0, #T_2428d_row4_col0, #T_2428d_row7_col0, #T_2428d_row9_col0, #T_2428d_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_2428d">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_2428d_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_2428d_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_2428d_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_2428d_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_2428d_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_2428d_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_2428d_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_2428d_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_2428d_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_2428d_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_2428d_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_2428d_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_2428d_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_c186f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c186f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_c186f_row0_col0, #T_c186f_row2_col0, #T_c186f_row4_col0, #T_c186f_row5_col0, #T_c186f_row6_col0, #T_c186f_row7_col0, #T_c186f_row8_col0, #T_c186f_row9_col0, #T_c186f_row10_col0, #T_c186f_row11_col0, #T_c186f_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_c186f_row1_col0, #T_c186f_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_c186f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c186f_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_c186f_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_c186f_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_c186f_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_c186f_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_c186f_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_c186f_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_c186f_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_c186f_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_c186f_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_c186f_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_c186f_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_c186f_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,0,150"> Descriptive Statistics and Bivariate Data Analysis </span> 
<br>

### <span style="color:RGB(139,69,19)"> Concepts  </span>


* bar chart
* bimodal
* box plot
* categorical data
* continuous data
* decile
* discrete data
* dot plot
* five-number summary
* frequency polygon
* histogram
* interquartile range
* median
* modality
* mode
* multimodal
* nomimal data
* numerical data
* ogive
* ordinal data
* outlier
* Pareto chart
* percentile
* pie chart
* quantile
* quartile
* range
* skewness
* stem-and-leaf plot
* symmetrical distribution
* two-way table


### <span style="color:RGB(150,0,0)">  Notes </span>


* Categorical data can be nominal or ordinal
<BR><BR>
* Numerical data can be discrete or continuous
<BR><BR>
* Displaying numerical data: 
    * histogram $($centre of column is lined up with value on x-axis.  No gap between columns$)$ 
    * Frequency polygon $($line graph displaying frequency, starts and ends on x-axis$)$ 
    * Cumulative frequency histogram 
    * Ogive $($cumulative frequency polygon$)$ 
    * Stem and leaf plot $[$graphical display of tens $($stems$)$ and units $($leaves$)]$
<BR><BR>
* Displaying categorical data:
    * Two way table
    * Bar chart $($there are gaps between columns, unlike the histogram$)$
    * Pie chart
    * Pareto chart $($bar chart of frequencies in descending order.  No gaps.  Non cumulative.   + Cumulative percentage frequency line graph starting at 0% on left and ending with 100% on right.  Two y-axis: frequency units on left and cumulative percentage frequency on the right$)$
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
    * Negatively skewed = more data to left of the centre
    * positively skewed = more data to the right of the centre
    & symmetrical
<BR><BR>
* Modality of data:
    * Unimodal  = 1 peak
    * bimodal  = 2 peaks
    * multimodal = has many peaks
<BR><BR>



<br>


###  <span style="color:RGB(150,0,0)"> Formulas </span>
<br>
{{< tabs "3b978a3b-1298-4d4a-9239-66048d5ff3ab" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_47c71 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_47c71 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_47c71">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_47c71_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_47c71_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_47c71_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_47c71_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_47c71_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_47c71_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_ba6fb th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ba6fb td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_ba6fb_row0_col0, #T_ba6fb_row1_col0, #T_ba6fb_row2_col0, #T_ba6fb_row3_col0, #T_ba6fb_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_ba6fb_row4_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_ba6fb">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ba6fb_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_ba6fb_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_ba6fb_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_ba6fb_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_ba6fb_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_ba6fb_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,0,150"> Random Variables </span> 
<br>

## <span style="color:RGB(0,0,150"> The Binomial Distribution </span> 
<br>