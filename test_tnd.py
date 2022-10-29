import unittest

import numpy as np

from tnd import TNDI, TNDU

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
    
    def test_get_I_amp_harmonics(self):
        '''
        Тест проверяет правильность вывода и корректность
        расчета внутреннего метода __calculate_I_amp_harmonics  
        '''
        self.assertEqual(self.current_amp_harmonics,
                    self.my_tnd_i.get_I_amp_harmonics())

    def test_get_I_rms_harmonic(self):
        '''
        Тест проверяет правильность вывода и корректность
        расчета внутреннего метода __calculate_I_rms_harmonic
        '''
        self.assertEqual(self.I_rms_harm,
                    self.my_tnd_i.get_I_rms_harmonics())

    def test_get_tnd_i(self):
        '''Тест проверяет правильность вывода и корректность
        расчета внутреннего метода __calculate_tnd_i'''
        self.assertEqual(self.tnd_i_value,
                    self.my_tnd_i.get_tnd_i())


class TestTNDU(unittest.TestCase):
    '''тесты для класса TNDU'''

    def setUp(self):
        self.n_harm = 25     
        self.I_oper_conv = 51
        self.U_phase_oper = 230
        self.r_sys = 0.00402
        self.x_sys = 0.0187
        self.my_tnd_u = TNDU(self.n_harm, self.I_oper_conv, 
                            self.r_sys, self.x_sys, self.U_phase_oper)

        self.__U_amp_harmonics_b1n = [9.379, 17.256, 22.416, 24.158, 22.416,
                                    17.749, 11.208, 4.109, -2.242, -6.798,
                                    -8.967, -8.688, -6.405, -2.92, 0.801,
                                    3.857, 5.604, 5.77, 4.483, 2.206,
                                    -0.408, -2.68, -4.076, -4.322, -3.449]
        self.__U_amp_harmonics_b2n = [305.592, -0.0, -44.698, 0.0, -44.698, 
                                    0.0, -22.349, -0.0, 4.47, -0.0, 17.879, 
                                    0.0, 12.771, -0.0, -1.596, -0.0, -11.175, 
                                    -0.0, -8.94, 0.0, 0.813, 0.0, 8.127, 
                                    -0.0, 6.877]
        self.__U_amp_harmonics_b3n = [9.379, -17.256, 22.416, -24.158, 22.416, 
                                    -17.749, 11.208, -4.109, -2.242, 6.798, 
                                    -8.967, 8.688, -6.405, 2.92, 0.801, 
                                    -3.857, 5.604, -5.77, 4.483, -2.206, 
                                    -0.408, 2.68, -4.076, 4.322, -3.449]
        self.__U_amp_harmonics = [324.35, 0.0, 0.134, 0.0, 0.134, 0.0, 0.067, 
                                0.0, -0.014, 0.0, -0.055, 0.0, -0.039, 0.0, 
                                0.006, 0.0, 0.033, 0.0, 0.026, 0.0, -0.003, 
                                0.0, -0.025, 0.0, -0.021]


if __name__ == '__main__':
    unittest.main()
