from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 50
	assert simple_work_calc(20, 3, 2) == 50
	assert simple_work_calc(30, 4, 2) == 124

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 50
	assert work_calc(20, 1, 2, lambda n: n*n) == 800
	assert work_calc(30, 3, 2, lambda n: n) == 270


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
	work_fn1 = work_calc(10, 2, 2, lambda n: 1)
	work_fn2 = work_calc(10, 2, 2, lambda n: n)
	res = compare_work(work_fn1, work_fn2)
	print(res)

	
def test_compare_span():
	span_fn1 = span_calc(10, 2, 2, lambda n: 1)
	span_fn2 = span_calc(10, 2, 2, lambda n: n)
	res = compare_span(span_fn1, span_fn2)
	print(res)
