from scipy.integrate import quad 
import numpy as np


class  TNDI():
    '''
    Простая модель коэфициента искажения гармоник тока
    Принято что преобразователь работает по схеме Ларионова
    '''

    def __init__(self, n_harm, I_oper_conv, I_oper_full ):
        '''
        Инициализирует исходные данные и атрибуты
        для расчета коэфициента гармоник тока
        I_oper_conv - действующий ток преобразователей
        I_oper_full - полный действующий ток
        n_harm   - количество гармоник
        '''
        if n_harm <= 0:
            self.n_harm = 1 
        else:
            self.n_harm = n_harm 
        self.I_oper_conv = I_oper_conv  
        if I_oper_full <= 0:
            self.I_oper_full = 1 
        else:
            self.I_oper_full = I_oper_full
        self.__I_amp_harmonics = []
        self.__lower_limit = np.pi / 6
        self.__upper_limit = 5 * np.pi / 6
        self.__calculate_I_amp_harmonics()
        self.__I_rms_harmonic = self.__calculate_I_rms_harmonic()
        self.__tnd_i = self.__calculate_tnd_i()

    def __get_integrand_bn(self, x, n, I):
        '''подъинтегральная функция для коэфициета bn токовой функции'''
        return I * np.sin(n * x)

    def __calculate_I_amp_harmonics(self):
        '''расчет амплитудных значений токов гармоник с 1 по n гармонику'''
        for n_i in range(1,self.n_harm + 1):
            I_n = 2 / np.pi * quad(self.__get_integrand_bn,
                                    self.__lower_limit,
                                    self.__upper_limit,
                                    args=(n_i,self.I_oper_conv))[0]
            self.__I_amp_harmonics.append(round(I_n, 2))
        
    def __calculate_I_rms_harmonic(self):
        '''
        Расчет среднеквадратичное  значения 
        действующего тока гармоник со 2 по n гармонику
        '''
        current_oper_harmonics = [(I_na**2)/2 for I_na 
                                    in self.__I_amp_harmonics[1:]]
        I_rms_harm = np.sqrt(sum(current_oper_harmonics))
        return round(I_rms_harm, 2)

    def __calculate_tnd_i(self):
        '''Получение коэфициента искажения тока'''
        I_rms_harm = self.__calculate_I_rms_harmonic()
        tnd_i = I_rms_harm / self.I_oper_full * 100
        return round(tnd_i, 2)

    def get_I_amp_harmonics(self):
        '''Получение  аплитудных значений токов гармоник с 1 по n гармонику'''
        return self.__I_amp_harmonics

    def get_I_rms_harmonics(self):
        '''
        Получение среднеквадратичное  значения 
        действующего тока гармоник со 2 по n гармонику
         '''
        return self.__I_rms_harmonic

    def get_tnd_i(self):
        '''Получение коэфициента искажения тока'''
        return self.__tnd_i


class TNDU():
    '''
    Простая модель коэфициента искажения напряжения гармоник.
    Принято что преобразователь работает по схеме Ларионова.
    '''

    def __init__(self,  n_harm, I_oper_conv, r_sys, x_sys, U_phase_oper=230):
        '''
        инициализирует исходные данные и атрибуты
        для расчета коэфициента гармоник тока
        I_oper_conv - действующий ток преобразователей
        r_sys, x_sys - активное индуктивное сопротивление системы
        U_phas - фазное напряжение
        n_harm   - количество гармоник
        '''
        if n_harm <= 0:
            self.n_harm = 1 
        else:
            self.n_harm = n_harm 
        self.I_oper_conv = I_oper_conv
        if U_phase_oper <=0:
            self.U_phase_oper = 230
        else:
            self.U_phase_oper = U_phase_oper
        self.r_sys = r_sys
        self.x_sys = x_sys
        self.__z_sys = round(np.sqrt(r_sys**2 + x_sys**2), 3)
        self.__U_phase_amp = U_phase_oper * np.sqrt(2)
        self.__U_phase_amp_conv = (self.__U_phase_amp - 
                                    self.I_oper_conv * self.__z_sys)
        self.__U_amp_harmonics_b1n = []
        self.__U_amp_harmonics_b2n = []
        self.__U_amp_harmonics_b3n = []
        self.__U_amp_harmonics = []
        self.__lower_limit_b1n = 0
        self.__upper_limit_b1n = np.pi / 6
        self.__lower_limit_b2n = np.pi / 6
        self.__upper_limit_b2n = 5 * np.pi / 6
        self.__lower_limit_b3n = 5 * np.pi / 6
        self.__upper_limit_b3n = np.pi
        self.__calculate_U_amp_harmonics_bn1()
        self.__calculate_U_amp_harmonics_bn2()
        self.__calculate_U_amp_harmonics_bn3()
        self.__calculate_U_amp_harmonics()
        self.__U_rms_harmonisc = self.__calculate_U_rms_harmonics()
        self.__tnd_u = self.__calculate_tnd_u()
        

    def __get_integrand(self, x, n, U):
            '''подъинтегральная функция для коэфициета bn функции напряжения'''
            return U * np.sin(x) * np.sin(n * x)

    def __calculate_U_amp_harmonics_bn1(self):
            '''
            расчет амплитудных значений напряжений гармоник 
            с 1 по n гармонику на отрезке от bn1 (0 до pi/6)
            '''
            for n_i in range(1, self.n_harm + 1):
                I_n = 2 / np.pi * quad(self.__get_integrand,
                                        self.__lower_limit_b1n,
                                        self.__upper_limit_b1n,
                                        args=(n_i,self.__U_phase_amp))[0]
                self.__U_amp_harmonics_b1n.append(round(I_n, 3))

    def __calculate_U_amp_harmonics_bn2(self):
            '''
            Расчет амплитудных значений напряжений гармоник 
            с 1 по n гармонику на отрезке от bn2 (pi/6 до 5*pi/6)
            '''
            for n_i in range(1, self.n_harm +1 ):
                I_n = 2 / np.pi * quad(self.__get_integrand,
                                        self.__lower_limit_b2n,
                                        self.__upper_limit_b2n,
                                        args=(n_i,self.__U_phase_amp_conv))[0]
                self.__U_amp_harmonics_b2n.append(round(I_n, 3))

    def __calculate_U_amp_harmonics_bn3(self):
            '''
            Расчет амплитудных значений напряжений гармоник 
            с 1 по n гармонику на отрезке от bn2 (5*pi/6 до pi)
            '''
            for n_i in range(1, self.n_harm +1 ):
                I_n = 2 / np.pi * quad(self.__get_integrand,
                                        self.__lower_limit_b3n,
                                        self.__upper_limit_b3n,
                                        args=(n_i,self.__U_phase_amp))[0]
                self.__U_amp_harmonics_b3n.append(round(I_n, 3))

    def __calculate_U_amp_harmonics(self):
            '''
            Расчет амплитудных значений напряжений гармоник 
            с 1 по n гармонику суммарный
            '''
            segment_bn1 = np.array(self.__U_amp_harmonics_b1n, float)
            segment_bn2 = np.array(self.__U_amp_harmonics_b2n, float)
            segment_bn3 = np.array(self.__U_amp_harmonics_b3n, float)
            U_amp_harmonics = segment_bn1 + segment_bn2+ segment_bn3
            self.__U_amp_harmonics = [round(U_amp_har, 3)
                                            for U_amp_har
                                            in U_amp_harmonics]

    def __calculate_U_rms_harmonics(self):
        '''
        Расчет среднекватратичного действующего
        значения напряжения гармоник со 2 по n гармонику
        '''
        U_oper_harmonics_square = [Uamp**2 / 2 for Uamp 
                                    in self.__U_amp_harmonics[1:]]
        U_rms_harmonics = np.sqrt(sum(U_oper_harmonics_square))
        return round(U_rms_harmonics, 3)

    def __calculate_tnd_u(self):
        '''Расчет коэфициента искажения напряжения'''
        tnd_u = self.__U_rms_harmonisc / self.U_phase_oper * 100
        return round(tnd_u, 3)

    def get_U_amp_harmonics(self):
        '''Получение амплитуд напряжения гармоник'''
        return self.__U_amp_harmonics

    def get_U_amp_harmonics_bn1(self):
        '''Получение амплитуд напряжения гармоник на отрезке bn1'''
        return self.__U_amp_harmonics_b1n
    
    def get_U_amp_harmonics_bn2(self):
        '''Получение амплитуд напряжения гармоник на отрезке bn2'''
        return self.__U_amp_harmonics_b2n

    def get_U_amp_harmonics_bn3(self):
        '''Получение амплитуд напряжения гармоник на отрезке bn2'''
        return self.__U_amp_harmonics_b3n

    def get_U_rms_harmonics(self):
        '''Получение среднекватратичного действующего
        значения напряжения гармоник'''
        return self.__U_rms_harmonisc

    def get_tnd_u(self):
        '''Получение коэфициента искажения напряжения'''
        return self.__tnd_u

    def get_z_sys(self):
        '''Получение полного сопротивления системы'''
        return self.__z_sys  