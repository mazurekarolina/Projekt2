from __future__ import unicode_literals # obsluga polskich znaków diaktrtycznych
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from kalk_geod import * # import kodu pythona ze schematem GUI
from transformacje import Transformacje

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.WGS84.clicked.connect(self.policz_wgs84)
        self.ui.GRS80.clicked.connect(self.policz_grs80)
        self.ui.pl1992.clicked.connect(self.check_s19)
        self.ui.pl2000_str5.clicked.connect(self.check_s5)
        self.ui.pl2000_str6.clicked.connect(self.check_s6)
        self.ui.pl2000_str7.clicked.connect(self.check_s7)
        self.ui.pl2000_str8.clicked.connect(self.check_s8)
        self.strefa = 1
        self.show()

    def policz_wgs84(self):
        t = Transformacje("wgs84")
        f = t.stopnie_na_dziesietne(int(self.ui.fi_stopnie_wprowadz.text()), 
                                                int(self.ui.fi_minuty_wprowadz.text()),
                                                float(self.ui.fi_sekundy_wprowadz.text()))
        l = t.stopnie_na_dziesietne(int(self.ui.lambda_stopnie_wprowadz.text()), 
                                                int(self.ui.lambda_minuty_wprowadz.text()),
                                                float(self.ui.lambda_sekundy_wprowadz.text()))
        wyniki_do_obrobki = t.wgs84(f, l, self.strefa)
        wyniki = {k: str(v) for k, v in wyniki_do_obrobki.items()}
        self.ui.wynik_x_w_ukladzie.setText(wyniki['x'])
        self.ui.wynik_y_w_ukladzie.setText(wyniki['y'])
        self.ui.wynik_xgk.setText(wyniki['xgk'])
        self.ui.ygk_wynik.setText(wyniki['ygk'])

    def policz_grs80(self):
        t = Transformacje("grs80")
        f = t.stopnie_na_dziesietne(int(self.ui.fi_stopnie_wprowadz.text()), 
                                                int(self.ui.fi_minuty_wprowadz.text()),
                                                float(self.ui.fi_sekundy_wprowadz.text()))
        l = t.stopnie_na_dziesietne(int(self.ui.lambda_stopnie_wprowadz.text()), 
                                                int(self.ui.lambda_minuty_wprowadz.text()),
                                                float(self.ui.lambda_sekundy_wprowadz.text()))
        wyniki_do_obrobki = t.wgs84(f, l, self.strefa)
        wyniki = {k: str(v) for k, v in wyniki_do_obrobki.items()}
        self.ui.wynik_x_w_ukladzie.setText(wyniki['x'])
        self.ui.wynik_y_w_ukladzie.setText(wyniki['y'])
        self.ui.wynik_xgk.setText(wyniki['xgk'])
        self.ui.ygk_wynik.setText(wyniki['ygk'])

    def check_s19(self):
        self.strefa = 1
    def check_s5(self):
        self.strefa = 5
    def check_s6(self):
        self.strefa = 6
    def check_s7(self):
        self.strefa = 7
    def check_s8(self):
        self.strefa = 8


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
