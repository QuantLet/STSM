#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:19:06 2019

@author: mariaculjak

LjungBoxtest.py ; plot_acf_pacf.py

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
