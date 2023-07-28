# Playing with digits

**<https://www.codewars.com/kata/5552101f47fc5178b1000050>**

Difficulty: **6 kyu**

Language: **Python**

# Description:

Some numbers have funny properties. For example:



> 
> 89 --> 8¹ + 9² = 89 \* 1
> 
> 
> 



> 
> 695 --> 6² + 9³ + 5⁴= 1390 = 695 \* 2
> 
> 
> 



> 
> 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51
> 
> 
> 


Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p 


* we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k \* n.


In other words:



> 
> Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n \* k
> 
> 
> 


If it is the case we will return k, if not return -1.


**Note**: n and p will always be given as strictly positive integers.



```
dig\_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
dig\_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
dig\_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
dig\_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
dig\_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
dig\_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
dig\_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
dig\_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
dig\_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
dig\_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
dig\_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
dig\_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
dig\_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
dig\_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
dig\_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
dig\_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
dig\_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
dig\_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
dig\_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
dig\_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
dig\_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
dig\_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
dig\_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
dig\_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digpow 89 1 should return 1 since 8¹ + 9² = 89 = 89 \* 1
digpow 92 1 should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digpow 695 2 should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digpow 46288 3 should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
dig-pow 89 1 should return 1 since 8¹ + 9² = 89 = 89 \* 1
dig-pow 92 1 should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
dig-pow 695 2 should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
dig-pow 46288 3 should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
mov edi, 89
mov esi, 1
call dig_pow  ; EAX <- 1 since 8¹ + 9² = 89 = 89 \* 1

mov edi, 92
mov esi, 1
call dig_pow  ; EAX <- -1 since there is no k such as 9¹ + 2² equals 92 \* k

mov edi, 695
mov esi, 2
call dig_pow  ; EAX <- 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2

mov edi, 46288
mov esi, 3
call dig_pow  ; EAX <- 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
dig\_pow(89, 1) -- should return 1 since 8¹ + 9² = 89 = 89 \* 1
dig\_pow(92, 1) -- should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
dig\_pow(695, 2) -- should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
dig\_pow(46288, 3) -- should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
dig-pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 \* 1
dig-pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 \* k
dig-pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
dig-pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
             DigPow(89, 1) => result = 1
      \* since 8¹ + 9² = 89 = 89 \* 1
             DigPow(92, 1) => result = -1
      \* since there is no k such as 9¹ + 2² equals 92 \* k
             DigPow(695, 2) => result = 2
      \* since since 6² + 9³ + 5⁴= 1390 = 695 \* 2
             DigPow(46288, 3) => result = 51
      \* since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```


```
dig\_pow(89, 1) --> 1 since 8¹ + 9² = 89 = 89 \* 1
dig\_pow(92, 1) --> -1 since there is no k such as 9¹ + 2² equals 92 \* k
dig\_pow(695, 2) --> 2 since 6² + 9³ + 5⁴= 1390 = 695 \* 2
dig\_pow(46288, 3) --> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

```

