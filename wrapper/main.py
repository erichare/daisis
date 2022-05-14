from pydaisi import Daisi
import streamlit as st


#######################################################
def __get_astro_picture__():
    d = Daisi("Astronomy picture of the day - Image output", base_url="https://dev3.daisi.io")
    img = d.return_img_obj().value

    return img


#######################################################
def __convert_to_black_and_white__(img):
    daisi = Daisi("Convert Image to Gray levels", base_url="https://dev3.daisi.io")
    final_res = daisi.compute(img=img).value

    return final_res


#######################################################
def __colorize__(img):
    color = Daisi("ImageColorization")
    in_color = color.run(image=img).value

    return in_color


#######################################################
def compute():
    """Return the recolored Astronomy picture of the day"""

    img = __get_astro_picture__()
    img_black_and_white = __convert_to_black_and_white__(img)
    img_color = __colorize__(img_black_and_white)

    return img_color


#######################################################
if __name__ == '__main__':
    st.title("Conversion of the Astronomy picture of the day")

    # Step 1: Astronomic picture of the day
    img = __get_astro_picture__()
    st.image(img, caption='Astronomy picture of the day')

    # Step 2: Convert image to grey levels
    img_black_and_white = __convert_to_black_and_white__(img)
    st.image(img_black_and_white, caption='Converted into grey levels')

    # Step 3: Colorization of the grey image
    img_color = __colorize__(img_black_and_white)
    st.image(img_color, caption='Colored')
