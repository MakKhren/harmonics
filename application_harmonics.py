import pyinputplus as pyip
import docx

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
file_name = 'report.docx'

print()
print(f'РЕЗУЛЬТАТЫ РАСЧЕТА'.center(24, '-'))
print(f"TNDi = {my_tnd_i.get_tnd_i()} "
    f"TNDu = {my_tnd_u.get_tnd_u()}".center(24, '-'))
print()





