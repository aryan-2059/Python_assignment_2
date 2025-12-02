# Project: Gradebook Management System
# Author: Aryan Solanki
# Date: 20-11-2025

import csv
import os
PASSING_SCORE = 40

def load_from_csv(filename):
    """Loads student data from a CSV file."""
    data = {}
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return None
    
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None) 
            for row in reader:
                if not row: continue
                name = row[0].strip()
                try:
                    score = int(row[1])
                    data[name] = score
                except ValueError:
                    print(f"Skipping invalid row: {row}")
        return data
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def manual_entry():
    """Allows manual entry of student scores."""
    temp_data = {}
    print("--- Manual Entry Mode ---")
    while True:
        name = input("Enter student name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        if not name:
            print("Name cannot be empty.")
            continue
        try:
            score = int(input(f"Enter score for {name}: "))
            if 0 <= score <= 100:
                temp_data[name] = score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid score. Please enter an integer.")
    return temp_data

def get_stats(scores):
    """Calculates all statistics in one pass for efficiency."""
    if not scores:
        return None
    
    scores.sort()
    n = len(scores)
    
    avg_score = sum(scores) / n
    min_score = scores[0]
    max_score = scores[-1]
    
    # Median calculation
    mid = n // 2
    if n % 2 == 0:
        median_score = (scores[mid-1] + scores[mid]) / 2
    else:
        median_score = scores[mid]
        
    return avg_score, min_score, max_score, median_score

def assign_grade(score):
    """Returns a letter grade based on the score."""
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    if score >= PASSING_SCORE: return 'E' 
    return 'F'

def main():
    gradebook = {}
    print("Welcome to the Gradebook Management System")
    
    while True:
        print("\nMenu:")
        print("1. Load data")
        print("2. Print report")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            method = input("Method (type 'manual' or hit Enter for file): ").strip().lower()
            if method == 'manual':
                data = manual_entry()
                gradebook.update(data)
            else:
                # Default to data.csv if user just hits Enter
                fname = input("Enter filename [default: data.csv]: ").strip()
                if not fname: fname = 'data.csv'
                
                data = load_from_csv(fname)
                if data:
                    gradebook.update(data)
                    print(f"Successfully loaded {len(data)} records.")

        elif choice == '2':
            if not gradebook:
                print("No data available. Please load data first.")
                continue
           
            scores = list(gradebook.values())
            avg, min_s, max_s, med = get_stats(scores)
            passed_count = sum(1 for s in scores if s >= PASSING_SCORE)
            failed_count = len(scores) - passed_count
            grade_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E':0, 'F': 0}
            
            print("\n" + "="*45)
            print(f"{'Name':<20} {'Marks':<10} {'Grade':<5}")
            print("-" * 45)
            
            for name, score in gradebook.items():
                grade = assign_grade(score)
                grade_dist[grade] += 1
                print(f"{name:<20} {score:<10} {grade:<5}")
                
            print("-" * 45)
            print(f"Average: {avg:.2f} | Median: {med}")
            print(f"Min: {min_s} | Max: {max_s}")
            print(f"Passed: {passed_count} | Failed: {failed_count}")
            print("Grade Distribution:", end=" ")
            for g, c in grade_dist.items():
                if c > 0: print(f"{g}:{c} ", end="")
            print("\n" + "="*45)

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
