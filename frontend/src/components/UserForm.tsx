import LargeTextBox from "../components/LargeTextBox"
import { FormControl } from "@mui/material"
import { Button } from '@mui/joy'
import Textarea from '@mui/joy/Textarea';
import { useRef } from "react"

export const UserForm = () => {
    const nameRef = useRef<HTMLTextAreaElement | null>(null);
    const studyNotesRef = useRef<HTMLTextAreaElement | null>(null);
    
    const showRefContent = () => {
      console.log(nameRef.current?.value);
      console.log(studyNotesRef.current?.value);
    };

    return (<>
<h2>Make a New Quiz:</h2>
        <FormControl sx={{width: "100%"}}>
        <Textarea placeholder="Quiz Name" slotProps={{ textarea: { ref: nameRef } }} sx={{background: "#23272f", color: "#ebecf0"}}/>
        <LargeTextBox ref={studyNotesRef}/>
        <Button onClick={showRefContent} sx={{ ml: 'auto' }}>Send</Button>
        </FormControl>
        </>
    );
    
}