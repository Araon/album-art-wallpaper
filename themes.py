themes = {
    "Default":{
        "settings_window":"",
        "menu":""
    },
    "Dark":{
        "settings_window":'''
            QLineEdit  {
                border: 1px solid white;
                width: 150;
                height: 20px;
                background: #6f6f76;
                color: white;
                padding-left: 6px;
                padding-right: 6px;
            }
            QLabel
            {
                color: white;
            }
            QRadioButton
            {
                color:white;
            }
            QPushButton
            {
                border-style: outset;
                border-width: 2px;
                border-radius: 15px;
                border-color: white;
                color: white;
                padding: 4px;
            }
            QSpinBox
            {
                border: 1px solid white;
                width: 150;
                height: 20px;
                background: #6f6f76;
                color: white;
                padding-left: 6px;
            }
            QDoubleSpinBox
            {
                border: 1px solid white;
                width: 150;
                height: 20px;
                background: #6f6f76;
                color: white;
                padding-left: 6px;
            }
            QComboBox
            {
                border: 1px solid white;
                width: 150;
                height: 20px;
                background-color: #6f6f76;
                color: white;
                padding-left: 6px;
            }
            QComboBox QAbstractItemView
            {
                border: 1px solid white;
                selection-background-color: #262626;
                color:white;
            }
            QWidget
            {
                background-color: black;
                font-size: 15px;
            }
        ''',
        "menu":'''
            QMenu
            {
                background-color:black;
                color: white;
            }
        '''
    }
}