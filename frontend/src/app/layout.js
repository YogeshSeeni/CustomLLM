import './globals.css'
import '@fontsource/inter';
import { CssVarsProvider } from '@mui/joy/styles';

export const metadata = {
  title: 'CustomLLM',
  description: 'An end-to-end',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <meta name="viewport" content="initial-scale=1, width=device-width" />
      <body>
        <CssVarsProvider>
            {children}
        </CssVarsProvider>
      </body>
    </html>
  )
}
