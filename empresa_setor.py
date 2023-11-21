data_number = int(input("Contability -> 0\nService -> 1\nHR -> 2\n: "))

list_data = []

company = {
    "Contability" : "Lucas|[(95) 98134-5678]| 1024, Claudio|[(95) 98123-2312]| 990",
    "Service" : "Marcos|[(95) 98132-1678]| 524, Andreas|[(95) 98109-1234]| 290",
    "HR" : "Maria|[(95) 98114-2019]| 1223, Lucio|[(95) 98112-3121]| 104"
}
for i in company:
    list_data.append(company.get(i))

print(list_data[data_number])