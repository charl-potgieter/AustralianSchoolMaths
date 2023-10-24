---
weight: 5
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


### <span style="color:RGB(139,69,19)">  Notes </span>


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


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "24d46100-026c-42be-8300-1ee182fdd726" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_4290d th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_4290d td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_4290d">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_4290d_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_4290d_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_4290d_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_4290d_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_4290d_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_4290d_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_4290d_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_4290d_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_4290d_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_4290d_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_4290d_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_4290d_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_4290d_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_495ce th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_495ce td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_495ce_row0_col0, #T_495ce_row3_col0, #T_495ce_row5_col0, #T_495ce_row6_col0, #T_495ce_row8_col0, #T_495ce_row10_col0, #T_495ce_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_495ce_row1_col0, #T_495ce_row2_col0, #T_495ce_row4_col0, #T_495ce_row7_col0, #T_495ce_row9_col0, #T_495ce_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_495ce">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_495ce_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_495ce_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_495ce_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_495ce_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_495ce_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_495ce_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_495ce_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_495ce_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_495ce_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_495ce_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_495ce_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_495ce_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_495ce_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_18b3e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_18b3e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_18b3e_row0_col0, #T_18b3e_row2_col0, #T_18b3e_row4_col0, #T_18b3e_row5_col0, #T_18b3e_row6_col0, #T_18b3e_row7_col0, #T_18b3e_row8_col0, #T_18b3e_row9_col0, #T_18b3e_row10_col0, #T_18b3e_row11_col0, #T_18b3e_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_18b3e_row1_col0, #T_18b3e_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_18b3e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_18b3e_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_18b3e_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_18b3e_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_18b3e_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_18b3e_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_18b3e_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_18b3e_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_18b3e_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_18b3e_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_18b3e_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_18b3e_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_18b3e_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_18b3e_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}