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
        ### First Image
        base64tobytes_one = bytes(self.image_one, 'utf-8')
        base64_image_one = base64.b64encode(base64tobytes_one)
        ### Second Image
        base64tobytes_two = bytes(self.image_two, 'utf-8')
        base64_image_two = base64.b64encode(base64tobytes_two)

        if base64_image_one == base64_image_two:
            Sg.PopupOK("Images Match (Base64)")
        else:
            Sg.PopupOK("Images Don't Match (Base64)")

    def pix(self):
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
        # print(list(second.getdata()))
        rgb_list_second.append(list(second.getdata()))

        if rgb_list_first == rgb_list_second:
            Sg.PopupOK("Images Match (Pixel)")
        else:
            Sg.PopupOK("Images Don't Match (Pixel)")

        # PIL docs: https://pillow.readthedocs.io/en/3.0.x/reference/
        # Image.html?highlight=.size#PIL.Image.size


layout = [[Sg.Button("Base64", key="b64"),
            Sg.Button("Pixel", key="pix"),
            Sg.Button("Quads", key="quad"),
            Sg.Button("Cubes", key="cube")]]

main_window = Sg.Window("imgMapppy").Layout(layout).Finalize()

mode = None

while True:

    b, v = main_window.Read()
    print(b, v)

    # this can be changed to PopUpGetFiles so you can just select two at once

    if b == "b64": # these can be abstracted
        first_image = Sg.PopupGetFile("First Image", default_path="c:/")
        second_image = Sg.PopupGetFile("Second Image", default_path="c:/")
        init = ImageHandler("b64", first_image, second_image, 1)
    if b == "pix":
        first_image = Sg.PopupGetFile("First Image", default_path="c:/")
        second_image = Sg.PopupGetFile("Second Image", default_path="c:/")
        init = ImageHandler("pix", first_image, second_image, 1)
    if b == "quad":
        first_image = Sg.PopupGetFile("First Image", default_path="c:/")
        second_image = Sg.PopupGetFile("Second Image", default_path="c:/")
        init = ImageHandler("quad", first_image, second_image, 1)
    if b == "cube":
        first_image = Sg.PopupGetFile("First Image", default_path="c:/")
        second_image = Sg.PopupGetFile("Second Image", default_path="c:/")
        init = ImageHandler("cube", first_image, second_image, 1)

    if b is None:
        break

    else:
        pass


