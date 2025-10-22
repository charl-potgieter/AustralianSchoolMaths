---
weight: 7
title: 'Descriptive statistics and bivariate data analysis'
---

###   Concepts 

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



###   Notes 

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

### Formulas
{{< tabs "tab4f6537f07896d09a" >}}

{{< tab "Standard View" >}}

<style type="text/css">
#T_NONE4f6537f07896d09a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_NONE4f6537f07896d09a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_NONE4f6537f07896d09a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_NONE4f6537f07896d09a_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_NONE4f6537f07896d09a_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_NONE4f6537f07896d09a_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_NONE4f6537f07896d09a_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_NONE4f6537f07896d09a_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_NONE4f6537f07896d09a_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

<style type="text/css">
#T_FORMULA_SHEET4f6537f07896d09a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_FORMULA_SHEET4f6537f07896d09a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_FORMULA_SHEET4f6537f07896d09a_row0_col0, #T_FORMULA_SHEET4f6537f07896d09a_row1_col0, #T_FORMULA_SHEET4f6537f07896d09a_row2_col0, #T_FORMULA_SHEET4f6537f07896d09a_row3_col0, #T_FORMULA_SHEET4f6537f07896d09a_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_FORMULA_SHEET4f6537f07896d09a_row4_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_FORMULA_SHEET4f6537f07896d09a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEET4f6537f07896d09a_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET4f6537f07896d09a_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET4f6537f07896d09a_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET4f6537f07896d09a_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET4f6537f07896d09a_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET4f6537f07896d09a_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
