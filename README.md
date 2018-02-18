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

input $n x n$
filter $f x f$ 

input * filter = n - f + 1 $

Same (with Padding)

output = $n + 2p - f + 1$ 

padding $p = \frac{f - 1}{2}$

### Strided Convolutions

input $n x n$

filter $f x f$

p padding 

s stride

output floor(\frac{n +2p - f}{s} + 1)

### 3D Convolutions
$n_c$ depth or channels of input matrix (RGB of image)

input $n x n x n_c$

filter $f x f x n_c$

output = input * filter = $(n - f + 1) x n_c'$

number of filters n_c' 
