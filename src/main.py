import csv

def load_students(filename):
    students=[]
    with open(filename,"r") as source:
        reader=csv.DictReader(source)
        for row in reader:
            students.append(row)
    return students

def calculate_stats(students):
    high=int(students[0]["Marks"])
    low=int(students[0]["Marks"])
    total=0
    top_name=students[0]["Name"]
    for student in students:
        current_marks=int(student["Marks"])
        if(current_marks>high):
            top_name=student["Name"]
            high=current_marks
        if(current_marks<low):
            low=current_marks
        total+=current_marks
    report={
    "total_students": len(students),
    "average_marks": total/len(students),
    "highest_marks": high,
    "lowest_marks": low,
    "topper":top_name,
    }
    return report

def print_report(report):
    print(
    f"\n========REPORT==========\n"
    f"\nTotal Students : {report["total_students"]}\n"
    f"\nAverage Marks : {report["average_marks"]}\n"
    f"\nHighest Marks : {report["highest_marks"]}\n"
    f"\nlowest Marks : {report["lowest_marks"]}\n"
    f"\nTopper : {report["topper"]}\n"
    )

def save_report(file):
    with open("output//report.csv","w") as destination:
        writer=csv.writer(destination)
        writer.writerow(["Metric","Value"])
        for key,value in file.items():
            writer.writerow([key,value])

def main():
    filename=input("Enter the file path:")
    try:
        data=load_students(filename)
    except FileNotFoundError:
        print("File not found")
    report=calculate_stats(data)
    print_report(report)
    save_report(report)

main()