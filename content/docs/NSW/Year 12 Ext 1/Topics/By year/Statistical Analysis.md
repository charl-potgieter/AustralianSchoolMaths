---
weight: 5
---

## <span style="color:RGB(0,32,96"> The Binomial Distribution </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - Bernoulli random variable
 - Binomial random variable
 - Bernoulli trial
 - Bernoulli distribution
 - Binomial distribution
 - population proportion
 - sample proportion
 - sampling distribution of proportions
 - central limit theorem



### <span style="color:RGB(139,69,19)">  Notes </span>

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


### <span style="color:RGB(139,69,19)"> Spreadsheets  </span>


Click on below to open spreadsheet examples

[BinomialDistributions](https://github.com/charl-potgieter/AustralianSchoolMaths/raw/main/WebsiteCreator/spreadsheets/BinomialDistributions.xlsx)
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "d497ee75-ef83-4bfe-a428-fabc63a2b6fe" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_57a6a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_57a6a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_57a6a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_57a6a_row0_col0" class="data row0 col0" >$ \text{Bernoulli distribution: } E(X) = p $</td>
    </tr>
    <tr>
      <td id="T_57a6a_row1_col0" class="data row1 col0" >$ \text{Bernoulli distribution: } VAR(X) = p(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_57a6a_row2_col0" class="data row2 col0" >$\text{Binomial distribution}: P(X=r) = ^nC_rp^r(1-p)^{n-r}$</td>
    </tr>
    <tr>
      <td id="T_57a6a_row3_col0" class="data row3 col0" >$\text{Binomial distribution}: X\sim Bin(n,p) $
$ \Rightarrow P(X=x) $
$ = \bigl({n \atop x} \bigr)p^x(1-p)^{n-x}, x=0,1,...,n$</td>
    </tr>
    <tr>
      <td id="T_57a6a_row4_col0" class="data row4 col0" >$ \text{binomial distribution: } E(X) = np $</td>
    </tr>
    <tr>
      <td id="T_57a6a_row5_col0" class="data row5 col0" >$ \text{binmomial distribution: } VAR(X) = np(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_57a6a_row6_col0" class="data row6 col0" >$ \hat{p} = \dfrac{x}{n} $</td>
    </tr>
    <tr>
      <td id="T_57a6a_row7_col0" class="data row7 col0" >$ \text{sample proportions: } E(\hat{p}) = p $</td>
    </tr>
    <tr>
      <td id="T_57a6a_row8_col0" class="data row8 col0" >$ \text{sample proportions: } \text{VAR} (\hat{p}) = \dfrac{p(1-p)}{n} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_f1616 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f1616 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_f1616_row0_col0, #T_f1616_row1_col0, #T_f1616_row7_col0, #T_f1616_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_f1616_row2_col0, #T_f1616_row3_col0, #T_f1616_row4_col0, #T_f1616_row5_col0, #T_f1616_row6_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_f1616">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_f1616_row0_col0" class="data row0 col0" >$ \text{Bernoulli distribution: } E(X) = p $</td>
    </tr>
    <tr>
      <td id="T_f1616_row1_col0" class="data row1 col0" >$ \text{Bernoulli distribution: } VAR(X) = p(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_f1616_row2_col0" class="data row2 col0" >$\text{Binomial distribution}: P(X=r) = ^nC_rp^r(1-p)^{n-r}$</td>
    </tr>
    <tr>
      <td id="T_f1616_row3_col0" class="data row3 col0" >$\text{Binomial distribution}: X\sim Bin(n,p) $
$ \Rightarrow P(X=x) $
$ = \bigl({n \atop x} \bigr)p^x(1-p)^{n-x}, x=0,1,...,n$</td>
    </tr>
    <tr>
      <td id="T_f1616_row4_col0" class="data row4 col0" >$ \text{binomial distribution: } E(X) = np $</td>
    </tr>
    <tr>
      <td id="T_f1616_row5_col0" class="data row5 col0" >$ \text{binmomial distribution: } VAR(X) = np(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_f1616_row6_col0" class="data row6 col0" >$ \hat{p} = \dfrac{x}{n} $</td>
    </tr>
    <tr>
      <td id="T_f1616_row7_col0" class="data row7 col0" >$ \text{sample proportions: } E(\hat{p}) = p $</td>
    </tr>
    <tr>
      <td id="T_f1616_row8_col0" class="data row8 col0" >$ \text{sample proportions: } \text{VAR} (\hat{p}) = \dfrac{p(1-p)}{n} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}