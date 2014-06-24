import item
import patron

class Library:
        def __init__(self):
                self.items = []
                self.patrons = []

        def loadCatalog(self, fileName):
                self.catalogFileName = fileName
                #Do logic to load catalog here.  Item class is in item.py

        def saveCatalog(self):
                #Logic to save catalog here.  Note that we stored the filename in self.catalogFileName
                pass

        def loadPatrons(self, fileName):
                self.patronFileName = fileName
                #Do logic to load patrons here. 

        def incrementDate(self):
                self.currentDate = self.currentDate + timedelta(days=1)
                pass

        def decrementDate(self):
                self.currentDate = self.currentDate - timedelta(days=1)
                pass

        def getItem(self, itemID):
                for i in self.items:
                        if i.ID == itemID:
                                return i
                return None

        def getPatron(self, patronID):
                for p in self.patrons:
                        if p.ID == patronID:
                                return p
                return None

        def getPatrons(self):
                returnList = []
                for p in self.patrons:
                        returnList.append(p)
                return returnList

        def getOverdueItems(self):
                returnList = []
                for i in self.items:
                        if i.isOverdue():
                                returnList.append(i)
                return returnList

        def getCheckedOutItems(self):
                returnList = []
                for i in self.items:
                        if i.status == CHECKED_OUT:
                                returnList.append(i)
                return returnList

library = Library()
library.loadCatalog('filename')
