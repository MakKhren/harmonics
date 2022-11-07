import pyinputplus as pyip
from report import Report, print_consol

from tnd import TNDI, TNDU
from input_initial_data import InputIinitialData 

iid = InputIinitialData()
my_tnd_i = TNDI(iid.n_harm, iid.I_oper_conv, iid.I_oper_full)
my_tnd_u = TNDU(iid.n_harm, iid.I_oper_conv, iid.r_sys, iid.x_sys,
                iid.U_phase_oper)
file_name = 'template.docx'

print_consol(my_tnd_i,my_tnd_u)
my_report = Report(my_tnd_i, my_tnd_u, file_name)
my_report.get_report()

input("Для завершения нажми Enter")