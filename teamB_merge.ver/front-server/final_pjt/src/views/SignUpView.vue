<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <div class="mb-3">
        <label for="username">username : </label>
        <input type="text" id="username" v-model="username"><br>
      </div>
      <div class="mb-3">
        <label for="password1"> password : </label>
        <input type="password" id="password1" v-model="password1"><br>
      </div>
      <div class="mb-3">
      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      </div>
      
      <input type="submit" value="SignUp" class="btn btn-primary">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>