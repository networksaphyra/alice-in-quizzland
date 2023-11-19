export type MultipleChoice = {
    question: string;
    options: string[];
    answer: string;
    explanation: string;
}

export type LongAnswer = {
    question: string
    answer: string
    explanation: string
}

export type TrueOrFalse = {
    question: string
    answer: string
    explanation: string
}

export type Quiz = {
    name?: string
    multipleChoice: MultipleChoice[]
    longAnswer: LongAnswer[]
    trueOrFalse: TrueOrFalse[]
    numQuestions: number
}

export type QuizStats = {
    quiz: Quiz
    correctMultipleChoice: any
    correctTrueOrFalse: any
    correctShortAnswers: any
}

export type Store = {
    quizzes: QuizStats[]
}