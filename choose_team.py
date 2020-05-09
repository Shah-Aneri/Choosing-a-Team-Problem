#!/usr/local/bin/python3
#
# choose_team.py : Choose a team of maximum skill under a fixed budget
#
# Code by: [Hely Modi - helymodi, Aneri Shah - annishah, Dhruva Bhavsar - dbhavsar]
#
# Based on skeleton code by D. Crandall, September 2019
#
import sys

def load_people(filename):
    people={}
    with open(filename, "r") as file:
        for line in file:
            l = line.split()
            people[l[0]] = [ float(i) for i in l[1:] ] 
    return people


# This function calculates all possible skills for given budget.
# It then returns the one with max skill.

def approx_solve(people, budget):

    people_list = sorted(people.items(), key=lambda x: x[1][1]/x[1][0])
    skills = [0]*len(people_list)
    solution = [0]*len(people_list)
    
    for i in range(len(people_list)):
        cost_so_far = 0
        temp = ()
        for j in range(i, i+len(people_list)):
            if (people_list[j%len(people_list)][1][1] + cost_so_far) <= budget:
                cost_so_far += people_list[j%len(people_list)][1][1]
                skills[i] += people_list[j%len(people_list)][1][0]
                temp += ( ( people_list[j%len(people_list)][0], 1), )
        solution[i] = temp

    max_skill = max(skills)
    return solution[skills.index(max_skill)]

if __name__ == "__main__":

    if(len(sys.argv) != 3):
        raise Exception('Error: expected 2 command line arguments')

    budget = float(sys.argv[2])
    people = load_people(sys.argv[1])
    
    solution = approx_solve(people, budget)
    if len(solution) > 0:
        print("Found a group with %d people costing %f with total skill %f" % \
                   ( len(solution), sum(people[p][1]*f for p,f in solution), sum(people[p][0]*f for p,f in solution)))
    
        for s in solution:
            print("%s %f" % s)
    else:
        print('Inf')