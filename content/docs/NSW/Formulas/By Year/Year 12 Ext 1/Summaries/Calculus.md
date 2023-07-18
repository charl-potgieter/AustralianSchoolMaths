---
weight: 1
---

{{< tabs "uniqueid" >}}

{{< tab "Standard view" >}}
<style type="text/css">
#T_df4d0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_df4d0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_df4d0_row0_col0, #T_df4d0_row0_col1, #T_df4d0_row1_col0, #T_df4d0_row1_col1, #T_df4d0_row2_col0, #T_df4d0_row2_col1, #T_df4d0_row3_col0, #T_df4d0_row3_col1, #T_df4d0_row4_col0, #T_df4d0_row4_col1, #T_df4d0_row5_col0, #T_df4d0_row5_col1, #T_df4d0_row6_col0, #T_df4d0_row6_col1 {
  width: 400px;
  white-space: pre-wrap;
}
#T_df4d0_row0_col2, #T_df4d0_row1_col2, #T_df4d0_row2_col2, #T_df4d0_row3_col2, #T_df4d0_row4_col2, #T_df4d0_row5_col2, #T_df4d0_row6_col2 {
  width: 600px;
  white-space: pre-wrap;
}
</style>
<table id="T_df4d0">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_df4d0_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_df4d0_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_df4d0_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_df4d0_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_df4d0_row0_col0" class="data row0 col0" >$y=sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_df4d0_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = sin^{-1} f(x) + c$</td>
      <td id="T_df4d0_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <th id="T_df4d0_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_df4d0_row1_col0" class="data row1 col0" >$ y = sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_df4d0_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_df4d0_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <th id="T_df4d0_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_df4d0_row2_col0" class="data row2 col0" >$y=cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_df4d0_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = cos^{-1}f(x) + c \text{ or } -sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_df4d0_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <th id="T_df4d0_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_df4d0_row3_col0" class="data row3 col0" >$y=cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_df4d0_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_df4d0_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <th id="T_df4d0_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_df4d0_row4_col0" class="data row4 col0" >$y=tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_df4d0_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ tan^{-1} f(x) + c$</td>
      <td id="T_df4d0_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <th id="T_df4d0_level0_row5" class="row_heading level0 row5" >5</th>
      <td id="T_df4d0_row5_col0" class="data row5 col0" >$y=tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_df4d0_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_df4d0_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <th id="T_df4d0_level0_row6" class="row_heading level0 row6" >6</th>
      <td id="T_df4d0_row6_col0" class="data row6 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
      <td id="T_df4d0_row6_col1" class="data row6 col1" ></td>
      <td id="T_df4d0_row6_col2" class="data row6 col2" >Formula can be utilised to calculate otherwise hard to differentiate inverse functions</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}Items on formula sheet are highlighted
<br><br><style type="text/css">
#T_035e3 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_035e3 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_035e3_row0_col0, #T_035e3_row1_col1, #T_035e3_row2_col0, #T_035e3_row4_col0, #T_035e3_row5_col1 {
  width: 400px;
  background-color: rgba(255,194,10, 0.2);
  white-space: pre-wrap;
}
#T_035e3_row0_col1, #T_035e3_row1_col0, #T_035e3_row2_col1, #T_035e3_row3_col0, #T_035e3_row3_col1, #T_035e3_row4_col1, #T_035e3_row5_col0, #T_035e3_row6_col0, #T_035e3_row6_col1 {
  width: 400px;
  white-space: pre-wrap;
}
#T_035e3_row0_col2, #T_035e3_row1_col2, #T_035e3_row2_col2, #T_035e3_row3_col2, #T_035e3_row4_col2, #T_035e3_row5_col2, #T_035e3_row6_col2 {
  width: 600px;
  white-space: pre-wrap;
}
</style>
<table id="T_035e3">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_035e3_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_035e3_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_035e3_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_035e3_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_035e3_row0_col0" class="data row0 col0" >$y=sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_035e3_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = sin^{-1} f(x) + c$</td>
      <td id="T_035e3_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <th id="T_035e3_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_035e3_row1_col0" class="data row1 col0" >$ y = sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_035e3_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_035e3_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <th id="T_035e3_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_035e3_row2_col0" class="data row2 col0" >$y=cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_035e3_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = cos^{-1}f(x) + c \text{ or } -sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_035e3_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <th id="T_035e3_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_035e3_row3_col0" class="data row3 col0" >$y=cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_035e3_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_035e3_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <th id="T_035e3_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_035e3_row4_col0" class="data row4 col0" >$y=tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_035e3_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ tan^{-1} f(x) + c$</td>
      <td id="T_035e3_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <th id="T_035e3_level0_row5" class="row_heading level0 row5" >5</th>
      <td id="T_035e3_row5_col0" class="data row5 col0" >$y=tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_035e3_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_035e3_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <th id="T_035e3_level0_row6" class="row_heading level0 row6" >6</th>
      <td id="T_035e3_row6_col0" class="data row6 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
      <td id="T_035e3_row6_col1" class="data row6 col1" ></td>
      <td id="T_035e3_row6_col2" class="data row6 col2" >Formula can be utilised to calculate otherwise hard to differentiate inverse functions</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}