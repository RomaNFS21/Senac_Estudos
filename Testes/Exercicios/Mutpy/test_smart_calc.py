from smart_calc import lcm
from smart_calc import hcf
from smart_calc import add
from smart_calc import sub
from smart_calc import mul
from smart_calc import div
from smart_calc import mod
from smart_calc import end
from smart_calc import myname
from smart_calc import sorry
from smart_calc import extract_from_text


def test_add():
  assert add(12,13) == 25


def test_sub():
  assert sub(12,13) == 1


def test_mul():
  assert mul(12,13) == 156


def test_div():
  assert div(12,2) == 6


def test_mod():
  assert mod(12,1) == 0