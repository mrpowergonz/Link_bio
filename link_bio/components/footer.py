import reflex as rx
import datetime #para pasar el año en el que estamos al footer

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"2020-{datetime.date.today().year} Mr. Power by Adam Power",
                href="https://mrpower.portfoliobox.net/",
                is_external=True),#para que se abra en una nueva pagina
        rx.text(" building web pages from Burgos to the world"),
    )