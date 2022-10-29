import unittest

import numpy as np

from tnd import TNDI

class TestTNDI(unittest.TestCase):
    '''тесты для класса TNDI'''

    def setUp(self):
        self.I_oper_full = 637.42
        self.I_oper_conv = 51
        self.n = 25
        self.my_tnd_i = TNDI(self.n, self.I_oper_conv, self.I_oper_full)
        self.current_amp_harmonics = [56.24, 0.0, 0.0, 0.0, -11.25, 0.0, -8.03, 
                                    -0.0, -0.0, -0.0, 5.11, 0.0, 4.33, -0.0, 
                                    0.0, -0.0, -3.31, -0.0, -2.96, 0.0, -0.0, 
                                    0.0, 2.45, -0.0, 2.25]
        self.I_rms_harm = 11.55
        self.tnd_i_value = 1.81
    
    def test__calculate_current_amp_harmonics(self):
        '''
        Тест проверяет правильность расчета амплитудных значений 
        токов гармоник, заполнения списка и получением списка
         методом  get_current_amp_harmoni
        '''
        self.assertEqual(self.current_amp_harmonics,
                    self.my_tnd_i.get_current_amp_harmonic())

    def test_get_rms_currents_harmonic(self):
        '''
        Тест проверки получения правильного значения среднеквадратичного 
        значения тока гармоник со 2 по n
        '''
        self.assertEqual(self.I_rms_harm,
                    self.my_tnd_i.get_rms_currents_harmonic())

    def test_get_tnd_i(self):
        '''Тест правильности расчета и получения коэфициента искажения тока'''
        self.assertEqual(self.tnd_i_value,
                    self.my_tnd_i.get_tnd_i())


if __name__ == '__main__':
    unittest.main()
