def metod1(img_path='', cell_channel=0, nuclei_channel=1):
    return {'Nuclei': 101,
             'Cells': 1001,
               '%': (1 - 101/1001) *100}
def metod2(img_path = '', cell_channel=0, nuclei_channel=1):
    return {'Nuclei': 202,
             'Cells': 2002,
               '%': (1 - 202/2002) *100}
def metod3(img_path = '', cell_channel=0, nuclei_channel=1):
    return {'Nuclei': 303,
             'Cells': 3003,
               '%': (1 - 303/3003) *100}
    