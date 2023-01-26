import rich  # インストールされてる前提
from pytest import Pytester, raises


def test_plugin_simple(pytester: Pytester):

    pytester.makepyfile(
        """
def test_hello():
    print("print_hello")
        """
    )

    res = pytester.runpytest("--kasima-skip").stdout.str()
    # print(res)
    assert "--- test_hello ---" not in res
    assert "print_hello" not in res

    res = pytester.runpytest("--kasima-rich-skip").stdout.str()
    # print(res)
    assert "--- test_hello ---" in res
    assert "print_hello" in res


def test_plugin_rich(pytester: Pytester):

    pytester.makepyfile(
        """
def test_hello():
    print("[red]print_hello")
        """
    )

    res = pytester.runpytest().stdout.str()
    # print(res)
    assert "--- test_hello ---" not in res
    assert "[red]" not in res  # マークアップされる為
