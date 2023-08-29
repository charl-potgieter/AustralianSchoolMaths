---
weight: 6
---

## <span style="color:RGB(0,0,150"> Probability and Discrete Probability Distributions </span> 
<br>

### <span style="color:RGB(139,69,19)"> Concepts  </span>


* complement
* theoretical probability
* conditional probability
* probability scale
* outcome
* equally likely outcomes
* event
* independent events
* mutually exclusive events
* non-mutually exclusive events
* probability tree
* relative frequency
* sample space
* set
* tree diagram
* array (table)
* Venn diagram
* random variable
* discrete random variable
* continuous random variable
* expected value
* population
* probability distribution
* discrete probability distribution
* standard deviation
* uniform discrete random variables
* non-uniform discrete random variables
* uniform probability distribution
* variance
* mean or expected value


### <span style="color:RGB(150,0,0)">  Notes </span>


* Probability trees: Use the product rule along branches to find $P( A \cap B )$   representing A and B
<BR><BR>* Probability trees: Use the additional rule for different branches to find $P(A \cup B) $ representing A or B.
<BR><BR>* $A \cup B $ is A union B
<BR><BR>* $A \cap B $  is A intersection B
<BR><BR>* The probability formula applies where each outcome is equally likely: $ P(E) = \dfrac{n(E)}{n(S)} $
<BR><BR>* The sum of all mutually exclusive probabilities is 1
<BR><BR>* $A \cup B = P(A) + P(B) $ is the addition rule for mutually exclusive events
<BR><BR>* $A \cup B = P(A) + P(B) - P(A \cap B) $ is the addition rule 
<BR><BR>* $A \cap B  = P(A)P(B)$ is the product rule for independent events only
<BR><BR>* Conditional probability is $ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $ while conditional proability for independent events is $ P(A|B) = P(A) $
<BR><BR>* Capital letter, e.g. X is often used for a random variable
<BR><BR>* Lower case letter such as x is used for the values of X
<BR><BR>* Properties of discrete probability distributions:
(a) All possible value of X are mutually exclusive
(b) The sum of probabilities = 1
(c) For each value of x: 0<=P(X=x)<=1
<BR><BR>* The expected values E(X) mof a probability distribution measures the centre of the distribution  = mean or average
<BR><BR>* $\overline{x} $ is the mean of a sample
<BR><BR>* $\mu $ is the mean of the population
<BR><BR>* $s$ is the sample standard deviation
<BR><BR>* $\sigma$ is the poplulation standard deviation
<BR><BR>* As the sample size increases $\overline{x} $ approaches  $\mu $
<BR><BR>* The complement of A can be written as $\overline A$ or $ \text{A'}$ or $A^c$
<BR><BR>


<br>


###  <span style="color:RGB(150,0,0)"> Formulas </span>
<br>
{{< tabs "82ec73b1-3081-43f9-bbe3-1c7887ee2dd3" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_1dd99 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_1dd99 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_1dd99">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_1dd99_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_1dd99_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_1dd99_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_1dd99_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_1dd99_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_1dd99_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_1dd99_row6_col0" class="data row6 col0" >$ E(X) = \mu = \sum xp(x $)</td>
    </tr>
    <tr>
      <td id="T_1dd99_row7_col0" class="data row7 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_1dd99_row8_col0" class="data row8 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_1dd99_row9_col0" class="data row9 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_1dd99_row10_col0" class="data row10 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_1dd99_row11_col0" class="data row11 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_2c231 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2c231 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_2c231_row0_col0, #T_2c231_row3_col0, #T_2c231_row5_col0, #T_2c231_row6_col0, #T_2c231_row7_col0, #T_2c231_row9_col0, #T_2c231_row11_col0 {
  background-color: rgba(0,0,0,0);
}
#T_2c231_row1_col0, #T_2c231_row2_col0, #T_2c231_row4_col0, #T_2c231_row8_col0, #T_2c231_row10_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_2c231">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_2c231_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_2c231_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_2c231_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_2c231_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_2c231_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_2c231_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_2c231_row6_col0" class="data row6 col0" >$ E(X) = \mu = \sum xp(x $)</td>
    </tr>
    <tr>
      <td id="T_2c231_row7_col0" class="data row7 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_2c231_row8_col0" class="data row8 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_2c231_row9_col0" class="data row9 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_2c231_row10_col0" class="data row10 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_2c231_row11_col0" class="data row11 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_ca20b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ca20b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_ca20b_row0_col0, #T_ca20b_row2_col0, #T_ca20b_row4_col0, #T_ca20b_row5_col0, #T_ca20b_row6_col0, #T_ca20b_row7_col0, #T_ca20b_row8_col0, #T_ca20b_row9_col0, #T_ca20b_row10_col0, #T_ca20b_row11_col0 {
  background-color: rgba(0,0,0,0);
}
#T_ca20b_row1_col0, #T_ca20b_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_ca20b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ca20b_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_ca20b_row1_col0" class="data row1 col0" >$A \cup B = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_ca20b_row2_col0" class="data row2 col0" >$A \cap B  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_ca20b_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_ca20b_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_ca20b_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_ca20b_row6_col0" class="data row6 col0" >$ E(X) = \mu = \sum xp(x $)</td>
    </tr>
    <tr>
      <td id="T_ca20b_row7_col0" class="data row7 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_ca20b_row8_col0" class="data row8 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_ca20b_row9_col0" class="data row9 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_ca20b_row10_col0" class="data row10 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_ca20b_row11_col0" class="data row11 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}