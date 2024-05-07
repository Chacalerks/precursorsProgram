class Substance:
    def __init__(self, name, unityMeasure, inventoryAdditions, additionNumber, inventoryExpenses, finalBalance, expenseJustification):
        self.name = name
        self.unityMeasure = unityMeasure
        self.inventoryAdditions = inventoryAdditions if inventoryAdditions is not None and inventoryAdditions != "-" else 0
        self.additionNumber = additionNumber if additionNumber is not None or additionNumber == "-" else ""
        self.inventoryExpenses = inventoryExpenses if inventoryExpenses is not None and inventoryExpenses != "-" else 0
        self.finalBalance = finalBalance if finalBalance is not None and finalBalance != "-" else 0
        self.expenseJustification = expenseJustification if expenseJustification is not None or expenseJustification == "-"  else ""
        
        #refactor
        if self.additionNumber == "-":
            self.additionNumber = ""
        if self.expenseJustification == "-":
            self.expenseJustification = ""
        self.additionNumber = str(self.additionNumber)
        self.expenseJustification = str(self.expenseJustification)

    def update(self, other):
        self.inventoryAdditions += other.inventoryAdditions
        self.inventoryExpenses += other.inventoryExpenses
        self.finalBalance += other.finalBalance
        self.expenseJustification += "\n" + str(other.expenseJustification) if other.expenseJustification != "" else ""
        self.additionNumber += "\n" + str(other.additionNumber) if other.additionNumber != "" else ""