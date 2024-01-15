---
weight: 6
---

## <span style="color:RGB(0,32,96"> Probability and Discrete Probability Distributions </span> 
<br>

### <span style="color:RGB(139,69,19)"> Concepts </span>

 - event
 - complement
 - independent events
 - mutually exclusive events
 - non-mutually exclusive events
 - outcome
 - equally likely outcomes
 - theoretical probability
 - conditional probability
 - probability scale
 - probability tree
 - tree diagram
 - array (table)
 - relative frequency
 - population
 - sample space
 - set
 - Venn diagram
 - random variable
 - discrete random variable
 - continuous random variable
 - uniform discrete random variables
 - non-uniform discrete random variables
 - expected value
 - probability distribution
 - discrete probability distribution
 - uniform probability distribution
 - mean or expected value
 - variance
 - standard deviation

<BR><BR>
### <span style="color:RGB(139,69,19)">  Notes </span>

 - Probability trees: Use the product rule along branches to find $P( A \cap B )$   representing A and B
  
 - Probability trees: Use the additional rule for different branches to find $P(A \cup B) $ representing A or B.
   
 - $A \cup B $ is A union B
   
 - $A \cap B $  is A intersection B
   
 - The probability formula applies where each outcome is equally likely: $ P(E) = \dfrac{n(E)}{n(S)} $
   
 - The sum of all mutually exclusive probabilities is 1
   
 - $P(A \cup B) = P(A) + P(B) $ is the addition rule for mutually exclusive events
   
 - $P(A \cup B) = P(A) + P(B) - P(A \cap B) $ is the addition rule
   
 - $P(A \cap B)  = P(A)P(B)$ is the product rule for independent events only
   
 - Conditional probability is $ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $ while conditional probability for independent events is $ P(A|B) = P(A) $
   
 - Capital letter, e.g. X is often used for a random variable
   
 - Lower case letter such as x is used for the values of X
   
 - Properties of discrete probability distributions:
    * All possible value of X are mutually exclusive
    * The sum of probabilities = 1
    * For each value of x: 0<=P(X=x)<=1
      
 - A probability distribution can be drawn as a table with columns for x and P$($x$)$
 
 - The expected values E(X) of a probability distribution measures the centre of the distribution  = mean or average
   
 - $\overline{x} $ is the mean of a sample
   
 - $\mu $ is the mean of the population
   
 - $s$ is the sample standard deviation
   
 - $\sigma$ is the poplulation standard deviation
   
 - As the sample size increases $\overline{x} $ approaches  $\mu $
   
 - The complement of A can be written as $\overline A$ or $ \text{A'}$ or $A^c$
   
 - The formula sheet defines variance as follows:  $ Var(X) = E(X^2) - \mu^2$.  The following may be an easier format to understand though: $ Var(X) = \sum[x^2p(x)] - \mu^2$
   
 - Know how to capture frequencies and calculate statistics on calculator

<BR><BR>
blah blah 
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "5c99efa5-7a47-4a1a-8216-fe0d9a393ec8" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_edd15 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_edd15 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_edd15">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_edd15_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_edd15_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_edd15_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_edd15_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_edd15_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_edd15_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_edd15_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_edd15_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_edd15_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_edd15_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_edd15_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_edd15_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_edd15_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_c807e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c807e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_c807e_row0_col0, #T_c807e_row3_col0, #T_c807e_row5_col0, #T_c807e_row6_col0, #T_c807e_row8_col0, #T_c807e_row10_col0, #T_c807e_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_c807e_row1_col0, #T_c807e_row2_col0, #T_c807e_row4_col0, #T_c807e_row7_col0, #T_c807e_row9_col0, #T_c807e_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_c807e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c807e_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_c807e_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_c807e_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_c807e_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_c807e_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_c807e_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_c807e_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_c807e_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_c807e_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_c807e_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_c807e_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_c807e_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_c807e_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_90f3c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_90f3c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_90f3c_row0_col0, #T_90f3c_row2_col0, #T_90f3c_row4_col0, #T_90f3c_row5_col0, #T_90f3c_row6_col0, #T_90f3c_row7_col0, #T_90f3c_row8_col0, #T_90f3c_row9_col0, #T_90f3c_row10_col0, #T_90f3c_row11_col0, #T_90f3c_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_90f3c_row1_col0, #T_90f3c_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_90f3c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_90f3c_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_90f3c_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_90f3c_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_90f3c_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_90f3c_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_90f3c_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_90f3c_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_90f3c_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_90f3c_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_90f3c_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_90f3c_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_90f3c_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_90f3c_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Descriptive Statistics and Bivariate Data Analysis </span> 
<br>

### <span style="color:RGB(139,69,19)">  Notes </span>
 * Categorical data can be nominal or ordinal
 
 
  Numerical data can be discrete or continuous

 - Displaying numerical data:
    *Frequency table
    * histogram (centre of column is lined up with value on x-axis.  No gap between columns)
    * frequency polygon (line graph displaying frequency, starts and ends on x-axis)
    * cumulative frequency histogram 
    * ogive (cumulative frequency polygon)
    * stem and leaf plot [graphical display of tens (stems) and units (leaves)
    * dot plot
    * five-number summary
    * box plot (box-and-whisker-plot)

 - 3 Measures of central tendency:
    * mean
    * mode
    * median

 - If ranges are provided in a frequency table a class centre will generally need to be added as an additional column in order to calculate statistics such as mean, standard deviation etc.

 - Grouped data has a modal class rather than a mode

 - If there are two middle values. In other words an even number of values, the median is the average of these values.

 - The median on an ogive is the halfway point on the cumulative frequency axis

 - Recommended, but not universal, method for computing quartiles:
    * Use the median to divide the ordered set into 2 halves.  
    * If there is an odd number in the original set then do not include the median in either half.
    * If there is an even number in the original set then split the set exactly in half
    * Q1 and Q3 are the medians of the lower and upper halves respectively

 - Quantile is a general term, quartiles divide set into 4 parts, deciles into 10 parts and percentiles into 100 parts

 - Shapes of data: 
    * negatively skewed = more area to left of the centre = the tail points to low scores
    * positively skewed = more area to the right of the centre = the tail points to high scores
    * symmetrical

 - Modality of data:
    * unimodal  = 1 peak
    * bimodal  = 2 peaks
    * multimodal = has many peaks

 - Scatterplots are used to graph bivariate data

 - Scatterplots can be:
    * linear
    * non-linear
    * have no shape

 - Don't need to utilise a formula to calculate Pearson's correlation co-efficient $($r$)$ but need to be able to calculate using calculator

 - Values of  Pearson's correlation co-efficient (r):
    * $ -1 \le r \le 1$
    * $ 0 \le r \le 1$ &emsp;&ensp;&nbsp;  scatterplot with positive direction
    * $r=1$ &emsp;&emsp;&emsp;&emsp; perfect positive correlation 
    * $ -1 \le r \le 0$ &ensp;&nbsp; scatterplot with negative direction 
    * $r=-1$ &emsp;&emsp;&emsp; perfect negative correlation
    * $r=0$ &emsp;&emsp;&emsp;&emsp; no correlation
    
 - Need to be able to calculate least squares regression line on a calculator but don’t need to be able to manually calculate with formula


<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "ff38a338-3add-4388-bc77-e6b26012288a" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_29958 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_29958 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_29958">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_29958_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_29958_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_29958_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_29958_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_29958_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_29958_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_5a558 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5a558 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_5a558_row0_col0, #T_5a558_row1_col0, #T_5a558_row2_col0, #T_5a558_row3_col0, #T_5a558_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_5a558_row4_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_5a558">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_5a558_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_5a558_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_5a558_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_5a558_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_5a558_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_5a558_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Random Variables </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "d90354fd-cd77-419e-aa61-3cb896682cb3" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_034c1 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_034c1 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_034c1">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_034c1_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_034c1_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_034c1_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_034c1_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_034c1_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_034c1_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_8ae8c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8ae8c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_8ae8c_row0_col0, #T_8ae8c_row1_col0, #T_8ae8c_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_8ae8c_row2_col0, #T_8ae8c_row3_col0, #T_8ae8c_row5_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_8ae8c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_8ae8c_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_8ae8c_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_8ae8c_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_8ae8c_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_8ae8c_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_8ae8c_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

### <span style="color:RGB(139,69,19)"> Spreadsheets  </span>


Click on below to open spreadsheet examples

[RandomVariables](https://github.com/charl-potgieter/AustralianSchoolMaths/raw/main/WebsiteCreator/spreadsheets/RandomVariables.xlsx)
