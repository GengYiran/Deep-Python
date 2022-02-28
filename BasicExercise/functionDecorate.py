def func():
	print("abc")

def decorator(func):
	def decoratedFunc():
		print("decoration")
		func()
	return decoratedFunc

decoratedFunc = decorator(func)
decoratedFunc()



def personalizedDecorator()