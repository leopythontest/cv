from PIL import Image


im1 = Image.open(f"leo_fl_modified.png")
print (im1.size)
im2 = im1.resize((150,150))
im2.save(f"leo_fl_modified2.png")


