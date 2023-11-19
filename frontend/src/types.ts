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
    correctRate: number
}

export type Store = {
    quizzes: [Quiz]

}