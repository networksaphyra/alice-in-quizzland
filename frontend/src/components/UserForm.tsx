import LargeTextBox from "../components/LargeTextBox"
import { FormControl, Input, MenuItem, Select, Slider, Stack } from "@mui/material"
import { Button } from '@mui/joy'
import Textarea from '@mui/joy/Textarea';
import { useRef, useState } from "react"
import { VolumeDown, VolumeUp } from "@material-ui/icons";
import axios from 'axios';

export const UserForm = () => {
    const nameRef = useRef<HTMLTextAreaElement | null>(null);
    const studyNotesRef = useRef<HTMLTextAreaElement | null>(null);
    const numQuestionsRef = useRef<HTMLTextAreaElement | null>(null);
    const [multipleChoice, setMultipleChoice] = useState<number>(0);
    const [shortAnswer, setShortAnswer] = useState<number>(0);
    const [trueOrFalse, setTrueOrFalse] = useState<number>(0);

    const submitData = () => {
      const total = multipleChoice + shortAnswer + trueOrFalse;

      axios.post('/members',{
          topic: studyNotesRef.current?.value,
          multipleChoice: Math.round((multipleChoice / total) * Number(numQuestionsRef.current?.value)),
          shortAnswer: Math.round((shortAnswer / total) * Number(numQuestionsRef.current?.value)),
          trueOrFalse: Math.round((trueOrFalse / total) * Number(numQuestionsRef.current?.value))
        }, {
          headers: {
              'Content-Type': 'application/json',
          }
      })
      .then(function (response) {
        console.log(response);
      })
    };

    return (<>
        <h2>Make a New Quiz:</h2>
        <FormControl sx={{width: "100%"}}>
        <Textarea placeholder="Quiz Name" slotProps={{ textarea: { ref: nameRef } }} sx={{background: "#23272f", color: "#ebecf0"}}/>
        <LargeTextBox ref={studyNotesRef}/>
        <Textarea placeholder="Num of Questions" slotProps={{ textarea: { ref: numQuestionsRef } }} sx={{background: "#23272f", color: "#ebecf0"}}/>
        <Stack spacing={2} direction="row" sx={{ mb: 1 }} alignItems="center">
          <label>Multiple Choice:</label>
          <Slider sx={{width: "30%"}} aria-label="multipleChoice" value={multipleChoice} onChange={(e, newNum) => {setMultipleChoice(newNum as number)}} />
          </Stack>
        <Stack spacing={2} direction="row" sx={{ mb: 1 }} alignItems="center">
          <label>Short Answer:</label>
          <Slider sx={{width: "30%"}} aria-label="shortAnswer" value={shortAnswer} onChange={(e, newNum) => {setShortAnswer(newNum as number)}} />
          </Stack>
        <Stack spacing={2} direction="row" sx={{ mb: 1 }} alignItems="center">
          <label>True or False:</label>
          <Slider sx={{width: "30%"}} aria-label="trueOrFalse" value={trueOrFalse} onChange={(e, newNum) => {setTrueOrFalse(newNum as number)}} />
          </Stack>
        <Button onClick={submitData} sx={{ ml: 'auto' }}>submit</Button>
        </FormControl>
        </>
    );
    
}