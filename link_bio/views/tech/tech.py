import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_tech import link_tech
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import text_color as Textcolor
from link_bio.styles.fonts import font




def tech() -> rx.Component:
    return rx.vstack(
        title("Tecnologias"),
        rx.hstack(
            rx.vstack(
                
                    link_tech(
                        "javascript.png",
                        const.JAVASCRIPT_URL,
                        
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
            
            spacing=Size.LARGE.value
        )
    )
