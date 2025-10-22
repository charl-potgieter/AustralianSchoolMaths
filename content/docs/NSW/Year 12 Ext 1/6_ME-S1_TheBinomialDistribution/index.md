---
weight: 6
title: 'The binomial distribution'
---


###   Concepts 

 - Bernoulli random variable
 - Binomial random variable
 - Bernoulli trial
 - Bernoulli distribution
 - Binomial distribution
 - population proportion
 - sample proportion
 - sampling distribution of proportions
 - central limit theorem



###   Notes 

 - Properties of binomial distribution:
    * fixed number of trials
    * there are only 2 outcomes: success or failure
    * each trial is independent
    * Probabilities are the same for each trial

 - Share of a binomial distribution:
    * p<0.5 : positively skewed
    * p=0.5 : normal / symmetrical
    * p>0.5 : negatively skewed
    
 - Be able to represent a Bernoulli distribution as a :
    * piecewise function
    * distribution table
    * bar chart


###  Spreadsheets  


Click on below to open spreadsheet examples

[BinomialDistributions](https://github.com/charl-potgieter/AustralianSchoolMaths/raw/main/WebsiteCreator/spreadsheets/BinomialDistributions.xlsx)

### Formulas
{{< tabs "tab3b5a8d2e5e932c1f" >}}

{{< tab "Standard View" >}}

<style type="text/css">
#T_NONE3b5a8d2e5e932c1f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_NONE3b5a8d2e5e932c1f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_NONE3b5a8d2e5e932c1f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_NONE3b5a8d2e5e932c1f_row0_col0" class="data row0 col0" >$ \text{Bernoulli distribution: } E(X) = p $</td>
    </tr>
    <tr>
      <td id="T_NONE3b5a8d2e5e932c1f_row1_col0" class="data row1 col0" >$ \text{Bernoulli distribution: } VAR(X) = p(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_NONE3b5a8d2e5e932c1f_row2_col0" class="data row2 col0" >$\text{Binomial distribution}: P(X=r) = ^nC_rp^r(1-p)^{n-r}$</td>
    </tr>
    <tr>
      <td id="T_NONE3b5a8d2e5e932c1f_row3_col0" class="data row3 col0" >$\text{Binomial distribution}: X\sim Bin(n,p) $
$ \Rightarrow P(X=x) $
$ = \bigl({n \atop x} \bigr)p^x(1-p)^{n-x}, x=0,1,...,n$</td>
    </tr>
    <tr>
      <td id="T_NONE3b5a8d2e5e932c1f_row4_col0" class="data row4 col0" >$ \text{binomial distribution: } E(X) = np $</td>
    </tr>
    <tr>
      <td id="T_NONE3b5a8d2e5e932c1f_row5_col0" class="data row5 col0" >$ \text{binmomial distribution: } VAR(X) = np(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_NONE3b5a8d2e5e932c1f_row6_col0" class="data row6 col0" >$ \hat{p} = \dfrac{x}{n} $</td>
    </tr>
    <tr>
      <td id="T_NONE3b5a8d2e5e932c1f_row7_col0" class="data row7 col0" >$ \text{sample proportions: } E(\hat{p}) = p $</td>
    </tr>
    <tr>
      <td id="T_NONE3b5a8d2e5e932c1f_row8_col0" class="data row8 col0" >$ \text{sample proportions: } \text{VAR} (\hat{p}) = \dfrac{p(1-p)}{n} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

<style type="text/css">
#T_FORMULA_SHEET3b5a8d2e5e932c1f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_FORMULA_SHEET3b5a8d2e5e932c1f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_FORMULA_SHEET3b5a8d2e5e932c1f_row0_col0, #T_FORMULA_SHEET3b5a8d2e5e932c1f_row1_col0, #T_FORMULA_SHEET3b5a8d2e5e932c1f_row6_col0, #T_FORMULA_SHEET3b5a8d2e5e932c1f_row7_col0, #T_FORMULA_SHEET3b5a8d2e5e932c1f_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_FORMULA_SHEET3b5a8d2e5e932c1f_row2_col0, #T_FORMULA_SHEET3b5a8d2e5e932c1f_row3_col0, #T_FORMULA_SHEET3b5a8d2e5e932c1f_row4_col0, #T_FORMULA_SHEET3b5a8d2e5e932c1f_row5_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_FORMULA_SHEET3b5a8d2e5e932c1f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEET3b5a8d2e5e932c1f_row0_col0" class="data row0 col0" >$ \text{Bernoulli distribution: } E(X) = p $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET3b5a8d2e5e932c1f_row1_col0" class="data row1 col0" >$ \text{Bernoulli distribution: } VAR(X) = p(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET3b5a8d2e5e932c1f_row2_col0" class="data row2 col0" >$\text{Binomial distribution}: P(X=r) = ^nC_rp^r(1-p)^{n-r}$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET3b5a8d2e5e932c1f_row3_col0" class="data row3 col0" >$\text{Binomial distribution}: X\sim Bin(n,p) $
$ \Rightarrow P(X=x) $
$ = \bigl({n \atop x} \bigr)p^x(1-p)^{n-x}, x=0,1,...,n$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET3b5a8d2e5e932c1f_row4_col0" class="data row4 col0" >$ \text{binomial distribution: } E(X) = np $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET3b5a8d2e5e932c1f_row5_col0" class="data row5 col0" >$ \text{binmomial distribution: } VAR(X) = np(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET3b5a8d2e5e932c1f_row6_col0" class="data row6 col0" >$ \hat{p} = \dfrac{x}{n} $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET3b5a8d2e5e932c1f_row7_col0" class="data row7 col0" >$ \text{sample proportions: } E(\hat{p}) = p $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET3b5a8d2e5e932c1f_row8_col0" class="data row8 col0" >$ \text{sample proportions: } \text{VAR} (\hat{p}) = \dfrac{p(1-p)}{n} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
