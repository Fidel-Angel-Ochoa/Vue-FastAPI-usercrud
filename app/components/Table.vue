<template>
  <v-data-table
    :headers="headers"
    :items="users"
    :items-per-page="5"
    class="elevation-1 my-table"

  > 
    <template v-slot:[`item.password`]="{ item }" >
      <td align="left" >
        <div class="password-column" >
          <span class="password-text">{{ item.password }}</span>
        </div>
      </td>
    </template>
    <template v-slot:[`item.edit`]="{item}">
      <v-btn color="primary" @click="editItem(item)"> Edit </v-btn>
    </template>
    <template v-slot:[`item.delete`]="{item}">
      <v-btn color="primary" @click="deleteItem(item.id)"> Delete </v-btn>
    </template>
  </v-data-table>
</template>

<script>
  export default {
    data() {
      return {
        headers: [
          {text:"Id",value:"id"},
          {text: "Name", value: "name"},
          {text: "Email", value: "email"},
          {text: "Password", value: "password"},
          {text: "", value: "edit"},
          {text: "", value: "delete"},
        ],
      };
    },
    computed: {
      users() {
        return this.$store.state.users.data;
      },
    },
    // this async take the data from the backend api and save it in the vuex store
    async fetch() {
      this.$store.commit(
        "users/storeData",
        (await this.$axios.get("https://vue-fastapi-backend.onrender.com/users")).data
      );
    },
    // check how this code is working
    methods:{
      editItem(user){
        // console.log(user)
        this.$store.commit("user/storeId",user.id);
        this.$store.commit("user/storeName",user.name);
        this.$store.commit("user/storeEmail",user.email);
        this.$store.commit("user/storePassword",user.password)
      },
      async deleteItem(id){
        await this.$axios.delete("https://vue-fastapi-backend.onrender.com/users/"+id);
        this.$store.commit("users/storeData",(await this.$axios.get("https://vue-fastapi-backend.onrender.com/users")).data)
      }
    }
  };
</script>

<style>
.my-table{
  width: 100%; /* Adjust the width as needed */
  font-size: 14px;
  padding: 5px 15px;
  display: "display-inside";
}
.password-column{
  height: auto;
  width:100px;
  overflow: hidden; /* Hide content that exceeds column width */
  white-space: nowrap; /* text wrapping */
  text-overflow: ellipsis; /* Add ellipsis (...) for truncated text */
}

/* Responsive styles */
@media (max-width: 600px) {

}
</style>