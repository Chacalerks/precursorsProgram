class Substance:
    def __init__(self, name, unityMeasure, inventoryAdditions, additionNumber, inventoryExpenses, finalBalance, expenseJustification):
        self.name = name
        self.unityMeasure = unityMeasure
        self.inventoryAdditions = inventoryAdditions if inventoryAdditions is not None else 0
        self.additionNumber = additionNumber if additionNumber is not None else ""
        self.inventoryExpenses = inventoryExpenses if inventoryExpenses is not None else 0
        self.finalBalance = finalBalance if finalBalance is not None else 0
        self.expenseJustification = expenseJustification if expenseJustification is not None else ""

    def update(self, other):
        self.inventoryAdditions += other.inventoryAdditions
        self.inventoryExpenses += other.inventoryExpenses
        self.finalBalance += other.finalBalance
        self.expenseJustification += "\n" + str(other.expenseJustification)
        self.additionNumber += "\n" + str(other.additionNumber)