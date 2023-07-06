---
weight: 2
---

# Financial mathematics

## Compounding interest


$\displaystyle A = P(1+r)^n$


## Arithmetic sequence and series

An **arithmetic sequence** is a sequence of numbers such that the difference from any succeeding term to its preceding term remains constant throughout the sequence

An **arithmetic series** is sum of the members of a finite arithmetic sequence


{{< tabs "uniqueid" >}}<br>{{< tab "Standard view" >}}<br><style type="text/css">
#T_2ddf0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2ddf0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_2ddf0_row0_col0, #T_2ddf0_row0_col1, #T_2ddf0_row1_col0, #T_2ddf0_row1_col1, #T_2ddf0_row2_col0, #T_2ddf0_row2_col1, #T_2ddf0_row3_col0, #T_2ddf0_row3_col1 {
  white-space: pre-wrap;
}
</style>
<table id="T_2ddf0">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_2ddf0_level0_col0" class="col_heading level0 col0" >Arithmetic sequence</th>
      <th id="T_2ddf0_level0_col1" class="col_heading level0 col1" >Geometric sequence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_2ddf0_level0_row0" class="row_heading level0 row0" >Recursive definition</th>
      <td id="T_2ddf0_row0_col0" class="data row0 col0" >$ T_n = T_{n-1} + d $</td>
      <td id="T_2ddf0_row0_col1" class="data row0 col1" >$T_n = rT_{n-1}$</td>
    </tr>
    <tr>
      <th id="T_2ddf0_level0_row1" class="row_heading level0 row1" >n-th term</th>
      <td id="T_2ddf0_row1_col0" class="data row1 col0" >$T_n = a + (n-1)d$</td>
      <td id="T_2ddf0_row1_col1" class="data row1 col1" >$T_n = ar^{n-1}$</td>
    </tr>
    <tr>
      <th id="T_2ddf0_level0_row2" class="row_heading level0 row2" >Sum of first n terms</th>
      <td id="T_2ddf0_row2_col0" class="data row2 col0" >$S_n = \dfrac{n}{2}[2a + (n-1)d] = \dfrac{n}{2}(a+l)$</td>
      <td id="T_2ddf0_row2_col1" class="data row2 col1" >$S_n = \dfrac{a(1-r^n)}{1-r} = \dfrac{a(r^n-1)}{r-1},\ \  r \neq 1$</td>
    </tr>
    <tr>
      <th id="T_2ddf0_level0_row3" class="row_heading level0 row3" >Limiting sum</th>
      <td id="T_2ddf0_row3_col0" class="data row3 col0" ></td>
      <td id="T_2ddf0_row3_col1" class="data row3 col1" >$S=\dfrac{a}{1-r},\ \ |r|<1$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}} <br><br>{{< tab "Formula sheet" >}}<br>Items on formula sheet are highlighted <style type="text/css">
#T_a0c69 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_a0c69 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_a0c69_row0_col0, #T_a0c69_row0_col1, #T_a0c69_row3_col0 {
  white-space: pre-wrap;
}
#T_a0c69_row1_col0, #T_a0c69_row1_col1, #T_a0c69_row2_col0, #T_a0c69_row2_col1, #T_a0c69_row3_col1 {
  background-color: rgba(255,194,10, 0.2);
  white-space: pre-wrap;
}
</style>
<table id="T_a0c69">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_a0c69_level0_col0" class="col_heading level0 col0" >Arithmetic sequence</th>
      <th id="T_a0c69_level0_col1" class="col_heading level0 col1" >Geometric sequence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_a0c69_level0_row0" class="row_heading level0 row0" >Recursive definition</th>
      <td id="T_a0c69_row0_col0" class="data row0 col0" >$ T_n = T_{n-1} + d $</td>
      <td id="T_a0c69_row0_col1" class="data row0 col1" >$T_n = rT_{n-1}$</td>
    </tr>
    <tr>
      <th id="T_a0c69_level0_row1" class="row_heading level0 row1" >n-th term</th>
      <td id="T_a0c69_row1_col0" class="data row1 col0" >$T_n = a + (n-1)d$</td>
      <td id="T_a0c69_row1_col1" class="data row1 col1" >$T_n = ar^{n-1}$</td>
    </tr>
    <tr>
      <th id="T_a0c69_level0_row2" class="row_heading level0 row2" >Sum of first n terms</th>
      <td id="T_a0c69_row2_col0" class="data row2 col0" >$S_n = \dfrac{n}{2}[2a + (n-1)d] = \dfrac{n}{2}(a+l)$</td>
      <td id="T_a0c69_row2_col1" class="data row2 col1" >$S_n = \dfrac{a(1-r^n)}{1-r} = \dfrac{a(r^n-1)}{r-1},\ \  r \neq 1$</td>
    </tr>
    <tr>
      <th id="T_a0c69_level0_row3" class="row_heading level0 row3" >Limiting sum</th>
      <td id="T_a0c69_row3_col0" class="data row3 col0" ></td>
      <td id="T_a0c69_row3_col1" class="data row3 col1" >$S=\dfrac{a}{1-r},\ \ |r|<1$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}<br>{{< /tabs >}}

