import { Button, MenuItem, Select } from "@mui/material";
import { Textarea } from "@mui/joy";
import { useState } from "react";
import axios from "axios";
import { redirect, useNavigate } from "react-router-dom";
import "../Quiz.css"
import { store } from "../store";

export const QuizForm = (props : any) : any => {
    const [correctMultipleChoice, setCorrectMultipleChoice] = useState<any>(props.correctmultiplechoice)
    const [correctTrueOrFalse, setCorrectTrueOrFalse] = useState<any>(props.correcttrueorfalse)
    const [shortAnswer, setShortAnswer] = useState<any>(props.correctshortanswer)
    const history = useNavigate();

    const submitQuiz = async (e: any) => {
        let correctShortAnswers : any = {};
        for (let i = 0; i < Object.keys(shortAnswer).length; i++) {
            console.log(props.quiz.longAnswer[i].answer, shortAnswer[i])
            await axios.post('/check', [
                props.quiz.longAnswer[i].answer,
                shortAnswer[i]
            ], {
            headers: {
                'Content-Type': 'application/json',
            }
        }).then(response => {correctShortAnswers[i] = response.data.confirmation[0].Confirmation})
        console.log(correctShortAnswers)
        }
        store.use.quizzes().push({
            quiz: props.quiz,
            correctTrueOrFalse: correctTrueOrFalse,
            correctMultipleChoice: correctMultipleChoice,
            correctShortAnswers: correctShortAnswers
        });

        history("/stats")
    }

    return (
        <div className="quiz-form-container">
            {props.quiz.multipleChoice.length !== 0 && <p>Multiple Choice Section:</p>}
            {props.quiz.multipleChoice.map((question: any, index: any) => (
                <div key={index}>
                    <p>{index + 1}. {question.question}</p>
                    <Select
                        onChange={(e) => {
                            let stateCopy = { ...correctMultipleChoice };
                            stateCopy[index] = e.target.value === question.answer;
                            setCorrectMultipleChoice(stateCopy);
                        }}
                    >
                        {question.options.map((option: any, optionIndex: any) => (
                            <MenuItem key={optionIndex} value={option}>{option}</MenuItem>
                        ))}
                    </Select>
                </div>
            ))}
            {props.quiz.longAnswer.length !== 0 && <p>Short Answer Section:</p>}
            {props.quiz.longAnswer.map((question: any, index: any) => (
                <div key={index}>
                    <p>{index + 1}. {question.question}</p>
                    <Textarea
                        placeholder="Your Answer"
                        onChange={(e) => {
                            let stateCopy = { ...shortAnswer };
                            stateCopy[index] = e.target.value;
                            setShortAnswer(stateCopy);
                        }}
                        sx={{ background: "#23272f", color: "#ebecf0" }}
                    />
                </div>
            ))}
            {props.quiz.trueOrFalse.length !== 0 && <p>True or False Section:</p>}
            {props.quiz.trueOrFalse.map((question: any, index: any) => (
                <div key={index}>
                    <p>{index + 1}. {question.question}</p>
                    <Select
                        onChange={(e) => {
                            let stateCopy = { ...correctTrueOrFalse };
                            stateCopy[index] = e.target.value === question.answer;
                            setCorrectTrueOrFalse(stateCopy);
                        }}
                    >
                        <MenuItem value={"True"}>True</MenuItem>
                        <MenuItem value={"False"}>False</MenuItem>
                    </Select>
                </div>
            ))}
            <Button onClick={submitQuiz} >Submit</Button>
            </div>)
}