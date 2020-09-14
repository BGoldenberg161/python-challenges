class NewJob():
    def __init__(self, pay, title):
        self.pay = pay
        self.bonus = 10000
        self.isFulltime = None
        self.perks = ''
        

    def changePay(self, pay):
        self.pay = pay
        
    def changePerks(self, newperk):
        self.perks = newperk
        

    def updateFullTime(self, time):
        self.isFulltime = time


DopeJob = NewJob(200000, 'Software Engineer')
DopeJob.updateFullTime(True)



