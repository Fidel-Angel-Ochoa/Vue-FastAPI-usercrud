<template>
  <v-form class="my-form">
    <v-text-field v-if="id" v-model="id" readonly></v-text-field>

    <v-text-field v-model="name" :counter="255" label="Name"></v-text-field>

    <v-text-field v-model="email" label="Email"></v-text-field>

    <v-text-field v-model="password" label="Password"></v-text-field>

    <v-btn color="success" class="mr-4" @click="submitUser({id,name,email,password})">
      {{ id ? 'Edit' : 'Submit' }}
    </v-btn>
  </v-form>
</template>

<script>

export default {
  computed:{
    id:{
      get(){
        return this.$store.state.user.id;
      },
      set(value){
        this.$store.commit("user/storeId", value);
      }
    },
    name:{
      get(){
        return this.$store.state.user.name;
      },
      set(value){
        this.$store.commit("user/storeName", value);
      }
    },
    email:{
      get(){
        return this.$store.state.user.email;
      },
      set(value){
        this.$store.commit("user/storeEmail", value)
      }
    },
    password:{
      get(){
        return this.$store.state.user.password
      },
      set(value){
        this.$store.commit("user/storePassword", value)
      }
    }
  },
  methods:{
    async submitUser(user){
      if (user.id) {
        await this.$axios.put("http://localhost:8000/users/"+user.id, user)
      } else {
        await this.$axios.post("http://localhost:8000/users/", user);
      }
      await this.resetForm({id:0, name:'', email:'', password:''});
      await this.$store.commit("users/storeData", (await this.$axios.get("http://localhost:8000/users/")).data)
    },
    resetForm(user) {
      this.$store.commit("user/storeId",user.id);
      this.$store.commit("user/storeName",user.name);
      this.$store.commit("user/storeEmail",user.email);
      this.$store.commit("user/storePassword",user.password)
    }
  }
}
</script>

<style>
.my-form {
  width: 100%; /* Adjust the width as needed */
}

/* Responsive styles */
@media (max-width: 600px) {
  .my-form {
    display: flex;
    /* Modify the styles for smaller screens */
  }
}
</style>