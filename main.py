from PIL import Image

#Настройка
file_name = "example"
offset_len = 40
small_size_result = 80
result_name = file_name + " with effect"


image_for_effect = Image.open(file_name + ".jpg")

red, green, blue = image_for_effect.split()

#1 Создаём смещение у красного канала
coord_crop_left_r = (offset_len, 0, red.width, red.height)

coord_crop_center_r = (offset_len/2, 0, red.width-(offset_len/2), red.height)

cropped_red_left = red.crop(coord_crop_left_r)

cropped_red_center = red.crop(coord_crop_center_r)

blended_red = Image.blend(cropped_red_left, cropped_red_center, 0.5)

#2 Создаём смещение у синего канала
coord_crop_right_l = (0, 0, blue.width - offset_len, blue.height)

coord_crop_center_l = (offset_len/2, 0, blue.width-(offset_len/2), blue.height)

cropped_blue_right = blue.crop(coord_crop_right_l)

cropped_blue_center = blue.crop(coord_crop_center_l)

blended_blue = Image.blend(cropped_blue_right, cropped_blue_center, 0.5)

#3 Кропаем зеленый канал
coord_crop_center_g = (offset_len/2, 0, blue.width - offset_len/2, blue.height)

cropped_green_center = green.crop(coord_crop_center_g)

#4 Мерджим, уменьшаем и сохраянем
image_with_effect = Image.merge("RGB", (blended_red, cropped_green_center, blended_blue))

image_with_effect.save(result_name + ".jpg")

image_with_effect.thumbnail((small_size_result, small_size_result))

image_with_effect.save(result_name +"_small.jpg")
