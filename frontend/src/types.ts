export type MultipleChoice = () => {
    question: string
    options: [string]
    answer: string
    explanation: string
    correctRate: number
}

export type LongAnswer = () => {
    question: string
    answer: string
    explanation: string
    correctRate: number
}

export type trueOrFalse = () => {
    question: string
    answer: string
    correctRate: number
}

export type Quiz = () => {
    name: string
    multipleChoice: [MultipleChoice]
    longAnswer: [LongAnswer]
    trueOrFalse: [trueOrFalse]
    correctRate: number
}

export type Store = () => {
    quizzes: [Quiz]

}