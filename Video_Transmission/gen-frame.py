from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Custom font style and font size
myFont = ImageFont.truetype("Comic-Sans-MS.ttf", 50)

num = "121"
for i in range(int(num)):
    img = Image.open("base.png")
    I1 = ImageDraw.Draw(img)

    # Add Text to an image
    I1.text((250, 250), str(i + 1), font=myFont, fill=(0, 0, 0))
    # Save the edited image
    img.save("frames/" + ((len(num) - len(str(i))) * "0") + str(i) + ".png")
