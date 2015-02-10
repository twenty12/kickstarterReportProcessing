import csv
from defs import basic_columns, added_columns, in_range, out_range, all_cleaned

t_in_range =  open(in_range,'w')
w_in_range = csv.writer(t_in_range)
w_in_range.writerow(basic_columns + added_columns)
t_in_range.close()

t_out_range =  open(out_range,'w')
p_out_range = csv.writer(t_out_range)
p_out_range.writerow(basic_columns + added_columns)
t_out_range.close()