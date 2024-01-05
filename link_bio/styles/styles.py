import reflex as rx
from enum import Enum



#Constantes
MAX_WIDTH="600px" 


#Sizes
class Size(Enum):
    SMALL= "0.5em"
    MEDIUM= "0.8em"
    DEFAULT= "1em"
    BIG= "2em"

#styles
#Para que todos los botones de la aplicacion tengan este estilo    
BASE_STYLE = {
    rx.Button:{
        "width": "100%",
        "height": "100%",
        "display":"block",
        "padding": Size.SMALL.value ,
        "border_radius": Size.DEFAULT.value
    },
    #Para eliminar el subrayado de los botones
    rx.Link: {
        "text-decoration": "none",
        "_hover": {}
    }
}
title_style = dict(
   
    width="100%",
    padding_top=Size.DEFAULT.value
)

button_title_style = dict(
    font_size = Size.DEFAULT.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value
)


    