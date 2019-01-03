import PySimpleGUI as Sg
import base64


class ImageHandler(object):
    def __init__(self, image_one, image_two, p_error):
        self.image_one = image_one
        self.image_two = image_two
        self.p_error = p_error

    def basic_compare(self):
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


layout = [[Sg.Radio("base64", group_id="type"),
           Sg.Radio("pixel", group_id="type"),
           Sg.Radio("quads", group_id="type"),
           Sg.Radio("cubes", group_id="type")],
          [Sg.Button("Initial File", key="first_file"),
           Sg.Button("Secondary File", key="second_file")],
          [Sg.Button("Run", key = "run")]]

main_window = Sg.Window("imgMapppy").Layout(layout).Finalize()


while True:

    b, v = main_window.Read(timeout=100)

    if b == "first_file":
        first_image = Sg.PopupGetFile("Select First Image", default_path="c:/")

    if b == "second_file":
        second_image = Sg.PopupGetFile("Select Second Image", default_path="c:/")

    if b == "run":
        init = ImageHandler(first_image, second_image, 1)
        init.basic_compare()

    if b is None:
        break

    else:
        pass


