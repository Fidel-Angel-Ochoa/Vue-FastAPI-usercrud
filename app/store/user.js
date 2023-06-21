export const  state = () =>({
    id: 0,
    name: "",
    email: "",
    password: ""
}
)
console.log('user: ',state)



export const mutations = {
    storeId: (state, data) =>{
        state.id = data;
    },
    storeName: (state, data)=> {
        state.name = data;
    },
    storeEmail: (state,data)=> {
        state.email =data;
    },
    storePassword: (state,data) => {
        state.password = data;
    }
}
console.log({mutations})
