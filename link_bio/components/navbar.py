import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as color
import link_bio.styles.styles as styles
from link_bio.styles.fonts import font
from link_bio.styles.styles import Size as Size, Textcolor

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("Adam", color=color.PRIMARY.value),
            rx.span("dev", color=color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        rx.box(
           
            rx.hstack(
                rx.link(
                    rx.text("Inicio",
                            margin_left="2rem",
                            _hover={
                                "cursor": "pointer",
                                "transform": "scale(1.05)",
                            },
                            ),
                    href="#header-section",
                    scroll="#header-section",
                    
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    font_size=Size.LARGE2.value,
                ),
                rx.link(
                    rx.text("Tecnologias",
                            margin_left="1rem",
                            _hover={
                                "cursor": "pointer",
                                "transform": "scale(1.05)",
                            },
                            ),
                    href="#tech-section",
                    scroll="#tech-section",
                    p="1",
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    font_size=Size.LARGE2.value,
                ),
                rx.link(
                    rx.text("Proyectos",
                            margin_left="1rem",
                            _hover={
                                "cursor": "pointer",
                                "transform": "scale(1.05)",
                            },
                            ),
                    href="#proyectos-section",
                    scroll="#proyectos-section",
                    p="1",
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    font_size=Size.LARGE2.value,
                ),
            ),
        ),
        rx.spacer(),
        
        rx.link(
            rx.image(
                src="github_white.png",
                height="2em",
                display="inline-flex",
                pr="0.2",
                alignItems="center",
                _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.15)",
                },
                transition="0.5s",
            ),
            "Source",
            href="https://github.com/mrpowergonz",
            scroll="false",
            padding_right="-5em",
            _hover={
                "textDecoration": "underline"
            },
            is_external=True
        ),
        rx.hstack(
        
            rx.icon(tag="email", color="white"),
            rx.text("adampg74@gmail.com", font_size=Size.MEDIUM.value, color="#f8c133"),
            margin_left="0.5rem",  
            _hover={
                "cursor": "pointer",
                "transform": "scale(1.15)",
            },
            transition="0.5s",
        ),
        position="sticky",
        bg=color.CONTENT.value,
        backdrop_filter="blur(10px)",
        padding_x=Size.BIG.value,
        padding_y=Size.MEDIUM.value,
        z_index="999",
        top="0"
    )
