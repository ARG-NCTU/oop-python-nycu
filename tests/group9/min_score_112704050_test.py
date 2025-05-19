import pytest
from min_score_112704050 import path
def test_path():
    n = 4
    roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
    result = path(roads,1,n)
    assert result == 5

    n = 4
    roads = [[1,2,2],[1,3,4],[3,4,7]]
    result = path(roads,1,n)
    assert result == 2