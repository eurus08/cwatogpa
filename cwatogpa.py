""" ######### cwatogpa.py #########
Author: eurus
Date: August 31, 2025
Description: Calculate gpa using scores and weights
"""

from courses import courses

# CWA calculator
# Attributes: course -> list of tuples(score, credit_hours)
# Returns rounded calculated CWA 

def cwa(courses: list): 

    total_weighted_scores = 0
    total_credits = 0

    for score, credit in courses:
        total_weighted_scores += score * credit
        total_credits += credit

    return round(total_weighted_scores / total_credits, 2)


# Score to Grade point converter
# Attributes: course -> float
# Returns corresponding grade for Score

def score_to_gp(score):
    if score >= 70:
        return 4.0   # A
    elif score >= 60:
        return 3.0   # B
    elif score >= 50:
        return 2.0   # C
    elif score >= 45:
        return 1.5   # D
    elif score >= 40:
        return 1.0   # E
    else:
        return 0.0   # F


# GPA calculator
# Attributes: course -> list of tuples(score, credit_hours)
# Returns rounded calculated GPA

def gpa(courses:list):
    total_points = 0
    total_credits = 0

    for score, credit in courses:
        grade_point = score_to_gp(score)
        total_points += grade_point * credit
        total_credits += credit

    return round(total_points / total_credits, 2)


### Print Out CWA and GPA
print("Your CWA is:", cwa(courses))
print("Your GPA is:", gpa(courses))