import { createApp } from 'vue'
import App from './App.vue'
import {createStore} from "vuex"
const store = createStore({
    state : ()=> ({
        username : ""
    
    }),
    
    getters : {
        getusername : state => state.username
    
    },
    
    actions : {
        setusername : ({commit } , newusername) =>{
            commit("setusername", newusername)
        }
    },
    
    mutations : {
        setusername : (state, newusername) => state.username = newusername
    }
})

const app = createApp(App)
app.use(store)
app.mount('#app')



