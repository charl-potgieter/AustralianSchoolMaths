---
weight: 1
---

{{< tabs "c57a29ec-0fe2-461c-8b95-eb82397c0a2d" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_28c81 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_28c81 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_28c81">
  <thead>
    <tr>
      <th id="T_28c81_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_28c81_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_28c81_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_28c81_row0_col0" class="data row0 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
      <td id="T_28c81_row0_col1" class="data row0 col1" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
      <td id="T_28c81_row0_col2" class="data row0 col2" >When n = -1 follow the integration rules for  $ {\Large\int} \dfrac{f'(x)}{f(x)}dx$</td>
    </tr>
    <tr>
      <td id="T_28c81_row1_col0" class="data row1 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
      <td id="T_28c81_row1_col1" class="data row1 col1" ></td>
      <td id="T_28c81_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_28c81_row2_col0" class="data row2 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
      <td id="T_28c81_row2_col1" class="data row2 col1" ></td>
      <td id="T_28c81_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_28c81_row3_col0" class="data row3 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
      <td id="T_28c81_row3_col1" class="data row3 col1" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
      <td id="T_28c81_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_28c81_row4_col0" class="data row4 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
      <td id="T_28c81_row4_col1" class="data row4 col1" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
      <td id="T_28c81_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_28c81_row5_col0" class="data row5 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
      <td id="T_28c81_row5_col1" class="data row5 col1" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
      <td id="T_28c81_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_28c81_row6_col0" class="data row6 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
      <td id="T_28c81_row6_col1" class="data row6 col1" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
      <td id="T_28c81_row6_col2" class="data row6 col2" ></td>
    </tr>
    <tr>
      <td id="T_28c81_row7_col0" class="data row7 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
      <td id="T_28c81_row7_col1" class="data row7 col1" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
      <td id="T_28c81_row7_col2" class="data row7 col2" >Stictly speaking these integral and derivative formulas are not exact mirrors but are recorded here as presented in the syllabus.  The scope of the derivative equation is limited to positive values of f(x) while the integral equation covers both positive and negative values of f(x).  The derivative equation could also be rewritten with an absolute value.</td>
    </tr>
    <tr>
      <td id="T_28c81_row8_col0" class="data row8 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
      <td id="T_28c81_row8_col1" class="data row8 col1" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
      <td id="T_28c81_row8_col2" class="data row8 col2" >ln a is a constant therefore can be removed from the integral it can go on the other side of the intergral equation when compared to the derivative equation.</td>
    </tr>
    <tr>
      <td id="T_28c81_row9_col0" class="data row9 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
      <td id="T_28c81_row9_col1" class="data row9 col1" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
      <td id="T_28c81_row9_col2" class="data row9 col2" >Is this integral expression correct, in particular the absolute value?</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_2f902 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2f902 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_2f902_row0_col0, #T_2f902_row0_col1, #T_2f902_row1_col0, #T_2f902_row2_col0, #T_2f902_row3_col0, #T_2f902_row3_col1, #T_2f902_row4_col0, #T_2f902_row4_col1, #T_2f902_row5_col0, #T_2f902_row5_col1, #T_2f902_row6_col0, #T_2f902_row6_col1, #T_2f902_row7_col0, #T_2f902_row7_col1, #T_2f902_row8_col0, #T_2f902_row8_col1, #T_2f902_row9_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_2f902_row1_col1, #T_2f902_row2_col1, #T_2f902_row9_col1 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_2f902">
  <thead>
    <tr>
      <th id="T_2f902_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_2f902_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_2f902_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_2f902_row0_col0" class="data row0 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
      <td id="T_2f902_row0_col1" class="data row0 col1" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
      <td id="T_2f902_row0_col2" class="data row0 col2" >When n = -1 follow the integration rules for  $ {\Large\int} \dfrac{f'(x)}{f(x)}dx$</td>
    </tr>
    <tr>
      <td id="T_2f902_row1_col0" class="data row1 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
      <td id="T_2f902_row1_col1" class="data row1 col1" ></td>
      <td id="T_2f902_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_2f902_row2_col0" class="data row2 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
      <td id="T_2f902_row2_col1" class="data row2 col1" ></td>
      <td id="T_2f902_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_2f902_row3_col0" class="data row3 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
      <td id="T_2f902_row3_col1" class="data row3 col1" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
      <td id="T_2f902_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_2f902_row4_col0" class="data row4 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
      <td id="T_2f902_row4_col1" class="data row4 col1" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
      <td id="T_2f902_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_2f902_row5_col0" class="data row5 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
      <td id="T_2f902_row5_col1" class="data row5 col1" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
      <td id="T_2f902_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_2f902_row6_col0" class="data row6 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
      <td id="T_2f902_row6_col1" class="data row6 col1" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
      <td id="T_2f902_row6_col2" class="data row6 col2" ></td>
    </tr>
    <tr>
      <td id="T_2f902_row7_col0" class="data row7 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
      <td id="T_2f902_row7_col1" class="data row7 col1" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
      <td id="T_2f902_row7_col2" class="data row7 col2" >Stictly speaking these integral and derivative formulas are not exact mirrors but are recorded here as presented in the syllabus.  The scope of the derivative equation is limited to positive values of f(x) while the integral equation covers both positive and negative values of f(x).  The derivative equation could also be rewritten with an absolute value.</td>
    </tr>
    <tr>
      <td id="T_2f902_row8_col0" class="data row8 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
      <td id="T_2f902_row8_col1" class="data row8 col1" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
      <td id="T_2f902_row8_col2" class="data row8 col2" >ln a is a constant therefore can be removed from the integral it can go on the other side of the intergral equation when compared to the derivative equation.</td>
    </tr>
    <tr>
      <td id="T_2f902_row9_col0" class="data row9 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
      <td id="T_2f902_row9_col1" class="data row9 col1" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
      <td id="T_2f902_row9_col2" class="data row9 col2" >Is this integral expression correct, in particular the absolute value?</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_6de48 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_6de48 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_6de48_row0_col0, #T_6de48_row1_col0, #T_6de48_row1_col1, #T_6de48_row2_col0, #T_6de48_row2_col1, #T_6de48_row5_col1, #T_6de48_row8_col1, #T_6de48_row9_col1 {
  background-color: rgba(0,0,0,0);
}
#T_6de48_row0_col1, #T_6de48_row3_col0, #T_6de48_row3_col1, #T_6de48_row4_col0, #T_6de48_row4_col1, #T_6de48_row5_col0, #T_6de48_row6_col0, #T_6de48_row6_col1, #T_6de48_row7_col0, #T_6de48_row7_col1, #T_6de48_row8_col0, #T_6de48_row9_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_6de48">
  <thead>
    <tr>
      <th id="T_6de48_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_6de48_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_6de48_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_6de48_row0_col0" class="data row0 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
      <td id="T_6de48_row0_col1" class="data row0 col1" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
      <td id="T_6de48_row0_col2" class="data row0 col2" >When n = -1 follow the integration rules for  $ {\Large\int} \dfrac{f'(x)}{f(x)}dx$</td>
    </tr>
    <tr>
      <td id="T_6de48_row1_col0" class="data row1 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
      <td id="T_6de48_row1_col1" class="data row1 col1" ></td>
      <td id="T_6de48_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_6de48_row2_col0" class="data row2 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
      <td id="T_6de48_row2_col1" class="data row2 col1" ></td>
      <td id="T_6de48_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_6de48_row3_col0" class="data row3 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
      <td id="T_6de48_row3_col1" class="data row3 col1" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
      <td id="T_6de48_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_6de48_row4_col0" class="data row4 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
      <td id="T_6de48_row4_col1" class="data row4 col1" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
      <td id="T_6de48_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_6de48_row5_col0" class="data row5 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
      <td id="T_6de48_row5_col1" class="data row5 col1" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
      <td id="T_6de48_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_6de48_row6_col0" class="data row6 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
      <td id="T_6de48_row6_col1" class="data row6 col1" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
      <td id="T_6de48_row6_col2" class="data row6 col2" ></td>
    </tr>
    <tr>
      <td id="T_6de48_row7_col0" class="data row7 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
      <td id="T_6de48_row7_col1" class="data row7 col1" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
      <td id="T_6de48_row7_col2" class="data row7 col2" >Stictly speaking these integral and derivative formulas are not exact mirrors but are recorded here as presented in the syllabus.  The scope of the derivative equation is limited to positive values of f(x) while the integral equation covers both positive and negative values of f(x).  The derivative equation could also be rewritten with an absolute value.</td>
    </tr>
    <tr>
      <td id="T_6de48_row8_col0" class="data row8 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
      <td id="T_6de48_row8_col1" class="data row8 col1" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
      <td id="T_6de48_row8_col2" class="data row8 col2" >ln a is a constant therefore can be removed from the integral it can go on the other side of the intergral equation when compared to the derivative equation.</td>
    </tr>
    <tr>
      <td id="T_6de48_row9_col0" class="data row9 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
      <td id="T_6de48_row9_col1" class="data row9 col1" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
      <td id="T_6de48_row9_col2" class="data row9 col2" >Is this integral expression correct, in particular the absolute value?</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}