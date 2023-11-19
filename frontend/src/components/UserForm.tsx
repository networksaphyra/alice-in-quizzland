import LargeTextBox from "../components/LargeTextBox"
import { FormControl, Input, MenuItem, Select, Slider, Stack } from "@mui/material"
import { Button } from '@mui/joy'
import Textarea from '@mui/joy/Textarea';
import { useRef, useState } from "react"
import { VolumeDown, VolumeUp } from "@material-ui/icons";
import axios from 'axios';
import { LongAnswer, MultipleChoice, Quiz, TrueOrFalse } from "../types";
import { QuizForm } from "./QuizForm";
import "../Form.css"

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
    const [correctShortAnswer, setCorrectShortAnswer] = useState<any>()

    const submitData = () => {
      const total = multipleChoice + shortAnswer + trueOrFalse;
      
      console.log(Math.round((multipleChoice / total) * Number(numQuestionsRef.current?.value)));
      console.log(Math.round((shortAnswer / total) * Number(numQuestionsRef.current?.value)));
      console.log(Math.round((trueOrFalse / total) * Number(numQuestionsRef.current?.value)));
      axios.post('/members', {
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
          }
          mc.push(questionDict);
          multiplechoice[count as keyof typeof multiplechoice] = false;
          count += 1;
        }
        setCorrectMultipleChoice(multiplechoice)

        let la = []
        count = 0
        let longanswer : any = {}

        for (let i of longAnswer) {
          let answer : string = i["Answer"];
          let _question : string = i["Question"];
          let explanation : string = i["Explanation"];
          let questionDict : LongAnswer = {
            question: _question,
            answer: answer,
            explanation: explanation,
          }
          longanswer[count] = false;
          count += 1;
          la.push(questionDict);
        }
        
        setCorrectShortAnswer(longanswer);

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
          }
          trueorfalse[count as keyof typeof multiplechoice] = false;
          count += 1;
          tf.push(questionDict);
        }
        
        setCorrectTrueOrFalse(trueorfalse)
        console.log(tf.length)
        setQuiz({name: nameRef.current?.value, multipleChoice: mc, longAnswer: la, trueOrFalse: tf, numQuestions: mc.length + la.length + tf.length});
      })
    };



    return (quiz ? <QuizForm quiz={quiz} correctmultiplechoice={correctMultipleChoice} correcttrueorfalse={correctTrueOrFalse} correctshortanswer={correctShortAnswer}/>
        : <div className="quiz-form-container">
        <h2 className="quiz-title">Make a New Quiz:</h2>
        <FormControl>
            <Textarea placeholder="Quiz Name" slotProps={{ textarea: { ref: nameRef } }}/>
            <p></p>
            <Textarea placeholder="Quiz Topic / Study Notes" slotProps={{ textarea: { ref: studyNotesRef } }} />
            <p></p>
            <Textarea placeholder="Num of Questions" slotProps={{ textarea: { ref: numQuestionsRef } }} />
            <p></p>

            <Stack spacing={2} direction="row" alignItems="center">
                <label>Multiple Choice:</label>
                <Slider aria-label="multipleChoice" value={multipleChoice} onChange={(e, newNum) => { setMultipleChoice(newNum as number) }} />
            </Stack>

            <Stack spacing={2} direction="row" alignItems="center">
                <label>Short Answer:</label>
                <Slider aria-label="shortAnswer" value={shortAnswer} onChange={(e, newNum) => { setShortAnswer(newNum as number) }} />
            </Stack>

            <Stack spacing={2} direction="row" alignItems="center">
                <label>True or False:</label>
                <Slider aria-label="trueOrFalse" value={trueOrFalse} onChange={(e, newNum) => { setTrueOrFalse(newNum as number) }} />
            </Stack>
            <Button onClick={submitData} >Submit</Button>
        </FormControl>
    </div>
    );
}