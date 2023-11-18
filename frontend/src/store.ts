import { createStore } from "@udecode/zustood";


export const store = createStore('store')({
    quizzes: []
}, {persist: {enabled: true}, })