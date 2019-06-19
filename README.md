[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **PythonTsa_call_functions** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: PythonTsa_call_functions

Published in: Quantlet

Description: 'This chapter first introduces the backshift operator which is one way to make a nonstationary time series stationary. It presents the AR, MA and ARMA models and discusses their properties. Also distinguishes the ARMA model from the ARMA process.'

Keywords: ARMA process, LjungBox test, ACF, PACF

Author: Changquan Huang, Maria Culjak

```

### PYTHON Code
```python

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:19:06 2019

@author: mariaculjak

Running LjungBoxtest.py ; plot_acf_pacf.py

Run this command in the terminal while making sure your terminal location is in the same directory as .whl file:
pip install PythonTsa-1.2-py3-none-any.whl

"""

import numpy as np
from PythonTsa.LjungBoxtest import *
from PythonTsa.plot_acf_pacf import *
import statsmodels.tsa.arima_process as arp

ar = np.array([ 1.  , -0.75,  0.25])
ar_process = arp.ArmaProcess(ar=ar,nobs=1000)
sample = ar_process.generate_sample()

acf_pacf_fig(x=sample)
qstatf(x=sample,type="LjungBox", noestimatedcoef=0, nolags=1)
acovf(x=sample, unbiased=False, demean=True, fft=False, missing='none')
plot_LB_pvalue(x=sample, noestimatedcoef=0, nolags=1)
qstatf(x=sample, noestimatedcoef=0, nolags=1, type="LjungBox")

```

automatically created on 2019-06-19