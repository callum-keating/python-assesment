import libs.console as consoleLib

console = consoleLib.Console()
table = consoleLib.selectableTable()
console.clear()
console.print("hello")
table.addCol("hello")
table.addRow("hello")
table.refresh()