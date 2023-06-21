<template>
    <v-app>
        <v-main>
            <v-app-bar class="custom-app-bar" color="orange" dense elevation="4" rounded>
                <span class="custom-app-bar-text">Vue-FastAPI</span>
                <div>User Registration</div>
            </v-app-bar>
            <v-container justify="center" align="center">
                <client-only>
                    <div>
                        <span class="content-text">In this app you can register, edit and delete users in the Database. The DB is MySQL</span>
                    </div>
                    <!-- Nuxt is called from 'pages/index.vue'-->
                    <Nuxt/>
                </client-only>
            </v-container>
        </v-main>
    </v-app>
</template>

<script> 
export default {
    
}
</script>

<style>
.custom-app-bar {
  font-family: 'Arial', sans-serif; 
  height: 100px; 
}

.custom-app-bar-text {
  color: white; 
  font-weight: bold; 
  font-size: 32px; 
}

.content-text{
    margin: 0 50px
}
</style>