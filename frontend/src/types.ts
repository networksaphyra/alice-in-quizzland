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

export type Quiz = () => {
    name: string
    multipleChoice: [MultipleChoice]
    longAnswer: [LongAnswer]
    correctRate: number
}

export type Store = () => {
    quizzes: [Quiz]

}