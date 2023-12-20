import cv2
import os


def convert_to_gray(input_path, output_path):
    # Resmi oku
    original_image = cv2.imread(input_path)

    # Gri tonlama dönüşümü
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Gri tonlama resmi kaydet
    cv2.imwrite(output_path, gray_image)


# HamVeri klasöründeki dosyaları işleyelim
input_folder = r'C:\Users\mehme\PycharmProjects\OPenCV\HamVeri'
output_folder = r'C:\Users\mehme\PycharmProjects\OPenCV\GrayVeri'

# Eğer çıktı klasörü yoksa oluştur
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 1'den 100'e kadar olan resimleri işleyelim
for i in range(68, 168):
    input_path = os.path.join(input_folder, f' ({i}).jpg')
    output_path = os.path.join(output_folder, f'gray_{i}.jpg')

    # Eğer dosya varsa işlemi gerçekleştir
    if os.path.exists(input_path):
        convert_to_gray(input_path, output_path)
        print(f'{input_path} başarıyla işlendi ve {output_path} olarak kaydedildi.')
    else:
        print(f'{input_path} bulunamadı.')

print('İşlem tamamlandı.')
