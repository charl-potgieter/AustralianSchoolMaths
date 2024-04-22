---
weight: 1
---

{{< tabs "06603a9f-cbdb-4e60-9038-03c45d610e6c" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_33730 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_33730 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_33730">
  <thead>
    <tr>
      <th id="T_33730_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_33730_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_33730_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_33730_row0_col0" class="data row0 col0" ></td>
      <td id="T_33730_row0_col1" class="data row0 col1" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
      <td id="T_33730_row0_col2" class="data row0 col2" >When n = -1 follow the integration rules for  $ {\Large\int} \dfrac{f'(x)}{f(x)}dx$</td>
    </tr>
    <tr>
      <td id="T_33730_row1_col0" class="data row1 col0" ></td>
      <td id="T_33730_row1_col1" class="data row1 col1" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
      <td id="T_33730_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_33730_row2_col0" class="data row2 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
      <td id="T_33730_row2_col1" class="data row2 col1" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
      <td id="T_33730_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_33730_row3_col0" class="data row3 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
      <td id="T_33730_row3_col1" class="data row3 col1" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
      <td id="T_33730_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_33730_row4_col0" class="data row4 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
      <td id="T_33730_row4_col1" class="data row4 col1" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
      <td id="T_33730_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_33730_row5_col0" class="data row5 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
      <td id="T_33730_row5_col1" class="data row5 col1" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
      <td id="T_33730_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_33730_row6_col0" class="data row6 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
      <td id="T_33730_row6_col1" class="data row6 col1" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
      <td id="T_33730_row6_col2" class="data row6 col2" >Why absolute value?</td>
    </tr>
    <tr>
      <td id="T_33730_row7_col0" class="data row7 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
      <td id="T_33730_row7_col1" class="data row7 col1" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
      <td id="T_33730_row7_col2" class="data row7 col2" >ln a is a constant therefore can be removed from the integral it can go on the other side of the intergral equation when compared to the derivative equation.</td>
    </tr>
    <tr>
      <td id="T_33730_row8_col0" class="data row8 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
      <td id="T_33730_row8_col1" class="data row8 col1" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
      <td id="T_33730_row8_col2" class="data row8 col2" >Is this integral expression correct, in particular the absolute value?</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_7f123 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_7f123 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_7f123_row0_col0, #T_7f123_row1_col0, #T_7f123_row8_col1 {
  background-color: rgba(0,0,0,0);
}
#T_7f123_row0_col1, #T_7f123_row1_col1, #T_7f123_row2_col0, #T_7f123_row2_col1, #T_7f123_row3_col0, #T_7f123_row3_col1, #T_7f123_row4_col0, #T_7f123_row4_col1, #T_7f123_row5_col0, #T_7f123_row5_col1, #T_7f123_row6_col0, #T_7f123_row6_col1, #T_7f123_row7_col0, #T_7f123_row7_col1, #T_7f123_row8_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_7f123">
  <thead>
    <tr>
      <th id="T_7f123_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_7f123_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_7f123_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_7f123_row0_col0" class="data row0 col0" ></td>
      <td id="T_7f123_row0_col1" class="data row0 col1" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
      <td id="T_7f123_row0_col2" class="data row0 col2" >When n = -1 follow the integration rules for  $ {\Large\int} \dfrac{f'(x)}{f(x)}dx$</td>
    </tr>
    <tr>
      <td id="T_7f123_row1_col0" class="data row1 col0" ></td>
      <td id="T_7f123_row1_col1" class="data row1 col1" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
      <td id="T_7f123_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f123_row2_col0" class="data row2 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
      <td id="T_7f123_row2_col1" class="data row2 col1" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
      <td id="T_7f123_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f123_row3_col0" class="data row3 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
      <td id="T_7f123_row3_col1" class="data row3 col1" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
      <td id="T_7f123_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f123_row4_col0" class="data row4 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
      <td id="T_7f123_row4_col1" class="data row4 col1" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
      <td id="T_7f123_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f123_row5_col0" class="data row5 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
      <td id="T_7f123_row5_col1" class="data row5 col1" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
      <td id="T_7f123_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_7f123_row6_col0" class="data row6 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
      <td id="T_7f123_row6_col1" class="data row6 col1" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
      <td id="T_7f123_row6_col2" class="data row6 col2" >Why absolute value?</td>
    </tr>
    <tr>
      <td id="T_7f123_row7_col0" class="data row7 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
      <td id="T_7f123_row7_col1" class="data row7 col1" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
      <td id="T_7f123_row7_col2" class="data row7 col2" >ln a is a constant therefore can be removed from the integral it can go on the other side of the intergral equation when compared to the derivative equation.</td>
    </tr>
    <tr>
      <td id="T_7f123_row8_col0" class="data row8 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
      <td id="T_7f123_row8_col1" class="data row8 col1" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
      <td id="T_7f123_row8_col2" class="data row8 col2" >Is this integral expression correct, in particular the absolute value?</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_733aa th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_733aa td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_733aa_row0_col0, #T_733aa_row0_col1, #T_733aa_row1_col0, #T_733aa_row1_col1, #T_733aa_row2_col1, #T_733aa_row3_col1, #T_733aa_row4_col1, #T_733aa_row5_col1, #T_733aa_row6_col1, #T_733aa_row7_col1, #T_733aa_row8_col1 {
  background-color: rgba(0,0,0,0);
}
#T_733aa_row2_col0, #T_733aa_row3_col0, #T_733aa_row4_col0, #T_733aa_row5_col0, #T_733aa_row6_col0, #T_733aa_row7_col0, #T_733aa_row8_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_733aa">
  <thead>
    <tr>
      <th id="T_733aa_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_733aa_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_733aa_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_733aa_row0_col0" class="data row0 col0" ></td>
      <td id="T_733aa_row0_col1" class="data row0 col1" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
      <td id="T_733aa_row0_col2" class="data row0 col2" >When n = -1 follow the integration rules for  $ {\Large\int} \dfrac{f'(x)}{f(x)}dx$</td>
    </tr>
    <tr>
      <td id="T_733aa_row1_col0" class="data row1 col0" ></td>
      <td id="T_733aa_row1_col1" class="data row1 col1" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
      <td id="T_733aa_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_733aa_row2_col0" class="data row2 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
      <td id="T_733aa_row2_col1" class="data row2 col1" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
      <td id="T_733aa_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_733aa_row3_col0" class="data row3 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
      <td id="T_733aa_row3_col1" class="data row3 col1" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
      <td id="T_733aa_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_733aa_row4_col0" class="data row4 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
      <td id="T_733aa_row4_col1" class="data row4 col1" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
      <td id="T_733aa_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_733aa_row5_col0" class="data row5 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
      <td id="T_733aa_row5_col1" class="data row5 col1" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
      <td id="T_733aa_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_733aa_row6_col0" class="data row6 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
      <td id="T_733aa_row6_col1" class="data row6 col1" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
      <td id="T_733aa_row6_col2" class="data row6 col2" >Why absolute value?</td>
    </tr>
    <tr>
      <td id="T_733aa_row7_col0" class="data row7 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
      <td id="T_733aa_row7_col1" class="data row7 col1" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
      <td id="T_733aa_row7_col2" class="data row7 col2" >ln a is a constant therefore can be removed from the integral it can go on the other side of the intergral equation when compared to the derivative equation.</td>
    </tr>
    <tr>
      <td id="T_733aa_row8_col0" class="data row8 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
      <td id="T_733aa_row8_col1" class="data row8 col1" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
      <td id="T_733aa_row8_col2" class="data row8 col2" >Is this integral expression correct, in particular the absolute value?</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}