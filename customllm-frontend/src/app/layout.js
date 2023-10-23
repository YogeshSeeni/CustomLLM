import '@fontsource/inter';
import { CssVarsProvider } from '@mui/joy/styles';
import NavBar from '@/components/NavBar';
import { getServerSession } from 'next-auth';
import { authOptions } from '../../pages/api/auth/[...nextauth]';
import SessionProvider from './SessionProvider';

export default async function RootLayout({ children }) {
  const session = await getServerSession(authOptions)

  return (
    <html lang="en">
      <meta name="viewport" content="initial-scale=1, width=device-width" />
      <body>
      <CssVarsProvider>
        <SessionProvider>
          <NavBar />
          {children}
        </SessionProvider>
      </CssVarsProvider>
      </body>
    </html>
  )
}
