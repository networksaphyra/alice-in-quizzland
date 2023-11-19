import LargeTextBox from "../components/LargeTextBox"
import { FormControl, Input, MenuItem, Select, Slider, Stack } from "@mui/material"
import { Button } from '@mui/joy'
import Textarea from '@mui/joy/Textarea';
import { useRef, useState } from "react"
import { VolumeDown, VolumeUp } from "@material-ui/icons";
import axios from 'axios';
import { LongAnswer, MultipleChoice, Quiz, TrueOrFalse } from "../types";

export const UserForm = () => {
    const nameRef = useRef<HTMLTextAreaElement | null>(null);
    const studyNotesRef = useRef<HTMLTextAreaElement | null>(null);
    const numQuestionsRef = useRef<HTMLTextAreaElement | null>(null);
    const [multipleChoice, setMultipleChoice] = useState<number>(0);
    const [shortAnswer, setShortAnswer] = useState<number>(0);
    const [trueOrFalse, setTrueOrFalse] = useState<number>(0);
    const [quiz, setQuiz] = useState<Quiz>()
    const [correctMultipleChoice, setCorrectMultipleChoice] = useState<any>({})
    const [correctTrueOrFalse, setCorrectTrueOrFalse] = useState<any>({})

    const submitQuiz = () => {
      axios.post('/check', { }, {
        headers: {
            'Content-Type': 'application/json',
        }
    })


    }

    const submitData = () => {
      const total = multipleChoice + shortAnswer + trueOrFalse;
      
      console.log(Math.round((multipleChoice / total) * Number(numQuestionsRef.current?.value)));
      console.log(Math.round((shortAnswer / total) * Number(numQuestionsRef.current?.value)));
      console.log(Math.round((trueOrFalse / total) * Number(numQuestionsRef.current?.value)));
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
        console.log(response)

        let multipleChoice = response.data.generated_questions[0];
        let longAnswer = response.data.generated_questions[1];
        let trueOrFalse = response.data.generated_questions[2];
        
        let mc = []
        let count = 0
        let multiplechoice : any = {}

        for (let i of multipleChoice) {
          let answer : string = i["Answer"];
          let _question : string = i["Question"];
          let explanation : string = i["Explanation"];
          let options : string[] = i["Options"];
          let questionDict : MultipleChoice = {
            question: _question,
            options: options,
            answer: answer,
            explanation: explanation,
            correctRate: 0
          }
          mc.push(questionDict);
          multiplechoice[count as keyof typeof multiplechoice] = false;
          count += 1;
        }
        setCorrectMultipleChoice(multiplechoice)

        let la = []

        for (let i of longAnswer) {
          let answer : string = i["Answer"];
          let _question : string = i["Question"];
          let explanation : string = i["Explanation"];
          let questionDict : LongAnswer = {
            question: _question,
            answer: answer,
            explanation: explanation,
            correctRate: 0
          }
          la.push(questionDict);
        }

        let tf = []
        count = 0
        let trueorfalse : any = {}

        for (let i of trueOrFalse) {
          let answer : string = i["Answer"];
          let _question : string = i["Question"];
          let explanation : string = i["Explanation"];

          let questionDict : TrueOrFalse = {
            question: _question,
            answer: answer,
            explanation: explanation,
            correctRate: 0
          }
          trueorfalse[count as keyof typeof multiplechoice] = false;
          count += 1;
          tf.push(questionDict);
        }
        
        setCorrectTrueOrFalse(trueorfalse)
        console.log(tf.length)
        setQuiz({name: nameRef.current?.value, multipleChoice: mc, longAnswer: la, trueOrFalse: tf, correctRate: 0, numQuestions: mc.length + la.length + tf.length});
      })
    };



    return (quiz ? 
        <>

        {quiz.multipleChoice.length != 0  && <p>Multiple Choice Section:</p>}
          {quiz.multipleChoice.map((question, index) => {
            return <div>
              <p>{index + 1}. {question.question}</p>
              <Select onChange={(e) => {
                    var stateCopy = Object.assign({}, correctMultipleChoice);
                    console.log(stateCopy)
                    stateCopy[index] = e.target.value == question.answer
                    setCorrectMultipleChoice(stateCopy)
                    console.log(correctMultipleChoice)}
                }>
                {question.options.map((option) => {

                  return (<MenuItem value={option} >{option}</MenuItem>)
                })}
              </Select>
            </div>
          }
          )}

          {quiz.longAnswer.length != 0 && <p>Short Answer Section:</p>}
          {quiz.longAnswer.map((question, index) => {
            return <div>
              <p>{index + 1}. {question.question}</p>
              <Textarea placeholder="Your Answer" slotProps={{  }} sx={{background: "#23272f", color: "#ebecf0"}}/>
            </div>
          })}

          {quiz.trueOrFalse.length != 0 && <p>True or False Section:</p>}
          {quiz.trueOrFalse.map((question, index) => {
            console.log(question.question);
            return <div>
              <p>{index + 1}. {question.question}</p>
              <Select onChange={(e) => {
                    var stateCopy = Object.assign({}, correctTrueOrFalse);
                    stateCopy[index] = e.target.value == question.answer
                    setCorrectTrueOrFalse(stateCopy)}
                }>
                  <MenuItem value={"True"} >True</MenuItem>
                  <MenuItem value={"False"} >False</MenuItem>
                </Select>
            </div>
          })}
          <Button onClick={submitQuiz} sx={{ ml: 'auto' }}>Submit</Button>
        </>
        : <>
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
        <Button onClick={submitData} sx={{ ml: 'auto' }}>Submit</Button>
        </FormControl>
        </>
    );
    
}