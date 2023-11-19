import { store } from "../store";

export const Statistics = () => {
    let quiz = store.get.quizzes();

    return <>
    
        <div>{quiz[0].quiz.multipleChoice.map(
            (elem : any, index: any) => {return (
            <div>
                <p>{elem.question}</p>
                <ol>
                {elem.options.map((e : any) => {
                    console.log(e);
                    return <li>{e}</li>
                })}
                </ol>
                <p>{elem.explanation}</p>
                {quiz[0].correctMultipleChoice[index] ? <p>Correct</p> : <p>Incorrect</p>}
            </div>
            )
        }
        )}
        </div>
        <div>{quiz[0].quiz.longAnswer.map(
            (elem : any, index : any) => {return (
            <div>
                <p>{elem.question}</p>
                <p>{elem.explanation}</p>
                {quiz[0].correctShortAnswers[index] ? <p>Correct</p> : <p>Incorrect</p>}
            </div>
            )
        }
        )}
        </div>
        <div>{quiz[0].quiz.trueOrFalse.map(
            (elem : any, index : any) => {return (
            <div>
                <p>{elem.question}</p>
                <ol>
                    <li>True</li>
                    <li>False</li>
                </ol>
                <p>{quiz[0].correctTrueOrFalse[index] ? <p>Correct</p> : <p>Incorrect</p>}</p>
                <p>{elem.explanation}</p>
            </div>
            )}
        )}
        </div>
    </>
}