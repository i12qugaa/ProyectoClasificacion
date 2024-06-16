#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Antonio Javier Quintero García y Noelia Ruiz Morón
"""

import sys
from PyQt5.QtWidgets import QApplication
from vistaClasificacion import ClasificadorDlg

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ClasificadorDlg()
    form.show()
    sys.exit(app.exec_())
