import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_tech import link_tech
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import text_color as Textcolor
from link_bio.styles.fonts import font




def tech() -> rx.Component:
    return rx.vstack(
        title("Tecnologias",),
        rx.hstack(
            rx.vstack(
                
                    link_tech(
                        "javascript.png",
                        const.JAVASCRIPT_URL,
                        alt="Logotipo Javascript",
                        
                    ),
                
                rx.text(
                    "JAVASCRIPT",
                    margin_top=Size.MEDIUM.value,
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    align_self="center", 
                    _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.05)",
                },
                ),
            ),
            rx.vstack(
                link_tech(
                    "python.png",
                    const.PYTHON_URL,
                    alt="Python logotipo",
                ),
                rx.text(
                    "PYTHON",
                    margin_top=Size.MEDIUM.value,
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    align_self="center", 
                    _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.05)",
                },
                ),
            ),

            rx.vstack(
                link_tech(
                    "react.png",
                    const.REACTJS_URL,
                    alt="Logotipo React"
                ),
                rx.text(
                    "REACTJS",
                    margin_top=Size.MEDIUM.value,
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    align_self="center", 
                    _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.05)",
                },
                ),
            ),

            rx.vstack(
                link_tech(
                    "node.png",
                    const.NODEJS_URL,
                    alt="logotipo Node"
                    
                ),
                rx.text(
                    "NODEJS",
                    margin_top=Size.VERY_BIG.value,
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    align_self="center", 
                    _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.15)",
                },
                ),
            
            ),
            
        ),

        rx.hstack(
            rx.vstack(
                link_tech(
                    "django.png",
                    const.DJANGO_URL,
                    alt="Logotipo Django"
                ),
                rx.text(
                    "DJANGO",
                    margin_top=Size.MEDIUM.value,
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    align_self="center", 
                    _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.05)",
                },
                ),
            ),

            rx.vstack(
                link_tech(
                    "git.png",
                    const.GIT_URL,
                    alt="Logotipo Git"
                ),
                rx.text(
                    "GIT",
                    margin_top=Size.MEDIUM.value,
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    align_self="center", 
                    _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.05)",
                },
                ),
            ),

            rx.vstack(
                link_tech(
                    "github_white.png",
                    const.GITHUB_URL,
                    "Logotipo Github"
                ),
                rx.text(
                    "GITHUB",
                    margin_top=Size.MEDIUM.value,
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    align_self="center", 
                    _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.05)",
                },
                ),
            ),

            rx.vstack(
                link_tech(
                    "tailwind.png",
                    const.TAILWIND_CSS_URL,
                    alt="Logotipo Tailwind"
                ),
                rx.text(
                    "TAILWIND",
                    margin_top=Size.MEDIUM.value,
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    align_self="center",
                     _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.05)",
                },
                ),
                
            ),
            
            align_items="start",
            
            spacing=Size.DEFAULT.value
        )
    )
