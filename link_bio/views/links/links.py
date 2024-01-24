import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
import link_bio.constants as const

def links()-> rx.Component:
    return rx.vstack(
        title("Links de interés"),
        link_button("Github",
                    "Proyectos personales" ,
                    "icons/github.svg",
                    const.GITHUB_URL,
                    ),

        link_button("Youtube",
                    "Mis proyectos de videos",
                    "icons/youtube.svg",
                    const.YOUTUBE_URL,                 
                    ),

        link_button("Musica", 
                    "Musica tranquila para programar" ,
                    "icons/music.svg",
                    const.MUSIC_URL,
                    ),

        link_button("Foto y video",
                    "Portfolio de foto y video",
                    "icons/foto.svg", 
                    const.FOTO_URL,
                    ),

        link_button("Instagram",
                    "Red social",
                    "icons/instagram.svg", 
                    const.INSTAGRAM_URL,
                    
                    
        ),
        link_button("Linkedin",
                    "Red social contacto",
                    "icons/linkedin.svg",
                    const.LINKEDIN_URL ,
            
                    
        ),
        
        
        title("Contacto"),
        link_button("Email",
                    const.EMAIL,
                    "icons/envelope.svg",
                    f"mailto:{const.EMAIL}"
                    
                    ),
        width = "100%",
        spacing=Size.MEDIUM.value,
        
    )

