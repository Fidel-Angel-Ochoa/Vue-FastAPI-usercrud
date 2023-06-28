export default {
  buildDir: "dist", // this is the dir where the project is create in the host(cloudflare)
  target: "static",
  buildModules: ["@nuxtjs/vuetify"],
  modules: ["@nuxtjs/axios"],
  // to import the components automatic
  components: true,
};