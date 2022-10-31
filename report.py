from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import RGBColor, Pt

from tnd import TNDI, TNDU

class Report():
    def __init__(self, my_tnd_i, my_tnd_u):
        self.my_tnd_i = my_tnd_i
        self.my_tnd_u = my_tnd_u
        self.doc = Document()
        self.__heading_text = [
            'Анализ гармонических искажений',
            'Расчет коэффициента искажения синусоидальности тока',
            'Расчет коэффициента искажения синусоидальности напряжения',
        ]
        self.__para_text =[
            'Таблица 1 Амплитудные значения токов гармоник',
            'Среднеквадратичное значение тока гармоник',
            f'Irms = {my_tnd_i.get_I_rms_harmonics()}',
            'Коэффициент искажения синусоидальности тока',
            f'TNDi = {my_tnd_i.get_tnd_i()}',
            'Среднеквадратичное значение напряжения гармоник',
            f'TNDi = {my_tnd_u.get_tnd_u()}',
        ]
        self.__table_cols_text = {
            'table_1': ['n', 'InA, А'],
            'table_2': ['n', 'bn1, B', 'bn2, B', 'bn3, B', 'Un, В'],
        }
        self.value_I = [self.my_tnd_i.get_I_amp_harmonics(),]
        self.value_U = [
            self.my_tnd_u.get_U_amp_harmonics_bn1(),
            self.my_tnd_u.get_U_amp_harmonics_bn2(),
            self.my_tnd_u.get_U_amp_harmonics_bn3(),
            self.my_tnd_u.get_U_amp_harmonics(),
        ]

    def __get_para_obj (self, text, aling='left'):
        para_obj = self.doc.add_paragraph(text)
        para_obj.runs[0].font.name = 'Arial'
        para_obj.runs[0].font.size = Pt(12)
        para_obj.runs[0].font.color.rgb = RGBColor(0x00, 0x00, 0x00)
        if aling == 'center':
            para_obj.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif aling == 'left':
            para_obj.alignment = WD_ALIGN_PARAGRAPH.LEFT

    def __get_heading_obj(self, text,aling='center'):
        heading_obj =self.doc.add_heading(text)
        heading_obj.runs[0].font.name = 'Arial'
        heading_obj.runs[0].font.size = Pt(14)
        heading_obj.runs[0].font.color.rgb = RGBColor(0x00, 0x00, 0x00)
        if aling == 'center':
            heading_obj.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif aling == 'left':
           heading_obj.alignment = WD_ALIGN_PARAGRAPH.LEFT

    def __get_table(self, name_cols, list_values):
        table = self.doc.add_table(rows=1, cols=len(name_cols))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.style = 'Table Grid'
        for num_col, name_col in enumerate(name_cols):
            table.rows[0].cells[num_col].text = name_col
            cell_para = table.rows[0].cells[num_col].paragraphs[0]
            cell_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for n in range(len(list_values[0])):
            row_cells = table.add_row().cells
            row_cells[0].text = str(n + 1)
            row_cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for col, values in enumerate(list_values):
            for row, value  in enumerate(values):
                table.rows[row+1].cells[col+1].text = str(value)
                cell_para = table.rows[row+1].cells[col+1].paragraphs[0] 
                cell_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    def get_report(self):
        self.__get_table(self.__table_cols_text['table_1'], self.value_I)
        self.__get_table(self.__table_cols_text['table_2'], self.value_U)
        self.doc.add_page_break()
        self.doc.save('report.docx')         
            
if __name__ == '__main__':
    my_tnd_i = TNDI(25, 51, 637)
    my_tnd_u = TNDU(25, 51, 0.00402, 0.0187, 230)
    report = Report(my_tnd_i, my_tnd_u)
    report.get_report()















