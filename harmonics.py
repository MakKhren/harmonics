import pyinputplus as pyip
from report import Report, print_consol

from tnd import TNDI, TNDU

n_harm = pyip.inputInt(prompt="Введите количество гармоник: ")
I_oper_conv = pyip.inputNum(prompt="Введите действующие значение "
                        "расчетного ток преобразовательной техники: ")
I_oper_full = pyip.inputNum(
                        prompt="Введите полный расчетный действующий ток: ",
                        greaterThan=0
                        )
U_phase_oper = int(pyip.inputChoice(["220", "230"],
                        prompt="Выберите действующие значение фазного "
                        "напряжения 220 / 230 В: "))
r_sys = pyip.inputNum(prompt="Введите активное сопротивление системы: ")
x_sys = pyip.inputNum(prompt="Введите индуктивное сопротивление системы: ")

my_tnd_i = TNDI(n_harm, I_oper_conv, I_oper_full)
my_tnd_u = TNDU(n_harm, I_oper_conv, r_sys, x_sys, U_phase_oper)


print_consol(my_tnd_i,my_tnd_u)
my_report = Report(my_tnd_i, my_tnd_u)
my_report.get_report()
input("Для завершения нажми Enter")




