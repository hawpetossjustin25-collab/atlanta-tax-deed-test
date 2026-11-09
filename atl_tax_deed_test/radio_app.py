"""Stand-alone Atlanta radio player (same stations and saved choice as the radio bar in the test)."""
from __future__ import annotations

import sys
from pathlib import Path

from PyQt6.QtCore import QPointF, QRectF, Qt
from PyQt6.QtGui import QColor, QFont, QIcon, QImage, QPainter, QPen, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

from atl_tax_deed_test.app import default_data_dir
from atl_tax_deed_test.radio import STATIONS
from atl_tax_deed_test.radio_widget import RadioWidget

TITLE = "Atlanta Radio"


def draw_icon(size: int = 256) -> QImage:
    img = QImage(size, size, QImage.Format.Format_ARGB32)
    img.fill(Qt.GlobalColor.transparent)
    p = QPainter(img)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    s = size / 256
    p.setPen(QPen(QColor("#e0e0e0"), 10 * s))
    p.drawLine(QPointF(70 * s, 90 * s), QPointF(190 * s, 30 * s))  # antenna
    p.setPen(Qt.PenStyle.NoPen)
    p.setBrush(QColor("#1f8a4c"))
    p.drawRoundedRect(QRectF(16 * s, 80 * s, 224 * s, 150 * s), 28 * s, 28 * s)
    p.setBrush(QColor("#1e1e1e"))
    p.drawEllipse(QPointF(90 * s, 155 * s), 48 * s, 48 * s)  # speaker
    p.setBrush(QColor("#3cc47c"))
    p.drawEllipse(QPointF(90 * s, 155 * s), 18 * s, 18 * s)
    p.setBrush(QColor("#e0e0e0"))
    for i in range(3):
        p.drawRoundedRect(QRectF(160 * s, (115 + i * 30) * s, 56 * s, 14 * s), 6 * s, 6 * s)
    p.end()
    return img


def write_icon(path: Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not draw_icon().save(str(path)):
        raise OSError(f"could not write icon {path}")
    return path


class RadioWindow(QMainWindow):
    def __init__(self, data_dir: Path | None = None):
        super().__init__()
        self.data_dir = Path(data_dir) if data_dir else default_data_dir()
        self.setWindowTitle(TITLE)
        self.setWindowIcon(QIcon(QPixmap.fromImage(draw_icon(64))))
        self.setStyleSheet("QMainWindow, QWidget { background: #1e1e1e; color: #e0e0e0; font-size: 14px; }"
                           "QPushButton { background: #1f8a4c; color: white; border: none; border-radius: 6px;"
                           " padding: 8px; font-weight: bold; } QPushButton:hover { background: #28a745; }"
                           "QComboBox { background: #333; border: 1px solid #555; padding: 6px; }")
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(16, 16, 16, 16)
        title = QLabel(TITLE)
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: #3cc47c;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        lineup = QLabel("\n".join(f"{s.name}  -  {s.dial}  -  {s.genre}" for s in STATIONS))
        lineup.setStyleSheet("color: #aaa;")
        lineup.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lineup)
        self.radio = RadioWidget(self.data_dir / "radio.json")
        layout.addWidget(self.radio)
        self.resize(760, 220)

    def closeEvent(self, event):
        self.radio.shutdown()
        super().closeEvent(event)


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv if argv is None else argv
    app = QApplication.instance() or QApplication(argv)
    if len(argv) > 2 and argv[1] == "--make-icon":
        print(write_icon(Path(argv[2])))
        return 0
    window = RadioWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
