#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from ckVtsClasificacion import ClasificacionDlg

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ClasificacionDlg()
    form.show()
    sys.exit(app.exec_())
