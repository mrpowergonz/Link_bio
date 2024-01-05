import reflex as rx
from link_bio.components.link_icon import link_icon

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
                        link_icon=("https://x.com/MrPower64165231"),
                        align_items="start"       
                ) 
            ),
               
            rx.text("Soy un programador autodidacta que esta intentando aprender todas las ultimas tecnologias. Aqui os dejo todos mis enlaces de interés. Bienvenid@! "),
            align_items="start"
        )
