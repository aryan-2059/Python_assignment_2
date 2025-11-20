# Project: Gradebook Management System
#Author: Aryan Solanki
# Date: 20-11-2025
import csv

def load_from_csv(filename):
    data={}
    try:
        with open(filename, mode ='r')as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                name=row[0]
                score=int(row[1])
                data[name]=score
        return data
    except FileNotFoundError:
        print("File not found.")
        return None

def manual_entry():
    temp_data = {}
    while True:
        name = input("Enter student name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            score = int(input(f"Enter score for {name}: "))
            temp_data[name] = score
        except ValueError:
            print("Invalid score. Please enter an integer value.")
    return temp_data

def calculate_avg(marks_dict):
    '''Calculate the average score from the marks dictionary.'''
    scores=list(marks_dict.values())
    if not scores:
        return 0
    return sum(scores)/len(scores)

def find_min_score(marks_dict):
    '''Find the minimum score from the marks dictionary.'''
    scores=list(marks_dict.values())
    if not scores:
        return None
    return min(scores)

def find_max_score(marks_dict):
    '''Find the maximum score from the marks dictionary.'''
    scores=list(marks_dict.values())
    if not scores:
        return None
    return max(scores)

def calculate_median(marks_dict):
    '''Calculate the median score from the marks dictionary.'''
    scores=sorted(marks_dict.values())
    n=len(scores)
    if n==0:
        return None
    mid=n//2
    if n%2==0:
        return (scores[mid-1]+scores[mid])/2
    else:
        return scores[mid]

def assign_grades(marks_dict):
    '''Assign letter grades based on scores.'''
    grades_dict={}
    for name, score in marks_dict.items():
        if score >= 90:
            grades_dict[name] = 'A'
        elif score >= 80:
            grades_dict[name] = 'B'
        elif score >= 70:
            grades_dict[name] = 'C'
        elif score >= 60:
            grades_dict[name] = 'D'
        else:
            grades_dict[name] = 'F'
    return grades_dict

def main():
    gradebook = {}
    print("Welcome to the Gradebook Management System")
    while True:
        print("\nMenu:")
        print("1. Load data from CSV (manual or file)")
        print("2. Print report")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()
        if choice == '1':
            method = input("Choose data entry method - 'file' or 'manual': ").strip().lower()
            if method == 'file':
                filename = input("Enter CSV filename: ").strip()
                data = load_from_csv(filename)
                if data is not None:
                    gradebook.update(data)
            elif method == 'manual':
                data = manual_entry()
                gradebook.update(data)
            else:
                print("Invalid method. Please choose 'file' or 'manual'.")
        
        elif choice == '2':
            if not gradebook:
                print("No data available. Please load data first.")
                continue
            avg_score = calculate_avg(gradebook)
            min_score = find_min_score(gradebook)
            max_score = find_max_score(gradebook)
            median_score = calculate_median(gradebook)
            grades = assign_grades(gradebook)
            distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
            for grade in grades.values():
                distribution[grade] += 1
            
            
            # pass-fail count
            passed=[name for name, score in gradebook.items() if score >= 40]
            failed=[name for name, score in gradebook.items() if score < 40]
            
            print("\n" + "="*40)
            print(f"{'Name':<20} {'Marks':<10} {'Grade':<5}")
            print("-" * 40)
            
            for name, score in gradebook.items():
                print(f"{name:<20} {score:<10} {grades[name]:<5}")
            print("-" * 40)
            print(f"Average Score: {avg_score:.2f}")
            print(f"Minimum Score: {min_score}")
            print(f"Maximum Score: {max_score}")
            print(f"Median Score: {median_score}")
            print(f"Number of Students Passed: {len(passed)}")
            print(f"Number of Students Failed: {len(failed)}")
            print("Grade Distribution:")
            for grade, count in distribution.items():
                print(f"  {grade}: {count}")
            print("="*40)
        
        elif choice == '3':
            print("Exiting the Gradebook Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

main()

