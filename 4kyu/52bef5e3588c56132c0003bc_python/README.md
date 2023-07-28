# Sort binary tree by levels

**<https://www.codewars.com/kata/52bef5e3588c56132c0003bc>**

Difficulty: **4 kyu**

Language: **Python**

# Description:

You are given a binary tree:



```
class TreeNode
  attr\_accessor :left
  attr\_accessor :right
  attr\_reader :value
end

```


```
data TreeNode a = TreeNode {
  left  :: Maybe (TreeNode a),
  right :: Maybe (TreeNode a),
  value :: a
  } deriving Show

```


```
class Node:
    def \_\_init\_\_(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

```


```
class Node {
    Integer value
    Node left
    Node right

    Node(left, right, value) {
        this.value = value
        this.left = left
        this.right = right
    }
}

```


```
public class Node
{
    public Node Left;
    public Node Right;
    public int Value;
    
    public Node(Node l, Node r, int v)
    {
        Left = l;
        Right = r;
        Value = v;
    }
}

```


```
public class Node {
  public Node left;
  public Node right;
  public int value;
  
  public Node(Node l, Node r, int v) {
    left = l;
    right = r;
    value = v;
  }
}

```


```
class Node { 
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left  = left;
    this.right = right;
  }
}

```


```
# Available in preloaded
# data Tree a = Leaf | Node a Tree Tree
Leaf = \ leaf \_node . leaf
Node = \ v l r . \ \_leaf node . node v l r

```


```
typedef struct Tree {
    struct Tree \*left, \*right;
    int value;
} Tree;

```


```
struct Node {
  value: u32,
  left: Option<Box<Node>>,
  right: Option<Box<Node>>
}

```

Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.


Return empty array if root is `nil`.


Example 1 - following tree:



```
                 2
            8        9
          1  3     4   5

```

Should return following list:



```
[2,8,9,1,3,4,5]

```

Example 2 - following tree:



```
                 1
            8        4
              3        5
                         7

```

Should return following list:



```
[1,8,4,3,5,7]

```

