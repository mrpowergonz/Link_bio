import reflex as rx
from link_bio.components.navbar import navbar #importamos el navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.tech.tech import tech
from link_bio.views.cards.cards import cards

from link_bio.components.footer import footer
import link_bio.styles.styles as styles #as para importalo con un alias
from link_bio.styles.styles import Size as Size

#Lo que necesitaria para un Hola mundo
class State(rx.State):
    pass

def index() -> rx.Component:
    return  rx.box(
        navbar(), #lo meto aqui para que ocupe todo
        rx.center(# manera de centrar con reflex
            rx.vstack( #componente que lo mete vertical
                header(),
                links(),
                tech(),
                cards(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y= Size.BIG.value,
                padding=Size.BIG.value,
           
            )
        ),
         footer()
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
    )
