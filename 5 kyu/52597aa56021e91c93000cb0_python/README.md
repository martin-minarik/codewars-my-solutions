# Moving Zeros To The End

**<https://www.codewars.com/kata/52597aa56021e91c93000cb0>**

Difficulty: **5 kyu**

Language: **Python**

# Description:

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.



```
moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

```


```
moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

```


```
move\_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

```


```
move\_zeros({1, 0, 1, 2, 0, 1, 3}) // returns {1, 1, 2, 1, 3, 0, 0}

```


```
moveZeros [false,1,0,1,2,0,1,3,"a"] # returns[false,1,1,2,1,3,"a",0,0]

```


```
Kata.MoveZeroes(new int[] {1, 2, 0, 1, 0, 1, 0, 3, 0, 1}) => new int[] {1, 2, 1, 1, 3, 1, 0, 0, 0, 0}

```


```
MoveZeros([]int{1, 2, 0, 1, 0, 1, 0, 3, 0, 1}) // returns []int{ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 }

```


```
moveZeros [1,2,0,1,0,1,0,3,0,1] -> [1,2,1,1,3,1,0,0,0,0]

```


```
{ 1 2 0 1 0 1 0 3 0 1 } move-zeros -> { 1 2 1 1 3 1 0 0 0 0 }

```


```
moveZeros [1,2,0,1,0,1,0,3,0,1] #-> [1,2,1,1,3,1,0,0,0,0]

```


```
move\_zeros(10, int [] {1, 2, 0, 1, 0, 1, 0, 3, 0, 1}); // -> int [] {1, 2, 1, 1, 3, 1, 0, 0, 0, 0}

```


```
moveZeroes(List(1, 0, 1, 2, 0, 1, 3)) // -> List(1, 1, 2, 1, 3, 0, 0)

```


```
"1012013\0"   -->   "1121300"

```

