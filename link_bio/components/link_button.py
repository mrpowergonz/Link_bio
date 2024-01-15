import reflex as rx
import link_bio.styles.styles as styles 
from link_bio.styles.styles import Size as Size

def link_button(title: str, body: str, url:str)-> rx.Component:
    return rx.link(
      rx.button(
          rx.hstack(
              rx.icon(
                  tag="arrow_forward",
                  width=styles.Size.BIG.value,
                  height=styles.Size.BIG.value,
                  margin=Size.MEDIUM.value
              ),
              rx.vstack(
                  rx.text(title, style= styles.button_title_style),
                  rx.text(body, style= styles.button_body_style),
                  spacing=Size.SMALL.value,
                  align_items= "start",
                  margin=Size.ZERO.value
              )
              
          )
      ),
      href=url,
      is_external=True,
      width="100%",
      
    )

