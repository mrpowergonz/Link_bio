import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import text_color as Textcolor
from link_bio.styles.fonts import font
from link_bio.styles.colors import Color as Color
import link_bio.constants as const
import link_bio.styles.styles as styles

def header()-> rx.Component:
        return rx.vstack(
                #Para que se quede alado del icono
            rx.hstack(
                rx.avatar(
                        name="Adam Power",
                        size="xl",
                        src="logo.png",
                        color=Textcolor.BODY.value,
                        bg=Color.BACKGROUND2.value,
                        padding="2px",
                        border="4px",
                        border_color=Color.PRIMARY.value, #color del borde del avatar
                        
                ),
                rx.vstack(
                        rx.heading(
                                "Adam Power Gonzalez", 
                                size="lg",
                                color=Textcolor.HEADER.value,
                                font_family= font.TITLE.value,
                        ),
                        rx.text(
                                "@mr___power",
                                margin_top=Size.ZERO.value,
                                color=Textcolor.BODY.value,
                                font_family= font.DEFAULT.value,
                                
                        ),
                        rx.hstack(
                                link_icon(
                                        "icons/x.svg",
                                        const.TWITTER_X_URL,
                                        
                                  ),
                        link_icon(
                                "icons/instagram.svg",
                                const.INSTAGRAM_URL,
                                
                                  ),

                        link_icon(
                                "icons/github.svg",
                                const.GITHUB_URL,
                                

                                ),

                        link_icon(
                                "icons/youtube.svg",
                                const.YOUTUBE_URL,
                                
                                ),
                        link_icon(
                                "icons/linkedin.svg",
                                const.LINKEDIN_URL,
                                 
                                 ),
                        link_icon(
                                "icons/envelope.svg",
                                const.EMAIL,
                                
                                ),
                                spacing=Size.DEFAULT.value,
                                
                        ),
                        align_items="start" ,
                        
                      
                ),
                
        ),


        rx.flex(
                    info_text("+2 " , "años de experiencia"),
                    rx.spacer(),
                    info_text("+2 " , "años de experiencia"),
                    rx.spacer(),
                    info_text("+2 " , "años de experiencia"),
                    width="100%",
                    font_family= font.DEFAULT.value,
        ),
               
        rx.text(
            "Soy un programador autodidacta que esta intentando aprender todas las ultimas tecnologias. Aqui os dejo todos mis enlaces de interés. Bienvenid@! ",
            color=Textcolor.BODY.value,
            font_family= font.DEFAULT.value,
            font_size = Size.MEDIUM1.value,

        ),
            spacing=Size.BIG.value, #Spacing para darle espacio a todos los componentes
            align_items="start"
               
        )
