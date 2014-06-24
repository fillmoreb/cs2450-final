CHECKED_OUT = 0
CHECKED_IN = 1

class Item:
	def __init__(self, ID, ISBN, itemType, status, patronID, dateOut, title, author, length, daysOut):
		self.ID = ID
		self.ISBN = ISBN
		self.itemType = itemType
		self.status = status
		self.patronID = patronID
		self.dateOut = dateOut
		self.title = title
		self.author = author
		self.length = length
		self.daysOut = daysOut

	def checkout(self, patronID):
		#need to determine checkout Length and apply to daysOut
		#need to determine if customer can checkout Any more items...
		self.status = CHECKED_OUT
		self.patronID = patronID

	def checkin(self):
		self.status = CHECKED_IN
		self.patronID = None

	def isOverdue(self, currentDate):
		if (self.dateOut + timedelta(days=self.daysOut)) > currentDate:
			return true
		else:
			return FALSE