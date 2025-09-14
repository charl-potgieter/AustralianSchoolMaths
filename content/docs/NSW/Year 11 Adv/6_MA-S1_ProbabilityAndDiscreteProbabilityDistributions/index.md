---
weight: 6
title: 'Probability and Discrete Probability Distributions'
---

## Probability and Discrete Probability Distributions

###   Concepts 

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


###   Notes 

 - Probability trees: Use the product rule along branches to find $P( A \cap B )$   representing A and B

 - Probability trees: Use the additional rule for different branches to find $P(A \cup B) $ representing A or B.

 - $A \cup B $ is A union B

 - $A \cap B $  is A intersection B

 - The probability formula applies where each outcome is equally likely: $ P(E) = \dfrac{n(E)}{n(S)} $

 - The sum of all mutually exclusive probabilities is 1

 - $P(A \cup B) = P(A) + P(B) $ is the addition rule for mutually exclusive events

 - $P(A \cup B) = P(A) + P(B) - P(A \cap B) $ is the addition rule 

 - $P(A \cap B)  = P(A)P(B)$ is the product rule for independent events only

 - Conditional probability is $ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) eq 0 $ while conditional probability for independent events is $ P(A|B) = P(A) $

 - Capital letter, e.g. X is often used for a random variable

 - Lower case letter such as x is used for the values of X

 - Properties of discrete probability distributions:
    * All possible value of X are mutually exclusive
    * The sum of probabilities = 1
    * For each value of x: 0<=P(X=x)<=1

 - A probability distribution can be drawn as a table with columns for x and P(x)

 - The expected values E(X) of a probability distribution measures the centre of the distribution  = mean or average
 - $\overline{x} $ is the mean of a sample

 - $\mu $ is the mean of the population

 - $s$ is the sample standard deviation

 - $\sigma$ is the poplulation standard deviation

 - As the sample size increases $\overline{x} $ approaches  $\mu $

 - The complement of A can be written as $\overline A$ or $ \text{A'}$ or $A^c$

 - The formula sheet defines variance as follows:  $ Var(X) = E(X^2) - \mu^2$.  The following may be an easier format to understand though: $ Var(X) = \sum[x^2p(x)] - \mu^2$
 
 - Know how to capture frequencies and calculate statistics on calculator

### Formulas
{{< tabs "tabcbf34da2f28905fc" >}}

{{< tab "Standard View" >}}

<style type="text/css">
#T_NONEcbf34da2f28905fc th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_NONEcbf34da2f28905fc td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_NONEcbf34da2f28905fc">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col2" class="data row0 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col3" class="data row0 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col4" class="data row0 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col5" class="data row0 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col10" class="data row0 col10" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col11" class="data row0 col11" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col12" class="data row0 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col2" class="data row1 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col3" class="data row1 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col4" class="data row1 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col5" class="data row1 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col10" class="data row1 col10" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col11" class="data row1 col11" >True</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col12" class="data row1 col12" >True</td>
      <td id="T_NONEcbf34da2f28905fc_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col2" class="data row2 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col3" class="data row2 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col4" class="data row2 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col5" class="data row2 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col10" class="data row2 col10" >$P(A \cap B)  = P(A)P(B)$</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col11" class="data row2 col11" >True</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col12" class="data row2 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col2" class="data row3 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col3" class="data row3 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col4" class="data row3 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col5" class="data row3 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col10" class="data row3 col10" >$P(\overline{E}) = 1 - P(E)$</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col11" class="data row3 col11" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col12" class="data row3 col12" >True</td>
      <td id="T_NONEcbf34da2f28905fc_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col2" class="data row4 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col3" class="data row4 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col4" class="data row4 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col5" class="data row4 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col10" class="data row4 col10" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col11" class="data row4 col11" >True</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col12" class="data row4 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col2" class="data row5 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col3" class="data row5 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col4" class="data row5 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col5" class="data row5 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col10" class="data row5 col10" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col11" class="data row5 col11" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col12" class="data row5 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col2" class="data row6 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col3" class="data row6 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col4" class="data row6 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col5" class="data row6 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col10" class="data row6 col10" >$ E(X) =\sum xp(x)$</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col11" class="data row6 col11" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col12" class="data row6 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col2" class="data row7 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col3" class="data row7 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col4" class="data row7 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col5" class="data row7 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col10" class="data row7 col10" >$ E(X) = \mu $</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col11" class="data row7 col11" >True</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col12" class="data row7 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col2" class="data row8 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col3" class="data row8 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col4" class="data row8 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col5" class="data row8 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col9" class="data row8 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col10" class="data row8 col10" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col11" class="data row8 col11" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col12" class="data row8 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col2" class="data row9 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col3" class="data row9 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col4" class="data row9 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col5" class="data row9 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col9" class="data row9 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col10" class="data row9 col10" >$ Var(X) = E[(x-\mu)^2]$</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col11" class="data row9 col11" >True</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col12" class="data row9 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col2" class="data row10 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col3" class="data row10 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col4" class="data row10 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col5" class="data row10 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col9" class="data row10 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col10" class="data row10 col10" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col11" class="data row10 col11" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col12" class="data row10 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row10_col13" class="data row10 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row11_col0" class="data row11 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col1" class="data row11 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col2" class="data row11 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col3" class="data row11 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col4" class="data row11 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col5" class="data row11 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col6" class="data row11 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col7" class="data row11 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col8" class="data row11 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col9" class="data row11 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col10" class="data row11 col10" >$ Var(X) = E(X^2) - \mu^2$</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col11" class="data row11 col11" >True</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col12" class="data row11 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row11_col13" class="data row11 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONEcbf34da2f28905fc_row12_col0" class="data row12 col0" >NSW</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col1" class="data row12 col1" >Year 11 Adv</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col2" class="data row12 col2" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col3" class="data row12 col3" >MA-S1</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col4" class="data row12 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col5" class="data row12 col5" >Statistical Analysis</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col6" class="data row12 col6" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col7" class="data row12 col7" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col8" class="data row12 col8" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col9" class="data row12 col9" >nan</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col10" class="data row12 col10" >$ \sigma = \sqrt{Var(X)}$</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col11" class="data row12 col11" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col12" class="data row12 col12" >False</td>
      <td id="T_NONEcbf34da2f28905fc_row12_col13" class="data row12 col13" >nan</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

<style type="text/css">
#T_FORMULA_SHEETcbf34da2f28905fc th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_FORMULA_SHEETcbf34da2f28905fc td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_FORMULA_SHEETcbf34da2f28905fc_row0_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row0_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row1_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row3_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row5_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row6_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row8_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row10_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col13, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col0, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col1, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col2, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col3, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col4, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col5, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col6, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col7, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col8, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col9, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col11, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col12, #T_FORMULA_SHEETcbf34da2f28905fc_row12_col13 {
  background-color: rgba(0,0,0,0);
}
#T_FORMULA_SHEETcbf34da2f28905fc_row1_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row2_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row4_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row7_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row9_col10, #T_FORMULA_SHEETcbf34da2f28905fc_row11_col10 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_FORMULA_SHEETcbf34da2f28905fc">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col2" class="data row0 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col3" class="data row0 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col4" class="data row0 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col5" class="data row0 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col10" class="data row0 col10" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col11" class="data row0 col11" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col12" class="data row0 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col2" class="data row1 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col3" class="data row1 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col4" class="data row1 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col5" class="data row1 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col10" class="data row1 col10" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col11" class="data row1 col11" >True</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col12" class="data row1 col12" >True</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col2" class="data row2 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col3" class="data row2 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col4" class="data row2 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col5" class="data row2 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col10" class="data row2 col10" >$P(A \cap B)  = P(A)P(B)$</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col11" class="data row2 col11" >True</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col12" class="data row2 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col2" class="data row3 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col3" class="data row3 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col4" class="data row3 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col5" class="data row3 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col10" class="data row3 col10" >$P(\overline{E}) = 1 - P(E)$</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col11" class="data row3 col11" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col12" class="data row3 col12" >True</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col2" class="data row4 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col3" class="data row4 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col4" class="data row4 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col5" class="data row4 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col10" class="data row4 col10" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col11" class="data row4 col11" >True</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col12" class="data row4 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col2" class="data row5 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col3" class="data row5 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col4" class="data row5 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col5" class="data row5 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col10" class="data row5 col10" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col11" class="data row5 col11" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col12" class="data row5 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col2" class="data row6 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col3" class="data row6 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col4" class="data row6 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col5" class="data row6 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col10" class="data row6 col10" >$ E(X) =\sum xp(x)$</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col11" class="data row6 col11" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col12" class="data row6 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col2" class="data row7 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col3" class="data row7 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col4" class="data row7 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col5" class="data row7 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col10" class="data row7 col10" >$ E(X) = \mu $</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col11" class="data row7 col11" >True</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col12" class="data row7 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col2" class="data row8 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col3" class="data row8 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col4" class="data row8 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col5" class="data row8 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col9" class="data row8 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col10" class="data row8 col10" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col11" class="data row8 col11" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col12" class="data row8 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col2" class="data row9 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col3" class="data row9 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col4" class="data row9 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col5" class="data row9 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col9" class="data row9 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col10" class="data row9 col10" >$ Var(X) = E[(x-\mu)^2]$</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col11" class="data row9 col11" >True</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col12" class="data row9 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col2" class="data row10 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col3" class="data row10 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col4" class="data row10 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col5" class="data row10 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col9" class="data row10 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col10" class="data row10 col10" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col11" class="data row10 col11" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col12" class="data row10 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row10_col13" class="data row10 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col0" class="data row11 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col1" class="data row11 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col2" class="data row11 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col3" class="data row11 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col4" class="data row11 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col5" class="data row11 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col6" class="data row11 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col7" class="data row11 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col8" class="data row11 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col9" class="data row11 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col10" class="data row11 col10" >$ Var(X) = E(X^2) - \mu^2$</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col11" class="data row11 col11" >True</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col12" class="data row11 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row11_col13" class="data row11 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col0" class="data row12 col0" >NSW</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col1" class="data row12 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col2" class="data row12 col2" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col3" class="data row12 col3" >MA-S1</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col4" class="data row12 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col5" class="data row12 col5" >Statistical Analysis</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col6" class="data row12 col6" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col7" class="data row12 col7" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col8" class="data row12 col8" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col9" class="data row12 col9" >nan</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col10" class="data row12 col10" >$ \sigma = \sqrt{Var(X)}$</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col11" class="data row12 col11" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col12" class="data row12 col12" >False</td>
      <td id="T_FORMULA_SHEETcbf34da2f28905fc_row12_col13" class="data row12 col13" >nan</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proof Required" >}}

<style type="text/css">
#T_PROOF_REQUIREDcbf34da2f28905fc th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_PROOF_REQUIREDcbf34da2f28905fc td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_PROOF_REQUIREDcbf34da2f28905fc_row0_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row0_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row1_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row2_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row4_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row5_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row6_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row7_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row8_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row9_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row10_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row11_col13, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col0, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col1, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col2, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col3, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col4, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col5, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col6, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col7, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col8, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col9, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col11, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col12, #T_PROOF_REQUIREDcbf34da2f28905fc_row12_col13 {
  background-color: rgba(0,0,0,0);
}
#T_PROOF_REQUIREDcbf34da2f28905fc_row1_col10, #T_PROOF_REQUIREDcbf34da2f28905fc_row3_col10 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_PROOF_REQUIREDcbf34da2f28905fc">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col2" class="data row0 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col3" class="data row0 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col4" class="data row0 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col5" class="data row0 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col10" class="data row0 col10" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col11" class="data row0 col11" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col12" class="data row0 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col2" class="data row1 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col3" class="data row1 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col4" class="data row1 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col5" class="data row1 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col10" class="data row1 col10" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col11" class="data row1 col11" >True</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col12" class="data row1 col12" >True</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col2" class="data row2 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col3" class="data row2 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col4" class="data row2 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col5" class="data row2 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col10" class="data row2 col10" >$P(A \cap B)  = P(A)P(B)$</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col11" class="data row2 col11" >True</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col12" class="data row2 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col2" class="data row3 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col3" class="data row3 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col4" class="data row3 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col5" class="data row3 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col10" class="data row3 col10" >$P(\overline{E}) = 1 - P(E)$</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col11" class="data row3 col11" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col12" class="data row3 col12" >True</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col2" class="data row4 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col3" class="data row4 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col4" class="data row4 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col5" class="data row4 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col10" class="data row4 col10" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col11" class="data row4 col11" >True</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col12" class="data row4 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col2" class="data row5 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col3" class="data row5 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col4" class="data row5 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col5" class="data row5 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col10" class="data row5 col10" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col11" class="data row5 col11" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col12" class="data row5 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col2" class="data row6 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col3" class="data row6 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col4" class="data row6 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col5" class="data row6 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col10" class="data row6 col10" >$ E(X) =\sum xp(x)$</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col11" class="data row6 col11" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col12" class="data row6 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col2" class="data row7 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col3" class="data row7 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col4" class="data row7 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col5" class="data row7 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col10" class="data row7 col10" >$ E(X) = \mu $</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col11" class="data row7 col11" >True</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col12" class="data row7 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col2" class="data row8 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col3" class="data row8 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col4" class="data row8 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col5" class="data row8 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col9" class="data row8 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col10" class="data row8 col10" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col11" class="data row8 col11" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col12" class="data row8 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col2" class="data row9 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col3" class="data row9 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col4" class="data row9 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col5" class="data row9 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col9" class="data row9 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col10" class="data row9 col10" >$ Var(X) = E[(x-\mu)^2]$</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col11" class="data row9 col11" >True</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col12" class="data row9 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col2" class="data row10 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col3" class="data row10 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col4" class="data row10 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col5" class="data row10 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col9" class="data row10 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col10" class="data row10 col10" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col11" class="data row10 col11" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col12" class="data row10 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row10_col13" class="data row10 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col0" class="data row11 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col1" class="data row11 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col2" class="data row11 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col3" class="data row11 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col4" class="data row11 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col5" class="data row11 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col6" class="data row11 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col7" class="data row11 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col8" class="data row11 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col9" class="data row11 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col10" class="data row11 col10" >$ Var(X) = E(X^2) - \mu^2$</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col11" class="data row11 col11" >True</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col12" class="data row11 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row11_col13" class="data row11 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col0" class="data row12 col0" >NSW</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col1" class="data row12 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col2" class="data row12 col2" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col3" class="data row12 col3" >MA-S1</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col4" class="data row12 col4" >Probability and Discrete Probability Distributions</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col5" class="data row12 col5" >Statistical Analysis</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col6" class="data row12 col6" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col7" class="data row12 col7" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col8" class="data row12 col8" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col9" class="data row12 col9" >nan</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col10" class="data row12 col10" >$ \sigma = \sqrt{Var(X)}$</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col11" class="data row12 col11" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col12" class="data row12 col12" >False</td>
      <td id="T_PROOF_REQUIREDcbf34da2f28905fc_row12_col13" class="data row12 col13" >nan</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
