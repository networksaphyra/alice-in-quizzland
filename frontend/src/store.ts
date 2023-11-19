import { createStore } from "@udecode/zustood";


export const store = createStore('store')<any>({
    quizzes: []
}, {persist: {enabled: true}, })