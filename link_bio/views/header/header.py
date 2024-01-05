import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size

def header()-> rx.Component:
        return rx.vstack(
                #Para que se quede alado del icono
            rx.hstack(
                rx.avatar(name="Adam Power", size="xl"),
                rx.vstack(
                        rx.heading(
                                "Adam Power", 
                                size="lg"
                        ),
                        rx.text(
                                "@mr___power",
                                margin_top="0px  !important"
                        ),
                        rx.hstack(
                        link_icon("https://github.com/mrpowergonz"),
                        link_icon("https://github.com/mrpowergonz"),
                        ),
                        align_items="start" ,
                        
                      
                ) ,
                spacing=Size.DEFAULT.value,
        ),


        rx.flex(
                    info_text("+2 " , "años de experiencia"),
                    rx.spacer(),
                    info_text("+2 " , "años de experiencia"),
                    rx.spacer(),
                    info_text("+2 " , "años de experiencia"),
                    width="100%"
        ),
               
            rx.text("Soy un programador autodidacta que esta intentando aprender todas las ultimas tecnologias. Aqui os dejo todos mis enlaces de interés. Bienvenid@! "),
            spacing=Size.BIG.value, #Spacing para darle espacio a todos los componentes
            align_items="start"
               
        )
