/** @jsxImportSource @emotion/react */


import { Fragment, useRef } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Avatar, Box, Button, Card, CardBody, CardFooter, CardHeader, Center, Container, Flex, Heading, HStack, Image as ChakraImage, Link, SimpleGrid, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import { EmailIcon } from "@chakra-ui/icons"
import { refs } from "/utils/state"
import NextHead from "next/head"



export default function Component() {
  const ref_proyectos_section = useRef(null); refs['ref_proyectos_section'] = ref_proyectos_section;
  const ref_header_section = useRef(null); refs['ref_header_section'] = ref_header_section;
  const ref_tech_section = useRef(null); refs['ref_tech_section'] = ref_tech_section;

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box>
  <HStack sx={{"position": "sticky", "bg": "#171F26", "backdropFilter": "blur(10px)", "paddingX": "2em", "paddingY": "1.5em", "zIndex": "999", "top": "0"}}>
  <Box sx={{"fontFamily": "Comfortaa", "fontSize": "1.5em", "fontWeight": "500"}}>
  <Text as={`span`} sx={{"color": "#14A1F0"}}>
  {`Adam`}
</Text>
  <Text as={`span`} sx={{"color": "#087ec4"}}>
  {`dev`}
</Text>
</Box>
  <Box>
  <HStack>
  <Link as={NextLink} href={`#header-section`} sx={{"scroll": ["smooth", "#header-section"], "scrollBehavior": "smooth", "color": "#C3C7CB", "fontFamily": "Poppins", "fontSize": "1.2em", "text-decoration": "none", "_hover": {}}}>
  <Text sx={{"marginLeft": "2rem", "_hover": {"cursor": "pointer", "transform": "scale(1.05)"}}}>
  {`Inicio`}
</Text>
</Link>
  <Link as={NextLink} href={`#tech-section`} sx={{"scroll": "#tech-section", "p": "1", "color": "#C3C7CB", "fontFamily": "Poppins", "fontSize": "1.2em", "text-decoration": "none", "_hover": {}}}>
  <Text sx={{"marginLeft": "1rem", "_hover": {"cursor": "pointer", "transform": "scale(1.05)"}}}>
  {`Tecnologias`}
</Text>
</Link>
  <Link as={NextLink} href={`#proyectos-section`} sx={{"scroll": "#proyectos-section", "p": "1", "color": "#C3C7CB", "fontFamily": "Poppins", "fontSize": "1.2em", "text-decoration": "none", "_hover": {}}}>
  <Text sx={{"marginLeft": "1rem", "_hover": {"cursor": "pointer", "transform": "scale(1.05)"}}}>
  {`Proyectos`}
</Text>
</Link>
</HStack>
</Box>
  <Spacer/>
  <Link as={NextLink} href={`https://github.com/mrpowergonz`} isExternal={true} sx={{"scroll": "false", "paddingRight": "-5em", "_hover": {"textDecoration": "underline"}, "text-decoration": "none"}}>
  <ChakraImage src={`github_white.png`} sx={{"height": "2em", "display": "inline-flex", "alignItems": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
  {`Source`}
</Link>
  <Link as={NextLink} href={`https://drive.google.com/file/d/1u8uokRuk21C46wBfQGCHjahzu9-DCpMU/view?usp=drive_link`} isExternal={true} sx={{"marginLeft": "1rem", "paddingRight": "2em", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "color": "#C3C7CB", "fontFamily": "Poppins", "fontSize": "1.2em", "text-decoration": "none"}}>
  {`CV`}
</Link>
  <HStack sx={{"marginLeft": "0.5rem", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}>
  <EmailIcon sx={{"color": "white"}}/>
  <Text sx={{"fontSize": "0.8em", "color": "#f8c133"}}>
  {`adampg74@gmail.com`}
</Text>
</HStack>
</HStack>
  <Center id={`header-section`} ref={ref_header_section}>
  <Box>
  <VStack sx={{"maxWidth": "600px", "width": "100%", "marginY": "2em", "padding": "2em"}}>
  <VStack alignItems={`start`} spacing={`1em`}>
  <HStack>
  <Flex sx={{"alignItems": "center", "width": "100%", "height": "100%"}}>
  <Box sx={{"alignItems": "start", "width": "50%", "height": "100%"}}>
  <VStack sx={{"padding": "0px !important"}}>
  <Avatar name={`Adam Power`} size={`2xl`} src={`lego2.jpg`} sx={{"width": "100%", "height": "100%", "color": "#C3C7CB", "bg": "#ffffff", "padding": "2px", "border": "4px", "borderColor": "#14A1F0", "_hover": {"cursor": "pointer", "transform": "scale(1.10)"}, "transition": "0.5s"}}/>
  <Text sx={{"color": "#A3ABB2", "fontFamily": "Poppins", "marginTop": "0px !important", "fontSize": "0.7em", "padding": "1em", "textAlign": "center"}}>
  {`Hecho con DALLE-3`}
</Text>
</VStack>
</Box>
  <VStack alignItems={`start`} spacing={`1em`} sx={{"marginLeft": "0.5em", "width": "100%", "height": "100%"}}>
  <Heading size={`lg`} sx={{"color": "#F1F2F4", "fontFamily": "Poppins", "fontWeight": "500"}}>
  {`Adam Power Gonzalez`}
</Heading>
  <Text sx={{"marginTop": "0px !important", "color": "#C3C7CB", "fontFamily": "Poppins"}}>
  {`@mr___power`}
</Text>
  <HStack>
  <Link as={NextLink} href={`https://www.youtube.com/playlist?list=PLu3m9uQSDld2jRdRieSRqJmHSUWM6jRmf`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage alt={``} src={`icons/music.svg`} sx={{"width": "1em"}}/>
</Link>
  <Link as={NextLink} href={`https://www.instagram.com/mr___power/?hl=en`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage alt={``} src={`icons/instagram.svg`} sx={{"width": "1em"}}/>
</Link>
  <Link as={NextLink} href={`https://github.com/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage alt={``} src={`icons/github.svg`} sx={{"width": "1em"}}/>
</Link>
  <Link as={NextLink} href={`https://www.youtube.com/channel/UCBOEjk6rJ67ruecmdC5nisQ`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage alt={``} src={`icons/youtube.svg`} sx={{"width": "1em"}}/>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/in/adam-power-gonzalez-47308b1b8/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage alt={``} src={`icons/linkedin.svg`} sx={{"width": "1em"}}/>
</Link>
  <Link as={NextLink} href={`adampg74@gmail.com`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage alt={``} src={`icons/envelope.svg`} sx={{"width": "1em"}}/>
</Link>
</HStack>
</VStack>
</Flex>
</HStack>
  <Flex sx={{"width": "100%", "fontFamily": "Poppins"}}>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeigh": "bold", "color": "#14A1F0"}}>
  {`+2 `}
</Text>
  {`años de experiencia programando`}
</Box>
  <Spacer/>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeigh": "bold", "color": "#14A1F0"}}>
  {`+10 `}
</Text>
  {`años de experiencia fotografiando`}
</Box>
</Flex>
  <Text sx={{"color": "#C3C7CB", "fontFamily": "Poppins", "fontSize": "0.9em"}}>
  {`Soy un programador autodidacta que esta intentando aprender todas las ultimas tecnologias. Aqui os dejo todos mis enlaces de interés. Bienvenid@! `}
</Text>
</VStack>
  <VStack spacing={`0.8em`} sx={{"width": "100%"}}>
  <Heading size={`lg`} sx={{"fontFamily": "Poppins", "width": "100%", "paddingTop": "1em", "color": "#F1F2F4", "fontWeight": "500"}}>
  {`Links de interés`}
</Heading>
  <Link as={NextLink} href={`https://github.com/`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "whiteSpace": "normal", "textAlign": "start", "_hover": {"backgroundColor": "#087ec4", "cursor": "pointer", "transform": "scale(1.05)", "backgroundImage": "linear-gradient(45deg,,#087ec4, #86bfdb)"}, "animation": "0.65s 0.15s ease-out forwards", "transition": "0.5s"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Github`} src={`icons/github.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "1.5em"}}/>
  <VStack alignItems={`start`} spacing={`0px !important`} sx={{"margin": "0px !important", "paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg", "fontWeight": "500"}}>
  {`Github`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB", "fontWeight": "500"}}>
  {`Proyectos personales`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.youtube.com/channel/UCBOEjk6rJ67ruecmdC5nisQ`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "whiteSpace": "normal", "textAlign": "start", "_hover": {"backgroundColor": "#087ec4", "cursor": "pointer", "transform": "scale(1.05)", "backgroundImage": "linear-gradient(45deg,,#087ec4, #86bfdb)"}, "animation": "0.65s 0.15s ease-out forwards", "transition": "0.5s"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Youtube`} src={`icons/youtube.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "1.5em"}}/>
  <VStack alignItems={`start`} spacing={`0px !important`} sx={{"margin": "0px !important", "paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg", "fontWeight": "500"}}>
  {`Youtube`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB", "fontWeight": "500"}}>
  {`Mis proyectos de videos`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.youtube.com/playlist?list=PLu3m9uQSDld2jRdRieSRqJmHSUWM6jRmf`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "whiteSpace": "normal", "textAlign": "start", "_hover": {"backgroundColor": "#087ec4", "cursor": "pointer", "transform": "scale(1.05)", "backgroundImage": "linear-gradient(45deg,,#087ec4, #86bfdb)"}, "animation": "0.65s 0.15s ease-out forwards", "transition": "0.5s"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Musica`} src={`icons/music.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "1.5em"}}/>
  <VStack alignItems={`start`} spacing={`0px !important`} sx={{"margin": "0px !important", "paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg", "fontWeight": "500"}}>
  {`Musica`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB", "fontWeight": "500"}}>
  {`Musica tranquila para programar`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://mrpower.portfoliobox.net/`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "whiteSpace": "normal", "textAlign": "start", "_hover": {"backgroundColor": "#087ec4", "cursor": "pointer", "transform": "scale(1.05)", "backgroundImage": "linear-gradient(45deg,,#087ec4, #86bfdb)"}, "animation": "0.65s 0.15s ease-out forwards", "transition": "0.5s"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Foto y video`} src={`icons/foto.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "1.5em"}}/>
  <VStack alignItems={`start`} spacing={`0px !important`} sx={{"margin": "0px !important", "paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg", "fontWeight": "500"}}>
  {`Foto y video`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB", "fontWeight": "500"}}>
  {`Portfolio de foto y video`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.instagram.com/mr___power/?hl=en`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "whiteSpace": "normal", "textAlign": "start", "_hover": {"backgroundColor": "#087ec4", "cursor": "pointer", "transform": "scale(1.05)", "backgroundImage": "linear-gradient(45deg,,#087ec4, #86bfdb)"}, "animation": "0.65s 0.15s ease-out forwards", "transition": "0.5s"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Instagram`} src={`icons/instagram.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "1.5em"}}/>
  <VStack alignItems={`start`} spacing={`0px !important`} sx={{"margin": "0px !important", "paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg", "fontWeight": "500"}}>
  {`Instagram`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB", "fontWeight": "500"}}>
  {`Red social`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/in/adam-power-gonzalez-47308b1b8/`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "whiteSpace": "normal", "textAlign": "start", "_hover": {"backgroundColor": "#087ec4", "cursor": "pointer", "transform": "scale(1.05)", "backgroundImage": "linear-gradient(45deg,,#087ec4, #86bfdb)"}, "animation": "0.65s 0.15s ease-out forwards", "transition": "0.5s"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Linkedin`} src={`icons/linkedin.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "1.5em"}}/>
  <VStack alignItems={`start`} spacing={`0px !important`} sx={{"margin": "0px !important", "paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg", "fontWeight": "500"}}>
  {`Linkedin`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB", "fontWeight": "500"}}>
  {`Red social contacto`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Heading size={`lg`} sx={{"fontFamily": "Poppins", "width": "100%", "paddingTop": "1em", "color": "#F1F2F4", "fontWeight": "500"}}>
  {`Contacto`}
</Heading>
  <Link as={NextLink} href={`mailto:adampg74@gmail.com`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "whiteSpace": "normal", "textAlign": "start", "_hover": {"backgroundColor": "#087ec4", "cursor": "pointer", "transform": "scale(1.05)", "backgroundImage": "linear-gradient(45deg,,#087ec4, #86bfdb)"}, "animation": "0.65s 0.15s ease-out forwards", "transition": "0.5s"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Email`} src={`icons/envelope.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "1.5em"}}/>
  <VStack alignItems={`start`} spacing={`0px !important`} sx={{"margin": "0px !important", "paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg", "fontWeight": "500"}}>
  {`Email`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB", "fontWeight": "500"}}>
  {`adampg74@gmail.com`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
</VStack>
  <Box id={`tech-section`} ref={ref_tech_section}>
  <VStack sx={{"width": "115%", "paddingTop": "8em"}}>
  <Heading size={`lg`} sx={{"fontFamily": "Poppins", "width": "100%", "paddingTop": "1em", "color": "#F1F2F4", "fontWeight": "500"}}>
  {`Tecnologias`}
</Heading>
  <HStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://www.javascript.com/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`javascript.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)"}}}>
  {`JAVASCRIPT`}
</Text>
</VStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://www.python.org/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`python.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)"}}}>
  {`PYTHON`}
</Text>
</VStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://reactjs.org/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`react.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)"}}}>
  {`REACTJS`}
</Text>
</VStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://nodejs.org/en/about`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`node.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "4em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}}}>
  {`NODEJS`}
</Text>
</VStack>
</HStack>
  <HStack alignItems={`start`} spacing={`1em`}>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://www.djangoproject.com/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`django.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)"}}}>
  {`DJANGO`}
</Text>
</VStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://git-scm.com/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`git.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)"}}}>
  {`GIT`}
</Text>
</VStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://github.com/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`github_white.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)"}}}>
  {`GITHUB`}
</Text>
</VStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://tailwindcss.com/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`tailwind.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)", "transition": "0.5s"}}}>
  {`TAILWIND`}
</Text>
</VStack>
</HStack>
  <HStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://developer.mozilla.org/en-US/docs/Web/CSS`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`css.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)", "transition": "0.5s"}}}>
  {`CSS`}
</Text>
</VStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://reflex.dev/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`reflex.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)", "transition": "0.5s"}}}>
  {`REFLEX`}
</Text>
</VStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://html.com/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`html.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)", "transition": "0.5s"}}}>
  {`HTML`}
</Text>
</VStack>
  <VStack sx={{"padding": "1em"}}>
  <Link as={NextLink} href={`https://www.figma.com/`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`figma.png`} sx={{"heigh": "2em", "width": "150px", "marginBottom": "10px", "_hover": {"cursor": "pointer", "transform": "scale(1.15)"}, "transition": "0.5s"}}/>
</Link>
  <Text sx={{"marginTop": "0.8em", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "center", "_hover": {"cursor": "pointer", "transform": "scale(1.05)", "transition": "0.5s"}}}>
  {`FIGMA`}
</Text>
</VStack>
</HStack>
</VStack>
</Box>
  <Box id={`proyectos-section`} ref={ref_proyectos_section}>
  <HStack>
  <Container centerContent={true} sx={{"justify": "center", "align": "start", "marginTop": "3em", "marginBottom": "-2em", "width": "100%", "alignItems": "center", "marginLeft": "-5em", "transition": "1s"}}>
  <Heading sx={{"fontFamily": "Poppins", "width": "100%", "paddingTop": "4em", "color": "#F1F2F4", "textAlign": "right", "marginBottom": "-51px", "marginLeft": "-1.5em", "fontWeight": "500"}}>
  {`Proyectos`}
</Heading>
  <HStack sx={{"marginBottom": "-10em"}}>
  <Box sx={{"width": "100%", "justify": "center", "align": "start"}}>
  <Link as={NextLink} href={`https://github.com/mrpowergonz/cryptoverse-main`} isExternal={true} sx={{"passHref": true, "scroll": "True", "fontWeight": "bold", "text-decoration": "none", "_hover": {}}}>
  <Card sx={{"alignItems": "center", "textAlign": "center", "background": "#000c16", "padding": "0em", "borderRadius": "2em", "boxShadow": "0 0 20px #2777bb", "margin": "9em", "_hover": {"transform": "translateY(-10px)", "boxShadow": "0 0 7px #f9cd45", "transition": "all 0.3s ease-in-out"}, "width": "70%", "height": ["13em", "18em", "18em", "18em", "18em"], "direction": "column", "align": "strech", "justify": "center", "transition": "0.5s", "heigh": "2em", "spacing": "1em"}}>
  <CardHeader>
  <Heading sx={{"fontSize": "1.5em", "fontWeight": "900", "color": "#C3C7CB", "fontFamily": "Poppins"}}>
  {`Cryptoverse`}
</Heading>
</CardHeader>
  <CardBody>
  <SimpleGrid columns={[2]} spacing={`2`} sx={{"alignItems": "center"}}>
  <Box sx={{"height": "5em", "width": "5em"}}>
  <ChakraImage src={`github_white.png`} sx={{"width": "100%", "margin": "1em"}}/>
</Box>
  <Box sx={{"color": "#C3C7CB", "fontSize": "0.7em", "fontFamily": "Poppins", "alignItems": "center", "paddingTop": "1.5em"}}>
  <Text>
  {`construido con`}
</Text>
  <ChakraImage src={`react.png`} sx={{"width": "30%", "margin": "auto", "paddingTop": "1.5em"}}/>
</Box>
</SimpleGrid>
</CardBody>
  <CardFooter>
  <Heading size={`sm`} sx={{"fontSize": "1em", "color": "#A3ABB2", "fontWeight": "500", "fontFamily": "Poppins"}}>
  {`Web page for ranking criptocurrencies`}
</Heading>
</CardFooter>
</Card>
</Link>
</Box>
  <Box sx={{"backgroundColor": "linear-gradient(to right, #e1e1e1, #f9cd45)", "backgroundClip": "text", "width": "100%", "marginLeft": "-6em"}}>
  <Link as={NextLink} href={`https://github.com/mrpowergonz/Sloth-machine-python`} isExternal={true} sx={{"passHref": true, "scroll": "True", "fontWeight": "bold", "text-decoration": "none", "_hover": {}}}>
  <Card sx={{"alignItems": "center", "textAlign": "center", "background": "#000c16", "padding": "0em", "borderRadius": "2em", "boxShadow": "0 0 20px #2777bb", "margin": "9em", "_hover": {"transform": "translateY(-10px)", "boxShadow": "0 0 7px #f9cd45", "transition": "all 0.3s ease-in-out"}, "width": "70%", "height": ["13em", "18em", "18em", "18em", "18em"], "direction": "column", "align": "strech", "justify": "center", "transition": "0.5s", "heigh": "2em", "spacing": "1em"}}>
  <CardHeader>
  <Heading sx={{"fontSize": "1.5em", "fontWeight": "900", "color": "#C3C7CB", "fontFamily": "Poppins"}}>
  {`Sloth machine`}
</Heading>
</CardHeader>
  <CardBody>
  <SimpleGrid columns={[2]} spacing={`2`} sx={{"alignItems": "center"}}>
  <Box sx={{"height": "5em", "width": "5em"}}>
  <ChakraImage src={`github_white.png`} sx={{"width": "100%", "margin": "1em"}}/>
</Box>
  <Box sx={{"color": "#C3C7CB", "fontSize": "0.7em", "fontFamily": "Poppins", "alignItems": "center", "paddingTop": "1.5em"}}>
  <Text>
  {`construido con`}
</Text>
  <ChakraImage src={`python.png`} sx={{"width": "30%", "margin": "auto", "paddingTop": "1.5em"}}/>
</Box>
</SimpleGrid>
</CardBody>
  <CardFooter>
  <Heading size={`sm`} sx={{"fontSize": "1em", "color": "#A3ABB2", "fontWeight": "500", "fontFamily": "Poppins"}}>
  {`Sloth machine built in Python`}
</Heading>
</CardFooter>
</Card>
</Link>
</Box>
  <Box sx={{"width": "100%", "marginLeft": "-2em"}}>
  <Link as={NextLink} href={`https://github.com/mrpowergonz/to-do-app-DJANGO`} isExternal={true} sx={{"passHref": true, "scroll": "True", "fontWeight": "bold", "text-decoration": "none", "_hover": {}}}>
  <Card sx={{"alignItems": "center", "textAlign": "center", "background": "#000c16", "padding": "0em", "borderRadius": "2em", "boxShadow": "0 0 20px #2777bb", "margin": "9em", "_hover": {"transform": "translateY(-10px)", "boxShadow": "0 0 7px #f9cd45", "transition": "all 0.3s ease-in-out"}, "width": "70%", "height": ["13em", "18em", "18em", "18em", "18em"], "direction": "column", "align": "strech", "justify": "center", "transition": "0.5s", "heigh": "2em", "spacing": "1em"}}>
  <CardHeader>
  <Heading sx={{"fontSize": "1.5em", "fontWeight": "900", "color": "#C3C7CB", "fontFamily": "Poppins"}}>
  {`To do app`}
</Heading>
</CardHeader>
  <CardBody>
  <SimpleGrid columns={[2]} spacing={`2`} sx={{"alignItems": "center"}}>
  <Box sx={{"height": "5em", "width": "5em"}}>
  <ChakraImage src={`github_white.png`} sx={{"width": "100%", "margin": "1em"}}/>
</Box>
  <Box sx={{"color": "#C3C7CB", "fontSize": "0.7em", "fontFamily": "Poppins", "alignItems": "center", "paddingTop": "1.5em"}}>
  <Text>
  {`construido con`}
</Text>
  <ChakraImage src={`django.png`} sx={{"width": "30%", "margin": "auto", "paddingTop": "1.5em"}}/>
</Box>
</SimpleGrid>
</CardBody>
  <CardFooter>
  <Heading size={`sm`} sx={{"fontSize": "1em", "color": "#A3ABB2", "fontWeight": "500", "fontFamily": "Poppins"}}>
  {`Take notes, App built in Django`}
</Heading>
</CardFooter>
</Card>
</Link>
</Box>
</HStack>
  <HStack justify={`center`} sx={{"marginRight": "-25px", "marginLeft": "2.5rem", "align": "start"}}>
  <Box sx={{"width": "100%", "justify": "center", "align": "start"}}>
  <Link as={NextLink} href={`https://adam-password-generator-site.netlify.app`} isExternal={true} sx={{"passHref": true, "scroll": "True", "fontWeight": "bold", "text-decoration": "none", "_hover": {}}}>
  <Card sx={{"alignItems": "center", "textAlign": "center", "background": "#000c16", "padding": "0em", "borderRadius": "2em", "boxShadow": "0 0 20px #2777bb", "margin": "9em", "_hover": {"transform": "translateY(-10px)", "boxShadow": "0 0 7px #f9cd45", "transition": "all 0.3s ease-in-out"}, "width": "70%", "height": ["13em", "18em", "18em", "18em", "18em"], "direction": "column", "align": "strech", "justify": "center", "transition": "0.5s", "heigh": "2em", "spacing": "1em"}}>
  <CardHeader>
  <Heading sx={{"fontSize": "1.5em", "fontWeight": "900", "color": "#C3C7CB", "fontFamily": "Poppins"}}>
  {`Password generator`}
</Heading>
</CardHeader>
  <CardBody>
  <SimpleGrid columns={[2]} spacing={`2`} sx={{"alignItems": "center"}}>
  <Box sx={{"height": "5em", "width": "5em"}}>
  <ChakraImage src={`github_white.png`} sx={{"width": "100%", "margin": "1em"}}/>
</Box>
  <Box sx={{"color": "#C3C7CB", "fontSize": "0.7em", "fontFamily": "Poppins", "alignItems": "center", "paddingTop": "1.5em"}}>
  <Text>
  {`construido con`}
</Text>
  <ChakraImage src={`javascript.png`} sx={{"width": "30%", "margin": "auto", "paddingTop": "1.5em"}}/>
</Box>
</SimpleGrid>
</CardBody>
  <CardFooter>
  <Heading size={`sm`} sx={{"fontSize": "1em", "color": "#A3ABB2", "fontWeight": "500", "fontFamily": "Poppins"}}>
  {`App built in Javascript, create your own password`}
</Heading>
</CardFooter>
</Card>
</Link>
</Box>
  <Box sx={{"width": "100"}}>
  <Link as={NextLink} href={`https://github.com/mrpowergonz/Link_bio`} isExternal={true} sx={{"passHref": true, "scroll": "True", "fontWeight": "bold", "text-decoration": "none", "_hover": {}}}>
  <Card sx={{"alignItems": "center", "textAlign": "center", "background": "#000c16", "padding": "0em", "borderRadius": "2em", "boxShadow": "0 0 20px #2777bb", "margin": "9em", "_hover": {"transform": "translateY(-10px)", "boxShadow": "0 0 7px #f9cd45", "transition": "all 0.3s ease-in-out"}, "width": "70%", "height": ["13em", "18em", "18em", "18em", "18em"], "direction": "column", "align": "strech", "justify": "center", "transition": "0.5s", "heigh": "2em", "spacing": "1em"}}>
  <CardHeader>
  <Heading sx={{"fontSize": "1.5em", "fontWeight": "900", "color": "#C3C7CB", "fontFamily": "Poppins"}}>
  {`Portfolio`}
</Heading>
</CardHeader>
  <CardBody>
  <SimpleGrid columns={[2]} spacing={`2`} sx={{"alignItems": "center"}}>
  <Box sx={{"height": "5em", "width": "5em"}}>
  <ChakraImage src={`github_white.png`} sx={{"width": "100%", "margin": "1em"}}/>
</Box>
  <Box sx={{"color": "#C3C7CB", "fontSize": "0.7em", "fontFamily": "Poppins", "alignItems": "center", "paddingTop": "1.5em"}}>
  <Text>
  {`construido con`}
</Text>
  <ChakraImage src={`reflex.png`} sx={{"width": "30%", "margin": "auto", "paddingTop": "1.5em"}}/>
</Box>
</SimpleGrid>
</CardBody>
  <CardFooter>
  <Heading size={`sm`} sx={{"fontSize": "1em", "color": "#A3ABB2", "fontWeight": "500", "fontFamily": "Poppins"}}>
  {`Personal webpage`}
</Heading>
</CardFooter>
</Card>
</Link>
</Box>
  <Box sx={{"width": "100%", "marginLeft": "-4em"}}>
  <Link as={NextLink} href={`https://booking-example-page.netlify.app/`} isExternal={true} sx={{"passHref": true, "scroll": "True", "fontWeight": "bold", "text-decoration": "none", "_hover": {}}}>
  <Card sx={{"alignItems": "center", "textAlign": "center", "background": "#000c16", "padding": "0em", "borderRadius": "2em", "boxShadow": "0 0 20px #2777bb", "margin": "9em", "_hover": {"transform": "translateY(-10px)", "boxShadow": "0 0 7px #f9cd45", "transition": "all 0.3s ease-in-out"}, "width": "70%", "height": ["13em", "18em", "18em", "18em", "18em"], "direction": "column", "align": "strech", "justify": "center", "transition": "0.5s", "heigh": "2em", "spacing": "1em"}}>
  <CardHeader>
  <Heading sx={{"fontSize": "1.5em", "fontWeight": "900", "color": "#C3C7CB", "fontFamily": "Poppins"}}>
  {`Booking`}
</Heading>
</CardHeader>
  <CardBody>
  <SimpleGrid columns={[2]} spacing={`2`} sx={{"alignItems": "center"}}>
  <Box sx={{"height": "5em", "width": "5em"}}>
  <ChakraImage src={`github_white.png`} sx={{"width": "100%", "margin": "1em"}}/>
</Box>
  <Box sx={{"color": "#C3C7CB", "fontSize": "0.7em", "fontFamily": "Poppins", "alignItems": "center", "paddingTop": "1.5em"}}>
  <Text>
  {`construido con`}
</Text>
  <ChakraImage src={`css.png`} sx={{"width": "30%", "margin": "auto", "paddingTop": "1.5em"}}/>
</Box>
</SimpleGrid>
</CardBody>
  <CardFooter>
  <Heading size={`sm`} sx={{"fontSize": "1em", "color": "#A3ABB2", "fontWeight": "500", "fontFamily": "Poppins"}}>
  {`CSS styles for a booking web page`}
</Heading>
</CardFooter>
</Card>
</Link>
</Box>
</HStack>
</Container>
</HStack>
</Box>
</VStack>
</Box>
</Center>
  <VStack sx={{"marginBottom": "2em", "paddingBottom": "2em", "paddingX": "2em", "color": "#A3ABB2", "paddingLeft": "6em"}}>
  <Avatar name={`Adam Power`} size={`2xl`} src={`logo.png`} sx={{"color": "#C3C7CB", "bg": "#ffffff", "padding": "2px", "border": "4px", "borderColor": "#14A1F0", "alt": "Logotipo MR.Power. Mi silueta en un diafragma de fotografia"}}/>
  <Link as={NextLink} href={`https://mrpower.portfoliobox.net/`} isExternal={true} sx={{"fontSize": "0.8em", "fontFamily": "Poppins", "text-decoration": "none", "_hover": {}}}>
  {`2020-2024 Mr. Power by Adam Power`}
</Link>
  <Text sx={{"fontFamily": "Poppins", "marginTop": "0px !important", "fontSize": "0.8em"}}>
  {` building web pages from Burgos to the world`}
</Text>
</VStack>
</Box>
  <NextHead>
  <title>
  {`Mr Power | pagina principal de mi portfolio`}
</title>
  <meta content={`Hola, mi nombre es Adam Power. Soy desarrollador freeelance y esta es mi pagina con mis links, contactos y proyectos`} name={`description`}/>
  <meta content={`link_bio/assets/logo.png`} property={`og:image`}/>
  <meta content={`website`} name={`og:type`}/>
</NextHead>
</Fragment>
  )
}
