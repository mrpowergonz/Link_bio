import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as color
import link_bio.styles.styles as styles
from link_bio.styles.fonts import font
from link_bio.styles.styles import Size as Size, Textcolor

def navbar()-> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("Adam", color=color.PRIMARY.value),
            rx.span("dev", color= color.SECONDARY.value),
            style= styles.navbar_title_style
        ),
        rx.box(
            rx.link(  
                    rx.text("Inicio",
                    margin_left="40rem", 
                    _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.05)",
                    },     
                    ),
                    href="#header-section",
                    scroll="#header-section",
                    p="3",
                    color=Textcolor.BODY.value,
                    font_family= font.DEFAULT.value,
                    font_size= Size.LARGE2.value,  
                ),
            ),
            rx.box(
                rx.link(  
                    rx.text("Tecnologias",
                    margin_left="2rem", 
                    _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.05)",
                    },     
                    ),
                    href="#tech-section",
                    scroll="#tech-section",
                    p="3",
                    color=Textcolor.BODY.value,
                    font_family= font.DEFAULT.value,
                    font_size= Size.LARGE2.value,  
                ),
            ),
            rx.box(
                    rx.link(  
                            rx.text("Proyectos",
                            margin_left="2rem", 
                            _hover={
                            "cursor": "pointer",
                            "transform": "scale(1.05)",
                            },     
                            ),
                            href="#proyectos-section",
                            scroll="#proyectos-section",
                            p="3",
                            color=Textcolor.BODY.value,
                            font_family= font.DEFAULT.value,
                            font_size= Size.LARGE2.value,  
                        ),
                    ),
            rx.spacer(),
            
            rx.link(
                    rx.image(
                        src="github_white.png", 
                        height="2em", 
                        display="inline-flex", 
                        pr="0.5", 
                        alignItems="center",
                        _hover={
                            "cursor": "pointer",
                            "transform": "scale(1.15)",
                            },   
                            transition= "0.5s",
                    ),
                    "Source",
                    href="https://github.com/mrpowergonz",
                    scroll="false",
                    p="3",
                    _hover={
                        "textDecoration": "underline"
                    },
                    is_external=True
                ),
                
        position ="sticky",#posicion que queda fija
        bg=color.CONTENT.value,    
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        z_index="999",#tiene prioridad y se quedaria fijado arriba
        top="0" #Para que la navbar se quede fijada cuando hagas scroll
    )