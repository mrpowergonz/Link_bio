import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size

def links()-> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch",
                    "Directos de Twitch" ,
                    "https://www.youtube.com/channel/UCBOEjk6rJ67ruecmdC5nisQ"),

        link_button("Youtube",
                    "Directos de Youtube",
                    "https://www.youtube.com/channel/UCBOEjk6rJ67ruecmdC5nisQ"),

        link_button("Discord", 
                    "Comunidad" ,
                    "https://www.youtube.com/channel/UCBOEjk6rJ67ruecmdC5nisQ"),

        link_button("Instagram",
                    "Red social", 
                    "https://www.instagram.com/mr___power/?hl=en"
        ),
        
        title("Comunidad"),
        link_button("Twitch",
                    "Directos de Twitch" ,
                    "https://www.youtube.com/channel/UCBOEjk6rJ67ruecmdC5nisQ"),

        link_button("Youtube",
                    "Directos de Youtube",
                    "https://www.youtube.com/channel/UCBOEjk6rJ67ruecmdC5nisQ"),

        link_button("Discord", 
                    "Comunidad" ,
                    "https://www.youtube.com/channel/UCBOEjk6rJ67ruecmdC5nisQ"),

        link_button("Instagram",
                    "Red social", 
                    "https://www.instagram.com/mr___power/?hl=en"),

        width = "100%",
        spacing=Size.MEDIUM.value,
    )