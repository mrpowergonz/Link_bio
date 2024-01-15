/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Avatar, Box, Button, Center, Flex, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import { ArrowForwardIcon, LinkIcon } from "@chakra-ui/icons"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box>
  <HStack sx={{"position": "sticky", "bg": "#171F26", "paddingX": "2em", "paddingY": "1em", "zIndex": "999", "top": "0"}}>
  <Box sx={{"fontFamily": "Comfortaa", "fontSize": "1.5em"}}>
  <Text as={`span`} sx={{"color": "#14A1F0"}}>
  {`Adam`}
</Text>
  <Text as={`span`} sx={{"color": "#087ec4"}}>
  {`dev`}
</Text>
</Box>
  <Text sx={{"fontFamily": "Poppins"}}>
  {`Mr.Power`}
</Text>
</HStack>
  <Center>
  <VStack sx={{"maxWidth": "600px", "width": "100%", "marginY": "2em", "padding": "2em"}}>
  <VStack alignItems={`start`} spacing={`2em`}>
  <HStack spacing={`1em`}>
  <Avatar name={`Adam Power`} size={`xl`} src={`logo.png`} sx={{"color": "#C3C7CB", "bg": "#ffffff", "padding": "2px", "border": "4px", "borderColor": "#14A1F0"}}/>
  <VStack alignItems={`start`}>
  <Heading size={`lg`} sx={{"color": "#F1F2F4", "fontFamily": "Poppins"}}>
  {`Adam Power`}
</Heading>
  <Text sx={{"marginTop": "0px !important", "color": "#C3C7CB", "fontFamily": "Poppins"}}>
  {`@mr___power`}
</Text>
  <HStack>
  <Link as={NextLink} href={`https://github.com/mrpowergonz`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <LinkIcon/>
</Link>
  <Link as={NextLink} href={`https://github.com/mrpowergonz`} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <LinkIcon/>
</Link>
</HStack>
</VStack>
</HStack>
  <Flex sx={{"width": "100%", "fontFamily": "Poppins"}}>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeigh": "bold", "color": "#14A1F0"}}>
  {`+2 `}
</Text>
  {`años de experiencia`}
</Box>
  <Spacer/>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeigh": "bold", "color": "#14A1F0"}}>
  {`+2 `}
</Text>
  {`años de experiencia`}
</Box>
  <Spacer/>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeigh": "bold", "color": "#14A1F0"}}>
  {`+2 `}
</Text>
  {`años de experiencia`}
</Box>
</Flex>
  <Text sx={{"color": "#C3C7CB", "fontFamily": "Poppins", "fontSize": "0.9em"}}>
  {`Soy un programador autodidacta que esta intentando aprender todas las ultimas tecnologias. Aqui os dejo todos mis enlaces de interés. Bienvenid@! `}
</Text>
</VStack>
  <VStack spacing={`0.8em`} sx={{"width": "100%"}}>
  <Heading size={`lg`} sx={{"fontFamily": "Poppins", "width": "100%", "paddingTop": "1em", "color": "#F1F2F4"}}>
  {`Comunidad`}
</Heading>
  <Link as={NextLink} href={``} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "_hover": {"backgroundColor": "#087ec4"}}}>
  <HStack>
  <ArrowForwardIcon sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": "0px !important"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg"}}>
  {`Github`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`Proyectos personales`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.youtube.com/channel/UCBOEjk6rJ67ruecmdC5nisQ`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "_hover": {"backgroundColor": "#087ec4"}}}>
  <HStack>
  <ArrowForwardIcon sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": "0px !important"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg"}}>
  {`Youtube`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`Mis proyectos de videos`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://twitter.com/MrPower64165231`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "_hover": {"backgroundColor": "#087ec4"}}}>
  <HStack>
  <ArrowForwardIcon sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": "0px !important"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg"}}>
  {`twitter`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`Red social`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.instagram.com/mr___power/?hl=en`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "_hover": {"backgroundColor": "#087ec4"}}}>
  <HStack>
  <ArrowForwardIcon sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": "0px !important"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg"}}>
  {`Instagram`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`Red social`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/in/adam-power-gonzalez-47308b1b8/`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "_hover": {"backgroundColor": "#087ec4"}}}>
  <HStack>
  <ArrowForwardIcon sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": "0px !important"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg"}}>
  {`Linkedin`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`Red social contacto`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Heading size={`lg`} sx={{"fontFamily": "Poppins", "width": "100%", "paddingTop": "1em", "color": "#F1F2F4"}}>
  {`Contacto`}
</Heading>
  <Link as={NextLink} href={`mailto:adampg74@gmail.com`} isExternal={true} sx={{"width": "100%", "text-decoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "borderRadius": "1em", "color": "#F1F2F4", "backgroundColor": "#171F26", "fontFamily": "Poppins", "_hover": {"backgroundColor": "#087ec4"}}}>
  <HStack>
  <ArrowForwardIcon sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": "0px !important"}}>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "1em", "color": "#F1F2F4", "size": "lg"}}>
  {`Email`}
</Text>
  <Text sx={{"fontFamily": "Poppins", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`adampg74@gmail.com`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
</VStack>
  <VStack>
  <Heading size={`lg`} sx={{"fontFamily": "Poppins", "width": "100%", "paddingTop": "1em", "color": "#F1F2F4"}}>
  {`Tecnologias`}
</Heading>
  <HStack alignItems={`start`} sx={{"width": "50%", "borderRadius": "3px", "borderColor": "white"}}>
  <VStack>
  <Link as={NextLink} href={``} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`javascript.png`} sx={{"heigh": "4em"}}/>
</Link>
  <Text sx={{"marginTop": "0px !important", "color": "#C3C7CB", "fontFamily": "Poppins", "alignSelf": "flex_start"}}>
  {`JAVASCRIPT`}
</Text>
  <Link as={NextLink} href={``} isExternal={true} sx={{"text-decoration": "none", "_hover": {}}}>
  <ChakraImage src={`python.png`} sx={{"heigh": "4em"}}/>
</Link>
</VStack>
</HStack>
</VStack>
</VStack>
</Center>
  <VStack sx={{"marginBottom": "2em", "paddingBottom": "2em", "color": "#A3ABB2"}}>
  <ChakraImage src={`logo.png`} sx={{"height": "4em"}}/>
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
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
