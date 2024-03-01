import pandas as pd

input_file = 'a.csv'  # 您的输入CSV文件

# 读取CSV文件
df = pd.read_csv(input_file)
# 将DataFrame中的每个元素乘以255，然后转换为整数类型
df_scaled_int = (df * 255).astype(int)


from PIL import Image
width =32
height=32
img = Image.new('RGBA', (width, height))

def create_image_from_csv(df_scaled_int,splits,width,height,img):
    # 截取指定列
    # split=1
    # print(splits)
    split=splits*4+1
    columns_to_extract = [split+1, split+2, split]  # 要截取的列的索引（从0开始）
    color=df_scaled_int.iloc[:,columns_to_extract]
    # 将像素数据放入图像中
    for y in range(height):
        # print(y)
        for x in range(32):
            # print(x)
            rgba_values = tuple(color.iloc[x+y*32].values)
            # print(rgba_values)
            # print(x+((split-1)*32))
            
            img.putpixel((x, y), rgba_values)

create_image_from_csv(df_scaled_int,31,width,height,img)


output_image = './image.png'

img.save(output_image)

