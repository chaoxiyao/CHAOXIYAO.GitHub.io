import os

# 定义图像文件夹的路径
image_folder = "/images"

# 获取所有图像文件的文件名
image_files = os.listdir(image_folder)

# 定义HTML代码
html_code = """
<!DOCTYPE html>
<html>
<head>
	<title>照片墙</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style type="text/css">
		.container {
			max-width: 1200px;
			margin: 0 auto;
			padding: 20px;
		}

		.gallery {
			display: grid;
			grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
			grid-gap: 20px;
		}

		.gallery img {
			width: 100%;
			height: auto;
			object-fit: cover;
		}
	</style>
</head>
<body>
	<div class="container">
		<div class="gallery">
"""

# 循环遍历所有图像文件，并将它们添加到HTML代码中
for image_file in image_files:
    html_code += f'<img src="{image_folder}/{image_file}">\n'

# 添加HTML代码的结尾
html_code += """
		</div>
	</div>
</body>
</html>
"""

# 将HTML代码写入HTML文件中
with open("index.html", "w") as html_file:
    html_file.write(html_code)
