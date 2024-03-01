import pandas as pd

input_file = 'a.csv'  # 您的输入CSV文件

# 读取CSV文件
df = pd.read_csv(input_file)

#无gama 矫正
df_scaled_int = (df * 255).astype(int)
#gama 矫正 
# 将DataFrame中的每个元素乘以255，然后转换为整数类型
df_scaled_int = ((df**0.45) * 255).astype(int)


from PIL import Image
width =1024
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
        for x in range(32):
            bitcolor=color.iloc[x+y*32].values
            # bitcolor[1]=255-bitcolor[1]
            rgba_values = tuple(bitcolor)
            # print(rgba_values)
            # print(x+((split-1)*32))
            
            img.putpixel((x+((splits)*32), 31-y), rgba_values)
for split in range(0,32):
    create_image_from_csv(df_scaled_int,split,width,height,img)

output_image = './image.png'
img.save(output_image)

