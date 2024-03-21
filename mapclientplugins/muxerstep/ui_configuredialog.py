# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(561, 340)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.labelIdentifier = QLabel(self.configGroupBox)
        self.labelIdentifier.setObjectName(u"labelIdentifier")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelIdentifier)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditIdentifier)

        self.labelMuxType = QLabel(self.configGroupBox)
        self.labelMuxType.setObjectName(u"labelMuxType")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelMuxType)

        self.labelNumberOfInputs = QLabel(self.configGroupBox)
        self.labelNumberOfInputs.setObjectName(u"labelNumberOfInputs")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelNumberOfInputs)

        self.spinBoxNumberOfInputs = QSpinBox(self.configGroupBox)
        self.spinBoxNumberOfInputs.setObjectName(u"spinBoxNumberOfInputs")
        self.spinBoxNumberOfInputs.setMinimumSize(QSize(75, 0))
        self.spinBoxNumberOfInputs.setMinimum(1)
        self.spinBoxNumberOfInputs.setValue(2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBoxNumberOfInputs)

        self.comboBoxMuxType = QComboBox(self.configGroupBox)
        self.comboBoxMuxType.addItem("")
        self.comboBoxMuxType.setObjectName(u"comboBoxMuxType")
        self.comboBoxMuxType.setEditable(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBoxMuxType)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Muxer", None))
        self.configGroupBox.setTitle("")
        self.labelIdentifier.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:  ", None))
        self.lineEditIdentifier.setText(QCoreApplication.translate("ConfigureDialog", u"Muxer", None))
        self.labelMuxType.setText(QCoreApplication.translate("ConfigureDialog", u"Mux type:", None))
        self.labelNumberOfInputs.setText(QCoreApplication.translate("ConfigureDialog", u"Number of inputs:", None))
        self.comboBoxMuxType.setItemText(0, QCoreApplication.translate("ConfigureDialog", u"http://physiomeproject.org/workflow/1.0/rdf-schema#file_location", None))

    # retranslateUi

