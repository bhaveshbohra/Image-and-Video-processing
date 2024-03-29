# -*- coding: utf-8 -*-
"""IVPAssignment_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/104DtwgDCKFRKhvQThyLK0Lbhv6S8VFNC

## Question 1
"""

from google.colab import files
files.upload()

"""### Ideal Low Pass FIlter"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open("/content/q1.png")
img_ar = np.array(img)
img_ar_fq = np.fft.fft2(img_ar)
img_ar_fq = np.fft.fftshift(img_ar_fq)
M,N = img_ar.shape[0],img_ar.shape[1]
low_pass_mask = np.zeros([M,N],dtype = np.float32)
D0 = 20
u_centre,v_centre = M/2,N/2
for i in range(M):
  for j in range(N):
    D_uv = np.sqrt((i-u_centre)**2 + (j-u_centre)**2)
    if D_uv <= D0:
      low_pass_mask[i][j] = 1
    else:
      low_pass_mask[i][j] = 0
img_ar_fil = np.multiply(img_ar_fq,low_pass_mask)
img_res = np.fft.ifftshift(img_ar_fil)
img_res = np.abs(np.fft.ifft2(img_ar_fil))
img_res = Image.fromarray(img_res)
img_res = img_res.convert("L")
img_res
#fig = plt.figure(figsize=(30,10))
#ax  = fig.add_subplot(1,2,1)
#ax.imshow(img_res,cmap="gray")

"""### Ideal High Pass Filter"""

high_pass_mask = np.zeros([M,N],dtype = np.float32)
D0 = 60
u_centre,v_centre = M/2,N/2
for i in range(M):
  for j in range(N):
    D_uv = np.sqrt((i-u_centre)**2 + (j-u_centre)**2)
    if D_uv <= D0:
      high_pass_mask[i][j] = 0
    else:
      high_pass_mask[i][j] = 1
img_ar_fil = np.multiply(img_ar_fq,high_pass_mask)
img_res = np.fft.ifftshift(img_ar_fil)
img_res = np.abs(np.fft.ifft2(img_ar_fil))
img_res = Image.fromarray(img_res)
img_res = img_res.convert("L")
img_res

"""## Question 2

### Low Pass Butterworth
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open("q2.pgm")
img_ar = np.array(img)
img_ar_fq = np.fft.fft2(img_ar)
img_ar_fq = np.fft.fftshift(img_ar_fq)
M,N = img_ar.shape[0],img_ar.shape[1]
low_pass_butter = np.zeros([M,N],dtype = np.float32)
D0 = 20
n = 5
u_centre,v_centre = M/2,N/2
for i in range(M):
  for j in range(N):
    D_uv = np.sqrt((i-u_centre)**2 + (j-u_centre)**2)
    low_pass_butter[i][j] = 1/(1 +(D_uv/D0)** 2*n)
plt.imshow(low_pass_butter,cmap='gray')
img_ar_fil = np.multiply(img_ar_fq,low_pass_butter)
img_res = np.fft.ifftshift(img_ar_fil)
img_res = np.abs(np.fft.ifft2(img_ar_fil))
img_res = Image.fromarray(img_res)
img_res = img_res.convert("L")
img_res

"""### Low Pass Gaussian"""

from math import exp
low_pass_gaussian = np.zeros([M,N],dtype = np.float32)
D0 = 10
n = 5
u_centre,v_centre = M/2,N/2
for i in range(M):
  for j in range(N):
    D_uv = np.sqrt((i-u_centre)**2 + (j-u_centre)**2)
    low_pass_gaussian[i][j] = exp(-(D_uv/(2*D0)))
plt.imshow(low_pass_gaussian,cmap='gray')
img_ar_fil = np.multiply(img_ar_fq,low_pass_gaussian)
img_res = np.fft.ifftshift(img_ar_fil)
img_res = np.abs(np.fft.ifft2(img_ar_fil))
img_res = Image.fromarray(img_res)
img_res = img_res.convert("L")
img_res

"""## Question 3

### High Pass ButterWorth
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open("q3.pgm")
img_ar = np.array(img)
img_ar_fq = np.fft.fft2(img_ar)
img_ar_fq = np.fft.fftshift(img_ar_fq)
M,N = img_ar.shape[0],img_ar.shape[1]
high_pass_butter = np.zeros([M,N],dtype = np.float32)
D0 = 15
n = 2
u_centre,v_centre = M/2,N/2
for i in range(M):
  for j in range(N):
    D_uv = np.sqrt((i-u_centre)**2 + (j-u_centre)**2)
    high_pass_butter[i][j] = 1/(1 +(D0/D_uv)** 2*n)
plt.imshow(high_pass_butter,cmap='gray')
img_ar_fil = np.multiply(img_ar_fq,high_pass_butter)
img_res = np.fft.ifftshift(img_ar_fil)
img_res = np.abs(np.fft.ifft2(img_ar_fil))
img_res = Image.fromarray(img_res)
img_res = img_res.convert("L")
img_res

"""### High Pass Gaussian"""

from math import exp
high_pass_gaussian = np.zeros([M,N],dtype = np.float32)
D0 = 20
u_centre,v_centre = M/2,N/2
for i in range(M):
  for j in range(N):
    D_uv = np.sqrt((i-u_centre)**2 + (j-u_centre)**2)
    high_pass_gaussian[i][j] = 1-exp(-(D_uv/(2*D0)))
plt.imshow(high_pass_gaussian,cmap='gray')
img_ar_fil = np.multiply(img_ar_fq,high_pass_gaussian)
img_res = np.fft.ifftshift(img_ar_fil)
img_res = np.abs(np.fft.ifft2(img_ar_fil))
img_res = Image.fromarray(img_res)
img_res = img_res.convert("L")
img_res