# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parametric_propellerKsVrDX.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(528, 361)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.blade_type_list = QComboBox(self.groupBox_2)
        self.blade_type_list.setObjectName(u"blade_type_list")

        self.horizontalLayout_2.addWidget(self.blade_type_list)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.num_blade_input = QSpinBox(self.groupBox_2)
        self.num_blade_input.setObjectName(u"num_blade_input")
        self.num_blade_input.setMinimum(2)
        self.num_blade_input.setMaximum(100)
        self.num_blade_input.setValue(12)

        self.horizontalLayout_3.addWidget(self.num_blade_input)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.attack_angle_input = QSpinBox(self.groupBox_2)
        self.attack_angle_input.setObjectName(u"attack_angle_input")
        self.attack_angle_input.setCursor(QCursor(Qt.ArrowCursor))
        self.attack_angle_input.setValue(30)

        self.horizontalLayout_6.addWidget(self.attack_angle_input)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.hub_diameter_input = QDoubleSpinBox(self.groupBox_2)
        self.hub_diameter_input.setObjectName(u"hub_diameter_input")
        self.hub_diameter_input.setDecimals(1)
        self.hub_diameter_input.setMaximum(1000.000000000000000)
        self.hub_diameter_input.setSingleStep(0.100000000000000)
        self.hub_diameter_input.setValue(2.000000000000000)

        self.horizontalLayout_4.addWidget(self.hub_diameter_input)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.out_diameter_input = QDoubleSpinBox(self.groupBox_2)
        self.out_diameter_input.setObjectName(u"out_diameter_input")
        self.out_diameter_input.setDecimals(1)
        self.out_diameter_input.setMaximum(1000.000000000000000)
        self.out_diameter_input.setSingleStep(0.100000000000000)
        self.out_diameter_input.setValue(4.000000000000000)

        self.horizontalLayout_7.addWidget(self.out_diameter_input)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.height_input = QDoubleSpinBox(self.groupBox_2)
        self.height_input.setObjectName(u"height_input")
        self.height_input.setDecimals(1)
        self.height_input.setValue(5.000000000000000)

        self.horizontalLayout_5.addWidget(self.height_input)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.vortex_gen_checkbox = QCheckBox(self.widget)
        self.vortex_gen_checkbox.setObjectName(u"vortex_gen_checkbox")

        self.verticalLayout_2.addWidget(self.vortex_gen_checkbox)

        self.preview_button = QPushButton(self.widget)
        self.preview_button.setObjectName(u"preview_button")

        self.verticalLayout_2.addWidget(self.preview_button)

        self.generate_button = QPushButton(self.widget)
        self.generate_button.setObjectName(u"generate_button")

        self.verticalLayout_2.addWidget(self.generate_button)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.foil_graph = QWidget(self.widget1)
        self.foil_graph.setObjectName(u"foil_graph")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foil_graph.sizePolicy().hasHeightForWidth())
        self.foil_graph.setSizePolicy(sizePolicy)
        self.foil_graph.setMinimumSize(QSize(300, 0))
        self.foil_graph.setAutoFillBackground(True)

        self.verticalLayout_3.addWidget(self.foil_graph)

        self.model_widget = QWidget(self.widget1)
        self.model_widget.setObjectName(u"model_widget")
        self.model_widget.setAutoFillBackground(True)

        self.verticalLayout_3.addWidget(self.model_widget)

        self.splitter.addWidget(self.widget1)

        self.verticalLayout_4.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 528, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Design parameters:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Type of blade:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number of blades:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Angle of attack (deg):", None))
        self.attack_angle_input.setSpecialValueText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hub diameter (mm):", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Outer diameter (mm):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Height (mm):", None))
        self.vortex_gen_checkbox.setText(QCoreApplication.translate("MainWindow", u"Vortex generator", None))
        self.preview_button.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

