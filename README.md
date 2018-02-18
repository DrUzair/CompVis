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

$n x n * f x f = n - f + 1 $

Same (with Padding)

$n + 2p - f + 1$ 

padding $p = \frac{f - 1}{2}$

### Strided Convolutions
n x n input

f x f filter

p padding 

s stride

floor(\frac{n +2p - f}{s} + 1)
