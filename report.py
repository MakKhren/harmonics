from docx import Document

from tnd import TNDI, TNDU

my_tnd_i = TNDI(25, 51, 637)
my_tnd_u = TNDU(25, 51, 0.00402, 0.0187, 230)

doc = Document()
para_obj_0 = doc.add_heading('Анализ гармонических искажений')
para_obj_1 = doc.add_paragraph('Расчет коэффициента искажения '
            'синусоидальности тока')
para_obj_2 = doc.add_paragraph('Таблица 1 Амплитудные значения токов гармоник')
table_1 = doc.add_table(rows=1, cols=2)
table_1.style = 'Table Grid'
table_1.rows[0].cells[0].text = 'n'
table_1.rows[0].cells[1].text = 'InA, А'
for n, I_amp in enumerate(my_tnd_i.get_I_amp_harmonics()):
    row_cells = table_1.add_row().cells
    row_cells[0].text = str(n + 1)
    row_cells[1].text = str(I_amp)
para_obj_3 = doc.add_paragraph(f'Среднеквадратичное значение тока гармоник')
para_obj_4 = doc.add_paragraph(f'Irms = {my_tnd_i.get_I_rms_harmonics()}')          
para_obj_5 = doc.add_paragraph(f'Коэффициент искажения синусоидальности тока')
para_obj_6 = doc.add_paragraph(f'TNDi = {my_tnd_i.get_tnd_i()}')            
para_obj_7 = doc.add_paragraph('Расчет коэффициента искажения '
            'синусоидальности напряжения')
para_obj_8 = doc.add_paragraph(f'Zпc = {my_tnd_u.get_z_sys()}')
table_2 = doc.add_table(rows=1, cols=5)
table_2.rows[0].cells[0].text = 'n'
table_2.rows[0].cells[1].text = 'bn1'
table_2.rows[0].cells[2].text = 'bn2'
table_2.rows[0].cells[3].text = 'bn3'
table_2.rows[0].cells[4].text = 'UnA'
for n, U_amp in enumerate(my_tnd_u.get_U_amp_harmonics()):
    row_cells = table_2.add_row().cells
    row_cells[0].text = str(n + 1)
    row_cells[4].text = str(U_amp)
for n, bn1 in enumerate(my_tnd_u.get_U_amp_harmonics_bn1()):
    table_2.rows[n+1].cells[1].text = str(bn1)
for n, bn2 in enumerate(my_tnd_u.get_U_amp_harmonics_bn2()):
    table_2.rows[n+1].cells[2].text = str(bn2)
for n, bn3 in enumerate(my_tnd_u.get_U_amp_harmonics_bn3()):
    table_2.rows[n+1].cells[3].text = str(bn2)
para_obj_9 = doc.add_paragraph(f'Среднеквадратичное значение напряжения гармоник')
para_obj_10 = doc.add_paragraph(f'Irms = {my_tnd_u.get_U_rms_harmonics()}')
para_obj_11 = doc.add_paragraph(f'Коэффициент искажения синусоидальности напряжения')
para_obj_12 = doc.add_paragraph(f'TNDi = {my_tnd_u.get_tnd_u()}')   

doc.add_page_break()
doc.save('report.docx')


