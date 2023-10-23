"use client"

import '@fontsource/inter';
import { CssVarsProvider } from '@mui/joy/styles';
import NavBar from '@/components/NavBar';


export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <meta name="viewport" content="initial-scale=1, width=device-width" />
      <body>
        <CssVarsProvider>
            <NavBar />
            {children}
        </CssVarsProvider>
      </body>
    </html>
  )
}
