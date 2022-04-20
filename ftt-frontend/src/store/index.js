export const state = ()=> ({
    username : "Bobby"

})

export const getters = {
    getusername : state => state.username

}

export const actions = {
    setusername : ({state, commit } , newusername) =>{
        commit("setusername", newusername)
    }
}

export const mutations = {
    setusername : (state, newusername) => state.username = newusername
}