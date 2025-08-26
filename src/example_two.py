def change_sign(a: int, b: float) -> float:
    """
    Add an integer and a float and change the sign

    Parameters
    ----------
    a (int):
        first number to add
    b (float):
        the second number to add

    Returns
    -------
    float
        Sum of both parameters with results sign changed

    Examples
    -------
    ```{python}
    #| echo: false
    {{< include "../_setup.qmd" >}}
    from src.example_two import change_sign
    ```
    ```{python}
    print(change_sign(3, 0.14))
    ```
    """
    return (a + b) * -1


def subtract(a: int, b: float) -> float:
    """
    Add an integer and a float

    Parameters
    ----------
    a (int):
        first number to sub
    b (float):
        the second number to sub

    Returns
    -------
    float
        Difference of numbers

    Examples
    -------
    ```{python}
    #| echo: false
    {{< include "../_setup.qmd" >}}
    from src.example_two import subtract
    ```
    ```{python}
    print(subtract(3, 0.14))
    ```
    """
    return a - b
