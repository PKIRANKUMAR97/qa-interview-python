from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sheet.title="Practice1"
sheet["A1"]="KIRAN"
sheet["A2"]="KUMAR"
wb.save("E:\Pavan_Trainings\Practice.xlsx")