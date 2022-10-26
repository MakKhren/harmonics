from scipy.integrate import quad 
import numpy as np


class  TNDI():
    '''Простая модель коэфициента искажения гармоник тока'''

    def __init__(self, n_harm, I_oper_conv, I_oper_full ):
        '''
        инициализирует исходные данные и атрибуты
        для расчета коэфициента гармоник
        I_oper_conv - действующий ток преобразователей
        I_oper_full - полный действующий ток
        n_harm   - количество гармоник
        '''

        self.n_harm = n_harm     # количество гармоник
        self.I_oper_conv = I_oper_conv  # действующий ток преобразователей
        self.I_oper_full = I_oper_full # полный действующий ток
        self._current_amp_harmonics = []
        self._lower_limit = np.pi / 6
        self._upper_limit = 5 * np.pi / 6
        self._calculate_current_amp_harmonics()

    def _get_integrand_bn(self, x, n, I):
        '''подъинтегральная функция для коэфициета bn токовой функции'''
        return I * np.sin(n * x)

    def _calculate_current_amp_harmonics(self):
        '''расчет амплитудных значений токов гармоник с 1 по n гармонику'''
        for n_i in range(1,self.n_harm):
            I_n = 2 / np.pi * quad(self._get_integrand_bn,
                                    self._lower_limit,
                                    self._upper_limit,
                                    args=(n_i,self.I_oper_conv))[0]
            self._current_amp_harmonics.append(round(I_n, 2))
        

    def get_current_amp_harmonic(self):
        '''Получение  аплитудных значений токов гармоник с 1 по n гармонику'''
        return self._current_amp_harmonics

    def get_rms_currents_harmonic(self):
        '''
        Получение среднеквадратичное  значения 
        действующего тока гармоник со 2 по n гармонику
        '''
        current_oper_harmonics = [round((I_na**2)/2, 2) for I_na 
                                    in self._current_amp_harmonics[1:]]
        I_rms_harm = np.sqrt(sum(current_oper_harmonics))
        return round(I_rms_harm, 2)

    def get_tnd_i(self):
        '''Получение коэфициента искажения тока'''
        I_rms_harm = self.get_rms_currents_harmonic()
        tnd_i = I_rms_harm / self.I_oper_full * 100
        return round(tnd_i, 2)
   