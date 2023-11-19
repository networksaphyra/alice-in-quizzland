import { createStore } from "@udecode/zustood";
import { QuizStats, Store } from "./types";


export const store = createStore('store')<Store>({
    quizzes: []
}, {persist: {enabled: true}, })