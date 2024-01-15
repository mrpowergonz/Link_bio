import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
import link_bio.constants as const

def links()-> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Github",
                    "Proyectos personales" ,
                    const.GITHUB_URL
                    ),

        link_button("Youtube",
                    "Mis proyectos de videos",
                    const.YOUTUBE_URL
                    ),

        link_button("twitter", 
                    "Red social" ,
                    const.TWITTER_X_URL
                    ),

        link_button("Instagram",
                    "Red social", 
                    const.INSTAGRAM_URL
                    
        ),
        link_button("Linkedin",
                    "Red social contacto",
                    const.LINKEDIN_URL 
                    
        ),
        
        
        title("Contacto"),
        link_button("Email",
                    const.EMAIL,
                    f"mailto:{const.EMAIL}"
                    ),
        width = "100%",
        spacing=Size.MEDIUM.value,
    )