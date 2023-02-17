# COMMENT OUT THE FOLLOWING CODE
#def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
#    print(empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    # the following code creates a for loop to read through EmpDetailList and assign values in list to variables
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        #write code to assign values to todate, empname, hours, hourlyrate, and taxrate from EmpLst
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]



        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        # the following line of code assigns TotEmployees totals to dictionary 
        EmpTotals["TotEmp"] = TotEmployees
        # write code to assign TotHours, TotGrossPay, TotTax, and TotNetPay to corresponding dictionary item




 
# COMMENT OUT THE FOLLOWING CODE
#def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
#    print()n
#    print(f"Total Number Of Employees: {TotEmployees}")
#    print(f"Total Hours Worked: {TotHours:,.2f}")
#    print(f"Total Gross Pay: {TotGrossPay:,.2f}")
#    print(f"Total Income Tax:  {TotTax:,.2f}")
#    print(f"Total Net Pay: {TotNetPay:,.2f}")

def PrintTotals(EmpTotals):    
    print()
    # use dictionary to print totals
    # the following line of code prints Total Employees from the dictionary
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    # write code to print TotalHrs, TotGrossPay, TotTax and TotNetPay from dictionary




if __name__ == "__main__":
    # COMMENT OUT THE FOLLOWING CODE
    # #TotEmployees = 0
    #TotHours = 0.00
    #TotGrossPay = 0.00
    #TotTax = 0.00
    #TotNetPay = 0.00

    #create empty list and dictionary
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        # COMMENT OUT THE FOLLOWING CODE
        #grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        #printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)

        #write code to insert fromdate, todate, empname, hours, hourlyrate, and taxrate into list EmpDetail


        #the following code appends the list EmpDetail to the list EmpDetailList
        EmpDetailList.append(EmpDetail)

        # COMMENT OUT THE FOLLOWING CODE
        #TotEmployees += 1
        #TotHours += hours
        #TotGrossPay += grosspay
        #TotTax += incometax
        #TotNetPay += netpay
    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)

