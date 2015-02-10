import csv
from defs import basic_columns, added_columns, inter, problem, all_cleaned

t_inter =  open(inter,'w')
w_inter = csv.writer(t_inter)
w_inter.writerow(basic_columns)
t_inter.close()

t_all_cleaned =  open(all_cleaned,'w')
p_all_cleaned = csv.writer(t_all_cleaned)
p_all_cleaned.writerow(basic_columns + added_columns)
t_all_cleaned.close()

t_problem =  open(problem,'w')
p_problem = csv.writer(t_problem)
p_problem.writerow(basic_columns)
t_problem.close()