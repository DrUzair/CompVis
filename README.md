# Convolutional Neural Networks

## Edge Detection Filter (Kernel)
### Horizontal / Vertical

### Hand-crafted Vs. Learned
One of the most powerful ideas: to learn the filter as a network parameter

## Issues
* Shrinking the output

* Information loss from the Edge of the image

### Padding

* Valid vs Same Convolutions
Valid ( without padding)

 input $n_h x n_w$
 filter $f x f$ 
 n = n_h = n_w
 input * filter = n - f + 1 $

Same (with Padding)

output = $n + 2p - f + 1$ 

padding $p = \frac{f - 1}{2}$

### Strided Convolutions

input $n_h x n_w$

filter $f x f$

p padding 

s stride

 n = n_h = n_w
 
output floor(\frac{n +2p - f}{s} + 1)

### 3D Convolutions
$n_c$ depth or channels of input matrix (RGB of image)

input $n_h x n_w x n_c$

filter $f x f x n_c$
 
 n = n_h = n_w
 
output = input * filter = $(n - f + 1) x n_c'$

number of filters n_c' 

### 1x1 Convolutions
Dimensionality reduction/increase in filter-space.

### Pooling / Down sampling (Max, Avg)
Reducing the spatial dimension. Applied on each channel/filter of input.
output = ((input - filter)/stride) + 1
## CNN Notation
image height n_h
imgage 

Let $\text{S}_1(N) = \sum_{p=1}^N \text{E}(p)$
