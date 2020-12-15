import datetime
import decimal
InputDatePrescribed= input("When was prescription written? (year-month-day): ")
InputPillPatchRefillCount = input("How many pills/inhalers in this refill?: ")
InputPillsPerday = input("How many pills can be taken in a day?: ")
InputPatchDuration = input("How often is the inhaler used (hours)?: ")
# Written in standard Year, month,day 2008-8-2
YearMonthDayInput = InputDatePrescribed.split('-')#split this in arguments using"-", then input that
InputYear,InputMonth,InputDay = InputDatePrescribed.split('-')
DatePrescribed = datetime.date (int(InputYear), int(InputMonth),int(InputDay))


def PillRefillDuration (InputPillPatchRefillCount,InputPillsPerday): #STATES HOW MANY DAYS IT SHOULD LAST AS READABLE OUTPUT
    PillRefillDuration = decimal.Decimal(decimal.Decimal(InputPillPatchRefillCount)/decimal.Decimal(InputPillsPerday))
    return PillRefillDuration

def PillDeltaDueDate (InputPillPatchRefillCount, InputPillsPerday): #RETURNS A TIMEDELTA OBJECT IN DAYS WHICHS ALLOWS MANIPULATION
    return datetime.timedelta (float(PillRefillDuration(InputPillPatchRefillCount, InputPillsPerday)))#Need to do this since timedelta doesn't take Decimal type
    
def PatchRefillDuration (InputPillPatchRefillCount,InputPatchDuration):
    PatchRefillDuration = decimal.Decimal(decimal.Decimal(InputPatchDuration)/decimal.Decimal(24)) *decimal.Decimal(InputPillPatchRefillCount)
    return PatchRefillDuration

def PatchDeltaDueDue (InputPillPatchRefillCount, InputPatchDuration):
    return datetime.timedelta (float (PatchRefillDuration(InputPillPatchRefillCount, InputPatchDuration)))
    
if InputPatchDuration == "":
    a = PillRefillDuration (InputPillPatchRefillCount, InputPillsPerday)
    print ("It shoud last ", a, " days.")
    print ("It was prescrbied", DatePrescribed)
    DueDate = DatePrescribed + PillDeltaDueDate (InputPillPatchRefillCount, InputPillsPerday)
    print ("It is due on", DueDate)

if InputPillsPerday == "":
    a = PatchRefillDuration(InputPillPatchRefillCount, InputPatchDuration)
    print ("It shoud last ", a, " days.")
    print ("It was prescrbied", DatePrescribed)
    DueDate = DatePrescribed + PatchDeltaDueDue (InputPillPatchRefillCount, InputPatchDuration)
    print ("It is due on", DueDate)

