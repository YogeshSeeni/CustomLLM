"use client"

import React from "react";
import Sheet from "@mui/joy/Sheet";
import Typography from "@mui/joy/Typography";
import FormControl from "@mui/joy/FormControl";
import FormLabel from "@mui/joy/FormLabel";
import Input from "@mui/joy/Input";
import Button from "@mui/joy/Button";
import Link from "@mui/joy/Link";

import {signOut, useSession} from "next-auth/react"

export default function Home() {
	const session = useSession()
	
	return (
		<>
			<div>{session?.data?.user?.name}</div>
			<button onClick={() => signOut()}>Logout</button>
		</>
	);
}
