import os

import pytest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
QtWidgets = pytest.importorskip("PyQt6.QtWidgets")

from PyQt6.QtGui import QImage  # noqa: E402

from atl_tax_deed_test.radio import STATIONS  # noqa: E402
from atl_tax_deed_test.radio_app import RadioWindow, draw_icon, main, write_icon  # noqa: E402


@pytest.fixture(scope="module")
def qapp():
    return QtWidgets.QApplication.instance() or QtWidgets.QApplication([])


def test_window_has_only_the_radio(qapp, tmp_path):
    w = RadioWindow(data_dir=tmp_path)
    assert w.windowTitle() == "Atlanta Radio"
    assert w.radio.combo.count() == len(STATIONS)
    w.radio.step(1)
    w.close()
    assert RadioWindow(data_dir=tmp_path).radio.state.index == 1  # shares saved choice


def test_icon_is_drawn_and_saved_as_ico(qapp, tmp_path):
    img = draw_icon(64)
    assert img.width() == 64 and img.pixelColor(32, 40).alpha() > 0
    path = write_icon(tmp_path / "radio.ico")
    assert path.stat().st_size > 1000 and not QImage(str(path)).isNull()


def test_make_icon_command(qapp, tmp_path, capsys):
    out = tmp_path / "x" / "radio.ico"
    assert main(["radio", "--make-icon", str(out)]) == 0
    assert out.exists() and str(out) in capsys.readouterr().out
