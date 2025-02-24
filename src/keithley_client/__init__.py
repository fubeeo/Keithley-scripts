"""
Fabio - 2025

Keithley SMU client
"""

import argparse
import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication

from keithley_client.gui.MainWindow import MainWindow

__version__ = "0.1.0"
__author__ = "Fabio"

win_title = f"Keithley SMU client {__version__} - {__author__}"

SMU_config = {
    "g": "a",
    "d": "b",
}


def config_pyqtgraph():
    """
    PyQtGraph configuration
    """
    pg.setConfigOptions(background="w", foreground="k", leftButtonPan=False)


def cli():
    """
    # Command line interface

    ## Usage

    `keithley_client [--idvd] [--idvg] [--time] [--help] [--version]`

    ## Options

    The default behavior is to show an interface that lets the user choose the type of measurement to perform.

    The following options can be used to show a specific interface:

    `--idvg`: show the transfer curve interface

    `--idvd`: show the output curve interface

    `--time`: show the time response interface

    `--version`: show the version of the program
    """

    parser = argparse.ArgumentParser(description="Keithley SMU client")
    parser.add_argument(
        "--idvg", action="store_true", help="show the transfer curve interface"
    )
    parser.add_argument(
        "--idvd", action="store_true", help="show the output curve interface"
    )
    parser.add_argument(
        "--time", action="store_true", help="show the time response interface"
    )
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    args = parser.parse_args()

    config_pyqtgraph()

    # Create the application
    app = QApplication([])
    if args.idvg:
        mode = "Id-Vg"
    elif args.idvd:
        mode = "Id-Vd"
    elif args.time:
        mode = "Time"
    else:
        mode = "Id-Vd"

    # Create the main window
    main = MainWindow(win_title, mode, SMU_config)
    main.show()

    # Run the application
    app.exec_()
