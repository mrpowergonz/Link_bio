import reflex as rx
from link_bio.components.navbar import navbar, navbar_mobile #importamos el navbar
from link_bio.components.link_icon import link_icon
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.tech.tech import tech, tech_mobile
from link_bio.views.cards.cards import cards
from link_bio.views.cards.cards_mobile import cards_mobile
from link_bio.components.footer import footer,footer_mobile
import link_bio.styles.styles as styles #as para importalo con un alias
from link_bio.styles.styles import Size as Size


#Lo que necesitaria para un Hola mundo
class State(rx.State):
    pass

def index() -> rx.Component:
    return  rx.box(
        rx.desktop_only(
        navbar(), #lo meto aqui para que ocupe todo
        
        rx.center(# manera de centrar con reflex
            rx.box(
                rx.vstack( #componente que lo mete vertical    
                    header(),
                    
                    links(),
                    rx.box(
                        tech(),
                        id="tech-section",),
                    rx.box(
                        cards(),
                        id="proyectos-section",),

                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y= Size.BIG.value,
                    padding=Size.BIG.value,   
            
                  ),
                ),
                id="header-section",
            ),
         footer(),
        
    ),
    rx.mobile_and_tablet(
     #lo meto aqui para que ocupe todo
        navbar_mobile(),
        rx.center(# manera de centrar con reflex
            rx.box(
                rx.vstack( #componente que lo mete vertical    
                    header(),
                    
                    links(),
                    rx.box(
                        tech_mobile(),
                        id="tech1-section",),
                    rx.box(
                        cards_mobile(),
                        id="proyectos1-section",),

                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y= Size.BIG.value,
                    padding=Size.BIG.value,   
            
                  ),
                  width="150%",
                  margin_left="1em"
                ),
                id="header1-section",
                width="100%",
                margin_left="5em",
                margin_top="6em",
            ),
         
         footer_mobile()
    ),
    )
    




#Le paso el estilo a la aplicacion
app = rx.App(
    stylesheets=styles.STYLESHEETS, #Pasarle los fonts
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="Mr Power | pagina principal de mi portfolio",
    description="Hola, mi nombre es Adam Power. Soy desarrollador freeelance y esta es mi pagina con mis links, contactos y proyectos",
    image="link_bio/assets/logo.png",
    meta=[
        {"name":"og:type", "content": "website"},
     
    ]
    ),

