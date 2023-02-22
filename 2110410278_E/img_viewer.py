import PySimpleGUI as sg 
import os.path 
from PIL import Image, ImageOps
from processing_list import *
from PySimpleGUI.PySimpleGUI import Slider, Cancel


# Kolom Area No 1: Area open folder and select image
file_list_column = [
    [
        sg.Text("Image Information:"),
    ],
    [
        sg.Text(size=(25, 1), key="ImgSize"),
    ],
    [
        sg.Text(size=(25, 1), key="ImgColorDepth"),
    ],
    [
        sg.Text(size=(25, 1), key=""),
    ],
    [
        sg.Text("Open Image Folder :"),
    ],
    [
        sg.In(size=(20, 1), enable_events=True, key="ImgFolder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Choose an image from list :"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(18, 10), key="ImgList"
            )
        ],
    ]


# Kolom Area No 2: Area viewer image input
image_viewer_column = [
    [sg.Text("Image Input :")],
    [sg.Text(size=(40, 1), key="FilepathImgInput")],
    [sg.Image(key="ImgInputViewer")],
]
 
# Kolom Area No 3: Area Image info dan Tombol list of processing
list_processing = [
    [
        sg.Text("List of Processing:"),
    ],
    [
        sg.Button("Thresholding", size=(9, 1), key="ImgThresholding"),
        sg.Button("Negative", size=(9, 1), key="ImgNegative"),
    ],
    [
        sg.Button("Brightness +", size=(9, 1), key="ImgBrightnessPos"),
        sg.Button("Brightness -", size=(9, 1), key="ImgBrightnessNeg"),
    ],
    [
        sg.Button("Image Rotate", size=(20, 1), key="ImgRotate"),
    ],
    [
        sg.Text("Flip    :         "),
        sg.Button("Verti & Hori", size=(9, 1), key="ImgFlipVerti_Hori"),
    ],
    [
        sg.Button("Vertical", size=(9, 1), key="ImgFlipVertical"),
        sg.Button("Horizontal", size=(9, 1), key="ImgFlipHorizontal"),
    ],
    [
        sg.Button("Zooming", size=(9, 1), key="ImgZooming"),
        sg.Button("Shrinking", size=(9, 1), key="ImgShrinking"),
    ],
    [
        sg.Button("Image Logarithmic", size=(20, 1), key="ImgLogarithmic"),
    ],
    [
        sg.Button("Translation", size=(20, 1), key="ImgTranslation"),
    ],
    [
        sg.Button("Median Filter", size=(9, 1), key="ImgMedianFilter"),
        sg.Button("Mean Filter", size=(9, 1), key="ImgMeanFilter"),
    ],
    [
        sg.Button("Gaussian Filter", size=(20, 1), key="ImgGaussian"),
    ],
    [
        sg.Text("Edge Detect:"),
        sg.Button("Laplacian", size=(9, 1), key="ImgLaplacian"),
    ],
    [
        sg.Button("Prewitt", size=(9, 1), key="ImgPrewitt"),
        sg.Button("Robert", size=(9, 1), key="ImgRobert"),
    ],
    [   
        sg.Button("Sobel", size=(20, 1), key="ImgSobel"),
    ],
    [
        sg.Button("Rgb2Grayscale", size=(20, 1), key="ImgRgb2Grayscale"),
    ],
    [
        sg.Button("Rgb2Hsv", size=(20, 1), key="ImgRgb2Hsv"),
    ],
    [
        sg.Text("Morfologi   : "),
        sg.Button("Erosi", size=(9, 1), key="ImgErosi"),
        
    ],
    [
        sg.Button("Dilasi", size=(20, 1), key="ImgDilasi"),
    ],
    [
        sg.Button("Opening", size=(9, 1), key="ImgOpening"),
        sg.Button("Closing", size=(9, 1),key="ImgClosing"),
    ],
    [
        sg.Slider(range=(0, 360), orientation='h', size=(20, 20), default_value=0, visible=False, key="slider_rotate"),
        sg.Slider(range=(2, 4), orientation='h', size=(19, 20),  visible=False, key="slider_zooming"),
        sg.Slider(range=(2, 4), orientation='h', size=(19, 20),  visible=False, key="slider_shrinking"),
        sg.Text("Nilai X :", visible=False, key="text_nilai_x"),
        sg.In(default_text=0, size=(10, 1), visible=False, key="input_x"),
        sg.Text("Nilai Y :", visible=False, key="text_nilai_y"),
        sg.In(default_text=0, size=(10, 1), visible=False, key="input_y")
    ],
    [
        sg.Button("Ok", size=(4, 1), key="submit_degree", visible=False), 
        sg.Button("Ok", size=(4, 1), key="submit_zooming", visible=False),
        sg.Button("Ok", size=(4, 1), key="submit_shrinking", visible=False),
        sg.Button("Ok", size=(4, 1), key="submit_translation", visible=False),
    ],
    [
        sg.Button("Cancel", size=(20,1), key="cancel")
    ],
    
]

n=0
val = 50

# Kolom Area No 4: Area viewer image output
image_viewer_column2 = [
    [sg.Text("Image Processing Output:")],
    [sg.Text(size=(40, 1), key="ImgProcessingType")],
    [sg.Image(key="ImgOutputViewer")],
]
# Gabung Full layout
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
        sg.VSeperator(),
        sg.Column(list_processing),
        sg.VSeperator(),
        sg.Column(image_viewer_column2),
    ]
] 
window = sg.Window("Mini Image Editor", layout)

#nama image file temporary setiap kali processing output
filename_out = "out.png"
# Run the Event Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "ImgFolder":
        folder = values["ImgFolder"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif",".jpg"))
        ]

        window["ImgList"].update(fnames)
    elif event == "ImgList": # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["ImgFolder"], values["ImgList"][0]
            )
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename)
            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)
            #img_input.show()

            #Size
            img_width, img_height = img_input.size
            window["ImgSize"].update("Image Size : "+str(img_width)+" x "+str(img_height))

            #Color depth
            mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB":24, "HSV": 24, "I": 32, "F": 32}
            coldepth = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth"].update("Color Depth : "+str(coldepth))

        except:
            pass
    
    elif event == "ImgThresholding":
        try:
            window["ImgProcessingType"].update("Image Thresholding")
            img_output=ImgThresholding(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgNegative":

        try:
            window["ImgProcessingType"].update("Image Negative")
            img_output=ImgNegative(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgBrightnessPos":
        try:
            window["ImgProcessingType"].update("Brightness +")
            img_output=ImgBrightnessPos(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgBrightnessNeg":
        try:
            window["ImgProcessingType"].update("Brightness -")
            img_output=ImgBrightnessNeg(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgFlipVertical":
        try:
            window["ImgProcessingType"].update("Flip Vertical")
            img_output=ImgFlipVertical(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgFlipHorizontal":
        try:
            window["ImgProcessingType"].update("Flip Horizontal")
            img_output=ImgFlipHorizontal(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgFlipVerti_Hori":
        try:
            window["ImgProcessingType"].update("Flip Vertical & Horizontal")
            img_output=ImgFlipVerti_Hori(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgRotate":
        try:
            window["ImgProcessingType"].update("Image Rotate")

            window["slider_rotate"].update(visible=True)
            window["submit_degree"].update(visible=True)
        except:
            pass
    elif event == "submit_degree":
        try:
            n = int(values["slider_rotate"])
            window["ImgProcessingType"].update("Image Rotate")
            img_output = ImgRotate(img_input, coldepth, n)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgZooming":
        try:
            window["slider_zooming"].update(visible=True)
            window["submit_zooming"].update(visible=True)
            window["slider_rotate"].update(visible=False)
            window["submit_degree"].update(visible=False)

        except:
            pass
    
    elif event == "submit_zooming":
        try:
            skala = int(values["slider_zooming"])
            window["ImgProcessingType"].update("Zooming")
            img_output = ImgZooming(img_input, coldepth, skala)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgShrinking":
        try:
            window["slider_shrinking"].update(visible=True)
            window["submit_shrinking"].update(visible=True)
            window["slider_rotate"].update(visible=False)
            window["submit_degree"].update(visible=False)

            
        except:
            pass
    
    elif event == "submit_shrinking":
        try:
            skala = int(values["slider_shrinking"])
            window["ImgProcessingType"].update("Shrinking")
            img_output = ImgShrinking(img_input, coldepth, skala)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgLogarithmic":

        try:
            window["slider_rotate"].update(visible=False)
            window["submit_degree"].update(visible=False)
            window["ImgProcessingType"].update("Image logarithmic")
            img_output = ImgLogarithmic(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgTranslation":
        try:
            window["ImgProcessingType"].update("Translation")
            window["text_nilai_x"].update(visible=True)
            window["input_x"].update(visible=True)
            window["text_nilai_y"].update(visible=True)
            window["input_y"].update(visible=True)
            window["submit_translation"].update(visible=True)

        except:
            pass
    elif event == "submit_translation":
        try:
            x = int(values["input_x"])
            y = int(values["input_y"])
            shift = [x, y]
            window["ImgProcessingType"].update("Image Translation")
            img_output = ImgTranslation(img_input, coldepth, shift)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgMedianFilter":
        try:
            window["ImgProcessingType"].update("Median Filtering")
            output_image = ImgMedianFilter(img_input, coldepth)
            output_image.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgMeanFilter":
        try:
            window["ImgProcessingType"].update("Mean Filtering")
            output_image = ImgMeanFilter(img_input, coldepth)
            output_image.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgGaussian":
        try:
            window["ImgProcessingType"].update("Gaussian Filtering")
            output_image = ImgGaussian(img_input, coldepth)
            output_image.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgLaplacian":
        try:
            window["ImgProcessingType"].update("Image Laplacian")
            img_output = ImgEdgeDetection(img_input, coldepth, val*2, 1)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgPrewitt":
        try:
            window["ImgProcessingType"].update("Image Prewitt")
            img_output = ImgEdgeDetection(img_input, coldepth, val*2, 2)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgRobert":
        try:
            window["ImgProcessingType"].update("Image Robert")
            img_output = ImgEdgeDetection(img_input, coldepth, val*2, 3)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgSobel":
        try:
            window["ImgProcessingType"].update("Image Sobel")
            img_output = ImgEdgeDetection(img_input, coldepth, val*2, 4)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgRgb2Grayscale":
        try:
            window["ImgProcessingType"].update("Rgb2Grayscale")
            output_image = ImgRgb2Grayscale(img_input, coldepth)
            output_image.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgRgb2Hsv":
        try:
            window["ImgProcessingType"].update("Rgb2Hsv")
            output_image = ImgRgb2Hsv(img_input, coldepth)
            output_image.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgErosi":
        try:
            window["ImgProcessingType"].update("Image Erosi")
            img_output = ImgMorfologi(img_input, coldepth, 1)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgDilasi":
        try:
            window["ImgProcessingType"].update("Image Dilasi")
            img_output = ImgMorfologi(img_input, coldepth, 2)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgOpening":
        try:
            window["ImgProcessingType"].update("Image Opening")
            img_output = ImgMorfologi(img_input, coldepth, 1)
            img_output = ImgMorfologi(img_output, coldepth, 2)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgClosing":
        try:
            window["ImgProcessingType"].update("Image Closing")
            img_output = ImgMorfologi(img_input, coldepth, 2)
            img_output = ImgMorfologi(img_output, coldepth, 1)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "cancel":
        try:
            window["ImgProcessingType"].update("")
            img_output = img_input
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            window["slider_rotate"].update(visible=False)
            window["submit_degree"].update(visible=False)

            window["slider_zooming"].update(visible=False)
            window["submit_zooming"].update(visible=False)

            window["slider_shrinking"].update(visible=False)
            window["submit_shrinking"].update(visible=False)
            
            window["text_nilai_x"].update(visible=False)
            window["text_nilai_y"].update(visible=False)
            window["input_x"].update(visible=False)
            window["input_y"].update(visible=False)
            window["submit_translation"].update(visible=False)

        except:
            pass

window.close()
