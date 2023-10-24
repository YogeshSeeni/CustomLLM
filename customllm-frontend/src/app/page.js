"use client"

import * as React from 'react';
import { CssVarsProvider } from '@mui/joy/styles';
import CssBaseline from '@mui/joy/CssBaseline';
import Box from '@mui/joy/Box';
import Sidebar from '@/components/Sidebar';
import Header from '@/components/Header';
import MyMessages from '@/components/MyMessages';

import {signOut, useSession} from "next-auth/react"
import NavBar from '@/components/NavBar';

export default function Home() {
	const session = useSession()
	
	return (
		<CssVarsProvider disableTransitionOnChange>
		  <CssBaseline />
		  <NavBar />
		  <Box sx={{ display: 'flex', minHeight: '100dvh' }}>
			<Header />
			<Box component="main" className="MainContent" sx={{ flex: 1 }}>
			  <MyMessages />
			</Box>
		  </Box>
		</CssVarsProvider>
	  );
}
