import reflex as rx
import link_bio.styles.styles as styles 
from link_bio.styles.styles import Size as Size

def link_button(title: str, body: str, image: str, url:str)-> rx.Component:
    return rx.link(
      rx.button(
          rx.hstack(
              rx.image(
                  src=image,
                  width=styles.Size.LARGE.value,
                  height=styles.Size.LARGE.value,
                  margin=Size.LARGE.value
              ),
              rx.vstack(
                  rx.text(title, style= styles.button_title_style),
                  rx.text(body, style= styles.button_body_style),
                  spacing=Size.ZERO.value,
                  align_items= "start",
                  margin=Size.ZERO.value
              )
              
          )
      ),
      href=url,
      is_external=True,
      width="100%",
      
    )

