
## Question 1

<details>
<summary>Sorting and removing duplicates</summary>

The function takes a list of integers as a parameter. This function first sort the elements in ascending order and after that, it removes duplicate elements from the list, keeping the previous order.

### Example:

```
 input: [8, 5, 10, 5, 2, 4, 4, 3]
 output: [2, 3, 4, 5, 8, 10]

```

</details>

## Question 2

<details>
<summary>Checking Sudoku</summary>

The function determines if a Sudoku table is valid, that is, the elements correspond to the rules of the game. These rules are:

1. Each line must contain digits from 1 - 9, WITHOUT repetition;
2. Each column must contain digits from 1 - 9, WITHOUT repetition;
3. All nine mini-tables must contain digits from 1 - 9, WITHOUT repetition;


#### Example:

```
board =
   [["5","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]]

   output: true
```

```
board =
   [["8","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]]

   output: false
```

</details>
