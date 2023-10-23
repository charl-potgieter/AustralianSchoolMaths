---
weight: 10
---

## <span style="color:RGB(0,32,96"> Introduction to Differentiation </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
<style type="text/css">
#T_fcb30 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_fcb30 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_fcb30">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_fcb30_row0_col0" class="data row0 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_fcb30_row1_col0" class="data row1 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_fcb30_row2_col0" class="data row2 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_fcb30_row3_col0" class="data row3 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_fcb30_row4_col0" class="data row4 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_fcb30_row5_col0" class="data row5 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_fcb30_row6_col0" class="data row6 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
  </tbody>
</table>


## <span style="color:RGB(0,32,96"> Differential Calculus </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "a0d7c4d7-9d2d-4c4e-bf8d-308b67f867f0" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_f3bcf th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f3bcf td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_f3bcf">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_f3bcf_row0_col0" class="data row0 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bcf_row1_col0" class="data row1 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bcf_row2_col0" class="data row2 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bcf_row3_col0" class="data row3 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bcf_row4_col0" class="data row4 col0" >$y=sinf(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bcf_row5_col0" class="data row5 col0" >$y=cosf(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bcf_row6_col0" class="data row6 col0" >$y=tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bcf_row7_col0" class="data row7 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bcf_row8_col0" class="data row8 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bcf_row9_col0" class="data row9 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bcf_row10_col0" class="data row10 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_8731e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8731e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_8731e_row0_col0, #T_8731e_row1_col0, #T_8731e_row2_col0, #T_8731e_row3_col0, #T_8731e_row4_col0, #T_8731e_row5_col0, #T_8731e_row6_col0, #T_8731e_row7_col0, #T_8731e_row8_col0, #T_8731e_row9_col0, #T_8731e_row10_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_8731e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_8731e_row0_col0" class="data row0 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_8731e_row1_col0" class="data row1 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_8731e_row2_col0" class="data row2 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_8731e_row3_col0" class="data row3 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_8731e_row4_col0" class="data row4 col0" >$y=sinf(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_8731e_row5_col0" class="data row5 col0" >$y=cosf(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_8731e_row6_col0" class="data row6 col0" >$y=tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_8731e_row7_col0" class="data row7 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_8731e_row8_col0" class="data row8 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_8731e_row9_col0" class="data row9 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_8731e_row10_col0" class="data row10 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Applications of Differentiation </span> 
<br>

## <span style="color:RGB(0,32,96"> Integral Calculus </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "fd68ce99-964c-4c13-b1b5-a8d820f4942b" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_6119f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_6119f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_6119f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_6119f_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_6119f_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_6119f_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_6119f_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)cosf(x)dx = sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_6119f_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)sin f(x)dx = -cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_6119f_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)sec^2 f(x)dx = tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_6119f_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_6119f_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_6119f_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_6119f_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_d8bb2 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d8bb2 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_d8bb2_row0_col0, #T_d8bb2_row1_col0, #T_d8bb2_row2_col0, #T_d8bb2_row3_col0, #T_d8bb2_row4_col0, #T_d8bb2_row5_col0, #T_d8bb2_row6_col0, #T_d8bb2_row7_col0, #T_d8bb2_row8_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_d8bb2_row9_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_d8bb2">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d8bb2_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_d8bb2_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_d8bb2_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_d8bb2_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)cosf(x)dx = sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_d8bb2_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)sin f(x)dx = -cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_d8bb2_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)sec^2 f(x)dx = tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_d8bb2_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_d8bb2_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_d8bb2_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_d8bb2_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Calculus Skills </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "c47056b0-756c-4cc9-8f89-799896f6eb78" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_aa4c6 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_aa4c6 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_aa4c6">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_aa4c6_row0_col0" class="data row0 col0" >$y=sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_aa4c6_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_aa4c6_row2_col0" class="data row2 col0" >$ y = sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_aa4c6_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_aa4c6_row4_col0" class="data row4 col0" >$y=cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_aa4c6_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = cos^{-1}f(x) + c \text{ or } -sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_aa4c6_row6_col0" class="data row6 col0" >$y=cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_aa4c6_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_aa4c6_row8_col0" class="data row8 col0" >$y=tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_aa4c6_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_aa4c6_row10_col0" class="data row10 col0" >$y=tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_aa4c6_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_aa4c6_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_d23f5 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d23f5 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_d23f5_row0_col0, #T_d23f5_row3_col0, #T_d23f5_row4_col0, #T_d23f5_row8_col0, #T_d23f5_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_d23f5_row1_col0, #T_d23f5_row2_col0, #T_d23f5_row5_col0, #T_d23f5_row6_col0, #T_d23f5_row7_col0, #T_d23f5_row9_col0, #T_d23f5_row10_col0, #T_d23f5_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_d23f5">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d23f5_row0_col0" class="data row0 col0" >$y=sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_d23f5_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_d23f5_row2_col0" class="data row2 col0" >$ y = sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_d23f5_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_d23f5_row4_col0" class="data row4 col0" >$y=cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_d23f5_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = cos^{-1}f(x) + c \text{ or } -sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_d23f5_row6_col0" class="data row6 col0" >$y=cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_d23f5_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_d23f5_row8_col0" class="data row8 col0" >$y=tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_d23f5_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_d23f5_row10_col0" class="data row10 col0" >$y=tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_d23f5_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_d23f5_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}


<br>


###  <span style="color:RGB(139,69,19)"> Derivatives vs integrals  </span>
<br>
{{< tabs "5dc86050-af74-4497-abee-b3bffa13fb0b" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_7f6dc th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_7f6dc td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_7f6dc">
  <thead>
    <tr>
      <th id="T_7f6dc_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_7f6dc_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_7f6dc_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_7f6dc_row0_col0" class="data row0 col0" >$y=sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_7f6dc_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = sin^{-1} f(x) + c$</td>
      <td id="T_7f6dc_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f6dc_row1_col0" class="data row1 col0" >$ y = sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_7f6dc_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_7f6dc_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f6dc_row2_col0" class="data row2 col0" >$y=cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_7f6dc_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = cos^{-1}f(x) + c \text{ or } -sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_7f6dc_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f6dc_row3_col0" class="data row3 col0" >$y=cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_7f6dc_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_7f6dc_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f6dc_row4_col0" class="data row4 col0" >$y=tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_7f6dc_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ tan^{-1} f(x) + c$</td>
      <td id="T_7f6dc_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f6dc_row5_col0" class="data row5 col0" >$y=tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_7f6dc_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_7f6dc_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f6dc_row6_col0" class="data row6 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
      <td id="T_7f6dc_row6_col1" class="data row6 col1" ></td>
      <td id="T_7f6dc_row6_col2" class="data row6 col2" >Formula can be utilised to calculate otherwise hard to differentiate inverse functions</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_727c9 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_727c9 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_727c9_row0_col0, #T_727c9_row1_col1, #T_727c9_row2_col0, #T_727c9_row4_col0, #T_727c9_row5_col1 {
  background-color: rgba(255,194,10, 0.2);
}
#T_727c9_row0_col1, #T_727c9_row1_col0, #T_727c9_row2_col1, #T_727c9_row3_col0, #T_727c9_row3_col1, #T_727c9_row4_col1, #T_727c9_row5_col0, #T_727c9_row6_col0, #T_727c9_row6_col1 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_727c9">
  <thead>
    <tr>
      <th id="T_727c9_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_727c9_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_727c9_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_727c9_row0_col0" class="data row0 col0" >$y=sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_727c9_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = sin^{-1} f(x) + c$</td>
      <td id="T_727c9_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_727c9_row1_col0" class="data row1 col0" >$ y = sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_727c9_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_727c9_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_727c9_row2_col0" class="data row2 col0" >$y=cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_727c9_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = cos^{-1}f(x) + c \text{ or } -sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_727c9_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_727c9_row3_col0" class="data row3 col0" >$y=cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_727c9_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_727c9_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_727c9_row4_col0" class="data row4 col0" >$y=tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_727c9_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ tan^{-1} f(x) + c$</td>
      <td id="T_727c9_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_727c9_row5_col0" class="data row5 col0" >$y=tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_727c9_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_727c9_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_727c9_row6_col0" class="data row6 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
      <td id="T_727c9_row6_col1" class="data row6 col1" ></td>
      <td id="T_727c9_row6_col2" class="data row6 col2" >Formula can be utilised to calculate otherwise hard to differentiate inverse functions</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Applications of Calculus </span> 
<br>

## <span style="color:RGB(0,32,96"> Further Integration </span> 
<br>