from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtPrintSupport import QPrinter

a = QApplication([])
document = QTextDocument()
html = """
<head>
<title>Report</title>
<style>
</style>
</head>
<body>
<table width="100%">
<tr>
<td><img src="{}" width="30"></td>
<td><h1>REPORT汉字试试哈</h1></td>
</tr>
</table>
<hr>
<p align=right><img src="{}" width="300"></p>
<p align=right>Sample</p>
</body>
""".format('./aa.png','./bb.png')
