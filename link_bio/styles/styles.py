import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import text_color as Textcolor
from .fonts import font , FontWeight


#Constantes
MAX_WIDTH="600px" 

# Fonts to include.
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]


#Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL= "0.5em"
    MEDIUM= "0.8em"
    MEDIUM1= "0.9em"
    DEFAULT= "1em"
    LARGE= "1.5em"
    BIG= "2em"
    VERY_BIG="4em"




#styles
#Para que todos los botones de la aplicacion tengan este estilo    
BASE_STYLE = {
    "font_family": font.DEFAULT.value,  # Set font family globally
    "font_weight":  FontWeight.LIGHT.value,
    
    "background_color": Color.BACKGROUND.value + "!important",

    rx.Heading: {
        "color" : Textcolor.HEADER.value,
        "font_weight":  FontWeight.MEDIUM.value,
        "font_family" : font.DEFAULT.value,
    },

    rx.Button:{
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value ,
        "border_radius": Size.DEFAULT.value,
        "color": Textcolor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "font_family": font.DEFAULT.value,
        "white_space" : "normal",
        "text_align" : "start",
        "_hover": {
            "background_color": Color.SECONDARY.value,
            "cursor": "pointer",
            "transform": "scale(1.05)",
           
        },

    },
    
    #Para eliminar el subrayado de los botones
    rx.Link: {
        "text-decoration": "none",
        "_hover": {}
    }
    
}


    
tech_style= dict(
    width="200%",
    padding_top=Size.DEFAULT.value,
)

navbar_title_style = dict(
    font_family= font.LOGO.value,
    font_size=Size.LARGE.value,
    font_weight=  FontWeight.MEDIUM.value,
    
)

title_style = dict(
    font_family= font.TITLE.value,
    width="100%",
    padding_top=Size.DEFAULT.value,
    color = Textcolor.HEADER.value,
)

button_title_style = dict(
    font_family= font.TITLE.value,
    font_size = Size.DEFAULT.value,
    color = Textcolor.HEADER.value,
    size="lg",
    font_weight= FontWeight.MEDIUM.value,
)

button_body_style = dict(
    font_family= font.DEFAULT.value,
    font_size = Size.MEDIUM.value,
    color = Textcolor.BODY.value,
    font_weight=  FontWeight.MEDIUM.value,

)


    