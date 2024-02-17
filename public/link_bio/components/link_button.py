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
                  margin=Size.LARGE.value,
                  alt=title
              ),
              rx.vstack(
                  rx.text(title, style= styles.button_title_style),
                  rx.text(body, style= styles.button_body_style),
                  spacing=Size.ZERO.value,
                  align_items= "start",
                  margin=Size.ZERO.value,
                  padding_y= Size.SMALL.value,
                  padding_right= Size.SMALL.value,
              ),
              width= "100%",
              
          )
      ),
      href=url,
      is_external=True,
      width="100%",
      
    )

