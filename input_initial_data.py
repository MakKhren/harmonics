import pyinputplus as pyip

class InputIinitialData():
    '''Ввод исходнных данных'''

    def __init__(self):
        self.n_harm = pyip.inputInt(prompt="Введите количество гармоник: ")
        self.I_oper_conv = pyip.inputNum(prompt="Введите действующие значение "
                        "расчетного ток преобразовательной техники: ")
        self.I_oper_full = pyip.inputNum(
                        prompt="Введите полный расчетный действующий ток: ",
                        greaterThan=0
                        )
        self.U_phase_oper = int(pyip.inputChoice(["220", "230"],
                        prompt="Выберите действующие значение фазного "
                        "напряжения 220 / 230 В: "))
        self.r_sys = pyip.inputNum(prompt=
                                "Введите активное сопротивление системы: ")
        self.x_sys = pyip.inputNum(prompt=
                                "Введите индуктивное сопротивление системы: ")

        
