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
                    rx.flex(
                            rx.box(
                                rx.vstack(
                                        rx.avatar(
                                                name="Adam Power",
                                                size="2xl",
                                                width="100%",
                                                height="100%",
                                                src="lego2.jpg",
                                                color=Textcolor.BODY.value,
                                                bg=Color.BACKGROUND2.value,
                                                padding="2px",
                                                border="4px",
                                                border_color=Color.PRIMARY.value, #color del borde del avatar
                                                 _hover={
                                                        "cursor": "pointer",
                                                        "transform": "scale(1.10)",
                                                        },
                                                        transition= "0.5s",
                                                
                                                
                                                
                                        ),
                                rx.text(
                                        "Hecho con DALLE-3",
                                        color=Textcolor.FOOTER.value,
                                        font_family= font.DEFAULT.value,
                                        margin_top=Size.ZERO.value,
                                        font_size=Size.SMALL1.value,
                                        padding=Size.DEFAULT.value,
                                        text_align= "center",
                                        ),
                                        
                                        padding=Size.ZERO.value,
                                        ),
                                        align_items="start",
                                        width="50%",
                                        height="100%",
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
                                                "icons/music.svg",
                                                const.MUSIC_URL,
                                                "Musica tranquila"                                        
                                                ),

                                        link_icon(
                                                "icons/instagram.svg",
                                                const.INSTAGRAM_URL,
                                                "Instagram"
                                                ),

                                        link_icon(
                                                "icons/github.svg",
                                                const.GITHUB_URL,
                                                "Github"

                                                ),

                                        link_icon(
                                                "icons/youtube.svg",
                                                const.YOUTUBE_URL,
                                                "Youtube"
                                                ),
                                        link_icon(
                                                "icons/linkedin.svg",
                                                const.LINKEDIN_URL,
                                                "Linkedin"
                                                ),
                                        link_icon(
                                                "icons/envelope.svg",
                                                const.EMAIL,
                                                "Email"
                                                ),
                                                
                                        
                                        ),
                                        align_items="start" ,
                                        margin_left=Size.SMALL.value,
                                        spacing=Size.DEFAULT.value,
                                        width="100%",  
                                        height="100%"
                                
                                ),
                                
                                align_items="center",
                                width="100%",  
                                height="100%",
                        ),
                
        ),


        rx.flex(
                    info_text("+2 " , "años de experiencia programando"),
                    rx.spacer(),
                    info_text("+10 " , "años de experiencia fotografiando"),
                    width="100%",
                    font_family= font.DEFAULT.value,
        ),
               
        rx.text(
            "Soy Adam Power, un apasionado especialista en desarrollo front-end y páginas web, con experiencia en fotografía. Me enfoco en crear experiencias de usuario excepcionales mediante tecnologías como HTML, CSS, JavaScript y Python, además de dominar frameworks modernos como React, Tailwind y Django. ",
            color=Textcolor.BODY.value,
            font_family= font.DEFAULT.value,
            font_size = Size.MEDIUM1.value,

        ),
        rx.text(
         "Graduado en desarrollo de aplicaciones multiplataforma, sigo explorando nuevas tecnologías y creando proyectos. Me interesa especialmente el front-end, la inteligencia artificial, la fotografía, el video y el vuelo con drones. También me apasiona viajar, la música y el mundo de las criptomonedas.",
        color=Textcolor.BODY.value,
        font_family= font.DEFAULT.value,
        font_size = Size.MEDIUM1.value,

        ),
        rx.text(
        "He tenido muchas aventuras haciendo voluntariados y viviendo en otros paises. Domino perfectamente el ingles y el español.",
        color=Textcolor.BODY.value,
        font_family= font.DEFAULT.value,
        font_size = Size.MEDIUM1.value,
        
        ),
            spacing=Size.DEFAULT.value, #Spacing para darle espacio a todos los componentes
            align_items="start",
            margin_top="3em"
               
        )


                
