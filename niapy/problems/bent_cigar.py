# encoding=utf8

"""Implementations of Bent Cigar functions."""
import numpy as np

from niapy.problems.problem import Problem

__all__ = ['BentCigar']


class BentCigar(Problem):
    r"""Implementations of Bent Cigar functions.

    Date: 2018

    Author: Klemen Berkovič

    License: MIT

    Function:
    **Bent Cigar Function**

        :math:`f(\textbf{x}) = x_1^2 + 10^6 \sum_{i=2}^D x_i^2`

        **Input domain:**
        The function can be defined on any input domain but it is usually
        evaluated on the hypercube :math:`x_i ∈ [-100, 100]`, for all :math:`i = 1, 2,..., D`.

        **Global minimum:**
        :math:`f(x^*) = 0`, at :math:`x^* = (0,...,0)`

    LaTeX formats:
        Inline:
            $f(\textbf{x}) = x_1^2 + 10^6 \sum_{i=2}^D x_i^2$

        Equation:
            \begin{equation} f(\textbf{x}) = x_1^2 + 10^6 \sum_{i=2}^D x_i^2 \end{equation}

        Domain:
            $-100 \leq x_i \leq 100$

    Reference:
        http://www5.zzu.edu.cn/__local/A/69/BC/D3B5DFE94CD2574B38AD7CD1D12_C802DAFE_BC0C0.pdf

    """

    def __init__(self, dimension=4, lower=-100.0, upper=100.0, *args, **kwargs):
        r"""Initialize Bent Cigar problem..

        Args:
            dimension (Optional[int]): Dimension of the problem.
            lower (Optional[Union[float, Iterable[float]]]): Lower bounds of the problem.
            upper (Optional[Union[float, Iterable[float]]]): Upper bounds of the problem.

        See Also:
            :func:`niapy.problems.Problem.__init__`

        """
        super().__init__(dimension, lower, upper, *args, **kwargs)

    @staticmethod
    def latex_code():
        r"""Return the latex code of the problem.

        Returns:
            str: Latex code.

        """
        return r'''$f(\textbf{x}) = x_1^2 + 10^6 \sum_{i=2}^D x_i^2$'''

    def _evaluate(self, x):
        return x[0] ** 2 + 1000000 * np.sum(np.square(x[1:]))
