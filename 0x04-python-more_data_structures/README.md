# More Data Structures: Set, Dictionary
Another data structures in python `set` and `dictionaries` project, each file represents separate task

<details>
<summary><b>0-square_matrix_simple</b></summary>
python program to that returns a new 2d matrix of each element squared
</details>
<hr />
<details>
<summary><b>1-search_replace</b></summary>
python program that replaces all occurrences of an element by another in a new list.
</details>
<hr />
<details>
<summary><b>2-uniq_add</b></summary>
python program that adds all unique integers in a list (only once for each integer).
</details>
<hr />
<details>
<summary><b>3-common_elements</b></summary>
python program that returns a set of common elements in two sets.
</details>
<hr />
<details>
<summary><b>4-only_diff_elements</b></summary>
python program that returns a set of all elements present in only one set.
</details>
<hr />
<details>
<summary><b>5-number_keys</b></summary>
python program that returns number of keys in a dictionary
</details>
<hr />
<details>
<summary><b>6-print_sorted_dictionary</b></summary>
python program that prints a dictionary by ordered keys.
</details>
<hr />
<details>
<summary><b>7-update_dictionary</b></summary>
python program that replaces or adds key/value in a dictionary.
</details>
<hr />
<details>
<summary><b>8-simple_delete</b></summary>
python program that deletes a key in a dictionary.
</details>
<hr />
<details>
<summary><b>9-multiply_by_2</b></summary>
python program that returns a new dictionary with all values multiplied by 2
</details>
<hr />
<details>
<summary><b>10-best_score</b></summary>
python program that returns a key with the biggest integer value.
</details>
<hr />
<details>
<summary><b>11-multiply_list_map</b></summary>
python program that returns a list with all values multiplied by a number without using any loops.
</details>
<hr />
<details>
<summary><b>12-roman_to_int</b></summary>
python program that converts a Roman numeral to an integer.<br />
Numbers are written with combinations of letters from the Latin alphabet,
each letter with a fixed integer value. Modern style uses only these seven:

| I | V | X | L | C | D | M |
|---|---|---|---|---|---|---|
| 1 | 5 |10 |50 |100|500|1000|
</details>
<hr />
<details>
<summary><b>100-weight_average</b></summary>
python program that returns the weighted average of all integers tuple (<score>, <weight>)
</details>
<hr />
<details>
<summary><b>101-square_matrix_map</b></summary>
python program that computes the square value of all integers of a matrix using map
</details>
<hr />
<details>
<summary><b>102-complex_delete</b></summary>
python program that deletes keys with a specific value in a dictionary.
</details>
<hr />
<details>
<summary><b>103-python.c</b></summary>
c program that extracts some basic info about Python lists and Python bytes objects.<br />

- `PyBytesObject` :
```
typedef struct {
    PyObject_VAR_HEAD
    Py_hash_t ob_shash;
    char ob_sval[1];

    /* Invariants:
     *     ob_sval contains space for 'ob_size+1' elements.
     *     ob_sval[ob_size] == 0.
     *     ob_shash is the hash of the byte string or -1 if not computed yet.
     */
} PyBytesObject;

```
- `PyListObject` :
```
typedef struct {
    PyObject_VAR_HEAD
    /* Vector of pointers to list elements.  list[0] is ob_item[0], etc. */
    PyObject **ob_item;

    /* ob_item contains space for 'allocated' elements.  The number
     * currently in use is ob_size.
     * Invariants:
     *     0 <= ob_size <= allocated
     *     len(list) == ob_size
     *     ob_item == NULL implies ob_size == allocated == 0
     * list.sort() temporarily sets allocated to -1 to detect mutations.
     *
     * Items must normally not be NULL, except during construction when
     * the list is not yet visible outside the function that builds it.
     */
    Py_ssize_t allocated;
} PyListObject;
```
__*Both of the above objects inherits from `PyObject`*__ : <br />
```
/* Nothing is actually declared to be a PyObject, but every pointer to
 * a Python object can be cast to a PyObject*.  This is inheritance built
 * by hand.  Similarly every pointer to a variable-size Python object can,
 * in addition, be cast to PyVarObject*.
 */
typedef struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    PyTypeObject *ob_type;
} PyObject;
```
</details>
