# hypergeometric_distribution_python
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/cyberrumor)

Python implimentation of hypergeometric distribution, for calculating probability without replacement. 

<img src="/screenshot.png">

This differs from other calculators. Instead calcultating the entire result of several factorials (14! is 87178291200) then dividing them by each other, it expands each factorial and compares the numerator to the denominator. It will cancel out what is appropriate (for example: (14!) / (10!) becomes (14 * 13 * 12 * 11) / 1) before multiplication (that equals 24024, btw), which keeps processing speed high and system requirements low. 

Run it from your favorite operating system's CLI with: python hypergeometric_distribution_python
