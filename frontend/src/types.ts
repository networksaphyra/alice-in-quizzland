export type MultipleChoice = {
    question: string;
    options: string[];
    answer: string;
    explanation: string;
    correctRate: number;
}

export type LongAnswer = {
    question: string
    answer: string
    explanation: string
    correctRate: number
}

export type TrueOrFalse = {
    question: string
    answer: string
    explanation: string
    correctRate: number
}

export type Quiz = {
    name?: string
    multipleChoice: MultipleChoice[]
    longAnswer: LongAnswer[]
    trueOrFalse: TrueOrFalse[]
    correctRate: number
    numQuestions: number
}

export type Store = {
    quizzes: [Quiz]

}