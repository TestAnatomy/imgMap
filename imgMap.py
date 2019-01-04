import PySimpleGUI as Sg
import base64
from PIL import Image


class ImageHandler(object):
    def __init__(self, method, image_one, image_two, p_error):
        self.method = method
        self.image_one = image_one
        self.image_two = image_two
        self.p_error = p_error

        print(self.method)

        if self.method == "b64": # these can be compressed later
            self.base64()
        if self.method == "pix":
            self.pix()
        if self.method == "quad":
            self.quad()
        if self.method == "cube":
            self.cube()

    def base64(self):
        # First Image
        opened_image_one = open(self.image_one, 'rb+')
        base64_image_one = base64.b64encode(opened_image_one.read())
        # Second Image
        opened_image_two = open(self.image_two, 'rb+')
        base64_image_two = base64.b64encode(opened_image_two.read())

        if base64_image_one == base64_image_two:
            Sg.PopupOK("Images Match (Base64)")
        else:
            Sg.PopupOK("Images Don't Match (Base64)")

    def diff(self, first, second):
        second = set(second)
        print([item for item in first if item not in second])
        # https://stackoverflow.com/questions/6486450/python-
        # compute-list-difference/6486467

    def pix(self):
        rgb_list_final = []
        # First Image:
        first = Image.open(self.image_one)
        size = first.size
        rgb_list_first = []
        #print(list(first.getdata()))
        rgb_list_first.append(list(first.getdata()))

        # Second Image:
        second = Image.open(self.image_two)
        size = second.size
        rgb_list_second = []
        #print(list(second.getdata()))
        rgb_list_second.append(list(second.getdata()))

        if rgb_list_first == rgb_list_second:
            Sg.PopupOK("Images Match (Pixel)")
        else:
            Sg.PopupOK("Images Don't Match (Pixel)")

        diff_compare = Sg.PopupOKCancel("Generate DIFF Comparision Image?")
        if diff_compare == "OK":
            final_diff_set = (set(list(first.getdata())) - set(list(second.getdata())))
            rgb_list_final.append(final_diff_set)
            loc_list = []
            print(rgb_list_final)
            for x in range(second.size[0]):
                for y in range(second.size[1]):
                    pix2 = second.getpixel((x, y))
                    pix1 = first.getpixel((x, y))
                    if pix1 != pix2:
                        print("Found Difference...")
                        loc_list.append([x, y, pix2, pix1])
            print(loc_list) # these are all the pixel differences and locations

        if diff_compare == "Cancel":
            pass

        # PIL docs: https://pillow.readthedocs.io/en/3.0.x/reference/
        # Image.html?highlight=.size#PIL.Image.size


layout = [[Sg.Multiline(key= "box1", size=(30,5)), Sg.Multiline(key="box2", size=(30,5))],
            [Sg.Button("Base64", key="b64"),
            Sg.Button("Pixel", key="pix"),
            Sg.Button("Quads", key="quad"),
            Sg.Button("Cubes", key="cube")]]

main_window = Sg.Window("imgMapppy", auto_size_text=True, size= (510, 150)).Layout(layout).Finalize()

box1 = main_window.FindElement("box1")
box2 = main_window.FindElement("box2")

mode = None

while True:

    b, v = main_window.Read()
    print(b, v)

    # this can be changed to PopUpGetFiles so you can just select two at once

    if b == "b64": # these can be abstracted
        first_image = Sg.PopupGetFile("First Image", default_path="c:/")
        second_image = Sg.PopupGetFile("Second Image", default_path="c:/")
        # First Image:
        # loading it in gui is too much, lots of data...
        #opened_image_one = open(first_image, 'rb+')
        #base64_image_one = base64.b64encode(opened_image_one.read())
        box1.Update("{}".format(first_image))
        # Second Image:
        # loading it in gui is too much, lots of data...
        #opened_image_two = open(second_image, 'rb+')
        #base64_image_two = base64.b64encode(opened_image_two.read())
        box2.Update("{}".format(second_image))
        init = ImageHandler("b64", first_image, second_image, 1)
    if b == "pix":
        first_image = Sg.PopupGetFile("First Image", default_path="c:/")
        second_image = Sg.PopupGetFile("Second Image", default_path="c:/")
        box1.Update(first_image)
        box2.Update(second_image)
        init = ImageHandler("pix", first_image, second_image, 1)
    if b == "quad":
        first_image = Sg.PopupGetFile("First Image", default_path="c:/")
        second_image = Sg.PopupGetFile("Second Image", default_path="c:/")
        box1.Update(first_image)
        box2.Update(second_image)
        init = ImageHandler("quad", first_image, second_image, 1)
    if b == "cube":
        first_image = Sg.PopupGetFile("First Image", default_path="c:/")
        second_image = Sg.PopupGetFile("Second Image", default_path="c:/")
        box1.Update(first_image)
        box2.Update(second_image)
        init = ImageHandler("cube", first_image, second_image, 1)

    if b is None:
        break

    else:
        pass


