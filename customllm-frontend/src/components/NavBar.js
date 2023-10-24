"use client"

import * as React from "react";
import { Box, CssVarsProvider, IconButton } from "@mui/joy";
import Typography from "@mui/joy/Typography";
import MapsHomeWorkIcon from "@mui/icons-material/MapsHomeWork";
import ColorSchemeToggle from "./ColorSchemeToggle";
import Button from "@mui/joy/Button";
import { redirect } from 'next/navigation'
import { useSession } from "next-auth/react";


export default function NavBar() {
	const {data: session} = useSession()

	return (
		<CssVarsProvider>
			<Box
			sx={{
				display: "flex",
				flexDirection: "row",
				justifyContent: "space-between",
				alignItems: "center",
				width: "100%",
				top: 0,
				px: 1.5,
				py: 1,
				zIndex: 10000,
				backgroundColor: "background.body",
				borderBottom: "1px solid",
				borderColor: "divider",
				position: "sticky",
			}}
		>
			<Box
				sx={{
					display: "flex",
					flexDirection: "row",
					alignItems: "center",
					gap: 1.5,
				}}
			>
				<IconButton size="sm" variant="soft">
					<MapsHomeWorkIcon />
				</IconButton>
				<Typography component="h1" fontWeight="xl">
					CustomLLM
				</Typography>
			</Box>
			<Box sx={{ display: "flex", flexDirection: "row", gap: 3 }}>
				{session ?  <Button size="sm" color="neutral">
						Sign Out
					</Button> : <Box sx={{ display: "flex", flexDirection: "row", gap: 3 }}>
						<Button size="sm" color="neutral">
							Sign Up
						</Button>
						<Button size="sm" color="neutral">
							Sign In
						</Button>
					</Box>}	
				<ColorSchemeToggle sx={{ alignSelf: "center" }} />
			</Box>
		</Box>
		</CssVarsProvider>
		
	);
}
