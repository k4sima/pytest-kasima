def test_plugin(pytester):

    pytester.makepyfile(
        """
def test_hello():
    print("hello")

def test_hello2(print_):
    print_("hello")
        """
    )

    res = pytester.runpytest()
