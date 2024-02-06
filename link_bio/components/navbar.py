import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as color
import link_bio.styles.styles as styles
from link_bio.styles.fonts import font
from link_bio.styles.styles import Size as Size, Textcolor
import link_bio.constants as const


def navbar() -> rx.Component:
    return rx.desktop_only(
    rx.hstack(
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
                    scroll=("smooth", "#header-section"),

                    scroll_behavior="smooth",

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
                
                alignItems="center",
                _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.15)",
                },
                transition="0.5s",
                margin_right="-2em",
            ),
            "< ... >",
            href="https://github.com/mrpowergonz",
            scroll="false",
            
            _hover={
                "textDecoration": "none"
            },
            is_external=True
        ),
        rx.link(
            "CV",
            href="https://drive.google.com/file/d/1u8uokRuk21C46wBfQGCHjahzu9-DCpMU/view?usp=drive_link",
            is_external=True,
            margin_left="1rem",
            padding_right="2em",
            _hover={
                "cursor": "pointer",
                "transform": "scale(1.15)",
            },
            color=Textcolor.BODY.value,
            font_family=font.DEFAULT.value,
            font_size=Size.LARGE2.value,
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
        width="100%",
        position="fixed",
        bg=color.CONTENT.value,
        backdrop_filter="blur(10px)",
        padding_x=Size.BIG.value,
        padding_y=Size.LARGE.value,
        z_index="9999",
        top="0"
    ),
    
)

def navbar_mobile() -> rx.Component:
    return rx.mobile_only(
    rx.hstack(
        rx.box(
            rx.span("Adam", color=color.PRIMARY.value),
            rx.span("dev", color=color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        rx.box(
            rx.hstack(
                rx.link(
                    rx.text("Inicio",
                            margin_left="-2rem",
                            _hover={
                                "cursor": "pointer",
                                "transform": "scale(1.05)",
                            },
                            ),
                    href="#header1-section",
                    scroll=("smooth", "#header-section"),

                    scroll_behavior="smooth",

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
                    href="#tech1-section",
                    scroll="#tech1-section",
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
                    href="#proyectos1-section",
                    scroll="#proyectos1-section",
                    p="1",
                    color=Textcolor.BODY.value,
                    font_family=font.DEFAULT.value,
                    font_size=Size.LARGE2.value,
                ),
            ),
        ),
        rx.spacer(),
        rx.hstack(
        rx.link(
            rx.image(
                src="github_white.png",
                height="2em",
                display="inline-flex",
                
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
            
            margin_right="-2em",
            _hover={
                "textDecoration": "underline"
            },
            is_external=True
        ),
        rx.link(
            "CV",
            href="https://drive.google.com/file/d/1u8uokRuk21C46wBfQGCHjahzu9-DCpMU/view?usp=drive_link",
            is_external=True,
            margin_left="1rem",
            padding_right="2em",
            _hover={
                "cursor": "pointer",
                "transform": "scale(1.15)",
            },
            color=Textcolor.BODY.value,
            font_family=font.DEFAULT.value,
            font_size=Size.LARGE2.value,
        ),
        rx.hstack(
            rx.icon(tag="email", color="white"),
            rx.text("adampg74@gmail.com", font_size=Size.MEDIUM.value, color="#f8c133"),
            margin_left="-5rem",
            padding_right="2em",
            _hover={
                "cursor": "pointer",
                "transform": "scale(1.15)",
            },
            transition="0.5s",
        ),),
        position="fixed",
        bg=color.CONTENT.value,
        backdrop_filter="blur(10px)",
        padding_x=Size.SMALL.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0",
        left="50%",
        transform="translateX(-50%)",
        width="120%",
        flex_direction="column"
    ),
)