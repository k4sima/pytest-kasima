from shutil import get_terminal_size

from pytest import CaptureFixture, FixtureRequest, Parser, fixture, hookimpl


# ---------------------------------- printer --------------------------------- #
class NormalPrinter:
    option = [
        (
            ("--kasima-skip",),
            {"action": "store_true", "help": "pytest-kasima を無効にする"},
        )
    ]

    print = print

    @staticmethod
    def rule(t: str = ""):
        _pad = "-"
        _term_width = get_terminal_size()[0]  # ターミナルの幅
        print(f"\n{t:{_pad}^{_term_width}}")


printer: type[NormalPrinter] = NormalPrinter

try:

    class RichPrinter(NormalPrinter):
        option = NormalPrinter.option + [
            (
                ("--kasima-rich-skip",),
                {"action": "store_true", "help": "rich を使った出力を無効にする"},
            )
        ]

        from rich import print
        from rich.rule import Rule as _Rule

        @staticmethod
        def rule(t: str = ""):
            RichPrinter.print(RichPrinter._Rule(title=t))

    printer = RichPrinter

except ImportError:
    pass
# ---------------------------------------------------------------------------- #


def pytest_addoption(parser: Parser):
    """オプション追加"""
    group = parser.getgroup("kasima")
    for a, k in printer.option:
        group.addoption(*a, **k)


@fixture()
def pretty_print(request: FixtureRequest):
    """printの出力を見やすくする"""
    global printer

    p = (
        NormalPrinter
        if request.config.getoption("--kasima-rich-skip", default=False)
        else printer
    )

    def _print(*a, **k):
        print()  # OPTIMIZE: ファイル名 の横に出力されるから改行
        p.rule(f" {request.node.name} ")
        p.print(*a, **k)
        p.rule()
        print()

    yield _print


@fixture(autouse=True)
def printcap(request: FixtureRequest, capsys: CaptureFixture, pretty_print):
    """captureされた出力をpretty_print"""

    yield

    if not request.config.getoption("--kasima-skip"):
        with capsys.disabled():
            pretty_print(capsys.readouterr().out)


"""
@hookimpl(trylast=True)
def pytest_configure(config):
    pass
"""
