---
weight: 5
---

## <span style="color:RGB(0,32,96"> Descriptive Statistics and Bivariate Data Analysis </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - categorical data
 - numerical data
 - nominal data
 - ordinal data
 - discrete data
 - continuous data
 - frequency table
 - histogram
 - frequency polygon
 - cumulative frequency histogram
 - ogive (cumulative frequency polygon)
 - stem-and-leaf plot
 - dot plot
 - five-number summary
 - box plot (box-and-whisker-plot)
 - two-way table
 - bar chart
 - pie chart
 - Pareto chart
 - mode
 - median
 - outlier
 - quantile
 - quartile
 - decile
 - percentile
 - range
 - interquartile range
 - skewness
 - symmetrical distribution
 - modality
 - unimodal
 - bimodal
 - multimodal
 - bivariate data
 - dependent and independent variables
 - extrapolation
 - interpolation
 - least-squares regression line
 - line of best fit
 - Pearson's correlation coefficient
 - scatterplot
 - causality



### <span style="color:RGB(139,69,19)">  Notes </span>

 - Categorical data can be nominal or ordinal

 - Numerical data can be discrete or continuous

 - Displaying numerical data:
    *Frequency table
    * histogram (centre of column is lined up with value on x-axis.  No gap between columns) 
    * frequency polygon (line graph displaying frequency, starts and ends on x-axis) 
    * cumulative frequency histogram 
    * ogive (cumulative frequency polygon) 
    * stem and leaf plot [graphical display of tens (stems) and units (leaves)]
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
 
 - Don't need to utilise a formula to calculate Pearson's correlation co-efficient (r) but need to be able to calculate using calculator

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
{{< tabs "bf88b653-99de-4e59-a418-d9e340b32aab" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_e12054fa th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_e12054fa td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_e12054fa">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_e12054fa_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_e12054fa_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_e12054fa_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_e12054fa_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_e12054fa_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_e12054fa_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_e12054fa th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_e12054fa td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_e12054fa_row0_col0, #T_e12054fa_row1_col0, #T_e12054fa_row2_col0, #T_e12054fa_row3_col0, #T_e12054fa_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_e12054fa_row4_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_e12054fa">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_e12054fa_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_e12054fa_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_e12054fa_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_e12054fa_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_e12054fa_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_e12054fa_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Random Variables </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - random variable
 - continuous random variable
 - continuous probability distribution
 - uniform probability distribution
 - probability density function (pdf)
 - cumulative distribution function (cdf)
 - empirical rule
 - normal distribution
 - z-score



### <span style="color:RGB(139,69,19)">  Notes </span>

 - The cumulative distribution function is the integral of the probability density function

 - A continuous probability distribution is reported by a probability density function

 - The probability of a single outcome of a continuous probability distribution cannot be calculated, in other words $P(X=x) = 0$.  The probability can only be calculated for a range

 - Given $P(X=a) = 0$ and $P(X=b) = 0$, therefore $P(a < X < b) = P(a \leq X \leq b)$

 - The area under a probability density function is 1 : $ {\Large\int}^\infty_{-\infty} f(x)dx = 1$

 - Given probability density function $f(x)$ over domain [a,b] and cumulative distribution function $F(x)$ $F(a) = 0$ and $F(b) = 1$

 - The median lies at point x where ${\Large\int}^x_a f(x)dx = \dfrac{1}{2}$ where $f(x)$ is a pdf defined on domain [a,b].  Alternatively $F(x)-F(a) = \dfrac{1}{2}$ Similiar rules apply to other quantiles.

 - The mean, mode, and median are equal for a normal distribution
 
 - Finding probability by integration in a normal distribution is complex, therefore use tables where $\mu = 0$ and $\sigma = 1$


### <span style="color:RGB(139,69,19)"> Spreadsheets  </span>


Click on below to open spreadsheet examples

[RandomVariables](https://github.com/charl-potgieter/AustralianSchoolMaths/raw/main/WebsiteCreator/spreadsheets/RandomVariables.xlsx)
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "19e23b74-4771-4aba-9c6e-90d4451f5ef4" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_12d7a03c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_12d7a03c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_12d7a03c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_12d7a03c_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_12d7a03c_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_12d7a03c_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_12d7a03c_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_12d7a03c_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_12d7a03c_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_12d7a03c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_12d7a03c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_12d7a03c_row0_col0, #T_12d7a03c_row1_col0, #T_12d7a03c_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_12d7a03c_row2_col0, #T_12d7a03c_row3_col0, #T_12d7a03c_row5_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_12d7a03c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_12d7a03c_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_12d7a03c_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_12d7a03c_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_12d7a03c_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_12d7a03c_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_12d7a03c_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}