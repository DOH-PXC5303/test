def add(a: int, b: float) -> float:
    """
    Add an integer and a float

    Parameters
    ----------
    a (int):
        first number to add
    b (float):
        the second number to add

    Returns
    -------
    float
        Sum of both parameters

    Examples
    -------
    ```{python}
    #| echo: false
    {{< include "../_setup.qmd" >}}
    from src.example import add
    ```
    ```{python}
    print(add(3, 0.14))
    ```
    """
    return a + b
