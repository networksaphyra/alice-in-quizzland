import LargeTextBox from "../components/LargeTextBox"
import { FormControl } from "@mui/material"
import { Button } from '@mui/joy'
import { useRef } from "react"
import Textarea from '@mui/joy/Textarea';


export const Home = () => {
    const nameRef = useRef<HTMLTextAreaElement | null>(null);
    const studyNotesRef = useRef<HTMLTextAreaElement | null>(null);
    
    const showRefContent = () => {
      console.log(nameRef.current?.value);
      console.log(studyNotesRef.current?.value);
    };

    return <div>
        <h1>Welcome to the Quiz Maker</h1>
        <p>Input your study notes, or what topic you would like to make a quiz.</p>
        <FormControl sx={{width: "100%"}}>
        <Textarea placeholder="Quiz Name" slotProps={{ textarea: { ref: nameRef } }}/>
        <LargeTextBox ref={studyNotesRef}/>
        <Button onClick={showRefContent} sx={{ ml: 'auto' }}>Send</Button>
        </FormControl>
    </div>
}